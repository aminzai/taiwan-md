---
title: 'The Backslash in the Character "Gong": The Two Layers of Default Tax Paid by Taiwan Engineers Daily'
description: 'On Windows 11 in the zh-TW locale, a translation status script dumped over 4,000 paths into `root`, making Technology zero, while Linux CI was green the same week. The script split category names by forward slashes, but the filesystem used backslashes, so it couldn''t split them. An older layer is hidden in the characters: the second byte of Big5''s "Gong" is the ASCII backslash, known in the dev community as "Xu Gong Gai". Neither the path format nor the symbols residing in the characters accounted for this machine''s defaults. Git''s `quotePath` is another line, with a different cause.'
date: 2026-08-13
category: 'Technology'
tags:
  [
    'Open Source',
    'Windows',
    'Big5',
    'UTF-8',
    'Character Encoding',
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
translatedAt: '2026-09-11T17:49:31+08:00'
---

> **30-Second Overview:** I ran the translation status script, and the screen displayed 4546, all under `root`. The Linux CI on GitHub was green. Only later did I clearly see two things. The backslashes in Windows paths could not be split by the script's forward slashes. The second half of "Gong"'s Big5 code is itself the ASCII `\`. These are two different mechanisms, but they often appear together on the same Traditional Chinese Windows machine.

I maintain Taiwan.md's translation status script on Windows 11 in the zh-TW locale. That night, I ran `i18n-status.py` as usual, waiting for the terminal to print the numbers. The console was cp950. There were no red error messages.

The screen stopped at 4546. All of them were in a single category called `root`. Technology was 0.

That same week, after pushing to GitHub, the CI on Linux was green.

The script variable was named `zh_articles`, scanning paths under `knowledge` excluding English, `about`, and underscore directories; Japanese, Korean, and Arabic would also be counted. That night, it couldn't even split the category names, and over 4,000 paths were stuffed into a single cell. No exceptions, no warnings. The statistics looked like the entire site was broken, with not a single file missing. [^8]

The paths on the disk were `knowledge\Technology\SomeArticle.md`, with folders separated by backslashes. The script used `split('/')` to extract the category name. On Linux, this line works because the paths are naturally forward slashes. On Windows, it cannot split backslashes, returning the entire path as is, and the article was dumped into the default `root`. [^1]

After changing it to let `pathlib` handle directories, there were 59 articles under Technology, consistent with what was in the folders. The only thing separating them was an assumption: which line your machine uses to separate folders.

> **📝 Curator's Note:** The script syntax was not wrong, and CI did indeed run tests. The rupture was between "the machine the author actually sits at" and "the machine the tool assumes you sit at." This gap belongs to no single component, so no one is responsible for watching it.

## The Line Inside "Gong"

Paths are the first layer. The second layer is much older, hidden within the characters.

Big5 was finalized in 1984, with two bytes per Chinese character. If the second byte falls between `0x40` and `0x7E`, it overlaps with common ASCII symbols: `[`, `]`, `{`, `}`, `\`, `|`. Former Associate Professor Hong Chao-gui (洪朝貴) of the Department of Information Management at Chaoyang University of Technology (retired August 2023) wrote on his teaching page: "Since 40-7E is the ASCII code range for general common characters, it sometimes brings some troubles to programmers." [^2]

"Gong"'s code is `A5 5C`. That `0x5C` at the end is the backslash `\` in ASCII. A program that scans strings byte-by-byte and treats `\` as an escape or delimiter, when encountering the second half of "Gong", will think it has encountered a path. If a filename contains "Gong", or a path contains "Gong", both might stumble here.

The dev communities in Taiwan and Hong Kong call it "Xu Gong Gai" (許功蓋): "Xu" is `B3 5C`, "Gong" is `A5 5C`, "Gai" is `BB 5C`. Three common characters written together look like a person's name. [^5] Hong Chao-gui also listed "Jia, Ye, Cheng, Zhen, Gong" (加也程陣功), whose second codes hit `[`, `]`, `{`, `}`, `\` respectively, and created a scanning tool `b5tm`. [^2] A bug given a person's name usually means it appears frequently enough that a generation must be able to point at it and speak of it.

In 2015, the author of the blog "Dark Execution Thread" (黑暗執行緒) switched to Visual Studio 2015. Old `.cs` files were still saved in BIG5. After the compiler switched to Roslyn, the Xu Gong Gai in the files would become compilation errors.

Two days later, a colleague told him that they had also switched and struggled for a long time, finally crawling back to his article through search results. One netizen had tens of thousands of files, converted some but still had many left, "so had to say Goodbye to VS2015". He later wrote a batch tool to convert to UTF-8 because manual saving was impossible. [^7]

This is not the same issue as the `split('/')` above. One is a modern tool assuming what a path looks like. The other is a symbol living inside the character's body after choosing double-byte encoding forty years ago. The mechanisms are different, but the bill often comes together on the same cp950 machine. How the input side sends characters to the computer is covered in [East Asian Input Methods](/en/technology/east-asian-input-methods/). Here we discuss what happens after the characters are already on the disk, and whether the toolchain still recognizes them.

## Defaults Do Not Branch for This Machine

Git has `core.quotePath` enabled by default. For filenames with bytes greater than `0x80`, `git status` prints them as octal sequences like `\344\270\255`. The Chinese filenames are still there; you just can't understand what your repository is saying every day. [^3] It escapes UTF-8 high bytes. Big5's `0x5C` is another line. They both look like backslashes, but the causes are different.

If Python 3 on Windows does not specify `encoding='utf-8'` in `open()`, it may use the system locale. The same UTF-8 file reads fine on Linux, but this machine decodes it with cp950, corrupting punctuation or bopomofo. [^4] I paid for this once myself: using PowerShell 5.1's `Get-Content | Set-Content` to modify a UTF-8 file, the long dash became `??` in the diff. That was also a default tax, but not the second theme.

When status messages include emojis, this cp950 console crashes directly. The character set does not contain those symbols, Python cannot print them, and the exception explodes to the top level. Linux CI cannot test for this because it does not run on this machine.

Git, Python, and CI example paths like `$HOME/project/src` do not have a branch for zh-TW Windows.

In a 2015 interview with iThome, Hong Chao-gui discussed what format government files should be opened in and how long they would survive. The report paraphrased his meaning: If the government only uses Microsoft products to open file data, it is equivalent to believing that Microsoft's lifespan will be longer than that of the Republic of China. [^6] That statement was about file formats and preservation periods. When data is bound to a set of default tools, stretching the timeline becomes a question of who can still read it. Open-source collaboration is bound to the default environment of a certain type of machine. The tension between civic tech and government file formats is covered in [Open Source Communities and g0v](/en/technology/open-source-and-g0v/). Taiwan developers have long absorbed the culture of this gap, covered in [Taiwan Open Source Spirit](/en/technology/taiwan-open-source-spirit/).

Path separators, terminal encodings, and `$HOME` in CI examples do not have branches for this machine. On the day 4,546 paths were misclassified, not a single line of code threw an error. The statistics looked normal until you sat in front of this machine.

## Further Reading

- [Taiwan Open Source Spirit](/en/technology/taiwan-open-source-spirit): The culture and context of Taiwan developers participating in open source.
- [East Asian Input Methods](/en/technology/east-asian-input-methods): How characters are typed into computers, from character sets to keyboards.
- [Open Source Communities and g0v](/en/technology/open-source-and-g0v): Collaboration between open data and government formats.

## References

[^1]: [Microsoft Learn: File Path Formats on Windows Systems](https://learn.microsoft.com/zh-tw/dotnet/standard/io/file-path-formats) — .NET documentation explains that traditional DOS paths use backslashes as directory separators, and forward slashes are converted to backslashes.

[^2]: [Hong Chao-gui: Big-5 Code Issues Encountered When Programming](https://frdm.cyut.edu.tw/~ckhung/b/pl/big5.php) — The teaching page lists common characters whose second codes fall into the ASCII danger zone (Jia, Ye, Cheng, Zhen, Gong) and introduces the scanning tool b5tm. The page footer does not list a job title. iThome in 2015 referred to him as Associate Professor. His personal homepage lists his tenure at Chaoyang University of Technology's Information Management Department from 1997 to 2023, retiring in August 2023.

[^3]: [git-config: core.quotePath](https://git-scm.com/docs/git-config) — Official documentation explains that by default, paths with bytes greater than 0x80 are displayed as octal escape sequences.

[^4]: [Python 3: open()](https://docs.python.org/3/library/functions.html#open) — Function documentation states that if encoding is not specified, the system locale may be used as the default encoding.

[^5]: [Wikipedia: Big5](https://zh.wikipedia.org/zh-tw/大五碼) — States that "Gong" is 0xA55C, "Xu" is 0xB35C, "Gai" is 0xBB5C, and explains that this issue is jokingly called Xu Gong Gai.

[^6]: [iThome: Hong Chao-gui Interview](https://www.ithome.com.tw/news/93606) — 2015 interview, article refers to him as Associate Professor of Information Management at Chaoyang University of Technology. The original page often returns 403; the "Microsoft lifespan" quote is only adopted from search result-visible report paraphrases, not treated as a verbatim original quote.

[^7]: [Dark Execution Thread: Stealth Fighter - Solving VS2015 Program File BIG5 Compatibility Issues](https://blog.darkthread.net/blog/big5-utf8-source-code-batch-converter/) — 2015 record of Visual Studio 2015 compilation errors caused by Xu Gong Gai when compiling BIG5 source code. The article contains "had to say Goodbye to VS2015".

[^8]: [taiwan-md PR #1260](https://github.com/frank890417/taiwan-md/pull/1260) — Merged on 2026-07-26. Before fix, categories on Windows were only root: 4546; after fix, Technology zh: 59. Also removed emojis that would crash the cp950 console.
