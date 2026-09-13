---
title: 'Pembayaran Digital di Taiwan: Mengapa Masih Membawa Uang Tunai Meskipun Sudah Punya Banyak Metode Pembayaran di Ponsel?'
description: 'Dalam survei sampel daring dari MIC (Taiwan) pada kuartal ketiga 2024, 92% pernah dan 84% sering menggunakan pembayaran digital. Namun, survei nasional lain dari Bank Sentral menunjukkan bahwa 73,8% masih mencampur uang tunai dan non-tunai. Artikel ini mengurai alat, kontrak, dan proses konfirmasi yang berbeda di balik pembayaran ponsel—mulai dari konsumen, pedagang, hingga QR bersama TWQR—untuk menjawab mengapa adopsi tinggi belum menghilangkan kebutuhan akan uang tunai, serta menjelaskan apa yang telah diselesaikan dan apa yang masih menjadi pengecualian dalam penerimaan.'
date: 2026-09-01
category: 'Technology'
tags:
  [
    'Pembayaran Digital',
    'Pembayaran Elektronik',
    'TWQR',
    'Taiwan Pay',
    'Kode QR',
    'Uang Tunai',
    'Teknologi Keuangan',
  ]
subcategory: '數位與網路'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-09-01
lastHumanReview: false
researchReport: 'reports/research/2026-09/台灣行動支付.md'
image: '/article-images/technology/taiwan-mobile-payments-merchant-2026.webp'
imageCredit: '財金資訊股份有限公司（TWQR 官方網站）'
imageLicense: 'Fair use editorial commentary'
imageSource: 'https://www.twqr.com.tw/'
translatedFrom: 'Technology/台灣行動支付.md'
sourceCommitSha: '574b1a339'
sourceContentHash: 'sha256:1e2fca6dab4c2f1c'
sourceBodyHash: 'sha256:62d9c6127e29bebe'
translatedAt: '2026-09-13T00:44:03+08:00'
---

# Pembayaran Digital di Taiwan: Mengapa Masih Membawa Uang Tunai Meskipun Sudah Punya Banyak Metode Pembayaran di Ponsel?

![Tangkapan layar toko dari wawancara resmi TWQR](/article-images/technology/taiwan-mobile-payments-merchant-2026.webp)
_Tangkapan layar wawancara resmi TWQR, hanya digunakan sebagai materi promosi sistem. Gambar ini hanya mewakili toko yang diwawancarai dan tidak dapat dijadikan bukti lapangan independen untuk kondisi toko kecil di seluruh Taiwan. Gambar: Financial Information Co., Ltd. (Situs web resmi TWQR), digunakan secara wajar dalam ulasan._

> **Ringkasan 30 Detik:** Dalam sampel daring MIC pada kuartal ketiga 2024, 92% pernah menggunakan pembayaran digital. Namun, survei yang ditugaskan oleh Bank Sentral menunjukkan bahwa 73,8% orang dewasa masih mencampur uang tunai dan non-tunai. Kedua angka ini berasal dari populasi dan kuesioner yang berbeda, namun keduanya menunjuk pada hal yang sama: kemampuan untuk membayar melalui ponsel, menyelesaikan transaksi di mana saja, dan merasa aman tanpa membawa uang tunai adalah tiga ambang batas yang berbeda. Banyak aplikasi mengisi celah layanan, atau mengejar fungsi _reward_ dan keanggotaan. TWQR sedang mengintegrasikan QR bersama, tetapi belum menyatukan semua sumber dana, kontrak toko, dan skenario kegagalan menjadi satu bentuk pembayaran.

Pada September 2025, analis industri senior MIC, Hu Zi-li (胡自立), merilis survei konsumen pembayaran digital. Ia mengamati bahwa pengguna aktif yang memasang lima atau lebih alat "terutama untuk menggunakan pembayaran digital di berbagai saluran."[^1] Kalimat ini mirip dengan apa yang dilakukan banyak orang di kasir: pertama melihat logo apa yang ditempelkan pada kaca atau konter, baru memutuskan aplikasi mana yang akan dibuka. Jika tidak menemukan merek yang dikenali, barulah mereka mengangkat kepala dan bertanya, "Di sini menerima jenis apa?"

Pilihan di ponsel semakin banyak, tetapi masih tersisa beberapa lembar uang kertas di dompet. Gambaran yang berdampingan ini mudah ditafsirkan sebagai pasar pembayaran Taiwan yang terlalu terfragmentasi, atau juga dianggap sebagai pilihan diskon sederhana oleh pihak lain. Kedua interpretasi tersebut menangkap sebagian kebenaran. Gesekan sistem dalam penerimaan dan interoperabilitas memang membuat orang memasang banyak alat sambil tetap menyimpan uang tunai; _reward_, keanggotaan, transfer, kebiasaan, preferensi pribadi, dan pemulihan kegagalan juga bekerja secara bersamaan. Untuk memahami hal ini dengan jelas, kita harus memecah tiga ambang batas tersebut: apakah orang mengadopsinya, apakah transaksi dapat digunakan lintas skenario, dan apakah transaksi yang gagal dapat dipulihkan sehingga pengguna berani meninggalkan lembaran uang terakhir di rumah.

## Membayar dengan Ponsel Tidak Berarti Cukup Hanya Membawa Ponsel Hari Ini

Angka 92% "pernah menggunakan" dan 84% "sering menggunakan" yang dirilis MIC berasal dari sampel daring selama dua bulan pada kuartal ketiga 2024. Halaman publik tidak mencantumkan secara lengkap kerangka pengambilan sampel, rentang usia, dan metode pembobotan; oleh karena itu, kedua persentase ini hanya dapat menggambarkan sampel daring tersebut, dan tidak dapat langsung ditulis sebagai tingkat adopsi populasi Taiwan secara keseluruhan.[^2] Bahkan dengan batasan ini, hal itu menunjukkan bahwa di antara kelompok konsumen yang mengisi kuesioner daring, pembayaran ponsel telah melampaui tahap teknologi asing.

Survei lain yang ditugaskan oleh Bank Sentral kepada Taiwan Institute of Economic Research menanyakan bagaimana masyarakat berusia di atas 18 tahun menggunakan uang tunai dan non-tunai dalam kehidupan sehari-hari. Survei ini menggunakan bahasa lokal, fokus pada ponsel, dengan bantuan internet, mencakup 22 kota/kabupaten, dan dibobot berdasarkan struktur populasi, menghasilkan sampel efektif sebanyak 4.234 responden. Hasilnya menunjukkan bahwa 73,8% menggunakannya secara bersamaan, 25% hanya menggunakan uang tunai, dan hanya 1,2% yang hanya menggunakan non-tunai.[^3] Non-tunai di sini termasuk kartu kredit, kartu keuangan, dan kartu prabayar; ini tidak dapat digunakan sebagai pangsa pasar pembayaran digital, tetapi sangat cocok untuk menggambarkan bentuk dompet saat ini.

```tw-waffle
Pencampuran adalah rutinitas mayoritas (%)
Menggunakan Uang Tunai & Non-tunai | 73.8
Hanya Menggunakan Uang Tunai | 25
Hanya Menggunakan Non-tunai | 1.2
Sumber: Survei Alat Pembayaran Bank Sentral, dirilis tahun 2024
```

Oleh karena itu, tidak ada kontradiksi dalam seseorang yang menggunakan pembayaran melalui ponsel di kedai kopi waralaba pada pagi hari, memindai kode untuk poin saat makan siang, dan beralih ke uang tunai di pasar pada malam hari. Ia telah melewati ambang batas pertama "orang menggunakannya," tetapi ia masih harus mengganti alat berdasarkan lokasi, toko, dan perangkat. Frasa "masih membawa uang tunai" dalam judul hanya dapat dipahami sebagai cadangan skenario berskala besar, bukan sesuatu yang dibutuhkan setiap orang Taiwan setiap hari.

Kebiasaan pembayaran telah berubah, tetapi pengecualian situasional masih ada di jalanan. Memasang beberapa aplikasi mungkin tampak mengisi semua pengecualian satu per satu, tetapi untuk memahami mengapa hal itu bisa mengisi celah, kita harus mengakui bahwa aplikasi-aplikasi tersebut bukanlah hal yang sama. Momen membuka ponsel terlihat serupa, tetapi jalur transaksi setelahnya mungkin sangat berbeda.

## Beberapa Aplikasi Terlihat Melakukan Pembayaran, Tetapi Jalur yang Ditempuh Bukan Satu Jalan

Kementerian Keuangan mengklasifikasikan pembayaran digital berdasarkan alat yang terikat, teknologi, dan peraturan yang berlaku: kartu kredit seluler, kartu keuangan seluler, pemindaian kode QR, lembaga pembayaran elektronik, dan tiket elektronik.[^4]

Tindakan yang dilakukan konsumen di bagian depan mungkin hanya sekadar menyentuh, memindai, atau mengonfirmasi sekali, tetapi di belakang layar, hal itu dapat diselesaikan oleh alat yang terikat, teknologi, pihak penerima, dan aturan yang berbeda. Meskipun membayar menggunakan ponsel, beberapa menggunakan kartu yang terikat, sementara yang lain menggunakan akun pembayaran elektronik. Pihak penerima dan spesifikasi toko akan menentukan kombinasi mana yang tersedia. Oleh karena itu, LINE Pay, Street, Apple Pay, Chunghwa Payment (全支付), dan Taiwan Pay tidak bisa hanya diatur sebagai lima dompet homogen berdasarkan logo mereka. Beberapa bersaing satu sama lain, beberapa bekerja sama secara berlapis dalam satu transaksi, dan beberapa mengisi celah di saluran yang berbeda.

Untuk melihat bagaimana platform seperti PChome, Shopee, dan Coupang mengubah skenario belanja daring, silakan baca [Ekosistem E-commerce dan Pembayaran Digital Taiwan](/id/technology/e-commerce-and-digital-payment-ecosystem). Artikel ini hanya berfokus pada mil terakhir pembayaran fisik.

Jadi, memiliki merek tertentu di ponsel hanya menjawab apakah sisi pengguna mendapatkan alat; itu tidak dapat secara langsung menjawab apakah toko menerima pihak penerima yang kompatibel. Melihat satu kode QR saja tidak berarti semua aplikasi, arah pemindaian, dan sumber dana dapat menyelesaikan transaksi. Dari ikon ponsel langsung melompat ke "tersedia di seluruh Taiwan" telah menghilangkan setidaknya tiga lapisan: alat yang terikat, kontrak toko, dan spesifikasi transaksi.

Jumlah aplikasi juga perlu dikoreksi dari klaim dilebih-lebihkan "rata-rata lima jenis." Sampel daring MIC tahun 2024 menunjukkan bahwa 86% menggunakan lima atau kurang, di mana 61% menggunakan tiga atau kurang, dan 14% menggunakan enam atau lebih. Data publik tidak memberikan rata-rata atau median, juga tidak memberikan distribusi lengkap untuk satu hingga lima jenis.[^5] Ini mendukung penggunaan ganda, tetapi tidak dapat membentuk "pengguna tipikal" yang memiliki tepat lima alat.

Tabel bulanan dari Biro Perbankan Kementerian Keuangan pada Juni 2026 menjumlahkan jumlah lembaga pembayaran elektronik menjadi 41,129 juta. Ini adalah total institusi, bukan jumlah pengguna unik setelah deduplikasi antar institusi.[^6]

> **📝 Catatan Kurator**
> Logo di konter adalah merek; apa yang ditampilkan di ponsel adalah antarmuka; dan data terakumulasi dalam tabel Kementerian Keuangan adalah kontrak akun yang belum berakhir. Menyebut ketiganya sebagai "jumlah pengguna" akan meratakan lapisan paling penting untuk dipahami dari pasar pembayaran.

Apa yang terlihat serupa di bagian depan, perbedaan muncul saat transaksi mencapai sisi lain. Tidak peduli berapa banyak aplikasi yang diunduh oleh pengguna, mereka tidak dapat menyelesaikan pendaftaran, konfirmasi, dan rekonsiliasi untuk toko. Ambang batas kedua ada di belakang konter.

## Konsumen Melihat Pemindaian Sekali, Toko Harus Menyambungkan Seluruh Proses

Untuk menerima Taiwan Pay, sebuah toko harus terlebih dahulu mengajukan permohonan kepada lembaga keuangan penerima untuk menjadi toko mitra yang terikat kontrak, mendapatkan kode bank penerima, kode toko khusus, dan kode terminal.[^7] Setelah mulai menerima pembayaran, perangkat dan jaringan harus berfungsi; staf toko perlu tahu cara mengonfirmasi notifikasi dan memproses pengembalian dana. Di belakang layar, mereka juga harus menyelesaikan rekonsiliasi dan transfer dana. Bagi toko kecil, menempelkan kode penerima hanyalah permulaan, diikuti oleh proses operasional yang harus diselesaikan setiap hari.

FAQ Taiwan Pay menjelaskan secara rinci momen di mana proses ini paling mudah ditutupi oleh satu kode QR: ketika perangkat _offline_, toko masih dapat menghasilkan kode QR tanpa jumlah di halaman masuk untuk dipindai konsumen, tetapi ponsel toko tidak menerima notifikasi transaksi.[^8] Layar pelanggan menunjukkan pembayaran berhasil, tetapi sisi penerima kekurangan notifikasi saat itu, sehingga konter harus memutuskan apakah akan menyerahkan barang atau ke mana mereka harus memeriksa transaksi ini. Pemindaian hanyalah titik awal tindakan; konfirmasi di tempat dan rekonsiliasi setelahnya yang membuat transaksi benar-benar terealisasi.

Taiwan Pay menyerahkan biaya kepada kontrak antara toko dan bank penerima; penjelasan resmi menyatakan bahwa "biaya pemrosesan transaksi ditentukan oleh kontrak antara penjual (penerima) dan bank penerima." Penawaran publik dari platform lain, negosiasi rantai toko, dan sumber pembayaran yang berbeda masing-masing memiliki syaratnya.[^9] Biaya layanan masuk ke dalam penilaian toko; waktu transfer dana, pengembalian dana, jaringan, perangkat, pelanggan, pembelajaran, dan rekonsiliasi juga berperan.

Studi akademis di kawasan bisnis Tainan bahkan menemukan korelasi positif antara kegunaan yang dirasakan, kemudahan penggunaan, adopsi konsumen, kompatibilitas, dan niat adopsi, sementara biaya yang dirasakan tidak menunjukkan hubungan yang signifikan dalam sampel tersebut.[^10] Ini juga berarti bahwa toko tidak hanya menanggung biaya; mereka juga menilai apakah alat itu berguna dan apakah pelanggan telah mengadopsinya. Studi lokal ini tidak dapat digeneralisasi ke seluruh Taiwan, tetapi cukup untuk mencegah interpretasi tunggal "toko tidak menerima karena biayanya mahal."

Survei yang ditugaskan oleh Bank Sentral memberikan skala perbedaan penerimaan. Dari 611 sampel pedagang kaki lima, 76,1% hanya menerima uang tunai. Dari 1.436 sampel toko, angka ini adalah 46,8%. Laporan mengaitkan proporsi yang lebih tinggi dari pedagang kaki lima dengan lokasi, peralatan, dan skala.[^11] "Hanya menerima uang tunai" di sini relatif terhadap semua alat non-tunai; itu tidak dapat diturunkan menjadi tingkat penerimaan pembayaran digital, juga tidak dapat digunakan untuk mengkritik pedagang karena kurangnya keinginan untuk maju.

```tw-bars
Kondisi Penerimaan Lapak dan Toko (Hanya Menerima Uang Tunai, %)
Sampel Pedagang Kaki Lima | 76.1 | 611 responden
Sampel Toko | 46.8 | 1.436 responden
Sumber: Survei Alat Pembayaran Bank Sentral, dirilis tahun 2024
```

Universalitas pembayaran harus diselesaikan oleh kedua belah pihak: konsumen memiliki alat, dan toko memiliki proses untuk menerima, mengonfirmasi, mengembalikan dana, dan merekonsiliasi secara berkelanjutan. Gesekan sistem sampai di sini sudah memiliki bentuk, tetapi itu hanya menjelaskan sebagian dari keberadaan banyak aplikasi bersamaan dengan uang tunai. Aplikasi berikutnya terkadang adalah cadangan; terkadang lebih seperti kartu keanggotaan.

## Memasang Satu Aplikasi Lebih Banyak, Kadang untuk Bisa Menggunakan, Kadang Hanya Ingin Lebih Baik

Dalam survei Bank Sentral mengenai kesulitan penggunaan pembayaran digital, 18,9% memilih toko tidak menerima, 12,0% memilih toko tidak menerima alat yang biasa mereka gunakan, dan 7,6% adalah karena terlalu banyak jenis di pasar. Sinyal jaringan buruk menyumbang 6,5%, dan baterai ponsel habis menyumbang 3,4%.[^12] Ini semua adalah jawaban pilihan ganda; itu tidak dapat menjadi proporsi kausal dari setiap faktor yang menyebabkan transaksi tunai, tetapi menunjukkan adanya kesenjangan antara "memiliki aplikasi" dan "aplikasi ini bisa digunakan."

Motivasi pengisian celah yang disebutkan oleh Hu Zi-li sangat sesuai dengan hal ini. Ketika sebuah toko tidak menerima alat yang biasa digunakan, pengguna mungkin memasang satu lagi. Saat teman makan bersama memerlukan pembagian tagihan, atau anggota keluarga ingin mentransfer poin hadiah, mereka juga mungkin menyimpan aplikasi lain. Survei seri MIC menunjukkan bahwa 57% pengguna pernah menggunakan layanan keuangan selain konsumsi; yang paling umum adalah transfer dan pengiriman poin hadiah, menyumbang 38%.[^13] Fungsi-fungsi ini membawa aplikasi pembayaran ke dalam kehidupan sosial dan keanggotaan, sehingga alasan kepemilikan telah melampaui apakah konter dapat memindai.

Dalam studi lintas empat wilayah yang ditugaskan oleh Visa pada tahun 2022, 1.000 responden Taiwan berusia antara 18 hingga 55 tahun diwawancarai; di antaranya, 40% secara rutin melacak poin konsumsi, dan 22% sangat teliti untuk mendapatkan _reward_ terbaik.[^14] Data ini tidak dapat mengestimasi "berapa banyak orang yang memasang aplikasi karena _reward_," tetapi hanya menunjukkan bahwa sebagian responden melacak poin dan menghitung diskon untuk _reward_. Ekosistem keanggotaan ritel juga mengembangkan alat pembayaran mereka sendiri. Untuk melihat bagaimana FamilyMart (全聯) beralih dari jaringan toko dan manajemen anggota menjadi platform kehidupan frekuensi tinggi, lihat [FamilyMart Welfare Center](/id/economy/pxmart-supermarket), di sini kami tidak menulis sejarah perusahaan yang kontroversial.

Survei Kementerian Ekonomi mengenai sektor ritel memberikan perubahan yang lebih panjang. Berdasarkan jumlah pembayaran sampel yang dikembalikan, proporsi penggunaan pembayaran digital oleh konsumen meningkat dari 0,6% pada tahun 2017 menjadi 11,2% pada tahun 2023, sementara uang tunai turun dari 41,1% menjadi 23,0%. Pihak resmi mengaitkan perubahan dalam ritel barang jadi dan kosmetik sebagian dengan ekosistem keanggotaan dan alat pembayaran yang dibangun sendiri oleh pelaku usaha.[^15] Peningkatan pangsa pembayaran digital bertepatan dengan penurunan pangsa uang tunai. Persaingan antar merek juga memang menciptakan pilihan. Jika banyak aplikasi hanya didiagnosis sebagai kegagalan sistem, lintasan kenaikan ini dan preferensi proaktif pengguna akan terlewatkan.

```tw-slope
Proporsi Nilai Pembayaran Ritel: Peningkatan Pembayaran Digital, Penurunan Uang Tunai (%)
2017 | 2023
*Pembayaran Digital | 0.6 | 11.2
Uang Tunai | 41.1 | 23.0
Sumber: Biro Statistik Kementerian Ekonomi, Survei Kondisi Operasi Perdagangan Besar, Ritel, dan Makanan
```

Banyak alat memainkan dua peran: satu mengisi kekurangan penerimaan dan sumber dana, sementara yang lain menampung diskon, poin, keanggotaan, dan transfer. Jumlah aplikasi itu sendiri tidak dapat mengukur jarak adopsi, universalitas, atau tanpa uang tunai. Setelah persaingan dan pengisian celah terjalin, masalahnya terletak pada tingkat integrasi apa yang telah dicapai.

## TWQR Mengintegrasikan QR Bersama, Tetapi Tidak Menyatukan Semua Pembayaran Menjadi Satu

TWQR adalah respons substantif terhadap "terlalu banyak spesifikasi pembayaran, terlalu banyak papan nama toko." Standar kode QR bersama ini menghubungkan lembaga keuangan dan lembaga pembayaran elektronik yang berpartisipasi. Pada akhir tahun 2025, data Bank Sentral mencantumkan 44 lembaga keuangan, 10 lembaga pembayaran elektronik, dan 678.000 toko mitra kontrak. Sepanjang tahun 2025, tercatat 146,73 juta transaksi senilai 713,6 miliar.[^16] "Pembayaran QR Taiwan sama sekali tidak dapat diinteroperasikan" sudah tidak sesuai dengan kenyataan saat ini.

![Ilustrasi materi penjelasan sistem resmi pembayaran multi-alat TWQR](/article-images/technology/taiwan-mobile-payments-single-contract-2026.webp)
_Materi penjelasan sistem resmi TWQR "Satu Kontrak, Pembayaran Multi-alat," yang menyajikan cara toko terhubung menurut klaim perusahaan keuangan. Ini adalah ilustrasi promosi sistem dan tidak dapat membuktikan secara independen bahwa setiap toko mitra aktif, setiap transaksi berhasil, atau semua sumber pembayaran saling terhubung. Gambar: Financial Information Co., Ltd. (Situs web resmi TWQR), digunakan secara wajar dalam ulasan._

Kode QR bersama telah menyelesaikan lapisan penting, tetapi halaman penerimaan yang dipublikasikan oleh bank mitra juga menunjukkan adanya batasan. Daftar "Pemindai Utama" mencantumkan 11 alat seperti Taiwan Pay, Street, Chunghwa Payment (全支付), YouYouFu (悠遊付), dan EasyCard (一卡通). Daftar "Yang Dipindai" lebih pendek dan dibatasi oleh spesifikasi QR Auth. Chunghwa Payment, Aijin Card (愛金卡), dan QuanYing Payment (全盈支付) muncul di daftar Pemindai Utama tetapi tidak ada di daftar Yang Dipindai pada halaman tersebut.[^17] Arah pemindaian, spesifikasi, dan partisipasi institusi akan mengubah kombinasi yang dapat digunakan; toko juga harus mengajukan permohonan TWQR kepada lembaga penerima.

678 ribu adalah jumlah toko mitra kontrak; data publik Bank Sentral tidak memberikan berapa banyak dari mereka yang aktif secara berkelanjutan, atau pangsa pasar total dan tingkat keberhasilan di lapangan. Kode QR bersama juga tidak akan secara otomatis menyatukan sumber dana seperti kartu kredit atau akun, poin keanggotaan, _reward_, kontrak toko, biaya, dan proses pengembalian dana. Ini mendorong papan nama dan spesifikasi transaksi menuju lapisan yang sama, tetapi tidak menghapus seluruh dunia bisnis setiap aplikasi.

> **📝 Catatan Kurator**
> Hasil TWQR yang paling patut dikenali terletak dalam lingkup kata "bersama": QR bersama dan pesan lintas institusi telah membentuk basis skala besar; penggunaan sehari-hari toko mitra, setiap sumber dana, dan setiap aturan keanggotaan masih ditentukan oleh lapisan lain. Universalitas sedang dibangun lapis demi lapis.

Ambang batas interoperabilitas telah maju, tetapi jumlah toko mitra tidak secara otomatis berarti bahwa setiap orang, setiap transaksi, dan setiap sumber dana dapat menggunakannya. Karena proses integrasi masih berlangsung, uang tunai memiliki penjelasan lain.

## Uang Tunai Tidak Membuktikan Kegagalan Pembayaran Digital, Biasanya Mereka Tidak Perlu Bertanya Apakah Bisa Digunakan

Apakah suatu alat dapat digunakan secara universal setidaknya harus memungkinkan pengguna mendapatkannya, toko mengenalinya dan mengonfirmasinya, dan transaksi selesai; juga harus ada metode pemulihan yang dapat diprediksi ketika ponsel mati, jaringan tidak stabil, atau notifikasi gagal. Ini berarti kedua belah pihak tahu ke mana harus memeriksa, kapan harus mencoba lagi, dan jalan apa yang bisa diambil setelah kegagalan. Mampu mencocokkan catatan yang sama setelah transaksi selesai juga merupakan bagian dari pemulihan.

Dengan penggaris ini, pembayaran digital telah mempersingkat penutupan dalam konsumsi sehari-hari, tetapi masih belum dapat menyediakan satu jalur untuk setiap skenario. Dalam sebagian besar transaksi kecil tatap muka, uang tunai dilakukan tanpa pendaftaran dan perangkat; penyerahan dan konfirmasi terjadi secara bersamaan, sehingga terus berfungsi sebagai antarmuka paling umum. Ini juga memiliki biaya kembalian, penyimpanan, dan inventaris; perbandingan di sini adalah ambang batas penerimaan dan kegagalan, bukan biaya operasional keseluruhan.

Survei yang ditugaskan oleh Bank Sentral membawa perbedaan individu ke dalam peran uang tunai: proporsi responden berusia 40 tahun ke atas dan dari daerah terpencil yang hanya menggunakan uang tunai lebih tinggi. Data ini mendukung perbedaan arah, tetapi tidak dapat diperluas menjadi gambaran tunggal untuk semua lansia atau penduduk pedesaan.[^18] Penelitian kali ini juga tidak memiliki data yang cukup untuk mengisi proporsi atau suara bagi anak di bawah umur, penyandang disabilitas, pekerja migran, dan wisatawan jangka pendek. Alat populer sangat nyaman bagi sebagian orang, tetapi itu tidak berarti setiap orang dapat memperoleh akun, kartu, ponsel, atau jaringan yang sama.

Pengguna berat memang mungkin tidak menyentuh uang kertas untuk waktu yang lama di toko waralaba dan lingkaran kehidupan yang mereka kenal. Orang lain menyimpan uang tunai mungkin hanya karena kebiasaan, preferensi privasi, atau kontrol pengeluaran, bukan karena pernah gagal membayar. Gesekan sistem, penerimaan toko, _reward_, keanggotaan, kebiasaan, preferensi, dan ketahanan kegagalan bekerja bersama; survei yang ada tidak dapat memberikan peringkat sebab-akibat tunggal untuk mereka.

Ambang batas adopsi menanyakan berapa banyak orang yang menggunakannya. Ambang batas universalitas menanyakan apakah orang dan toko yang berbeda dapat menyelesaikannya lintas skenario. Masih harus bertanya tentang tanpa uang tunai. Setelah kegagalan, bisakah dipulihkan? Semakin maju dua ambang batas pertama, semakin sedikit orang yang membawa uang tunai, tetapi kapan lembaran terakhir meninggalkan dompet tergantung pada apakah pengecualian sudah terlalu sedikit untuk dicadangkan.

Bagian di bawah ini adalah skenario hipotesis berdasarkan batasan _offline_ FAQ resmi, dan bukan kasus aktual: ponsel toko _offline_, halaman masuk masih dapat menampilkan kode QR tanpa jumlah. Pelanggan memindai kode, tetapi toko tidak menerima notifikasi deposit. Kedua belah pihak melihat layar masing-masing, transaksi tertahan antara "bisa membayar" dan "bisa dikonfirmasi di tempat." Pelanggan akhirnya menyimpan ponselnya dan mengeluarkan selembar uang kertas. Uang kertas itu tidak menentukan pemenang atau pecundang bagi teknologi; ia hanya berarti bahwa dalam skenario semacam ini, Anda masih belum perlu bertanya: "Di sini menerima jenis apa?"

## Bacaan Lanjutan

- [Ekosistem E-commerce dan Pembayaran Digital Taiwan](/id/technology/e-commerce-and-digital-payment-ecosystem) — Meninjau perang platform dan logistik e-commerce Taiwan selama dua dekade.
- [Perkembangan Teknologi Keuangan Taiwan](/id/economy/taiwan-fintech-development) — Menempatkan kasus pembayaran dalam perkembangan sepuluh tahun teknologi keuangan Taiwan antara keterbukaan dan kontrol risiko.
- [FamilyMart Welfare Center](/id/economy/pxmart-supermarket) — Melihat bagaimana FamilyMart beralih dari jaringan toko dan manajemen anggota menjadi platform kehidupan frekuensi tinggi.

## Sumber Gambar

- Gambar utama: Financial Information Co., Ltd. (Situs web resmi TWQR), [Sumber asli](https://www.twqr.com.tw/), Komentar editorial penggunaan wajar. Gambar aslinya adalah tangkapan layar video resmi "Cerita Bos Kecil | Sun Moon Meat Floss," dan artikel ini hanya digunakan untuk mengomentari promosi sistem TWQR.
- Gambar dalam teks: Financial Information Co., Ltd. (Situs web resmi TWQR), [Sumber asli](https://www.twqr.com.tw/), Komentar editorial penggunaan wajar. Gambar aslinya adalah ilustrasi materi penjelasan sistem resmi "Satu Kontrak, Pembayaran Multi-alat."

## Referensi

[^1]: [MIC Taiwan: Survei Konsumen Pembayaran Digital 2025](https://mic.iii.org.tw/research.aspx?id=730) — Hu Zi-li menjelaskan bahwa pengguna aktif memasang lebih banyak alat untuk berbagai saluran dan mengumumkan metode survei, tingkat adopsi, dan rentang jumlah.

[^2]: [MIC Taiwan: Survei Konsumen Pembayaran Digital 2025](https://mic.iii.org.tw/research.aspx?id=730) — Data dikumpulkan pada kuartal ketiga 2024 melalui survei daring dengan sampel efektif sebanyak 5.000 responden. 92% pernah menggunakan dan 84% sering menggunakan terbatas pada sampel tersebut.

[^3]: [Bank Sentral: Hasil Survei Kuesioner Isu CBDC](https://knowledge.cbc.gov.tw/uploads/20240613/d2196a6b-784b-45ea-b559-10b824915887.pdf) — Penjelasan metode, sampel, dan pembobotan, serta hasil bahwa 73,8% mencampur, 25% hanya menggunakan uang tunai, dan 1,2% hanya menggunakan non-tunai.

[^4]: [Situs Web Cerdas Keuangan Kementerian Keuangan: Materi Pembayaran Digital](https://moneywise.fsc.gov.tw/uploaddowndoc?file=financeroom%2F202001131202240.pdf&filedisplay=%E6%96%B0%E5%A2%9E%E6%95%99%E6%9D%90PPT-+%E8%A1%8C%E5%8B%95%E6%94%AF%E4%BB%98-%E5%AE%9A%E7%A8%BF.pdf&flag=doc) — Membedakan kartu kredit seluler, kartu keuangan seluler, pemindaian kode QR, lembaga pembayaran elektronik, dan tiket elektronik berdasarkan alat yang terikat, teknologi, dan peraturan.

[^5]: [MIC Taiwan: Survei Konsumen Pembayaran Digital 2025](https://mic.iii.org.tw/research.aspx?id=730) — Distribusi rentang publik untuk lima atau kurang, tiga atau kurang, dan enam atau lebih pada tahun 2024; rata-rata atau median tidak diumumkan.

[^6]: [Biro Perbankan Kementerian Keuangan: Informasi Penting Akun Pembayaran Elektronik Juni 115](https://www.fsc.gov.tw/userfiles/file/BB-1156_%E9%9B%BB%E5%AD%90%E6%94%AF%E4%BB%98%E5%B8%B3%E6%88%B6%E9%87%8D%E8%A6%81%E8%B3%87%E8%A8%8A%E6%8F%AD%E9%9C%B2.pdf) — Dijumlahkan menjadi 41,128,870, dan didefinisikan dalam catatan kaki sebagai jumlah pengguna yang telah mendaftar dan belum mengakhiri kontrak di setiap institusi.

[^7]: [Pembayaran Digital Taiwan: FAQ Operasi Toko Khusus](https://www.twmp.com.tw/Faq?n=95c7608a1dfc4fa1834f4467d41a32d1) — Menjelaskan bahwa toko harus menandatangani kontrak dengan lembaga keuangan penerima dan memperoleh kode bank penerima, kode toko khusus, dan kode terminal.

[^8]: [Pembayaran Digital Taiwan: FAQ Penerimaan Toko](https://www.twmp.com.tw/Faq?n=29250e1aae5e4963a550de09d86a26be) — Menjelaskan bahwa meskipun perangkat _offline_ masih dapat menghasilkan kode QR tanpa jumlah, notifikasi transaksi tidak dapat diterima atau diproses.

[^9]: [Pembayaran Digital Taiwan: FAQ Penerimaan Toko](https://www.twmp.com.tw/Faq?n=29250e1aae5e4963a550de09d86a26be) — Secara resmi menyatakan bahwa biaya pemrosesan ditentukan oleh kontrak antara toko dan bank penerima, dan tidak dapat diturunkan menjadi tarif tunggal pasar.

[^10]: [Universitas Tsuchi (成功大學): Studi Adopsi Pembayaran Digital di Kawasan Bisnis Tainan](https://researchoutput.ncku.edu.tw/en/studentTheses/what-factors-affect-stores-willingness-to-adopt-mobile-payment-de/) — Ringkasan tesis doktoral mencantumkan faktor signifikan dan tidak signifikan dari niat adopsi, dengan lingkup penelitian terbatas pada sampel kawasan bisnis Tainan.

[^11]: [Bank Sentral: Hasil Survei Kuesioner Isu CBDC](https://knowledge.cbc.gov.tw/uploads/20240613/d2196a6b-784b-45ea-b559-10b824915887.pdf) — Sampel 611 pedagang kaki lima dan 1.436 toko, mengaitkan perbedaan hanya menerima uang tunai dengan lokasi, peralatan, dan skala.

[^12]: [Bank Sentral: Survei Alat Pembayaran dalam Laporan Stabilitas Keuangan](https://www.cbc.gov.tw/tw/dl-207586-2f35d674d8a34ee09d1d1c0fd68a6fea.html) — Tabel mencantumkan keluhan pilihan ganda seperti toko tidak menerima, alat yang biasa digunakan tidak diterima, terlalu banyak jenis, sinyal, dan daya baterai ponsel.

[^13]: [MIC Taiwan: Survei Konsumen Pembayaran Digital 2025](https://mic.iii.org.tw/research.aspx?id=730) — Survei mencantumkan layanan keuangan selain konsumsi, di mana transfer dan pengiriman poin hadiah adalah jenis yang paling umum.

[^14]: [Visa Taiwan: Studi Konsumen Dompet Seluler dan Pembayaran Elektronik 2022](https://www.visa.com.tw/about-visa/newsroom/press-releases/nr-tw-230310.html) — Mengungkap sampel 1.000 orang Taiwan berusia 18 hingga 55 tahun serta proporsi pelacakan _reward_ dan perhitungan diskon.

[^15]: [Biro Statistik Kementerian Ekonomi: PDF Survei Pembayaran Ritel](https://www.moea.gov.tw/Mns/populace/news/wHandNews_File.ashx?file_id=116845) — Proporsi nilai pembayaran pada tahun 2017 dan 2023 dari survei kondisi operasi perdagangan besar, ritel, dan makanan, serta penjelasan ekosistem keanggotaan.

[^16]: [Bank Sentral: Laporan Tahunan 2025](https://www.cbc.gov.tw/tw/dl-225165-b56d9b5e547843a4822acd679cb4868e.html) — Mencantumkan lembaga yang berpartisipasi dalam TWQR pada akhir tahun 2025, toko mitra kontrak, jumlah transaksi dan nilai sepanjang tahun.

[^17]: [Bank Mitra: Layanan Penerimaan Lintas Institusi TWQR](https://www.tcb-bank.com.tw/company-banking/credit-card/special-store/twqr) — Mengklasifikasikan alat penerima utama dan yang dipindai, spesifikasi QR Auth, dan cara pengajuan toko, menunjukkan lapisan perbedaan berdasarkan arah dan spesifikasi.

[^18]: [Bank Sentral: Hasil Survei Kuesioner Isu CBDC](https://knowledge.cbc.gov.tw/uploads/20240613/d2196a6b-784b-45ea-b559-10b824915887.pdf) — Laporan menyajikan perbedaan arah usia dan wilayah; artikel ini tidak mengarang proporsi atau suara kelompok tertentu berdasarkan laporan tersebut.
