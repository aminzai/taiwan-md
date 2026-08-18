---
title: 'Masalah Penandaan Taiwan dalam Standar Internasional'
description: 'Dari kode ISO hingga perangkat lunak sumber terbuka—bagaimana nama Taiwan ditulis, diperdebatkan, dan diperbaiki dalam infrastruktur digital global'
date: 2026-03-18
category: 'Society'
tags:
  [
    'ISO 3166',
    'Standar Internasional',
    'Perangkat Lunak Sumber Terbuka',
    'g0v',
    'Kedaulatan Digital',
    'Penandaan Taiwan',
  ]
subcategory: 'Hubungan Internasional'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-03-19
lastHumanReview: false
translatedFrom: 'Society/台灣在國際標準中的標示問題.md'
sourceCommitSha: '18157ab5d'
sourceContentHash: 'sha256:5aa5d3ad7e4d012f'
translatedAt: '2026-08-10T03:40:22.494148+00:00'
---

# Masalah Penandaan Taiwan dalam Standar Internasional

> **Ringkasan 30 Detik:** Dalam infrastruktur digital global, Taiwan sering ditandai sebagai "Taiwan, Province of China". Penandaan ini berasal dari lanskap politik internasional pasca Resolusi Majelis Umum PBB Nomor 2758 tahun 1971, memengaruhi standar internasional seperti ISO 3166, dan meluas ke perangkat lunak sumber terbuka serta layanan jaringan global. Komunitas sumber terbuka terus mendorong cara penandaan yang lebih netral melalui laporan bug dan pull request.

Dalam infrastruktur digital global, cara penandaan Taiwan mencerminkan perbedaan politik internasional yang berlangsung selama setengah abad. Dari ISO 3166 hingga antarmuka pemilihan mirror Ubuntu, di balik sebuah detail teknis tersembunyi kontroversi yang belum terselesaikan mengenai pengakuan identitas Taiwan dalam sistem internasional.

## Konteks historis: UN 2758 hingga ISO 3166

Pada tahun 1971, Resolusi Majelis Umum PBB Nomor 2758 disahkan, memutuskan bahwa "kursi Tiongkok di PBB" diwakili oleh Republik Rakyat Tiongkok, sehingga Republik Tiongkok (Taiwan) kehilangan kursi PBB. Keputusan ini awalnya hanya menyangkut kursi perwakilan PBB, namun kemudian banyak dikutip sebagai dasar Taiwan dikecualikan atau ditampilkan dengan cara tertentu di berbagai organisasi internasional dan badan penentu standar.[^1]

Pada tahun 1974, nama entri Taiwan dalam standar internasional ISO 3166 diubah dari "Taiwan" menjadi "Taiwan, Province of China", secara resmi menetapkan cara penunjukan yang berlaku hingga saat ini. ISO 3166-1 sekaligus memberikan kode dua huruf `TW` untuk Taiwan, namun kontroversi mengenai nama resmi berlanjut tanpa ketentuan hingga kini.

Posisi ISO adalah mengikuti basis data nama geografis Biro Statistik PBB (UNSD), yang penunjukannya kembali mengacu pada lanskap politik pasca-UN 2758. Hal ini membentuk sistem saling ketergantungan: standar internasional merujuk data PBB, perangkat lunak sumber terbuka merujuk standar internasional, dan akhirnya "Taiwan, Province of China" muncul di menu tarik-turun para pengembang di seluruh dunia.[^2]

## Tindakan Koreksi Komunitas Perangkat Lunak Sumber Terbuka

Bug #1138121 Ubuntu (dilaporkan 2013) adalah salah satu kasus yang paling banyak dikutip. Ketika pengguna Taiwan memilih situs cermin sumber perangkat lunak, melihat label 「Taiwan, Province of China」 muncul di antarmuka, banyak yang merasa bingung. Pelapor menyarankan mengadopsi kolom common name di ISO 3166, yaitu sekadar 「Taiwan」, bukan nama resmi lengkap.

Masalah serupa juga berulang muncul di proyek sumber terbuka lain. Issue #43 ISO-3166-Countries-with-Regional-Codes, FreeBSD PR 138672, dan Drupal Issue #1938892 semuanya mencatat keberatan komunitas terhadap penandaan ini. Solusinya biasanya adalah beralih ke data CLDR (Unicode Common Locale Data Repository), karena penandaan CLDR untuk Taiwan relatif lebih netral.[^3]

Tindakan koreksi komunitas sumber terbuka mencerminkan pertemuan antara teknik dan politik: pengembang biasanya ingin mengadopsi penandaan yang lebih netral, tetapi terbatas oleh pertimbangan 「mengikuti standar internasional」, sehingga perubahan sering memerlukan diskusi komunitas yang lama, dan sebagian pemelihara juga memilih menghindari isu ini. Anggota komunitas g0v, chewei, lama mengumpulkan kasus terkait, mencatat luasnya masalah penandaan Taiwan di ekosistem perangkat lunak global.

## Dampak Penamaan yang Lebih Luas

Dalam acara resmi organisasi internasional, cakupan masalah penamaan Taiwan lebih luas. Dalam Sidang Kesehatan Dunia (WHA), Taiwan pernah diundang menghadiri sebagai observator dengan identitas 「Chinese Taipei」, pada periode 2009 hingga 2016 (total delapan kali); sejak 2017, Tiongkok menentang kehadiran Taiwan, undangan terhenti sejak saat itu, dan Taiwan tidak lagi menerima undangan formal.[^6] Di Organisasi Penerbangan Sipil Internasional (ICAO), Taiwan juga tidak dapat berpartisipasi dalam pengambilan keputusan sebagai anggota formal, dan dalam jangka lama bergantung pada saluran tidak formal untuk memperoleh informasi standar teknis penerbangan, menciptakan celah potensial dalam aliran informasi keselamatan penerbangan. Di Olimpiade, Taiwan berpartisipasi dengan nama 「Chinese Taipei」 (「中華台北」) sejak 1981 — nama ini berasal dari Perjanjian Lausana 1981 yang ditandatangani oleh Komite Olimpiade Internasional dan Komite Olimpiade Tionghoa. Solusi kompromi ini juga diadopsi oleh banyak organisasi internasional non-pemerintah, dan diperluas ke forum seperti APEC.

Masalah penamaan mendapat ekstensi baru di era digital. Selain ISO 3166, kode bank SWIFT, kode bandara ICAO, dan basis data geografis berbagai negara pemerintah, masing-masing memiliki cara penunjukan Taiwan yang berbeda, kekurangan standar seragam.

Sejak 2023, sejumlah perusahaan teknologi internasional (seperti Apple, Google Maps) secara bertahap menyesuaikan nama tampilan Taiwan setelah laporan pengguna, namun penunjukan resmi ISO 3166-1 itu sendiri tidak berubah, menunjukkan pemisahan antara implementasi perusahaan dan standar internasional terus melebar.

## Perubahan Desain Sampul Paspor 2020

**2 September 2020**, Kementerian Luar Negeri Republik Tiongkok (Taiwan) mengumumkan desain paspor baru: teks 「REPUBLIC OF CHINA」 di sampul yang semula jelas diperkecil (masih mempertahankan lambang negara), sementara teks 「TAIWAN」 diperbesar signifikan hingga sejajar dengan 「REPUBLIC OF CHINA」. Perubahan ini menanggapi insiden selama pandemi COVID-19 di mana wisatawan Taiwan di berbagai negara disalahartikan sebagai warga negara Tiongkok dan ditolak masuk, dan merupakan kali pertama pemerintah Taiwan merespons masalah konkret 「kebingungan penunjukan kedaulatan」 melalui desain paspor. Paspor baru diterbitkan mulai **Januari 2021**.[^4]

## Kontroversi Taipei Tionghoa di Olimpiade Paris 2024

Selama **Olimpiade Paris Juli-Agustus 2024**, Taiwan berpartisipasi dengan nama 「Chinese Taipei」, namun masyarakat sipil Tiongkok di berbagai platform media sosial menerjemahkan nama tersebut sebagai 「中國台北」, yang memiliki perbedaan jelas dengan terjemahan bahasa Tionghoa resmi yang ditetapkan oleh Komite Olimpiade Internasional: 「Chinese Taipei = 中華台北」. Insiden seperti bendera direbut oleh penonton Tiongkok dan tim pendukung warga Taiwan di luar negeri diganggu oleh pemimpin delegasi Tiongkok selama Olimpiade, memicu refleksi ulang di masyarakat Taiwan terhadap Perjanjian Lausana 1981.[^5]

## Kasus Tekanan Perusahaan Multinasional

Tekanan perluasan 「Prinsip Satu Tiongkok」 oleh Tiongkok pada akhir 2010-an menyebar luas ke ranah perusahaan multinasional. **China Airlines (華航)** yang lama menggunakan nama 「China Airlines」 di rute internasional memicu kontroversi internal terkait identitas kebangsaan Taiwan (petisi 「Penggantian Nama China Airlines」 2018). Perusahaan seperti **Delta Air Lines**, **Marriott International**, **United Airlines**, **Zara**, **Starbucks**, **Marriott** pernah mengalami tekanan dari Administrasi Penerbangan Sipil Tiongkok atau Kantor Informasi Siber Tiongkok karena situs web mereka mencantumkan 「Taiwan」 sebagai negara, dan dipaksa mengubahnya menjadi 「Taiwan Tiongkok」 atau 「Wilayah Taiwan Tiongkok」. Kasus-kasus ini menunjukkan bahwa 「efek politik standar ISO」 telah meluas dari ranah teknis menjadi alat tekanan geopolitik.

## Perspektif: Kedudukan Tiongkok

Dari sudut pandang resmi Republik Rakyat Tiongkok, 「Prinsip Satu Tiongkok」 adalah fondasi politik hubungan lintas selat, yang mengklaim bahwa Republik Rakyat Tiongkok adalah satu-satunya pemerintah sah China, dan Taiwan adalah sebuah provinsi Republik Rakyat Tiongkok (tingkat administratif 「Provinsi Taiwan」). Kedudukan ini secara langsung memengaruhi penunjukan 「Taiwan, Province of China」 untuk Taiwan di ISO 3166 sejak 1974. Memahami masalah Taiwan dalam standar internasional mengharuskan kita melihat secara bersamaan posisi penolakan pemerintah Republik Tiongkok (Taiwan), klaim Republik Rakyat Tiongkok, serta spektrum identitas plural masyarakat Taiwan — ketiganya tidak selaras, dan tidak dapat direduksi.

## Menara Babel Kedaulatan: sovereignty preservation

Masalah penunjukan Taiwan dalam standar internasional, pada hakikatnya adalah masalah **infrastruktur pelestarian kedaulatan** (sovereignty preservation infrastructure). Memastikan suara first-person Taiwan hadir di setiap bahasa, setiap sistem, setiap basis data, adalah cara mempertahankan Taiwan sebagai subjek politik independen agar terus terlihat di era informasi. Setiap laporan bug, setiap pull request, setiap pembaruan desain paspor, adalah sebuah bata dalam infrastruktur ini.

## Referensi

## Bacaan Lanjutan

- [Komunitas g0v — Pengumpulan Masalah Penunjukan Taiwan](https://g0v.hackmd.io/5YRoMhveTt-aXwH60T2NZg) — basis data kasus penunjukan Taiwan dalam perangkat lunak sumber terbuka yang dikumpulkan oleh chewei
- [Platform Pencarian Daring ISO 3166](https://www.iso.org/obp/ui/#iso:code:3166:TW) — mencari penunjukan Taiwan saat ini di ISO 3166-1

[^1]: [Resolusi Majelis Umum PBB Nomor 2758 (1971)](https://undocs.org/zh/A/RES/2758(XXVI) — ) — Teks lengkap resolusi yang menentukan kursi representasi China di PBB diwakili oleh Republik Rakyat Tiongkok.

[^2]: [ISO 3166 Maintenance Agency — Online Browsing Platform](https://www.iso.org/obp/ui/#iso:code:3166:TW) — Entri Taiwan di ISO 3166-1, berisi kode TW dan nama resmi.

[^3]: [Ubuntu Launchpad — Bug #1138121](https://bugs.launchpad.net/ubuntu/+source/software-properties/+bug/1138121) — Laporan asli mengenai masalah penandaan Taiwan di antarmuka sumber perangkat lunak Ubuntu, 2013.

[^4]: [Kementerian Luar Negeri Republik Cina — Penjelasan Paspor Baru](https://www.mofa.gov.tw/) — Mengumumkan desain paspor baru pada 2 September 2020, kata TAIWAN diperbesar, diterbitkan mulai Januari 2021.

[^5]: [Komite Olimpiade Internasional — Perjanjian Komite Olimpiade Tiongkok Taipei](https://www.olympic.org/) — Perjanjian Lausanne 1981 menetapkan nama 'Chinese Taipei'; pada Olimpiade Paris 2024, China menggunakan 'China Taipei' yang salah terjemahan memicu kontroversi.

[^6]: [Kementerian Kesehatan dan Kesejahteraan Republik Cina — Penjelasan Partisipasi Taiwan di WHO](https://www.mohw.gov.tw/) — Taiwan menghadiri WHA sebagai observan dari 2009 hingga 2016, sejak 2017 tidak diundang lagi; latar belakang pengecualian ICAO lihat penjelasan terkait Kementerian Luar Negeri.
