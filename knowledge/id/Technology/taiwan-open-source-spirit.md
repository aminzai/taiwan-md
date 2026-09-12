---
title: 'Semangat Open Source Taiwan — Para Insinyur yang "Ditenagai Cinta"'
description: 'Proyek open source paling berpengaruh Taiwan bukanlah sebuah perangkat lunak, melainkan sekelompok insinyur yang di hackathon berkata kepada pemerintah: "Kalian tidak bisa melakukannya dengan baik, kami yang akan melakukannya."'
date: 2026-03-29
category: 'Technology'
tags:
  [
    'open source',
    'g0v',
    'COSCUP',
    'GitHub',
    'teknologi sipil',
    'perangkat lunak bebas',
  ]
subcategory: '社群與數位文化'
author: 'p3nchan'
featured: false
lastVerified: 2026-03-29
lastHumanReview: false
readingTime: 8
translatedFrom: 'Technology/台灣開源精神.md'
sourceCommitSha: '4b6d28c54'
sourceContentHash: 'sha256:8cc121a9cccbf90a'
sourceBodyHash: 'sha256:98feb4bab36f053f'
translatedAt: '2026-09-13T05:56:48+08:00'
---

> Skala industri perangkat lunak Taiwan tidak termasuk barisan depan global, namun pengguna GitHub yang menandai Taiwan melebihi 44.000 orang, hackathon komunitas kumulatif lebih dari 70 kali, ribuan kontributor — hampir semuanya pengembang individu yang mengeluarkan uang sendiri setelah jam kerja. Artikel ini tidak hanya membahas g0v, melainkan dari empat sudut pandang: manusia, komunitas, pendidikan, industri, menyusun peta lengkap budaya open source Taiwan.

---

## Sebuah Iklan yang Memicu Hackathon

Oktober 2012, Yuan Administratif (行政院) menayangkan iklan 40 detik di televisi, mempromosikan "Rencana Peningkatan Momentum Ekonomi". Isi iklan hanya satu kalimat: "Rencana ini benar-benar kompleks, tidak bisa dijelaskan dengan jelas hanya dalam beberapa kalimat sederhana."

Kao Chia-liang (clkao), lulusan Ilmu Komputer Universitas Taiwan, menonton iklan itu lalu membuka komputer. Ia dan beberapa teman berpartisipasi dalam Yahoo! Open Hack Day, mengganti topik secara mendadak, dan dalam tiga hari menulis proyek "Visualisasi Anggaran Pemerintah Pusat", meraih penghargaan runner-up. Dua bulan kemudian, Kao Chia-liang mendaftarkan g0v.tw, menggunakan uang hadiah untuk mengadakan "Hackathon Mobilisasi Periode Nol".

Penamaan g0v mengganti huruf o pada gov (pemerintah) dengan angka 0. Artinya sangat langsung: kalian tidak melakukannya dengan baik, kami yang akan melakukannya.

Ini bukan sebuah organisasi. g0v tidak memiliki kantor, tidak memiliki dewan direksi, tidak memiliki karyawan penuh waktu. Ia adalah komunitas terdesentralisasi, dipertahankan oleh hackathon dua bulanan. Hingga akhir 2025, hackathon telah diadakan lebih dari 70 kali, Slack memiliki lebih dari 8.000 anggota, HackMD mengumpulkan lebih dari 4.500 catatan kolaboratif.

---

## 72 Jam, 100 Aplikasi

Momen g0v paling terlihat secara internasional adalah 2020.

Awal pandemi COVID-19, Taiwan menerapkan kebijakan masker real-name. Kementerian Kesehatan dan Kesejahteraan (衛福部) merilis API terbuka stok masker apotek, pada saat itu Komisaris Digital Audrey Tang mengumumkan berita tersebut di saluran obrolan g0v. 72 jam berikutnya, komunitas pengembang Taiwan meledak dengan energi kolaboratif yang belum pernah terlihat: Chiang Ming-tsung (kiang) membuat peta masker apotek, Jarvis Lin membuat aplikasi Android, bot obrolan LINE juga diluncurkan di hari yang sama.

Dalam seminggu, aplikasi terkait pencarian masker melebihi 100. Perkiraan insinyur yang berpartisipasi mendekati seribu orang.

《Foreign Affairs》 menerbitkan artikel khusus _Civic Technology Can Help Stop a Pandemic_, menyebut Taiwan menunjukkan jalan ketiga yang berbeda dari pengawasan bergaya Tiongkok, juga berbeda dari raksasa teknologi Barat: inovasi demokrasi yang didorong oleh teknologi sipil (civic tech). Laporan Fakultas Kedokteran Stanford mencatat 124 langkah intervensi independen yang diterapkan Taiwan selama pandemi. NPR, MIT Technology Review, Harvard Business Review semuanya membuat liputan khusus.

Ini bukan kredit pemerintah, juga bukan hanya kredit Audrey Tang. Ini adalah sekelompok insinyur tanpa gaji, di akhir pekan membuka laptop dan menciptakannya.

---

## Sebelum Audrey Tang: Akar Open Source Taiwan

g0v mampu terbentuk cepat pada 2012 karena Taiwan sudah memiliki dua puluh tahun tanah open source.

Audrey Tang (唐鳳) belajar Perl usia 12 tahun, usia 14 tahun keluar sekolah dan berwirausaha. Sebelum memasuki pemerintah, ia di CPAN (platform modul Perl) memulai lebih dari 100 proyek, memimpin Pugs — implementasi pertama yang bisa dijalankan dari Perl 6 menggunakan Haskell, dan bersama bapak spreadsheet Dan Bricklin mengembangkan EtherCalc. Ia adalah tokoh kepemimpinan yang diakui komunitas Perl dan Haskell, pengaruhnya di lingkaran open source internasional jauh lebih awal dari karir politiknya.

Hung Jen-yu (PCMan) adalah tokoh representatif lain. Ia adalah dokter penyakit dalam, SMA belajar pemrograman mandiri, menulis perangkat lunak koneksi BBS PCMan. 2006 ia memulai proyek LXDE — lingkungan desktop Linux ringan. LXDE pernah menjadi lingkungan desktop utama dengan penggunaan memori terendah global, diadopsi oleh Knoppix, Lubuntu, dan distribusi lain. Seorang dokter Taiwan menulis lingkungan desktop, berjalan di mesin Linux di seluruh dunia. Hung Jen-yu kemudian bergabung ke Google, tapi kisah LXDE menggambarkan ciri khas kontributor open source Taiwan: profesi utama bukan perangkat lunak, menggunakan waktu luang menciptakan proyek kelas internasional.

Huang Ching-chun (jserv) menempuh jalur lain. Ia di MediaTek (聯發科)、Andes Technology (晶心科技) berpartisipasi pengembangan perangkat lunak sistem, kemudian mengajar di Jurusan Ilmu Komputer Universitas Cheng Kung, membuka mata kuliah "Desain Inti Linux" — satu-satunya mata kuliah universitas Taiwan yang secara sistematis membedah kernel Linux terbaru. Mahasiswanya langsung mengirim patch ke Linux, glibc, GCC, LLVM. Ia berkali-kali berbicara di COSCUP dan FOSDEM Eropa. jserv mewakili bukan kontributor "jenius", melainkan upaya menanamkan praktik open source ke dalam sistem pendidikan.

---

## Ekosistem Komunitas: Bukan Hanya COSCUP

Kepadatan komunitas open source Taiwan, di Asia terhitung luar biasa.

**COSCUP** (Conference for Open Source Coders, Users and Promoters) bermula 2006, adalah konferensi open source tahunan terbesar Taiwan. Hingga 2024, peserta melebihi 2.800 orang, ruang komunitas (community rooms) lebih dari 40, mencakup Kubernetes, PostgreSQL, Ruby, Python, Blockchain, dll. Setiap ruang komunitas memiliki sekitar 6 jam jadwal, direncanakan mandiri oleh masing-masing komunitas. COSCUP tidak memungut tiket masuk. Relawan lebih dari seratus orang, semuanya tanpa imbalan. 2025 adalah edisi ke-20 COSCUP.

**SITCON** (Students' Information Technology Conference) bermula 2013, sepenuhnya diinisiasi dan diorganisasi mahasiswa. Eksistensinya bermakna: membiarkan siswa SMA 18 tahun melihat, kamu tidak perlu menunggu lulus untuk berpartisipasi open source. SITCON tiap tahun Maret mengadakan konferensi tahunan, serta HackGen semesteran, kamp musim panas, pertemuan dua mingguan.

**PyCon TW** adalah konferensi tahunan komunitas Python, mengumpulkan pengguna Python lintas bidang. **MozTW** adalah komunitas relawan Mozilla Taiwan, sejak 2004 memelihara versi Mandarin tradisional Firefox, mengelola program duta kampus, tim terjemahan subtitle. Ruang komunitas "MozTW Workshop" Taipei beroperasi 2014–2023, setelah sponsor Mozilla berakhir dipertahankan oleh donasi lokal.

Antara komunitas ini ada partisipasi silang masif. Orang yang sama bisa jadi pembicara COSCUP, kontributor g0v, relawan PyCon TW. Lingkaran open source Taiwan tidak besar, tapi kepadatannya tinggi.

---

## Warisan dan Putusnya Sistem

Taiwan pernah memiliki upaya pemerintah mendorong open source.

2003, Institut Ilmu Pengetahuan Akademia Sinica (中研院) Institut Penelitian Ilmu Informasi menerima subsidi Biro Industri Kementerian Ekonomi, mendirikan "Open Source Software Foundry" (OSSF, 自由軟體鑄造場). OSSF menyediakan hosting proyek, konsultasi hukum, promosi e-newsletter, membina komunitas open source lokal lebih dari sepuluh tahun. 2015, Kementerian Sains dan Teknologi memutuskan tidak lagi mensubsidi, OSSF berhenti operasi, situs web dipelihara hingga akhir 2021 lalu ditutup.

Kehilangan OSSF tidak menimbulkan mundurnya aktivitas open source Taiwan — justru ini membuktikan, energi open source Taiwan dari awal tidak bergantung pada pemerintah. Yang benar-benar menopang ekosistem adalah "Yayasan Budaya Terbuka" (OCF, Open Culture Foundation) yang didirikan 2014. OCF didirikan bersama beberapa komunitas open source, adalah badan hukum nirlaba, memainkan peran pengelola keuangan komunitas: menerbitkan invoice untuk COSCUP, menangani donasi proyek, menyediakan konsultasi hukum lisensi open source. OCF juga bekerja sama dengan AIT, Kantor Inggris di Taiwan, Bank Dunia, dan lembaga internasional lain, mengekspor pengalaman teknologi sipil Taiwan ke internasional.

Struktur ini menarik: program pemerintah berakhir, yayasan sipil mengambil alih. Sistem tumbuh dari bawah ke atas.

---

## Alasan Struktural "Ditenagai Cinta"

Kontributor open source Taiwan, absolut mayoritas adalah individu. Tidak ada perusahaan open source kelas Red Hat, tidak ada program sponsor perusahaan skala Google Summer of Code, investasi open source perusahaan teknologi kebanyakan "mengizinkan karyawan melakukannya di waktu luang" bukan "memasukkan open source ke KPI".

Mengapa?

Industri teknologi Taiwan berpusat pada manufaktur keras dan desain IC. TSMC, MediaTek, Foxconn model bisnis dibangun pada kemampuan manufaktur dan tembok paten, bukan kode sumber terbuka. Perangkat lunak dalam ekosistem ini seringkali adalah "aksesoris pendamping keras", bukan sumber pendapatan independen. Di ribuan perusahaan jasa perangkat lunak, sembilan puluh persen melakukan integrasi sistem, melayani pasar dalam negeri.

Hasilnya: orang yang menulis kode banyak, tapi orang yang "makan dari open source" hampir tidak ada. Open source adalah urusan setelah jam kerja, urusan pertemuan komunitas, urusan hackathon Sabtu. Daftar sponsor COSCUP, kamu akan melihat perusahaan asing (Google, LINE, Trend Micro) lebih banyak dari perusahaan lokal.

Ini tidak sepenuhnya buruk. Karena open source bukan KPI, motivasi pesertanya lebih murni. Peta masker g0v bisa meledak dalam 72 jam, bukan karena ada yang turunkan work order, tapi karena seribu insinyur merasa "hal ini harus dilakukan".

Tapi model ini memiliki langit-langit. Tanpa investasi berkelanjutan tingkat perusahaan, proyek mudah stagnan setelah pemelihara inti kelelahan. Taiwan tidak kekurangan weekend hacker, kekurangan posisi pekerjaan penuh waktu yang bisa full-time investasi ke open source.

---

## Kekuatan Diam 44.000 Orang

Pengguna GitHub yang menandai Taiwan berjumlah 44.408 (statistik Maret 2026). Butuh minimal 67 pengikut untuk masuk ranking Taiwan committers.top. Mengambil populasi Taiwan 23 juta, angka ini berarti setiap 500 orang Taiwan ada satu akun GitHub aktif. Dibandingkan Jepang, Singapura, Hong Kong, aktivitas GitHub per kapita pengembang Taiwan berada di kelas atas Asia.

Lebih layak diperhatikan bukan angka, tapi jenis kontribusi. Peran pengembang Taiwan di proyek internasional, seringkali adalah "infrastruktur dasar tak terlihat": patch kernel, optimisasi compiler, terjemahan lokalisasi, penulisan dokumentasi. Mahasiswa Universitas Cheng Kung langsung mengirim kode ke kernel Linux. MozTW memelihara versi Mandarin Firefox dua puluh tahun. Kontribusi ini tidak naik berita, tapi tanpa itu perangkat lunak tidak bisa dipakai.

Komunitas open source Taiwan masih memiliki ciri Asia yang jarang: g0v menerapkan metodologi open source ke kebijakan publik. Platform vTaiwan menggunakan teknologi Polis untuk deliberasi daring, menangani lebih dari 30 isu seperti regulasi Uber, regulasi fintech. 《MIT Technology Review》 menyebutnya "sistem sederhana tapi cerdik Taiwan untuk crowdsourcing undang-undang". Ini sudah bukan soal menulis kode, ini adalah menerapkan logika kolaborasi open source ke tata kelola demokrasi.

Open source di Taiwan, dari awal bukan hanya urusan komunitas teknis. Ini adalah sebuah sikap: melihat masalah, membuka editor, mulai menulis.

---

## Referensi

1. [Manual Proyek dan Komunitas Teknologi Sipil g0v](https://g0v.hackmd.io/@jothon/ctpbook)（sumber primer）
2. [2020 Tahun Gempar, Kontribusi g0v Bukan Hanya "Peta Masker"](https://www.gvm.com.tw/article/76428) — Majalah Vision
3. [Civic Technology Can Help Stop a Pandemic](https://www.foreignaffairs.com/articles/asia/2020-03-20/how-civic-technology-can-help-stop-pandemic) — Foreign Affairs（sumber bahasa Inggris）
4. [Kekuatan Hacker Warga Negara g0v Pemerintah Nol](https://www.taiwan-panorama.com/Articles/Details?Guid=61281c3d-f79c-4db7-93d9-d18b29f90ba0) — Majalah Taiwan Panorama
5. [Pemimpin Komunitas Open Source Internasional Audrey Tang: Open Source adalah Paradigma Pertukaran Era Baru](https://www.ithome.com.tw/news/93603) — iThome
6. [Hung Jen-yu — Wikipedia](https://zh.wikipedia.org/zh-tw/%E6%B4%AA%E4%BB%BB%E8%AB%AD)
7. [Huang Ching-chun — Wikipedia](https://zh.wikipedia.org/zh-tw/%E9%BB%83%E6%95%AC%E7%BE%A4)
8. [Open Source Software Foundry — Wikipedia](https://zh.wikipedia.org/zh-tw/%E8%87%AA%E7%94%B1%E8%BB%9F%E9%AB%94%E9%91%84%E9%80%A0%E5%A0%B4)
9. [About OCF — Open Culture Foundation](https://ocf.tw/en/p/what_is_ocf_en.html)
10. [committers.top — Pengguna GitHub Paling Aktif di Taiwan](https://committers.top/taiwan.html)
11. [COSCUP — Wikipedia](https://en.wikipedia.org/wiki/COSCUP)
12. [The simple but ingenious system Taiwan uses to crowdsource its laws](https://www.technologyreview.com/2018/08/21/240284/the-simple-but-ingenious-system-taiwan-uses-to-crowdsource-its-laws/) — MIT Technology Review

---

## Bacaan Lanjutan

- [Komunitas Open Source dan g0v](/id/technology/open-source-and-g0v) — Narasi kolektif fork pemerintah
- [Sejarah Migrasi Komunitas Internet Taiwan](/technology/台灣網路社群遷徙史) — Sejarah generasi dari BBS ke Discord
- [Mini Taiwan Pulse](/id/technology/mini-taiwan-pulse-civic-tech) — Sampel pribadi open source teknologi sipil, enam minggu 193 commits mengubah data terbuka menjadi jejak cahaya 3D
- [Pedang Ganda Dayu](/id/technology/softstar-twin-classics) — Kisah Taiwan lain tentang "menciptakan hal yang melebihi skala dengan semangat" (RPG yang lahir dari mengintai Mal Cahaya)
- [Tidak Masuk Lembah Bagaimana Bisa Tidur](/id/technology/into-the-cellar-taiwan-game-podcast) — Komunitas pemain 6 juta anggota yang tumbuh dari asrama Universitas Chung Cheng
