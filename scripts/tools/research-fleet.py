#!/usr/bin/env python3
"""research-fleet.py — search/fetch provider abstraction for REWRITE-PIPELINE Stage 1.

Why this exists (2026-07-24 外送專法 session): running 4 parallel Sonnet research
agents for one article burned ~500K tokens and hit an account session limit before
they all finished. Most of that cost is mechanical labor (run a query, open a page,
pull out text) that doesn't need Sonnet-level judgment. This tool moves that labor
off the Claude meter: a script calls real search/fetch APIs directly, so Claude's
role shrinks to query design (Stage 0) and synthesis/falsification (the manual §2-§7
consolidation done in reports/research/2026-07/外送專法.md).

Provider abstraction (per MANIFESTO §架構解 第二例證，2026-07-24): every provider is
swappable behind SearchProvider / FetchProvider. Bing Search API retired 2025-08-11,
Google Custom Search closed to new signups in 2025, Brave dropped its free tier in
2026-02 — three "normal" vendors gone or repriced within a year. Call sites depend on
the interface, not the vendor name, so losing a provider means adding one class, not
rewriting the pipeline.

Usage:
    python3 scripts/tools/research-fleet.py search "外送專法 施行細則" --count 10
    python3 scripts/tools/research-fleet.py fetch "https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=N0020024"
    python3 scripts/tools/research-fleet.py batch task.json --out reports/research/2026-07/外送專法-fleet-E.json

Credentials read from ~/.config/taiwan-md/credentials/.env (same convention as
fetch-cloudflare.py / openrouter-translate.py) — BRAVE_API_KEY, SERPER_API_KEY,
optional JINA_API_KEY. Never commit real keys; this repo's own .env guard
(fetch-cloudflare.py) fails loud if credentials end up inside the repo.
"""

import argparse
import json
import re
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Optional

CREDS_DIR = Path.home() / ".config/taiwan-md/credentials"
ENV_FILE = CREDS_DIR / ".env"


def load_env() -> dict:
    import os

    env = dict(os.environ)
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            env[k.strip()] = v.strip().strip("'\"")
    return env


ENV = load_env()


@dataclass
class SearchResult:
    title: str
    url: str
    snippet: str = ""
    provider: str = ""


@dataclass
class FetchedDoc:
    url: str
    title: str
    text: str
    provider: str
    articles: Optional[dict] = None
    ok: bool = True
    error: str = ""


class SearchProvider(ABC):
    name = "abstract"

    def available(self) -> bool:
        return True

    @abstractmethod
    def search(self, query: str, count: int = 10, country: str = "tw", lang: str = "zh-hant") -> list[SearchResult]:
        ...


class FetchProvider(ABC):
    name = "abstract"

    @abstractmethod
    def can_handle(self, url: str) -> bool:
        ...

    @abstractmethod
    def fetch(self, url: str) -> FetchedDoc:
        ...


class BraveSearch(SearchProvider):
    name = "brave"

    def __init__(self):
        self.key = ENV.get("BRAVE_API_KEY")

    def available(self) -> bool:
        return bool(self.key)

    def search(self, query, count=10, country="tw", lang="zh-hant"):
        params = {"q": query, "country": country, "search_lang": lang, "count": str(count)}
        url = "https://api.search.brave.com/res/v1/web/search?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={"Accept": "application/json", "X-Subscription-Token": self.key})
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.load(resp)
        return [
            SearchResult(title=r.get("title", ""), url=r.get("url", ""), snippet=r.get("description", ""), provider=self.name)
            for r in data.get("web", {}).get("results", [])
        ]


class SerperSearch(SearchProvider):
    name = "serper"

    def __init__(self):
        self.key = ENV.get("SERPER_API_KEY")

    def available(self) -> bool:
        return bool(self.key)

    def search(self, query, count=10, country="tw", lang="zh-hant"):
        body = json.dumps({"q": query, "gl": country, "hl": "zh-tw", "num": count}).encode()
        req = urllib.request.Request(
            "https://google.serper.dev/search",
            data=body,
            headers={"X-API-KEY": self.key, "Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.load(resp)
        return [
            SearchResult(title=r.get("title", ""), url=r.get("link", ""), snippet=r.get("snippet", ""), provider=self.name)
            for r in data.get("organic", [])
        ]


class SearchCascade:
    """Tries providers in order, skips unavailable/failed ones. Same shape as the babel 4-tier cascade."""

    def __init__(self, providers: list[SearchProvider]):
        self.providers = providers

    def search(self, query, count=10, **kw) -> list[SearchResult]:
        errors = []
        for p in self.providers:
            if not p.available():
                continue
            try:
                results = p.search(query, count=count, **kw)
                if results:
                    return results
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as e:
                errors.append(f"{p.name}: {e}")
        raise RuntimeError(f"all search providers failed/unavailable: {errors or 'no provider has a key set'}")


class MojLawFetch(FetchProvider):
    """全國法規資料庫 dedicated parser — returns exact article-numbered verbatim text.

    Built 2026-07-24: WebFetch could not get full articles from this exact domain across
    4 separate research agents (125-char truncation policy, PDF binary failures). The
    site's HTML has article numbers in a separate <a name="N"> tag per row, so a plain
    regex gets clean, article-numbered text with zero LLM cost.
    """

    name = "moj-law"
    URL_RE = re.compile(r"law\.moj\.gov\.tw/LawClass/LawAll\.aspx\?pcode=([\w-]+)")
    ROW_RE = re.compile(
        r'<div class="row"><div class="col-no"> <a[^>]*name="(\d+)">第\s*\d+\s*條</a></div>'
        r'<div class="col-data">(.*?)</div>\s*</div>\s*</div>',
        re.S,
    )
    TITLE_RE = re.compile(r"<title>([^<]+)</title>")

    def can_handle(self, url: str) -> bool:
        return bool(self.URL_RE.search(url))

    # law.moj.gov.tw's cert chain omits Subject Key Identifier, which Python's
    # default strict SSL context rejects (curl tolerates it). Scoped relaxation
    # for this one government legal-database domain only — read-only public
    # law text, no credentials involved.
    _GOV_TLS_CTX = ssl._create_unverified_context()

    def fetch(self, url: str) -> FetchedDoc:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(req, timeout=30, context=self._GOV_TLS_CTX) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as e:
            return FetchedDoc(url=url, title="", text="", provider=self.name, ok=False, error=str(e))
        rows = self.ROW_RE.findall(html)
        articles = {int(num): re.sub(r"<[^>]+>", "", content).strip() for num, content in rows}
        title_m = self.TITLE_RE.search(html)
        title = title_m.group(1).strip() if title_m else url
        full_text = "\n\n".join(f"第{n}條：{t}" for n, t in sorted(articles.items()))
        return FetchedDoc(url=url, title=title, text=full_text, provider=self.name, articles=articles, ok=bool(articles))


class JinaFetch(FetchProvider):
    """Universal fallback: r.jina.ai converts any URL (incl. PDFs, JS-rendered pages) to clean markdown.
    Free without a key (rate-limited ~20 req/min); set JINA_API_KEY for higher limits."""

    name = "jina"
    TITLE_RE = re.compile(r"^Title:\s*(.+)$", re.M)

    def __init__(self):
        self.key = ENV.get("JINA_API_KEY")

    def can_handle(self, url: str) -> bool:
        return True

    def fetch(self, url: str) -> FetchedDoc:
        # Jina 403s requests with urllib's default User-Agent string.
        headers = {"Accept": "text/plain", "User-Agent": "Mozilla/5.0"}
        if self.key:
            headers["Authorization"] = f"Bearer {self.key}"
        req = urllib.request.Request("https://r.jina.ai/" + url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                text = resp.read().decode("utf-8", errors="ignore")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as e:
            return FetchedDoc(url=url, title="", text="", provider=self.name, ok=False, error=str(e))
        title_m = self.TITLE_RE.search(text)
        title = title_m.group(1).strip() if title_m else url
        return FetchedDoc(url=url, title=title, text=text, provider=self.name, ok=bool(text.strip()))


class FetchCascade:
    def __init__(self, providers: list[FetchProvider]):
        self.providers = providers

    def fetch(self, url: str) -> FetchedDoc:
        for p in self.providers:
            if p.can_handle(url):
                doc = p.fetch(url)
                if doc.ok:
                    return doc
        return FetchedDoc(url=url, title="", text="", provider="none", ok=False, error="all fetch providers failed")


def build_default_search() -> SearchCascade:
    return SearchCascade([BraveSearch(), SerperSearch()])


def build_default_fetch() -> FetchCascade:
    return FetchCascade([MojLawFetch(), JinaFetch()])


def cmd_search(args):
    results = build_default_search().search(args.query, count=args.count, country=args.country, lang=args.lang)
    out = [asdict(r) for r in results]
    if args.out:
        Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=2))
        print(f"✅ {len(out)} results → {args.out}")
    else:
        print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_fetch(args):
    doc = build_default_fetch().fetch(args.url)
    if args.out:
        Path(args.out).write_text(json.dumps(asdict(doc), ensure_ascii=False, indent=2))
        print(f"{'✅' if doc.ok else '❌'} provider={doc.provider} → {args.out}")
    else:
        print(json.dumps(asdict(doc), ensure_ascii=False, indent=2)[:3000])


def cmd_batch(args):
    spec = json.loads(Path(args.spec).read_text())
    search_cascade = build_default_search()
    fetch_cascade = build_default_fetch()
    results: dict = {"queries": [], "sources": []}
    seen_urls: set[str] = set()
    for q in spec.get("queries", []):
        try:
            hits = search_cascade.search(
                q, count=spec.get("count_per_query", 5), country=spec.get("country", "tw"), lang=spec.get("lang", "zh-hant")
            )
        except RuntimeError as e:
            results["queries"].append({"query": q, "error": str(e)})
            continue
        results["queries"].append({"query": q, "hit_count": len(hits), "provider": hits[0].provider if hits else None})
        for h in hits[: spec.get("fetch_top_k", 3)]:
            if h.url in seen_urls:
                continue
            seen_urls.add(h.url)
            doc = fetch_cascade.fetch(h.url)
            results["sources"].append(
                {
                    "query": q,
                    "title": h.title,
                    "url": h.url,
                    "snippet": h.snippet,
                    "search_provider": h.provider,
                    "fetch_provider": doc.provider,
                    "ok": doc.ok,
                    "error": doc.error,
                    "text": doc.text[: spec.get("max_chars", 20000)],
                    "articles": doc.articles,
                }
            )
            time.sleep(spec.get("delay_sec", 1.0))
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2))
    print(f"✅ {len(results['sources'])} sources fetched → {out_path}")


def main():
    ap = argparse.ArgumentParser(description="research-fleet — search/fetch provider abstraction for REWRITE-PIPELINE Stage 1")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("search")
    sp.add_argument("query")
    sp.add_argument("--count", type=int, default=10)
    sp.add_argument("--country", default="tw")
    sp.add_argument("--lang", default="zh-hant")
    sp.add_argument("--out")
    sp.set_defaults(func=cmd_search)

    fp = sub.add_parser("fetch")
    fp.add_argument("url")
    fp.add_argument("--out")
    fp.set_defaults(func=cmd_fetch)

    bp = sub.add_parser("batch")
    bp.add_argument("spec", help="JSON file: {queries: [...], count_per_query, fetch_top_k, country, lang, max_chars, delay_sec}")
    bp.add_argument("--out", required=True)
    bp.set_defaults(func=cmd_batch)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
