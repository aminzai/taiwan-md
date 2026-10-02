---
title: 'Cerita Teknologi Taiwan: Chip Sempurna 100 Poin, Mikrofon 60 Poin'
description: 'Taiwan mampu membuat chip bernilai seratus poin, tetapi terbiasa membicarakannya dengan nada presentasi pemasok. Chip yang sama diceritakan Qualcomm sebagai mitos dan oleh MediaTek sebagai lembar spesifikasi; NVIDIA tidak membuat satu chip pun sendiri, tetapi laba bersihnya dua kali lipat dari pihak manufakturnya. Selisih 40 poin ini sudah lama dihitung oleh pasar, dan tagihannya tercetak pada margin laba bersih.'
date: 2026-08-15
category: 'Technology'
tags:
  [
    'teknologi',
    'storytelling',
    'branding',
    'semikonduktor',
    'TSMC',
    'NVIDIA',
    'MediaTek',
    'Qualcomm',
    'HTC',
    'Jensen Huang',
    'Morris Chang',
    'Kurva Senyum',
    'Subteks',
  ]
subcategory: '半導體與硬體'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-08-15
lastHumanReview: false
difficulty: 'beginner'
readingTime: 16
image: '/article-images/technology/tsmc-fab-14b-2025.webp'
imageCredit: '4300streetcar'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg'
rationale:
  why_this_hook: '從「同一顆晶片兩種講法」的反差切入，讓讀者先看見那 40 分長什麼樣子，再用財報數字把它換算成錢。'
  whats_excluded: '政府政策與主權 AI（政治敏感，超出本文查證範圍）；韓國三星製程競爭史；台灣新創公司名單流水帳；估值模型的公式化推導。'
  where_it_hedges: '張忠謀「護國神山」2021 原始報導與張忠謀自傳銷量標「待補來源」；蘋果手機利潤占比以「高峰估計」軟化；示意歸納的引語在文內明示非逐字。'
  whos_pushing_back: '認為低調是代工生意命脈、吹牛會傷信任的供應鏈從業者；認為台灣工程師文化不需要向矽谷敘事投降的人；被拿來當負面教材的公司員工。'
sporeLinks: []
curation: incubating
translatedFrom: 'Technology/台灣科技說故事.md'
sourceCommitSha: '18585807b'
sourceContentHash: 'sha256:056a94a81916a22b'
sourceBodyHash: 'sha256:805b10284be61867'
translatedAt: '2026-10-03T01:02:12+08:00'
---

# Cerita Teknologi Taiwan: Chip Sempurna 100 Poin, Mikrofon 60 Poin

![Tampilan luar bangunan Fab 14B TSMC di Tainan, dengan bangunan industri berlapis menjulur di bawah langit biru, merupakan lokasi fisik kapasitas proses canggih](/article-images/technology/tsmc-fab-14b-2025.webp)
_Fasilitas Fab 14B TSMC Tainan, Mei 2025. Foto: 4300streetcar. [Lisensi via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg)._

> **Ikhtisar 30 detik:** Juni 2024, Jensen Huang di Auditorium Olahraga Taiwan menceritakan chip yang dibuat TSMC sebagai sebuah era; kuartal yang sama, konferensi hasil TSMC masih berupa angka finansial, tingkat pemanfaatan kapasitas, prospek konservatif. NVIDIA FY2026 pendapatan $215,9 miliar, laba bersih $120,1 miliar; TSMC yang membuat chipnya, 2025 pendapatan $122,4 miliar, laba bersih $55,1 miliar[^5][^6]. Perusahaan yang merancang cerita menghasilkan dua kali lipat dari mereka yang membuat. Artikel ini akan mengungkap dialog di balik dialog.

2 Juni 2024, Auditorium Olahraga Taiwan. Jensen Huang naik panggung dengan jaket kulit hitam ikoniknya, bercakap dua jam. Pengaturan di depan terlihat seperti konser: siaran langsung, media internasional, lautan orang memegang ponsel. Dia berbicara tentang Blackwell, tentang CUDA, mengubah setiap slide menjadi pembukaan era[^19].

Di pulau yang sama, mengendarai ke selatan kurang dari 100 kilometer, Hsinchu. Konferensi hasil TSMC adalah lanskap yang berbeda: angka keuangan, tingkat pemanfaatan kapasitas, pertumbuhan kuartal ke kuartal, prospek konservatif. Chip paling canggih di dunia semua berada di lini produksi itu, namun seluruh presentasi terdengar seperti kelas akuntansi.

Satu chip yang sama, dua cara bercerita. Perbedaan 40 poin di tengahnya sudah diperhitungkan pasar.

Perbedaan antara dua skenario ini, orang Taiwan sebenarnya sudah melihatnya sejak kecil. Kami terbiasa: produk yang kami buat, pujian dari orang lain. Di pameran dagang, stan perusahaan Taiwan berbicara tentang biaya, tingkat keberhasilan, waktu pengiriman; panggung merek Amerika berbicara tentang masa depan, misi, mengubah dunia. Kesenjangan di tengahnya adalah empat puluh poin itu. Empat puluh poin itu terlihat seperti apa, artikel ini akan menerjemahkan untuk Anda.

## Satu Chip, Dua Cara Bercerita

Oktober 2024, dua acara peluncuran selang kurang dari dua minggu. MediaTek meluncurkan Dimensity 9400 di Shenzhen, Qualcomm mengadakan Snapdragon Summit di Maui, Hawaii[^9][^10].

[MediaTek](/id/economy/mediatek/) adalah salah satu pemasok chip ponsel terbesar di dunia menurut volume pengiriman, memiliki pangsa pasar TV chip sebesar 70%[^4b]. Volume pengiriman Qualcomm kalah darinya, namun pendapatan dan premium merek memenangkannya. Dimana perbedaannya? Qualcomm menjual nama "Snapdragon": sejak diberi nama pada tahun 2006 hingga sekarang telah diupayakan selama hampir dua puluh tahun[^8], memiliki maskot sendiri, acara teknologi tahunan sendiri. Di acara peluncuran ponsel flagship global itu "Powered by Snapdragon" lebih mencolok daripada trademark ponsel itu sendiri.

MediaTek menjual spesifikasi. Konferensi peluncuran Dimensity 9400 adalah tentang proses, IPC, kurva efisiensi energi, semua angka dapat dipertanggungjawabkan, lingkaran evaluasi memberinya nama panggilan "Raja Efisiensi Energi"[^9]. Namun konsumen hanya mengenal Snapdragon.

Kursi pemimpin volume pengiriman, MediaTek sebenarnya sudah pernah duduk. Kuartal ketiga 2020, volume pengiriman chip ponsel MediaTek untuk pertama kalinya melebihi Qualcomm, dengan pangsa pasar sekitar 31%[^7]. Namun selama beberapa tahun ketika MediaTek berada di posisi pertama dalam volume pengiriman, pendapatan utamanya berada di ponsel mid-range, layer teratas flagship selalu milik Qualcomm. Baru pada akhir 2021 ketika Dimensity 9000 hadir, MediaTek untuk pertama kalinya mengirimkan chip flagship ke tabel perbandingan ponsel Android flagship berbagai produsen. Spesifikasi sudah menyamai, namun konferensi peluncuran masih terasa seperti laporan supplier kepada klien.

MediaTek sebenarnya tahu tentang masalah ini. Dalam beberapa tahun terakhir, itu mulai belajar: chip flagship memiliki nama sendiri, konferensi peluncuran memiliki pembukaan yang spektakuler, produsen ponsel yang bekerja sama juga bersedia meletakkan "Dimensity" dalam tagline iklan. Arahnya benar, hanya saja mulainya terlambat satu dekade. Pembentukan merek adalah marathon, orang yang mulai lebih awal mendapat keuntungan majemuk setiap putaran.

> 💡 **Tahukah Anda**
> Snapdragon adalah nama bahasa Inggris untuk bunga snapdragon (bunga), nama sejenis bunga; Dimensity adalah bintang ketiga dari Tujuh Bintang Utara[^8]. Satu perusahaan mengambil nama dari taman, satu dari peta bintang, keduanya sangat bagus. Perbedaannya adalah: Qualcomm telah membuat bunga ini menjadi merek yang berjalan di red carpet, cahaya Dimensity sebagian besar waktunya masih terhenti di spesifikasi.

> 📝 **Catatan Kurator**
> Perang merek di industri chip sangat kejam dan konkret: ketika konsumen mengeluarkan uang mereka mengenali Snapdragon atau Dimensity, tidak ada yang bertanya chip TSMC mana yang dibuat. Qualcomm mulai membangun merek pada tahun 2006, MediaTek baru menempatkan seri "Dimensity" di flagship pada akhir 2019. Dua puluh tahun keuntungan narasi, tabel spesifikasi apa pun tidak akan mengejar ketertinggalan.

## Quietly Brilliant, Bagaimana Mati

Maju mundur ke kasus yang lebih menyakitkan. 7 April 2011, nilai pasar HTC melampaui Nokia, sekitar $33,8 miliar[^1]. Pada saat itu HTC memiliki sekitar 20% dari pasar ponsel, bersama Samsung dan Apple sebagai tiga raksasa[^2].

Dalam pilihan teknis, HTC hampir semuanya benar: pada tahun 2008 membuat smartphone Android pertama G1[^3]. One pada tahun 2013 menggunakan bodi paduan aluminium satu-kesatuan, jalur kamera piksel besar, lensa ganda, semuanya adalah yang pertama. Namun apakah Anda masih ingat tagline brand globalnya?

![Tampak samping casing HTC One M7, desain satu-kesatuan paduan aluminium, standar keahlian industri saat diluncurkan pada 2013](/article-images/technology/htc-one-m7-2013.webp)
_HTC One (M7), 2013. Foto: Asmoth, CC BY-SA 4.0. [Lisensi via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG)._

"Quietly Brilliant." Jago yang rendah hati.

Pada waktu yang bersamaan, iklan Samsung "The Next Big Thing is already here" secara langsung merekam penggemar Apple antri di depan toko, membuat antrian terlihat seperti bodoh[^18]. HTC menjadikan kerendahan hati sebagai proposisi merek, Samsung menjadikan Apple sebagai karakter antagonis. Sedikit lebih dari dua tahun kemudian, harga saham HTC runtuh dari ribuan hingga ratusan[^2].

HTC sebenarnya pernah memiliki kesempatan untuk bangkit. One pada tahun 2013 (M7) memiliki banyak tempat yang memimpin industri: bodi paduan aluminium satu-kesatuan, kamera UltraPixel berpiksel besar, speaker depan ganda BoomSound. Tahun itu, itu memenangkan "Ponsel Tahun Ini" dari berbagai media besar, namun penjualannya kalah jauh dari Samsung S4 periode yang sama. Konferensi peluncuran M7 berbicara tentang spesifikasi, Samsung berbicara tentang gaya hidup, Apple menceritakan pembaca sidik jari sebagai perubahan dunia. Satu generasi ponsel yang sama, tiga cara bercerita, tiga nasib.

Melihat kembali alasan kegagalan HTC, tentu saja tidak hanya satu tagline. Namun kehilangan narasi adalah batu pertama yang jatuh: ketika pasar mulai memilih faksi melalui cerita, pihak yang tidak bisa bercerita dimasukkan lebih dulu ke dalam keranjang "akan segera ketinggalan zaman". Insinyur tidak percaya pada ini, merasa produk akan berbicara. Produk memang berbicara, hanya saja sebagian besar konsumen tidak mengerti, dan mereka tidak ingin mendengarkan.

![Tampilan HTC Dream dengan keyboard geser terbuka, 2008 smartphone Android pertama G1 di dunia](/article-images/technology/htc-dream-g1-2008.webp)
_HTC Dream (T-Mobile G1), 2008. Foto: Marcus Sümnick, CC BY 3.0. [Lisensi via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg)._

> 📝 **Catatan Kurator**
> "Quietly Brilliant" itu sendiri adalah terjemahan subteks: sebuah perusahaan memilih "kerendahan hati" sebagai proposisi merek global, setara dengan secara aktif menyerahkan kekuasaan narasi. Spesifikasi akan dilupakan, cerita akan dikenang. HTC membuat pilihan teknis yang benar, kehilangan setiap pilihan narasi.

## Kurva Senyum: Orang Taiwan Menggambar Diagram Masa Depan Mereka Sendiri 30 Tahun Lalu

Tragedi HTC bukan kasus terisolasi, itu memiliki diagram sebagai bukti.

Pada tahun 1992, Stan Shih menggambar "Kurva Senyum" dalam _Remanufakturing Acer_: R&D dan merek di kedua ujung, nilai tertinggi, manufaktur di tengah, nilai terendah[^4]. Orang Taiwan menggambar diagram ini sendiri, dan kemudian selama tiga puluh tahun berikutnya, pasukan utama teknologi Taiwan terjebak di titik terendah kurva: Foxconn merakit iPhone untuk Apple, margin keuntungan sering hanya satu digit. Apple mengambil sebagian besar keuntungan dari seluruh industri ponsel, estimasi puncak penelitian pasar melebihi 80%[^11].

[TSMC](/id/economy/tsmc/) adalah pengecualian itu. Dengan prinsip "tidak merancang produk sendiri", itu mengubah manufaktur kontrak itu sendiri menjadi bisnis mencengkeram kedua ujung: pelanggan tidak dapat pergi darinya, dan ia tidak perlu bersaing dengan pelanggan untuk pujian konsumen. Namun bisnis ini dibangun di atas kepercayaan B2B, tidak perlu bercerita kepada publik. Kerendahan hati TSMC adalah strategi bisnis, efek samping adalah: tempat Taiwan yang paling mahir membuat chip, justru adalah tempat yang paling tidak perlu berlatih bercerita.

Juga bukan tidak ada yang pindah ke ujung kanan. ASUS menciptakan sub-brand ROG (Republic of Gamers) pada tahun 2006, menumbuhkan pemain game menjadi komunitas yang mengenal merek, Eradicator adalah salah satu penanda identifikasi perangkat keras gaming global paling terkenal[^15]. Namun ROG adalah minoritas: kebanyakan trademark perusahaan Taiwan bahkan tidak berani diperbesar di wajah depan produk.

Ujung kanan kurva, Taiwan sebenarnya sudah pernah berdiri. Acer pernah menjadi merek PC tiga besar dunia, empat huruf Acer pernah ditempel di pintu boarding seluruh dunia. Namun keuntungan PC terlalu tipis, terlalu tipis untuk premium merek menopang berat ujung kanan. ROG membuktikan ujung kanan dapat dinaiki, hanya saja Anda harus memilih medan perang yang tepat.

Hal yang paling kejam tentang kurva senyum adalah bahwa itu adalah pertanyaan pilihan ganda yang tidak ada orang yang ulang dalam tiga puluh tahun. Tiga puluh tahun lalu Taiwan memilih untuk berdiri di tengah, karena itu adalah jawaban yang paling masuk akal pada saat itu: tanpa modal, tanpa merek, tanpa pasar, manufaktur kontrak adalah satu-satunya jalan keluar. Bahaya yang sebenarnya adalah terus menggunakan jawaban masuk akal tiga puluh tahun lalu sebagai jawaban hari ini.

## Ekonomi Bercerita

Angka paling jujur. NVIDIA tahun fiskal 2026 (Februari 2025 hingga Januari 2026) pendapatan $215,9 miliar, laba bersih $120,1 miliar[^5]. TSMC tahun 2025 pendapatan $122,4 miliar, laba bersih $55,1 miliar[^6]. Hampir semua chip NVIDIA dikirimkan ke TSMC untuk diproduksi, dirinya sendiri menjual ekosistem CUDA, "era AI" ini. Hasilnya: perusahaan yang merancang cerita, pendapatannya 1,8 kali lipat perusahaan yang membuat, laba bersih 2,2 kali lipat.

Naik ke ujung konsumen di rantai pasokan yang sama, gradien lebih curam:

| Posisi Rantai Pasokan  | Pendapatan 2025 | Laba Bersih      | Margin Laba Bersih |
| ---------------------- | --------------- | ---------------- | ------------------ |
| Foxconn (Rakit iPhone) | 8,1 triliun NTD | 189,4 miliar NTD | 2,3%               |
| Apple (Jual iPhone)    | $416,2 miliar   | $112 miliar      | 26,9%              |
| TSMC (Buat Chip)       | $122,4 miliar   | $55,1 miliar     | 45,0%              |
| NVIDIA (Ceritakan)     | $215,9 miliar   | $120,1 miliar    | 55,6%              |

_Data: Foxconn dan Apple tahun fiskal 2025, NVIDIA FY2026 (hingga Januari 2026), TSMC tahun 2025, diambil dari laporan keuangan masing-masing perusahaan (cross-checked melalui kolom laporan Wikipedia)[^5][^6][^11]._

Rakitan menghasilkan 2,3%, penjualan merek menghasilkan 26,9%, membuat proses canggih menghasilkan 45%, menceritakan chip sebagai era menghasilkan 55,6%. Valuasi adalah diskon dari aliran kas masa depan. Masa depan setengah dibangun oleh teknik, setengah dikatakan. Budaya default Silicon Valley adalah fake it till you make it (mengklaim dulu, cari cara kemudian). Budaya default Taiwan adalah "belum dilakukan, tidak berani berbicara". Perbedaan antara dua budaya bukan perbedaan moral, itu perbedaan tingkat diskonto: pasar memberi diskon kecil pada "cerita yang bisa diceritakan", memberi diskon besar pada "kemampuan yang tidak bisa diceritakan".

Mekanisme premium merek juga sangat langsung: chip yang sama dari TSMC, tempel merek Snapdragon, pabrik ponsel bersedia membayar lebih uang, itu adalah premium. Dari mana premium datang? Dari pertemuan peluncuran, dari Snapdragon Summit tahunan yang teratur, dari harapan pembiasaan pengembang "Snapdragon berikutnya pasti lebih cepat". Hal-hal ini tidak memasuki tabel spesifikasi, namun mereka memasuki laporan keuangan.

Ada yang mengatakan, ini adalah kesalahan pasar, Wall Street sedang hype. Namun pasar yang sama, untuk TSMC tidak ada diskon: margin laba bersih TSMC 45%, lebih tinggi dari Apple. Pasar sebenarnya sangat bersedia membayar kemampuan Taiwan, syaratnya adalah bahwa kemampuan harus bisa diceritakan. Pelanggan TSMC menceritakannya: setiap konferensi peluncuran Apple, setiap GTC NVIDIA, adalah iklan gratis TSMC.

Ada yang bertanya, menceritakan cerita besar, apakah akan menjadi kebohongan? Jawaban Jensen Huang ditulis di laporan keuangan: setiap kata yang dia katakan, di belakangnya ada kapasitas produksi, tingkat keberhasilan, volume pengiriman yang menopang. Garis batas antara bercerita baik dan tipu adalah apakah ada sesuatu yang menangkap setelah bercerita. Taiwan memiliki sesuatu, hanya saja sering lupa untuk menceritakannya.

> ⚠️ **Sudut Pandang Kontroversial**
> Satu pihak mengatakan, narasi 60 poin Taiwan adalah kebajikan: urat nadi bisnis manufaktur kontrak adalah kepercayaan, kerendahan hati adalah aset; jika TSMC sepanjang waktu mengadakan konferensi peluncuran, pelanggan malah tidak bisa tidur. Pihak lain mengatakan, diskon narasi akan ditransmisikan secara sistematis: valuasi perusahaan Taiwan diremehkan, gaji mengikutinya, talenta mengalir ke perusahaan yang bisa bercerita, generasi berikutnya dari produk kemudian lebih tidak bisa bercerita. Pihak mana pun yang Anda percayai, itulah loop yang akan Anda tinggali. Kedua pernyataan ini masih hidup sekarang, dan keduanya belum menang.

## Taiwan Tidak Bisa Bercerita? Tidak Sebenarnya

Orang yang berbicara dengan baik, Taiwan sebenarnya semuanya memiliki.

Morris Chang pada tahun 2021 menyebut TSMC "Gunung Pelindung Negara"[^12]. Empat kata, membuat seluruh Taiwan dengan senang hati memberikan jalan bagi industri chip, air, listrik. Ini adalah penamaan tingkat atas dalam sejarah pemasaran: sejak saat itu setiap berita tentang kekurangan air atau listrik secara otomatis menjadi iklan layanan publik "Gunung Pelindung Negara membutuhkan Anda". Seorang pengusaha berusia sembilan puluhan pada tahun 2024 menerbitkan otobiografi jilid dua, menjadi buku penjual terbaik[^13b].

Fakta bahwa otobiografi menjadi buku penjual terbaik itu sendiri sangat menjelaskan masalahnya: seorang pengusaha berusia sembilan puluhan, menulis hidupnya menjadi dua buku, orang Taiwan rela mengantre untuk membeli. Orang Taiwan suka mendengarkan cerita, juga suka membeli cerita, hanya saja ketika sampai giliran sendiri untuk naik panggung, cerita menjadi pendek.

Batch orang Taiwan yang bisa bercerita ini, resume mereka memiliki satu kesamaan: Morris Chang bekerja di Texas Instruments selama dua puluh lima tahun, Jensen Huang memulai bisnis di Silicon Valley selama tiga puluh tahun, Lisa Su mendapat gelar doktor di MIT. Tidak satu pun yang berlatih kemampuan ini di Taiwan. Tanah Taiwan menghasilkan jenis orang ini, namun tempat kerja Taiwan tidak mengajar hal ini. Sekolah mengajar cara menggambar sirkuit dengan benar, tidak mengajar cara menceritakan sirkuit sebagai era.

Jadi masalah tidak pernah tentang bakat. Masalahnya adalah struktur industri Taiwan mengirim semua orang yang bisa bercerita ke luar negeri, atau mengirim ke ruang rapat manufaktur kontrak. Untuk membuka simpul ini, tidak cukup dengan departemen PR beberapa perusahaan, perlu diubah dari tata kelola perusahaan, struktur gaji sampai pendidikan sekolah.

![Morris Chang hadir sebagai perwakilan pemimpin dalam video pertemuan pemimpin ekonomi APEC 2021, foto resmi kantor presiden](/article-images/technology/morris-chang-apec-2021.webp)
_Morris Chang menghadiri pertemuan pemimpin ekonomi APEC 2021. Foto: Wang Yu Ching / Kantor Presiden, CC BY 2.0. [Lisensi via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg)._

Stan Shih menggambar kurva senyum, juga menjual konsep: satu konsep membuat filosofi manajemen perusahaannya dirujuk oleh sekolah bisnis di seluruh dunia.

Jensen Huang lahir di Tainan, pindah ke Amerika pada usia sembilan tahun[^13]. Lisa Su lahir di Tainan, pindah ke Amerika pada usia tiga tahun[^14]. Dua orang yang paling mahir menceritakan kisah semikonduktor di dunia, keduanya adalah benih Taiwan, tanah Amerika.

![Jensen Huang memberikan kuliah di kelas CS 153 Universitas Stanford, mengenakan jaket kulit hitam ikonik, dengan tangan membuat gestur penjelasan](/article-images/technology/jensen-huang-stanford-2026.webp)
_Jensen Huang memberikan kuliah di CS 153 Universitas Stanford, April 2026. Foto: Anderseidesvik, CC BY-SA 4.0. [Lisensi via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg)._

Ada juga orang yang bisa bercerita di startup Taiwan. Gogoro didirikan pada tahun 2011, pada tahun 2015 di CES menceritakan stasiun penggantian baterai sebagai "jaringan energi", mengatakan dirinya adalah perusahaan energi, kebetulan menjual sepeda motor. Cerita sangat menarik sehingga pada tahun 2022 membuatnya naik ke Nasdaq melalui SPAC, pada tahun 2024 bahkan Castrol di bawah BP menginvestasikan lima puluh juta dolar[^16]. Gogoro masih mencari loop bisnis tertutup sampai sekarang, namun contohnya menunjukkan: bisa bercerita, setidaknya mendapat tiket untuk diperiksa oleh pasar. Tidak bisa bercerita, bahkan pintunya tidak bisa masuk.

Pola sangat jelas: Taiwan tidak kekurangan bakat bercerita, kekurangan lingkungan yang memungkinkan cerita dikembangkan. Gen manufaktur kontrak mengajar "pelanggan adalah tokoh utama", lingkungan bercerita mengajar "saya bisa menjadi tokoh utama".

> 📝 **Catatan Kurator**
> Hal paling menarik tentang empat kata "Gunung Pelindung Negara": ketika Morris Chang menceritakannya, dia berbicara kepada masyarakat Taiwan tentang cerita yang perlu didukung: butuh listrik, butuh air, butuh tanah, butuh talenta. Bercerita dengan baik bukan vanitas, itu infrastruktur kebijakan industri. Orang Taiwan mengerti empat kata ini, berarti kekuatan narasi Taiwan tidak rusak, hanya tidak sering digunakan untuk berkomunikasi ke luar.

## Tabel Terjemahan Subteks

Satu fakta teknis yang sama, dua cara berbicara. Terjemahkan dialog di balik dialog, lihat sendiri perbedaannya.

| Pembicara                             | Apa yang Mereka Katakan Secara Terbuka                                                                     | Terjemahan Subteks                                                                                                                                                         |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Konferensi Hasil TSMC                 | "Tingkat pemanfaatan kapasitas terus meningkat, kami tetap percaya diri dalam pertumbuhan jangka panjang." | Chip paling canggih di dunia hanya saya yang bisa buat, tapi bicara begini tidak terasa seperti insinyur.                                                                  |
| Presentasi Insinyur Taiwan            | "Teknologi ini masih memiliki ruang optimasi."                                                             | Kami sudah mencapai nomor satu dunia, dulu kasih diskon 20%, takut ketahuan kalau berhasil.                                                                                |
| Startup Amerika pitch halaman pertama | "We are building the world's first AI-native platform to reinvent a $5 trillion industry."                 | Sekarang kantor hanya punya tiga insinyur dan satu PowerPoint, tapi impian tak ternilai, kasih uang dulu.                                                                  |
| Startup Taiwan pitch halaman pertama  | "Anggota tim lulus dari universitas top, pernah bekerja di MediaTek delapan tahun, memiliki 12 paten."     | Kami tidak tahu cara bercerita visi, pakai gelar dan pengalaman kerja jadi rompi anti peluru dulu.                                                                         |
| Jensen Huang                          | "The more you buy, the more you save."                                                                     | Kartu ini mahal, tapi kalau tidak beli, listrik dan antrian komputasi akan makan lebih banyak.                                                                             |
| Qualcomm Snapdragon Summit            | "The era of on-device AI begins now."                                                                      | Performa menunggu iPhone keluar baru bilang, sekarang bikin Anda merasa sedang saksikan era.                                                                               |
| Iklan HTC 2010                        | "Quietly Brilliant"                                                                                        | Kami sangat brilliant, cuma sungkan bersuara keras.                                                                                                                        |
| Iklan Samsung 2011                    | "The Next Big Thing is already here."                                                                      | Orang di antrian toko Apple kelihatannya bodoh, datang beli saya.                                                                                                          |
| Elon Musk                             | "We will make life multiplanetary."                                                                        | Roket kadang meledak sekarang, tapi narasi harus terbang duluan.                                                                                                           |
| Morris Chang 2021                     | "Semikonduktor adalah Gunung Pelindung Negara Taiwan."                                                     | Empat kata, buat semua Taiwan mau kasih jalan, air, listrik untuk chip. Satu orang Taiwan yang bisa bercerita, satu kalimat setara seluruh slide konferensi hasil setahun. |

_Kalimat dalam kutipan untuk TSMC, insinyur Taiwan, dua startup, dan Qualcomm adalah generalisasi kalimat tipikal, bukan kutipan harfiah; lima kalimat untuk Jensen Huang, HTC, Samsung, Musk, Morris Chang adalah slogan atau pernyataan publik sebenarnya[^17][^18][^12]._

Setelah terjemahan, Anda akan menemukan, perbedaan antara bercerita baik dan bercerita buruk, sering hanya dua cara mengatur ulang kalimat yang sama.

Tabel ini bukan untuk menertawakan siapa pun. Kerendahan hati sangat berguna dalam teknik: itu membuat kerja sama berjalan lancar, membuat kontrol kualitas tidak berani longgar. Tapi kerendahan hati sekali keluar dari ruang rapat, berubah menjadi kupon diskon. Taiwan perlu belajar, simpan kerendahan hati di lab, bawa kepercayaan diri ke panggung.

## Kembali ke Auditorium Olahraga Taiwan University

Setiap slide yang Jensen Huang ceritakan malam itu, lokasi fisiknya berada di ruang bersih Hsinchu, Taichung, Tainan. Cerita selesai, dunia membelinya. Orang di ruang bersih terus bergantian shift, konferensi hasil tetap konservatif.

Teknologi 100 poin tidak akan otomatis menjadi narasi 100 poin. 40 poin itu butuh ada orang naik panggung, buat jaket kulit jadi perlengkapan perang, ceritakan chip menjadi era.

Gunung Pelindung Negara berikutnya Taiwan, mungkin bukan chip baru mana pun, tapi cerita baru mana pun.

> ✦ Qualcomm membuat satu SoC menjadi merek yang berjalan di red carpet, Jensen Huang membuat chip yang dibuat TSMC menjadi era, Morris Chang dengan empat kata buat semua Taiwan mau kasih jalan untuk semikonduktor. Taiwan punya sesuatu yang 100 poin, kekurangan orang yang mau naik panggung, menceritakannya menjadi 100 poin.

---

**Bacaan Lanjutan**:

- [Industri Semikonduktor: Dari Transfer Teknologi RCA ke Nitrida Gallium dan Kemasan Kuantum, 50 Tahun Revolusi Material](/id/technology/taiwan-electricity-and-semiconductors) — Narasi teknis lengkap Gunung Pelindung Negara, dan "NVIDIA mengosongkan kapasitas CoWoS" yang mengikat itu
- [Taiwan: TSMC](/id/economy/tsmc) — Perusahaan yang membuat kerendahan hati menjadi model bisnis ini, struktur tata kelola dan keuangannya
- [Taiwan: MediaTek](/id/economy/mediatek) — Pabrik chip ponsel volume terbesar dunia, mengapa narasi masih tertinggal
- [Taiwan: HTC](/id/economy/htc-android-pioneer-vr-transformation) — Cerita bisnis perusahaan lengkap Quietly Brilliant yang mati
- [Jensen Huang](/id/people/jensen-huang) — Lahir di Tainan, tumbuh besar di Amerika, orang paling mahir bercerita tentang chip di dunia
- [NVIDIA di Taiwan](/id/technology/nvidia-in-taiwan) — Hubungan jaket kulit itu dengan rantai pasokan Taiwan
- [Computex: Tiga Pameran Komputer Internasional Besar, Dua Tertutup, Sisanya Tumbuh di Taipei](/id/technology/computex) — Setiap Mei, raksasa AI global secara bergilir di Taipei menggunakan cara bercerita yang sama

## Sumber Gambar

Artikel ini menggunakan 5 gambar berlisensi CC, di-cache di `public/article-images/technology/`:

- [TSMC Fab 14B May 2025](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg) — Foto: 4300streetcar, CC BY 4.0, Wikimedia Commons
- [HTC One 03](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG) — Foto: Asmoth, CC BY-SA 4.0, Wikimedia Commons
- [HTC Dream opened](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg) — Foto: Marcus Sümnick, CC BY 3.0, Wikimedia Commons
- [Morris Chang at APEC 2021](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg) — Foto: Wang Yu Ching / Kantor Presiden, CC BY 2.0, Wikimedia Commons
- [Jensen Huang at Stanford CS 153](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg) — Foto: Anderseidesvik, CC BY-SA 4.0, Wikimedia Commons

## Referensi

[^1]: [The Free Library — HTC Market Cap Surpasses Nokia](https://www.thefreelibrary.com/HTC+Market+Cap+Surpasses+Nokia.-a0253461010) — 7 April 2011 nilai pasar HTC sekitar $33,8 miliar, melampaui Nokia

[^2]: [Wikipedia — HTC (perusahaan)](https://zh.wikipedia.org/wiki/%E5%AE%8F%E9%81%94%E5%9C%8B%E9%9A%9B%E9%9B%BB%E5%AD%90) — Pangsa pasar ponsel 2011 sekitar 20%, nilai pasar melampaui triliun, harga saham pernah naik di atas seribu

[^3]: [Wikipedia — HTC Dream](https://en.wikipedia.org/wiki/HTC_Dream) — Smartphone Android pertama di dunia tahun 2008

[^4]: [Wikipedia — Kurva Senyum (Smile Curve)](https://zh.wikipedia.org/wiki/%E5%BE%AE%E7%AC%91%E6%9B%B2%E7%B7%9A) — Stan Shih mengajukan dalam _Remanufakturing Acer_ tahun 1992

[^4b]: [Wikipedia — MediaTek](https://zh.wikipedia.org/wiki/%E8%81%AF%E7%99%BC%E7%A7%91%E6%8A%80) — Pemasok SoC ponsel terbesar di dunia menurut volume pengiriman; pangsa pasar chip TV sekitar 70%

[^5]: [Nvidia — Fourth Quarter and Fiscal 2026 Financial Results](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026) — Siaran pers resmi NVIDIA; FY2026 pendapatan $215,9 miliar, laba bersih $120,1 miliar (cross-checked dengan kolom laporan Wikipedia: https://en.wikipedia.org/wiki/Nvidia)

[^6]: [TSMC — Quarterly Results Q4 2025](https://investor.tsmc.com/english/quarterly-results/2025/q4) — Halaman investor resmi TSMC; tahun 2025 penuh pendapatan $122,42 miliar, laba bersih $55,13 miliar (cross-checked dengan kolom laporan Wikipedia: https://en.wikipedia.org/wiki/TSMC)

[^7]: [Counterpoint — MediaTek Becomes Biggest Smartphone Chipset Vendor in Q3 2020](https://www.counterpointresearch.com/insights/mediatek-becomes-biggest-smartphone-chipset-vendor-q3-2020/) — Kuartal ketiga 2020 volume pengiriman chip ponsel MediaTek untuk pertama kalinya melampaui Qualcomm, pangsa pasar sekitar 31%

[^8]: [Wikipedia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — Platform SoC Snapdragon diluncurkan November 2006; asal penamaan merek dari nama bunga snapdragon, Dimensity berasal dari bintang ketiga Tujuh Bintang Utara (kedua sumber penamaan adalah data publik merek, menunggu link sumber resmi komplementer)

[^9]: [MediaTek — Siaran Pers Dimensity 9400](https://corp.mediatek.com/news-events/press-releases/mediatek-launches-flagship-dimensity-9400-soc-for-advanced-capabilities) — Dimensity 9400 diluncurkan Oktober 2024; lingkaran evaluasi umumnya dipimpin oleh performa efisiensi energi (deskripsi generalisasi). Lihat [Wikipedia — Vivo X200](https://en.wikipedia.org/wiki/Vivo_X200) untuk perangkat peluncuran pertama

[^10]: [Wikipedia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — Snapdragon Summit 2024 diadakan di Maui, Hawaii, meluncurkan Snapdragon 8 Elite (URL siaran pers resmi sudah hilang, menggunakan sumber sekunder Wikipedia sebagai gantinya)

[^11]: [Wikipedia — Foxconn](https://en.wikipedia.org/wiki/Foxconn) / [Apple Inc.](https://en.wikipedia.org/wiki/Apple_Inc.) — Pendapatan tahun fiskal 2025 Foxconn 8,103 triliun NTD, laba bersih 189,35 miliar NTD (margin laba bersih sekitar 2,3%); pendapatan FY2025 Apple $416,2 miliar, laba bersih $112 miliar (margin laba bersih sekitar 26,9%). Pangsa keuntungan ponsel Apple periode puncak melebihi 80%: estimasi sejarah Counterpoint (menunggu link sumber komplementer)

[^12]: [Wikipedia — Gunung Pelindung Negara](https://zh.wikipedia.org/wiki/%E8%AD%B7%E5%9C%8B%E7%A5%9E%E5%B1%B1) — Nama alternatif TSMC (silicon shield); "Semikonduktor adalah Gunung Pelindung Negara Taiwan" adalah pernyataan publik Morris Chang tahun 2021 (menunggu link sumber berita komplementer)

[^13]: [Wikipedia — Jensen Huang](https://zh.wikipedia.org/wiki/%E9%BB%83%E4%BB%81%E5%8B%B3) — Lahir 1963 di Tainan, pindah ke Amerika pada 1972 (usia sembilan tahun)

[^13b]: Otobiografi Morris Chang jilid dua diterbitkan November 2024, penjualan tingkat buku penjual terbaik tahun itu (menunggu link sumber komplementer)

[^14]: [Wikipedia — Lisa Su](https://zh.wikipedia.org/wiki/%E8%98%87%E5%A7%BF%E4%B8%B0) — Lahir 1969 di Tainan, pindah ke Amerika pada usia tiga tahun bersama keluarga

[^15]: [Wikipedia — ASUS](https://zh.wikipedia.org/wiki/%E8%8F%AF%E7%A2%A9) — Menciptakan sub-brand "Republic of Gamers" (ROG) tahun 2006

[^16]: [Wikipedia — Gogoro](https://en.wikipedia.org/wiki/Gogoro) — Didirikan 2011; 2015 meluncurkan Gogoro Smartscooter dan jaringan energi di CES; 2022 bergabung dengan SPAC Poema Global untuk naik ke Nasdaq; 2024 Castrol di bawah BP mengumumkan investasi maksimal $50 juta

[^17]: [NVIDIA GTC 2024 Keynote](https://www.youtube.com/watch?v=Y2F8yisiS6E) — Jensen Huang "The more you buy, the more you save" berasal dari video acara resmi ini

[^18]: "Quietly Brilliant" adalah tagline brand global HTC sejak 2009, "The Next Big Thing is Already Here" adalah tagline iklan Galaxy Samsung 2011, "We will make life multiplanetary" adalah pernyataan misi SpaceX (ketiganya adalah teks bisnis publik)

[^19]: [NVIDIA at Computex 2024 — Video Pidato Utama Resmi](https://www.youtube.com/watch?v=pKXDVsWZmUU) — Jensen Huang pidato utama Computex 2 Juni 2024 di Auditorium Olahraga Taiwan University
