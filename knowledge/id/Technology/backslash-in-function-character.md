---
title: 'Garis Miring dalam Karakter "Gong": Dua Lapisan Pajak Bawaan yang Dibayar Setiap Hari oleh Insinyur Taiwan'
description: 'Pada Windows 11 dengan lokalitas zh-TW, skrip status terjemahan memasukkan lebih dari empat ribu jalur yang terdeteksi ke `root`, membuat Technology menjadi nol, sementara CI Linux pada minggu yang sama berwarna hijau. Skrip menggunakan garis miring untuk memisahkan nama kategori, dan garis miring terbalik untuk disk; pemisahan gagal. Lapisan yang lebih tua tertanam dalam karakter: byte kedua dari "Gong" Big5 adalah garis miring terbalik ASCII, yang disebut oleh komunitas pengembang sebagai *Xu Gong Gai*. Cara jalur ditulis, simbol apa yang ada di dalam karakter, dan nilai bawaan semuanya tidak diperhitungkan pada mesin ini. `quotePath` Git adalah lini lain dengan penyebab yang berbeda.'
date: 2026-08-13
category: 'Technology'
tags:
  [
    'Open Source',
    'Windows',
    'Big5',
    'UTF-8',
    'Pengkodean Karakter',
    'Mandarin Tradisional',
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
translatedAt: '2026-09-14T00:53:31+08:00'
---

> **Ringkasan 30 Detik:** Saya menjalankan skrip status terjemahan, dan layar menunjukkan 4546, semuanya berada di `root`. CI Linux di GitHub berwarna hijau. Kemudian saya melihat dua hal. Garis miring terbalik pada jalur Windows tidak dapat dipisahkan oleh skrip menggunakan garis miring. Bagian belakang kode Big5 dari "Gong" itu sendiri adalah `\`, karakter ASCII. Kedua mekanisme ini berbeda, namun sering muncul bersamaan pada mesin Windows Mandarin Tradisional yang sama.

Saya memelihara skrip status terjemahan Taiwan.md di Windows 11 dengan lokalitas zh-TW. Malam itu, saya menjalankan `i18n-status.py` seperti biasa, menunggu terminal mencetak angka. Konsol utama adalah cp950. Tidak ada teks merah dalam output.

Layar berhenti pada 4546. Semuanya berada di kategori bernama `root`. Technology adalah 0.

Pada minggu yang sama, saat didorong ke GitHub, CI di Linux berwarna hijau.

Variabel skrip dinamai `zh_articles`, dan ia memindai jalur di bawah `knowledge` kecuali direktori bahasa Inggris, _about_, dan garis bawah; Jepang, Korea, dan Arab juga disertakan. Malam itu, ia bahkan tidak dapat memisahkan nama kategori, dan lebih dari empat ribu jalur dimasukkan ke dalam satu kotak. Tidak ada pengecualian, tidak ada peringatan. Statistik tampak seperti seluruh situs rusak, tanpa kehilangan satu pun file.[^8]

Jalur di disk adalah `knowledge\Technology\nama_artikel.md`, dengan garis miring terbalik memisahkan folder. Skrip menggunakan `split('/')` untuk mengambil nama kategori. Baris ini berfungsi di Linux karena jalurnya memang menggunakan garis miring. Di Windows, ia tidak dapat memotong garis miring terbalik, dan seluruh jalur dikembalikan apa adanya, artikel tersebut dibuang ke `root` bawaan.[^1]

Setelah mengubahnya agar `pathlib` menangani direktori, Technology memiliki 59 artikel di bawahnya, sesuai dengan isi folder. Hanya ada satu asumsi di antaranya: jenis garis apa yang digunakan mesin Anda untuk memisahkan folder.

> **📝 Catatan Kurator:** Sintaks skrip tidak salah, dan CI memang menjalankan pengujian. Titik patahannya terletak antara "mesin tempat penulis benar-benar duduk" dan "mesin yang diasumsikan oleh alat". Celah ini tidak termasuk dalam proses apa pun, jadi tidak ada yang bertanggung jawab untuk mengawasinya.

## Garis di Dalam "Gong"

Jalur adalah lapisan pertama. Lapisan kedua jauh lebih tua, tertanam dalam karakter.

Big5 ditetapkan pada tahun 1984, satu karakter Tionghoa menggunakan dua byte. Jika byte kedua berada di rentang `0x40` hingga `0x7E`, ia akan tumpang tindih dengan simbol umum ASCII: `[` , `]` , `{` , `}` , `\` , `|`. Seorang profesor madya Ilmu Manajemen dari Universitas Teknologi Chaoyang (yang pensiun pada Agustus 2023) pernah menulis di halaman pengajarannya: "Karena 40-7E adalah rentang kode ASCII karakter umum, terkadang ini menyebabkan kesulitan bagi para programmer."[^2]

Kode untuk "Gong" adalah `A5 5C`. Bagian belakang itu, yaitu `0x5C`, adalah garis miring terbalik ASCII (`\`). Program yang memindai string byte demi byte dan memperlakukan `\` sebagai _escape_ atau pemisah, ketika menemukan bagian belakang "Gong", akan mengira ia telah menemukan jalur. Nama file mengandung "Gong", dan jalur mengandung "Gong"; keduanya bisa tersandung di sini.

Komunitas pengembang Taiwan dan Hong Kong menyebutnya _Xu Gong Gai_: "Xu" adalah `B3 5C`, "Gong" adalah `A5 5C`, dan "Gai" adalah `BB 5C`; tiga karakter umum yang ditulis berurutan menyerupai nama orang.[^5] Hong pernah mencantumkan "Jia Ye Cheng Zhen Gong", di mana byte kedua bertabrakan dengan `[` , `]` , `{` , `}` , `\`, dan membuat alat pemindai `b5tm`.[^2] Sebuah _bug_ dinamai berdasarkan nama seseorang, biasanya karena ia muncul cukup sering sehingga satu generasi harus bisa membicarakannya.

Pada tahun 2015, penulis blog "Dark Thread" beralih ke Visual Studio 2015. File `.cs` lama masih disimpan dalam BIG5. Setelah kompiler beralih ke Roslyn, _Xu Gong Gai_ di file menjadi kesalahan kompilasi.

Dua hari kemudian, rekan kerja memberitahunya bahwa mereka juga mengalami masalah selama berhari-hari, dan akhirnya mengunduh artikelnya. Seorang pengguna internet memiliki ribuan file, mengubah satu masih menyisakan banyak lagi, "terpaksa mengucapkan selamat tinggal pada VS2015." Dia kemudian membuat alat kecil untuk konversi batch ke UTF-8 karena tidak bisa menyimpan secara manual.[^7]

Ini berbeda dengan `split('/')` sebelumnya. Yang satu adalah asumsi alat modern tentang bagaimana jalur terlihat. Yang lainnya adalah simbol yang hidup di dalam tubuh karakter setelah dua byte dipilih empat puluh tahun lalu. Mekanismenya berbeda, tetapi tagihan sering datang bersama pada mesin cp950 yang sama. Bagaimana input dikirim ke komputer dari sisi pengetikan dapat dilihat di [Metode Input Karakter Asia Timur](/id/technology/east-asian-input-methods/). Di sini kita berbicara tentang apakah _toolchain_ masih mengenalinya setelah karakter berada di disk.

## Nilai Bawaan Tidak Membuat Cabang untuk Mesin Ini

Git secara bawaan mengaktifkan `core.quotePath`. Nama file dengan byte lebih besar dari `0x80` akan dicetak oleh `git status` sebagai urutan _escape_ oktal seperti `\344\270\255`. Karakter Tionghoa masih ada, Anda hanya tidak mengerti apa yang dikatakan repositori Anda setiap hari.[^3] Ini adalah _escape_ untuk byte tinggi UTF-8. `0x5C` Big5 adalah lini lain. Keduanya terlihat seperti garis miring terbalik, tetapi penyebabnya berbeda.

Di Windows, jika Python 3 menggunakan `open()` tanpa menulis `encoding='utf-8'`, ia mungkin mewarisi lokalitas sistem. File UTF-8 yang sama dapat dibaca oleh Linux, tetapi rusak ketika diuraikan dengan cp950 pada mesin ini; tanda baca atau _bopomofo_ akan rusak.[^4] Saya pernah mengalaminya: menggunakan `Get-Content | Set-Content` PowerShell 5.1 untuk mengubah file ke UTF-8, dan garis miring panjang berubah menjadi `??` dalam _diff_. Itu juga pajak bawaan, bukan topik kedua.

Ketika pesan status menyertakan emoji, konsol cp950 ini akan langsung _crash_. Set karakter tidak memiliki simbol-simbol itu; Python tidak dapat mencetaknya, sehingga pengecualian meledak di lapisan teratas. CI Linux tidak bisa mendeteksi hal ini karena ia tidak berjalan di mesin ini.

Git, Python, dan contoh jalur CI `$HOME/project/src` tidak membuat cabang khusus untuk Windows zh-TW.

Pada tahun 2015, Hong diwawancarai oleh iThome mengenai format apa yang harus digunakan untuk membuka file pemerintah dan berapa lama ia dapat bertahan. Laporan itu mengutip maksudnya: jika pemerintah hanya menggunakan produk Microsoft untuk membuka data file, sama saja dengan mempercayai bahwa masa pakai Microsoft akan lebih lama daripada Republik Tiongkok (Taiwan).[^6] Kalimat itu berbicara tentang format file dan masa simpan. Data terikat pada seperangkat alat bawaan, dan seiring berjalannya waktu, muncullah pertanyaan siapa yang masih bisa membacanya. Kolaborasi _open source_ terikat pada lingkungan bawaan mesin tertentu. Ketegangan antara teknologi warga negara dan format file pemerintah dapat dilihat di [Komunitas Open Source dan g0v](/id/technology/open-source-and-g0v/). Budaya menyerap kesenjangan ini dalam jangka panjang oleh pengembang Taiwan dapat dilihat di [Semangat Open Source Taiwan](/id/technology/taiwan-open-source-spirit/).

Pemisah jalur, pengkodean terminal, dan `$HOME` dalam contoh CI tidak membuat cabang khusus untuk mesin ini. Pada hari ketika 4546 jalur diklasifikasikan secara salah, tidak ada satu baris kode pun yang melaporkan kesalahan. Statistik tampak normal, sampai Anda duduk di depan mesin ini.

## Bacaan Lanjutan

- [Semangat Open Source Taiwan](/id/technology/taiwan-open-source-spirit): Budaya dan konteks partisipasi pengembang Taiwan dalam _open source_.
- [Metode Input Karakter Asia Timur](/id/technology/east-asian-input-methods): Bagaimana karakter diketik ke komputer, dari tabel kode hingga papan ketik.
- [Komunitas Open Source dan g0v](/id/technology/open-source-and-g0v): Kolaborasi antara data terbuka dan format pemerintah.

## Referensi

[^1]: [Microsoft Learn: Format Jalur File pada Sistem Windows](https://learn.microsoft.com/zh-tw/dotnet/standard/io/file-path-formats) — Dokumentasi .NET menjelaskan bahwa DOS tradisional menggunakan garis miring terbalik sebagai pemisah direktori, dan garis miring akan diubah menjadi garis miring terbalik.

[^2]: [Hong: Masalah Kode Big-5 Saat Pemrograman](https://frdm.cyut.edu.tw/~ckhung/b/pl/big5.php) — Halaman pengajaran mencantumkan karakter umum (Jia Ye Cheng Zhen Gong) yang byte keduanya berada di zona berbahaya ASCII, dan memperkenalkan alat pemindai b5tm. Gelar tidak disebutkan di akhir halaman. Di iThome pada tahun 2015 disebut profesor madya. Saya mengajar di Manajemen Informasi Chaoyang dari 1997 hingga 2023, pensiun Agustus 2023.

[^3]: [git-config: core.quotePath](https://git-scm.com/docs/git-config) — Dokumentasi resmi menjelaskan bahwa secara bawaan, jalur dengan byte lebih besar dari 0x80 akan ditampilkan sebagai urutan _escape_ oktal.

[^4]: [Python 3: open()](https://docs.python.org/3/library/functions.html#open) — Deskripsi fungsi menunjukkan bahwa jika `encoding` tidak ditentukan, ia mungkin mewarisi lokalitas sistem sebagai pengkodean bawaan.

[^5]: [Wikipedia: Big5](https://zh.wikipedia.org/zh-tw/大五碼) — Mencantumkan "Gong" 0xA55C, "Xu" 0xB35C, dan "Gai" 0xBB5C, dan menjelaskan masalah ini dijuluki _Xu Gong Gai_.

[^6]: [iThome: Wawancara Eksklusif Hong](https://www.ithome.com.tw/news/93606) — Wawancara tahun 2015, menyebutnya profesor madya Ilmu Manajemen Universitas Teknologi Chaoyang. Laporan tersebut mengutip maksudnya: jika pemerintah hanya menggunakan produk Microsoft untuk membuka data file, sama saja dengan mempercayai bahwa masa pakai Microsoft akan lebih lama daripada Republik Tiongkok (Taiwan).

[^7]: [Dark Thread: Penjaga Bayangan - Menyelesaikan Masalah Kompatibilitas File BIG5 VS2015](https://blog.darkthread.net/blog/big5-utf8-source-code-batch-converter/) — Mencatat kesalahan kompilasi _Xu Gong Gai_ saat mengkompilasi kode sumber Visual Studio 2015 dalam BIG5 pada tahun 2015. Artikel tersebut menyebutkan "terpaksa mengucapkan selamat tinggal pada VS2015".

[^8]: [taiwan-md PR #1260](https://github.com/frank890417/taiwan-md/pull/1260) — Digabungkan pada 2026-07-26. Sebelum perbaikan, kategori di Windows hanya menyisakan root: 4546; setelah diperbaiki Technology zh: 59. Emoji yang menyebabkan _crash_ konsol cp950 juga dihapus.
