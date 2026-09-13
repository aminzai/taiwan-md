---
title: 'Backslash di dalam karakter "Gōng": Dua lapis pajak default yang dibayar insinyur Taiwan setiap hari'
description: 'Di Windows 11 berbahasa zh-TW, skrip status terjemahan memasukkan lebih dari empat ribu jalur yang dipindai ke dalam "root", membuat Technology menjadi nol, sementara CI Linux pada minggu yang sama menunjukkan hijau. Skrip menggunakan slash forward untuk memisahkan nama kategori, sedangkan disk menggunakan backslash, sehingga tidak dapat memisahkannya. Lapisan lebih tua tertanam di dalam karakter: byte kedua Big5 dari "Gōng" adalah backslash ASCII, yang disebut "Xǔ Gōng Gài" oleh komunitas pengembang. Baik cara penulisan jalur maupun simbol yang berada di dalam karakter, nilai default tidak memasukkan mesin ini ke dalam perhitungan. quotePath Git adalah garis lain, dengan penyebab yang berbeda.'
date: 2026-08-13
category: 'Technology'
tags:
  [
    'open source',
    'Windows',
    'Big5',
    'UTF-8',
    'encoding karakter',
    'Tionghoa tradisional',
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
translatedAt: '2026-09-13T05:56:48+08:00'
---

> **Ringkasan 30 detik:** Saya menjalankan skrip status terjemahan, layar menampilkan 4546, semuanya di `root`. GitHub CI di Linux hijau. Baru kemudian terlihat dua hal. Backslash jalur Windows, skrip menggunakan slash forward tidak bisa memisahkannya. Byte kedua Big5 "Gōng", sendiri adalah ASCII `\`. Dua hal mekanismenya berbeda, namun sering muncul bersama di Windows zh-TW yang sama.

Saya memelihara skrip status terjemahan Taiwan.md di Windows 11 berbahasa zh-TW. Malam itu seperti biasa menjalankan `i18n-status.py`, menunggu terminal mencetak angka. Konsol adalah cp950. Keluaran tidak ada teks merah.

Layar berhenti di 4546. Semuanya di satu kategori bernama `root`. Technology adalah 0.

Minggu yang sama dipush ke GitHub, CI di Linux lampu hijau.

Variabel skrip bernama `zh_articles`, memindai `knowledge` kecuali direktori bahasa Inggris, about, dan underscore, bahasa Jepang, Korea, Arab juga dihitung. Malam itu ia bahkan tidak bisa memotong nama kategori, lebih dari empat ribu jalur dimasukkan ke kotak yang sama. Tidak ada pengecualian, tidak ada peringatan. Statistik terlihat seperti seluruh situs rusak, file tidak berkurang satu pun.[^8]

Jalur di disk adalah `knowledge\Technology\artikel-tertentu.md`, folder dipisahkan backslash. Skrip menggunakan `split('/')` mengambil nama kategori. Di Linux baris ini berfungsi, karena jalur memang slash forward. Di Windows ia tidak memotong backslash, seluruh jalur kembali utuh, artikel dibuang ke `root` default.[^1]

Setelah diubah biarkan `pathlib` menangani direktori, Technology di bawahnya 59 artikel, konsisten dengan isi folder. Di antara keduanya hanya terpisah satu asumsi: mesin Anda menggunakan garis apa untuk memisahkan folder.

> **📝 Catatan Kurator:** Sintaks skrip tidak salah, CI memang menjalankan tes. Retaknya berada di antara "mesin tempat penulis duduk" dan "mesin yang dikira alat tempat Anda duduk". Celah ini tidak milik tahap manapun, sehingga tidak ada yang bertanggung jawab memantau.

## Di dalam "Gōng" garis itu

Jalur adalah lapisan pertama. Lapisan kedua lebih tua, tertanam di dalam karakter.

Big5 ditetapkan 1984, satu karakter Tionghoa dua byte. Byte kedua jika jatuh di `0x40` sampai `0x7E`, tumpang tindih dengan simbol ASCII umum: `[`, `]`, `{`, `}`, `\`, `|`. Mantan wakil dekan Fakultas Manajemen Informasi Universitas Teknologi Chaoyang Hong Chao-kuei (洪朝貴, pensiun Agustus 2023) menulis di halaman pengajaran: "Karena 40-7E adalah rentang kode ASCII karakter umum, terkadang membawa kesulitan bagi programmer."[^2]

Kode "Gōng" adalah `A5 5C`. `0x5C` belakang itu, di ASCII adalah backslash `\`. Program memindai per byte, memperlakukan `\` sebagai escape atau pemisah, memindai belakang "Gōng", akan mengira menemui jalur. Nama file ada "Gōng", jalur ada "Gōng", semua mungkin tersandung di sini.

Pengembang Taiwan dan Hong Kong menyebutnya "Xǔ Gōng Gài": "Xǔ" adalah `B3 5C`, "Gōng" adalah `A5 5C`, "Gài" adalah `BB 5C`, tiga karakter umum ditulis berurutan seperti nama orang.[^5] Hong Chao-kuei juga mencantumkan "Jiā Yě Chéng Zhèn Gōng", byte kedua masing-masing menabrak `[`, `]`, `{`, `}`, `\`, dan membuat alat pemindaian `b5tm`.[^2] Sebuah bug diberi nama orang, biasanya karena muncul cukup sering, satu generasi harus punya cara menunjuk dan berbicara tentangnya.

2015, penulis blog "Dark Thread" (黑暗執行緒) berganti Visual Studio 2015. `.cs` lama masih disimpan BIG5. Compiler beralih ke Roslyn, Xǔ Gōng Gài di file menjadi error kompilasi.

Dua hari kemudian rekan berkata, mereka berganti juga macet lama, akhirnya merayap kembali ke artikelnya. Netizen punya ribuan file, konversi satu masih banyak, "terpaksa ucapkan Goodbye ke VS2015". Ia kemudian menulis alat batch konversi UTF-8, karena simpan manual tidak selesai.[^7]

Ini bukan hal yang sama dengan `split('/')` sebelumnya. Satu adalah alat modern mengasumsikan jalur berbentuk apa. Satu adalah empat puluh tahun lalu memilih dua byte, tubuh karakter menampung simbol. Mekanisme berbeda, tagihan namun sering datang bersama di mesin cp950 yang sama. Sisi input bagaimana memasukkan karakter ke komputer, lihat metode input teks Asia Timur (東亞文字輸入法)。Di sini membahas karakter sudah di disk, rantai alat apakah masih mengenalnya.

## Nilai default tidak membuka cabang untuk mesin ini

Git default mengaktifkan `core.quotePath`. Byte lebih besar `0x80` nama file, `git status` mencetak `\344\270\255` octal semacam itu. Nama file Tionghoa masih ada, hanya Anda tiap hari tidak mengerti gudang sendiri bicara apa.[^3] Ia escape byte tinggi UTF-8. Big5 `0x5C` garis lain. Terlihat sama-sama backslash, penyebab berbeda.

Python 3 di Windows jika `open()` tidak tulis `encoding='utf-8'`, mungkin mengikuti bahasa sistem. File UTF-8 yang sama, Linux baca lolos, mesin ini pakai cp950 decode, tanda baca atau zhuyin rusak.[^4] Saya sendiri bayar sekali: pakai PowerShell 5.1 `Get-Content | Set-Content` ubah file UTF-8, dash panjang di diff jadi `??`. Itu juga pajak default, bukan tema kedua.

Pesan status bawa emoji, konsol cp950 ini langsung crash. Charset tidak punya simbol itu, Python tidak cetak, exception meledak ke lapisan atas. CI Linux tidak tes hal ini, karena tidak di mesin ini jalan.

Git, Python, contoh jalur CI `$HOME/project/src`, tidak untuk Windows zh-TW buka cabang lain.

Hong Chao-kuei 2015 diwawancara iThome, bahas file pemerintah pakai format apa buka, bisa hidup berapa lama. Liputan merangkum maksudnya: jika pemerintah hanya pakai produk Microsoft buka file data, sama saja percaya umur Microsoft lebih panjang dari Republik Tiongkok.[^6] Kalimat itu bahas format file dan batas preservasi. Data terikat alat default mana, waktu ditarik panjang, jadi siapa masih bisa baca. Kolaborasi open source terikat lingkungan default mesin tertentu. Tarik-menarik teknologi sipil dan format file pemerintah, lihat [komunitas open source dan g0v](/id/technology/open-source-and-g0v/). Budaya pengembang Taiwan lama menyerap kesenjangan ini, lihat semangat open source Taiwan (台灣開源精神)。

Pemisah jalur, encoding terminal, `$HOME` di contoh CI, tidak ada cabang untuk mesin ini. Hari 4546 jalur salah kategori, tidak ada satu baris kode lapor error. Statistik terlihat normal, sampai Anda duduk di depan mesin ini.

## Bacaan Lanjutan

- [semangat open source Taiwan](/id/technology/taiwan-open-source-spirit)：Budaya dan konteks pengembang Taiwan berpartisipasi open source.
- [metode input teks Asia Timur](/technology/東亞文字輸入法)：Karakter कैसे diketik ke komputer, dari tabel kode ke keyboard.
- [komunitas open source dan g0v](/id/technology/open-source-and-g0v)：Kolaborasi data terbuka dan format pemerintah.

## Referensi

[^1]: [Microsoft Learn: Format jalur file di sistem Windows](https://learn.microsoft.com/zh-tw/dotnet/standard/io/file-path-formats) — Dokumentasi .NET menjelaskan jalur DOS tradisional menggunakan backslash sebagai pemisah direktori, slash forward dikonversi ke backslash.

[^2]: [Hong Chao-kuei: Masalah kode Big-5 yang mungkin dihadapi saat menulis program](https://frdm.cyut.edu.tw/~ckhung/b/pl/big5.php) — Halaman pengajaran mencantumkan karakter umum byte kedua jatuh di zona bahaya ASCII (Jiā Yě Chéng Zhèn Gōng), dan memperkenalkan alat pemindaian b5tm. Akhir halaman tidak tulis jabatan. 2015 iThome sebut wakil dekan. Halaman pribadi muat 1997-2023 jabatan Manajemen Informasi Chaoyang, pensiun Agustus 2023.

[^3]: [git-config: core.quotePath](https://git-scm.com/docs/git-config) — Dokumentasi resmi menjelaskan default akan menampilkan jalur byte lebih besar 0x80 sebagai urutan escape oktal.

[^4]: [Python 3: open()](https://docs.python.org/3/library/functions.html#open) — Dokumentasi fungsi menegaskan encoding tidak ditentukan, mungkin mengikuti bahasa sistem sebagai encoding default.

[^5]: [Wikipedia: Kode Big5](https://zh.wikipedia.org/zh-tw/大五碼) — Mencantumkan "Gōng" 0xA55C, "Xǔ" 0xB35C, "Gài" 0xBB5C, dan menjelaskan masalah ini disebut Xǔ Gōng Gài.

[^6]: [iThome: Wawancara Hong Chao-kuei](https://www.ithome.com.tw/news/93606) — Wawancara 2015, teks sebut wakil dekan Fakultas Manajemen Informasi Chaoyang. Halaman asing sering 403, kalimat umur Microsoft hanya pakai rangkuman hasil pencarian terlihat, tidak sebagai kutipan kata demi kata.

[^7]: [Dark Thread: Mesin terowongan - Solusi masalah kompatibilitas BIG5 file program VS2015](https://blog.darkthread.net/blog/big5-utf8-source-code-batch-converter/) — Catatan 2015 Visual Studio 2015 kompilasi kode sumber BIG5, Xǔ Gōng Gài menyebabkan error kompilasi. Teks ada "terpaksa ucapkan Goodbye ke VS2015".

[^8]: [taiwan-md PR #1260](https://github.com/frank890417/taiwan-md/pull/1260) — 2026-07-26 merged. Sebelum perbaikan Windows categories hanya root: 4546, sesudah Technology zh: 59. Satu paket buang emoji yang bikin konsol cp950 crash.
