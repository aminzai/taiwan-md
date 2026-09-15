---
title: 'The Backslash in "Kung": The Two Layers of Default Tax Taiwanese Engineers Pay Every Day'
description: 'On Windows 11 with the zh-TW locale, the translation-status script dumped all 4,546 scanned paths into `root`, making Technology zero — while Linux CI stayed green the same week. The script splits category names on forward slashes, but the disk uses backslashes, so it can''t split them. An even older layer is buried in the characters themselves: the second byte of Big5 "kung" is the ASCII backslash, which developers call "Hsu kung tsai" (a pun on the surname Hsu). How paths are written and what symbols live inside the characters — the defaults never account for this machine. Git''s quotePath is a separate line with a different cause.'
date: 2026-08-13
category: 'Technology'
tags:
  [
    'open source',
    'Windows',
    'Big5',
    'UTF-8',
    'character encoding',
    'Traditional Chinese',
  ]
subcategory: '文字與工具'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-08-13
lastHumanReview: false
translatedFrom: 'Technology/功字裡的那根反斜線.md'
sourceCommitSha: '5dcaeea42'
sourceContentHash: 'sha256:57b41e308a296fb4'
sourceBodyHash: 'sha256:9af4500f829effce'
translatedAt: '2026-09-15T19:45:20+08:00'
---

> **30-second overview:** I ran the translation-status script, the screen showed 4546, all in `root`. GitHub CI on Linux was green. Later I realized two things. The backslash in Windows paths can't be split by the script using forward slashes. The second byte of Big5 for "kung" is itself the ASCII `\`. Two different mechanisms, yet they often appear together on the same Traditional Chinese Windows machine.

I maintain Taiwan.md's translation-status script on Windows 11 with the zh-TW locale. That night I ran `i18n-status.py` as usual, waiting for the terminal to print the numbers. The console was cp950. No red text in the output.

The screen stopped at 4546. All in a category called `root`. Technology was 0.

The same week I pushed to GitHub, CI on Linux was green.

The script variable is named `zh_articles`, scanning paths under `knowledge` except for English, about, and underscore directories. Japanese, Korean, and Arabic are also counted. That night it couldn't even split the category names, dumping over 4,000 paths into a single cell. No exceptions, no warnings. The statistics looked like the entire site had broken, yet not a single file was missing. [^8]

Paths on disk are `knowledge\Technology\some-article.md`, separated by backslashes between folders. The script uses `split('/')` to extract category names. On Linux this works because paths are natively forward slashes. On Windows it can't split backslashes, so the entire path comes through unchanged and articles get dumped into the default `root`. [^1]

After switching to let `pathlib` handle directories, Technology had 59 articles, matching the folder contents. Between them lay just one assumption: which line your machine uses to separate folders.

> **📝 Editor's note:** The script syntax wasn't wrong, and CI did run the tests. The crack is between "the machine the author actually sits at" and "the machine the tool thinks you sit at." That gap belongs to no single link in the chain, so no one is assigned to watch it.

## The Line Inside "Kung"

Paths are the first layer. The second is older, buried in the characters themselves.

Big5 was finalized in 1984, with each Chinese character taking two bytes. If the second byte falls between `0x40` and `0x7E`, it overlaps with common ASCII symbols: `[`, `]`, `{`, `}`, `\`, `|`. Hung Chao-kuei (retired August 2023, formerly associate professor in the Department of Information Management at Chaoyang University of Technology) wrote on his teaching page: "Since 40-7E is the ASCII range for commonly used characters, it sometimes causes trouble for programmers." [^2]

The code for "kung" is `A5 5C`. That trailing `0x5C` is the ASCII backslash `\` in Latin-1. A program that scans byte-by-byte and treats `\` as an escape or separator will mistake the second half of "kung" for a path. Filenames or paths containing "kung" can both trip here.

In Taiwan and Hong Kong's dev circles this is called "Hsu kung tsai": "Hsu" is `B3 5C`, "kung" is `A5 5C`, "tsai" is `BB 5C` — three common characters written together resembling a person's name. [^5] Hung also listed "Chia yeh cheng tsun kung," whose second bytes collide with `[`, `]`, `{`, `}`, `\`, and built a scanning tool called b5tm. [^2] A bug given a human name is usually one that shows up often enough that a generation must be able to point at it and talk about it.

In 2015, the author of the blog "Dark Thread" upgraded to Visual Studio 2015. The old `.cs` files were still saved in BIG5. After switching to the Roslyn compiler, the Hsu kung tsai inside the files turned into compile errors.

Two days later a colleague told him they had switched too and got stuck for a long time, eventually tracing back to his post. Some users had thousands of files, converting one at a time still left many behind — "had no choice but to say goodbye to VS2015." He later wrote a small batch tool to convert to UTF-8, because manual re-saving wasn't feasible. [^7]

This is not the same issue as the `split('/')` above. One is a modern tool assuming what paths look like. The other is a symbol that moved into the body of a character forty years ago after the decision to use double-byte encoding. Different mechanisms, yet they often arrive together on the same cp950 machine. How characters are inputted, see [East Asian Text Input Methods](/en/technology/east-asian-input-methods/). Here we're talking about what happens after the characters are already on disk — whether the toolchain still recognizes them.

## Defaults Never Branch for This Machine

Git defaults to `core.quotePath` being on. Filenames with bytes above `0x80` get printed by `git status` as octal escapes like `\344\270\255`. The Chinese filenames are still there — you just can't read what your repository is saying every day. [^3] It escapes the high bytes of UTF-8. Big5's `0x5C` is a different line. They both look like backslashes, but for different reasons.

In Python 3 on Windows, if `open()` doesn't specify `encoding='utf-8'`, it may inherit the system locale. The same UTF-8 file reads fine on Linux, but on this machine it decodes with cp950, and punctuation or bopomofo gets garbled. [^4] I've paid this tax myself: using PowerShell 5.1's `Get-Content | Set-Content` to convert a UTF-8 file, the long dash turned into `??` in the diff. That's another default tax, not the second theme.

When status messages include emoji, this cp950 console crashes outright. The character set lacks those symbols, Python can't print them, and the exception propagates to the top. Linux CI can't detect this because it's not running on this machine.

Git, Python, and CI sample paths like `$HOME/project/src` — none of them branch for zh-TW Windows.

Hung Chao-kuei was interviewed by iThome in 2015, discussing what format government files should be opened in and how long they could last. The report conveyed his meaning: if the government only uses Microsoft products to open file data, it's equivalent to betting that Microsoft's lifespan will outlast the Republic of China. [^6] That statement was about file formats and preservation duration. Data tied to a particular default tool becomes unreadable over time — whoever can still read it wins. Open-source collaboration binds itself to a particular machine's default environment. The tension between civic tech and government file formats is discussed in [Open Source and g0v](/en/technology/open-source-and-g0v/). The long-term cultural absorption of this gap by Taiwanese developers is explored in [The Taiwan Open Source Spirit](/en/technology/taiwan-open-source-spirit/).

Path separators, terminal encoding, and the `$HOME` in CI sample paths — none of them branch for this machine. On the day 4,546 paths were misclassified, no line of code threw an error. The statistics looked normal until you sat in front of this machine.

## Further Reading

- [The Taiwan Open Source Spirit](/en/technology/taiwan-open-source-spirit): The culture and context of Taiwanese developers participating in open source.
- [East Asian Text Input Methods](/en/technology/east-asian-input-methods): How characters are typed into computers, from character maps to keyboards.
- [Open Source and g0v](/en/technology/open-source-and-g0v): Collaboration between open data and government formats.

## References

[^1]: [Microsoft Learn: File path formats on Windows systems](https://learn.microsoft.com/zh-tw/dotnet/standard/io/file-path-formats) — .NET documentation states that traditional DOS paths use backslashes as directory separators, and forward slashes get converted to backslashes.

[^2]: [Hung Chao-kuei: Big-5 code issues you might encounter when programming](https://frdm.cyut.edu.tw/~ckhung/b/pl/big5.php) — Teaching page listing common characters whose second byte falls in the ASCII danger zone (Hsu kung tsai, Chia yeh cheng tsun kung), and introducing the scanning tool b5tm. No job title listed at the bottom of the page. iThome referred to him as associate professor in 2015. His personal homepage lists his tenure from 1997 to 2023 at Chaoyang University of Technology's Department of Information Management, retiring in August 2023.

[^3]: [git-config: core.quotePath](https://git-scm.com/docs/git-config) — Official documentation explaining that paths with bytes above 0x80 are displayed as octal escape sequences by default.

[^4]: [Python 3: open()](https://docs.python.org/3/library/functions.html#open) — Function documentation noting that when encoding is not specified, the system locale may be used as the default encoding.

[^5]: [Wikipedia: Big5 code](https://zh.wikipedia.org/zh-tw/大五碼) — Lists "kung" at 0xA55C, "Hsu" at 0xB35C, "tsai" at 0xBB5C, and explains that this issue is jokingly referred to as "Hsu kung tsai."

[^6]: [iThome: Interview with Hung Chao-kuei](https://www.ithome.com.tw/news/93606) — 2015 interview, the article refers to him as associate professor in the Department of Information Management at Chaoyang University of Technology. The original page often returns 403; the quote about Microsoft's lifespan is paraphrased from search-result snippets, not treated as verbatim.

[^7]: [Dark Thread: Stealth Shield — Solving VS2015 source file BIG5 compatibility issues](https://blog.darkthread.net/blog/big5-utf8-source-code-batch-converter/) — 2015 record of compile errors caused by Hsu kung tsai when compiling BIG5 source files with Visual Studio 2015. The article includes the line "had no choice but to say goodbye to VS2015."

[^8]: [taiwan-md PR #1260](https://github.com/frank890417/taiwan-md/pull/1260) — Merged 2026-07-26. Before the fix, categories on Windows were all `root`: 4546. After the fix, Technology zh: 59. Also removed emoji that caused the cp950 console to crash.
