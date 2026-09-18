---
title: 'Taiwan Teknologi Cerita: 100 Poin Chip, 60 Poin Mikrofon'
description: 'Taiwan mampu membuat chip dengan skor 100, namun terbiasa mempromosikannya dengan nada presentasi pemasok. Chip yang sama, Qualcomm mempromosikannya sebagai mitos, MediaTek sebagai spesifikasi teknis; NVIDIA bahkan tidak pernah membuatnya sendiri, namun labanya dua kali lipat dibanding pihak yang membuatnya. Selisih 40 poin ini, pasar sudah lama menghitungnya, dan faktur penuhnya ada pada margin laba.'
date: 2026-08-15
category: 'Technology'
tags:
  [
    'teknologi',
    'cerita',
    'merek',
    'setengah pengarah',
    'TSMC',
    'NVIDIA',
    'MediaTek',
    'Qualcomm',
    'HTC',
    'Jensen Huang',
    'Morris Chang',
    'kurva senyum',
    'pesan tersirat',
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
rationale: "{'why_this_hook': '從「同一顆晶片兩種講法」的反差切入，讓讀者先看見那 40 分長什麼樣子，再用財報數字把它換算成錢。', 'whats_excluded': '政府政策與主權 AI（政治敏感，超出本文查證範圍）；韓國三星製程競爭史；台灣新創公司名單流水帳；估值模型的公式化推導。', 'where_it_hedges': '張忠謀「護國神山」2021 原始報導與張忠謀自傳銷量標「待補來源」；蘋果手機利潤占比以「高峰估計」軟化；示意歸納的引語在文內明示非逐字。', 'whos_pushing_back': '認為低調是代工生意命脈、吹牛會傷信任的供應鏈從業者；認為台灣工程師文化不需要向矽谷敘事投降的人；被拿來當負面教材的公司員工。'}"
sporeLinks: []
curation: 'incubating'
translatedFrom: 'Technology/台灣科技說故事.md'
sourceCommitSha: '6d762f5ac'
sourceContentHash: 'sha256:7e79f4d7834c55c1'
sourceBodyHash: 'sha256:e24305e511c42507'
translatedAt: '2026-09-19T01:37:24+08:00'
---

# Taiwan Teknologi Cerita: 100 Poin Chip, 60 Poin Mikrofon

![Fasade gedung Fab 14B TSMC di Kawasan Ilmu Tainan, bangunan industri bertingkat menjulang di bawah langit biru, menjadi representasi fisik kapasitas proses maju](/article-images/technology/tsmc-fab-14b-2025.webp)
_Industri Fab 14B TSMC di Tainan, Mei 2025. Foto: 4300streetcar. [Lisensi melalui Wikimedia Commons](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg)._

> **Ringkasan 30 detik:** Juni 2024, Jensen Huang di gedung olahraga Nasional Universitas Taiwan (NTU) mempromosikan chip yang dibuat oleh TSMC sebagai simbol sebuah zaman; pada kuartal yang sama, presentasi konferensi pers TSMC masih penuh dengan angka keuangan, utilizasi kapasitas, dan proyeksi konservatif. NVIDIA FY2026 mencatatkan pendapatan $21,59 miliar dan laba bersih $12,01 miliar; TSMC yang membuat chip untuk NVIDIA, pada 2025 mencatatkan pendapatan $12,24 miliar dan laba bersih $5,51 miliar[^5][^6]。Mereka yang merancang cerita, masing-masinging memperoleh ganda lipat laba dibanding mereka yang membuatnya. Artikel ini akan mengekstrak cerita di balik cerita.

2 Juni 2024, gedung olahraga NTU. Jensen Huang mengenakan jaket kulit hitamnya, berbicara selama dua jam. Penontonnya seperti konser: live streaming, media asing, kerumunian orang dengan ponsel. Ia berbicara tentang Blackwell, tentang CUDA, mengubah setiap slide menjadi upacara pembukaan sebuah zaman[^19]。

Di pulau yang sama, hanya berkendara selama kurang dari 100 km ke selatan, ke Hsinchu. Konferensi pers TSMC adalah pengalaman yang berbeda: angka keuangan, utilizasi kapasitas, pertumbuhan kuartalan, proyeksi konservatif. Semua chip paling canggih di dunia berada di lini produksi itu, namun presentasinya terdengar seperti kelas akuntansi.

Satu chip, dua cara berbicara. Selisih 40 poin di antara keduanya, pasar sudah lama menghitungnya.

Perbedaan antara dua adegan ini, orang Taiwan sebenarnya sudah melihat sejak kecil. Kita terbiasa: produk kami buat, sorak sorai adalah milik orang lain. Di pameran, booth perusahaan Taiwan bicara tentang biaya, yield, dan jadwal pengiriman; panggung merek asing bicara tentang masa depan, misi, dan perubahan dunia. Jeda di antara keduanya adalah 40 poin itu. Artikel ini akan menunjukkan apa kelihatannya.

## Satu Chip, Dua Cara Berbicara

Oktober 2024, dua presentasi berjarak kurang dari dua minggu. MediaTek mengadakan presentasi Dimensity 9400 di Shenzhen, sementara Qualcomm mengadakan Snapdragon Summit di Hawai[^9][^10]。

[MediaTek](/id/economy/mediatek/) adalah salah satu pemasok chip seluler terbesar di dunia berdasarkan volume pengiriman, dengan pangsa pasar TV chip sebesar 70%[^4b]。Volume pengiriman Qualcomm lebih sedikit, namun pendapatan dan premi mereknya lebih tinggi. Apa perbedaannya? Qualcomm menjual nama "Snapdragon": sejak dinamai pada 2006, hampir dua puluh tahun terjalin[^8]，memiliki mascot sendiri, dan acara teknologi tahunan sendiri. Kalimat "Powered by Snapdragon" di setiap presentasi ponsel flagship global lebih mencuri perhatian daripada merek ponsel itu sendiri.

MediaTek menjual spesifikasi teknis. Presentasi Dimensity 9400 penuh dengan proses teknis, IPC, dan kurva efisiensi energi, semua angka dapat diverifikasi; komunitas pengujicoba memberinya julukan "Raja Efisiensi"[^9]。Namun konsumen hanya mengenal Snapdragon.

Throne volume pengiriman, MediaTek sebenarnya sudah lama duduk di sana. Pada kuartal ketiga 2020, volume pengiriman chip seluler MediaTek berhasil melampaui Qualcomm, dengan pangsa pasar sekitar 31%[^7]。Namun selama bertahun-tahun di puncak volume pengiriman, pendapatan utama MediaTek berasal dari ponsel kelas menengah dan bawah; puncak kelas flagship tetap berada di tangan Qualcomm. Hingga akhir 2021, ketika Dimensity 9000 diluncurkan, MediaTek baru pertama kali berhasil masuk ke tabel perbandingan ponsel flagship Android. Spesifikasinya sudah menyamai, namun presentasinya masih terlihat seperti presentasi pemasok kepada klien.

MediaTek sebenarnya menyadari masalah ini. Beberapa tahun terakhir, mereka mulai belajar: chip flagship memiliki nama sendiri, presentasi dilengkapi dengan pertunjukan pembukaan, dan produsen ponsel kolaboratif pun rela memasukkan "Dimensity" ke dalam iklan. Arahnya benar, hanya saja dimulai terlalu lama—lebih dari satu dekade. Membangun merek adalah lomba jarak jauh, dan mereka yang lebih dulu mulai akan terus mendapatkan keuntungan kompounding setiap putaran.

> 💡 **Fakta Menarik**
> Snapdragon berasal dari nama bunga (snapdragon flower), sejenis bunga; Dimensity berasal dari bintang ketujuh kelima Bintang Kecil Urut, yaitu bintang ketiga[^8]。Satu perusahaan mengambil nama dari kebun bunga, satu lagi dari peta bintang. Keduanya bagus. Perbedaannya adalah: Qualcomm telah menanam bunga itu menjadi merek yang bisa berjalan di red carpet, sementara cahaya Dimensity kebanyakan hanya tersimpan di spesifikasi teknis.

> 📝 **Catatan Kurator**
> Perang merek di industri chip sangat konkret: konsumen tidak peduli apakah chip itu dibuat oleh TSMC, yang penting apakah mereka membeli Snapdragon atau Dimensity. Qualcomm mulai membangun merek pada 2006, sementara MediaTek baru pada akhir 2019 mulai menempelkan seri "Dimensity" ke kelas flagship. Dua puluh tahun pertumbuhan naratif, tidak ada satu spesifikasi teknis pun yang bisa menyainginya.

## Bagaimana "Quietly Brilliant" Tewas

Mari kita mundur satu kasus yang lebih menyakitkan. Pada 7 April 2011, nilai pasar HTC melebihi Nokia, sekitar $33,8 miliar[^1]。Pada saat itu, HTC mendominasi pasar ponsel dengan sekitar 20%, bersama Samsung dan Apple sebagai Big Three[^2]。

Dari segi teknis, HTC hampir sempurna: pada 2008, HTC membuat ponsel Android pertama di dunia, G1[^3]。Pada 2013, One menggunakan body logam CNC, kamera resolusi tinggi, kamera ganda—semua inovasi yang ia lakukan lebih dulu. Namun, apakah Anda masih ingat slogan brand globalnya?

![Detail sisi HTC One M7, desain body logam CNC, pada saat diluncurkan pada 2013 menjadi patokan industri](/article-images/technology/htc-one-m7-2013.webp)
_HTC One (M7), 2013. Foto: Asmoth, CC BY-SA 4.0. [Lisensi melalui Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG)._

"Quietly Brilliant."

Di era yang sama, iklan Samsung "The Next Big Thing is Already Here" langsung memotret penggemar Apple yang mengantre di depan toko, menggambarkan mereka sebagai orang bodoh[^18]。HTC mengambil kesopanan sebagai nilai merek, sementara Samsung mengambil Apple sebagai tokoh antagonis. Beberapa tahun kemudian, harga saham HTC jatuh dari ribuan hingga ratusan[^2]。

HTC sebenarnya pernah mendapatkan kesempatan untuk bangkit. HTC One (M7) pada 2013 memiliki banyak keunggulan: body logam CNC, kamera UltraPixel resolusi tinggi, speaker stereo depan BoomSound. Tahun itu, HTC memenangkan hampir semua penghargaan "Ponsel Tahunan" dari berbagai media, namun penjualannya kalah jauh dibanding Samsung S4 yang rilis pada periode yang sama. Presentasi M7 berbicara tentang spesifikasi, Samsung berbicara tentang gaya hidup, Apple berbicara tentang sidik jari yang mengubah dunia. Tiga ponsel dari generasi yang sama, tiga cara berbicara, tiga nasib yang berbeda.

Melihat kembali, sebab kegagalan HTC tentu bukan hanya karena satu slogan. Namun kegagalan dalam menyusun narasi adalah boneka pertama yang jatuh: ketika pasar mulai memilih segmen berdasarkan cerita, mereka yang tidak bisa bercerita akan pertama-tama dimasukkan ke dalam keranjang "yang akan usang". Para insinyur tidak percaya hal ini, mereka merasa produk akan berbicara sendiri. Memang, produk bisa berbicara, namun sebagian besar konsumen tidak mengerti dan tidak ingin mendengarkan.

![HTC Dream dengan papan ketuknya yang terbuka, ponsel Android pertama di dunia pada 2008](/article-images/technology/htc-dream-g1-2008.webp)
_HTC Dream (T-Mobile G1), 2008. Foto: Marcus Sümnick, CC BY 3.0. [Lisensi melalui Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg)._

> 📝 **Catatan Kurator**
> "Quietly Brilliant" sebenarnya adalah terjemahan dari pesan tersirat: sebuah perusahaan yang memilih "rendah hati" sebagai nilai merek global, berarti mereka secara aktif melepahkan hak naratif. Spesifikasi teknis akan dilupakan, cerita akan diingat. HTC membuat semua pilihan teknis yang benar, namun kalah dalam semua pilihan naratif.

## Kurva Senyum: Taiwan sudah menggambar peta posisinya 30 tahun yang lalu

Tragedi HTC bukanlah kasus tunggal, ada diagramnya.

Pada 1992, Shi Zhenrong menggambarkan "Kurva Senyum" dalam buku "Membangun Acer": R&D dan merek berada di ujung-ujung, di mana nilainya tertinggi, sementara manufaktur berada di tengah, di mana nilainya terendah[^4]。Taiwan sendiri yang menggambar diagram ini, lalu selama tiga puluh tahun berikutnya, mayoritas industri teknologi Taiwan terjebak di titik terendah kurva: Foxconn merakit iPhone untuk Apple, marginnya selalu berada di angka tunggal. Apple mengambil sebagian besar keuntungan dari seluruh industri ponsel, perkiraan puncaknya melebihi 80%[^11]。

[TSMC](/id/economy/tsmc/) adalah pengecualiannya. Dengan menjaga prinsip "tidak merancang produk sendiri", TSMC berhasil mengubah layanan kontrak menjadi bisnis yang menghubungkan kedua ujung: klien tidak bisa berpisah darinya, dan TSMC tidak perlu bersaing dengan klien untuk menaklukkan konsumen. Namun bisnis ini didasarkan pada kepercayaan B2B, tidak perlu untuk cerita kepada publik. Kebijaksanaan rendah hati TSMC adalah strategi bisnis, dampak sampingnya adalah: tempat di Taiwan yang paling ahli membuat chip, justru adalah tempat yang paling tidak perlu berlatih cerita.

Tidak berarti tidak ada yang mencapai ujung kanan. ASUS pada 2006 mendirikan merek sekunder ROG (Republic of Gamers), memupuk komunitas gamer yang mengenali logo merek; "Beggar My Wallet" adalah salah satu logo pengenal hardware e-sports paling dikenal di dunia[^15]。Namun ROG adalah minoritas: sebagian besar merek perusahaan Taiwan, bahkan tidak berani menaruhnya di bagian depan produk.

Ujung kanan kurva, Taiwan juga pernah berdiri di sana. Acer dulu adalah salah satu tiga merek PC terbesar di dunia, lima huruf "Acer" pernah dipasang di pintu pesawat di bandara di seluruh dunia. Namun margin PC terlalu tipis, terlalu tipis untuk merek yang bisa menopang beban di ujung kanan. ROG membuktikan bahwa kita bisa berdiri di ujung kanan, hanya perlu memilih medan yang tepat.

Yang paling menyakitkan dari Kurva Senyum adalah ia adalah soal pilihan yang belum pernah dipertanyakan selama 30 tahun. Tiga puluh tahun yang lalu, Taiwan memilih untuk berdiri di tengah, karena itu adalah jawaban yang paling masuk akal saat itu: tidak ada dana, tidak ada merek, tidak ada pasar, kontrak adalah satu-satunya jalan. Yang benar-benar berbahaya adalah menganggap jawaban yang masuk akal 30 tahun yang lalu sebagai jawaban yang sama untuk hari ini.

## Ekonomi Berteriak

Angka paling jujur. NVIDIA tahun fiskal 2026 (Februari 2025 hingga Januari 2026) mencatatkan pendapatan $21,59 miliar dan laba bersih $12,01 miliar[^5]。TSMC pada 2025 mencatatkan pendapatan $12,24 miliar dan laba bersih $5,51 miliar[^6]。Chip NVIDIA hampir seluruhnya dibuat oleh TSMC, namun NVIDIA menjual ekosistem CUDA, menjual cerita "Zaman AI". Akhirnya: perusahaan yang merancang cerita, pendapatan 1,8 kali lipat dan laba bersih 2,2 kali lipat dibanding perusahaan yang membuatnya.

Di pasca pasokan yang sama, ketika bergerak ke konsumen, kemiringannya semakin curam:

| Posisi Pasokan           | Pendapatan 2025 | Laba Bersih      | Margin Laba |
| ------------------------ | --------------- | ---------------- | ----------- |
| Foxconn (merakit iPhone) | 8,1 triliun TWD | 18,94 miliar TWD | 2.3%        |
| Apple (menjual iPhone)   | $41,62 miliar   | $11,2 miliar     | 26.9%       |
| TSMC (membuat chip)      | $12,24 miliar   | $5,51 miliar     | 45.0%       |
| NVIDIA (bercerita)       | $21,59 miliar   | $12,01 miliar    | 55.6%       |

_Data: Foxconn dan Apple untuk tahun fiskal 2025, NVIDIA untuk FY2026 (hingga Januari 2026), TSMC untuk 2025, diambil dari laporan keuangan masing-masing perusahaan (diverifikasi silang dengan laman keuangan Wikipedia)[^5][^6][^11]。_

Merakit hanya mendapatkan 2.3%, menjual merek mendapatkan 26.9%, membuat chip proses maju mendapatkan 45%, dan bercerita tentang chip mendapatkan 55.6%. Valuasi adalah diskonto dari aliran kas masa depan. Setengah dari masa depan dibuat oleh rekayasa, setengahnya diceritakan. Budaya standar di Silicon Valley adalah "fake it till you make it" (klaim dulu, lalu buat). Budaya standar di Taiwan adalah "belum selesai, jangan bicarakan". Perbedaan antara kedua budaya bukan perbedaan moral, melainkan perbedaan diskonto: pasar memberikan sedikit diskonto untuk "cerita yang bisa diceritakan", namun memberikan banyak diskonto untuk "keahlian yang tidak bisa diceritakan".

Mekanisme premi merek sangat jelas: chip yang sama yang dibuat oleh TSMC, jika diberi logo Snapdragon, produsen ponsel akan rela membayar lebih. Dari mana premi itu berasal? Dari spektakel presentasi, dari setiap Summit tahunan, dari ekspektasi rutin pengembang bahwa "Snapdragon berikutnya pasti lebih cepat". Hal-hal ini tidak masuk ke spesifikasi teknis, namun masuk ke laporan keuangan.

Beberapa orang mungkin berkata, ini kesalahan pasar, Wall Street sedang membesok-besok. Namun pasar yang sama, tidak memberikan diskonto kepada TSMC: margin laba TSMC mencapai 45%, melebihi Apple. Pasar memang rela membayar untuk kemampuan Taiwan, dengan syarat kemampuan itu bisa diceritakan. Klien TSMC yang mewakili namanya: setiap presentasi Apple, setiap GTC NVIDIA, semuanya adalah iklan gratis TSMC.

Beberapa orang bertanya, apakah membesar-besarkan cerita akan berubah menjadi kebohongan? Jensen Huang menjawabnya di laporan keuangan: setiap kalimat yang ia katakan, didukung oleh kapasitas, yield, dan volume pengiriman. Perbedaan antara bisa bercerita dan bisa berteriak, adalah apakah ada sesuatu yang menangkap setelah cerita selesai. Taiwan memiliki sesuatu, hanya sering lupa untuk menceritakannya.

> ⚠️ **Pendapat Kontroversial**
> Satu kelompok berkata, 60 poin narasi Taiwan adalah kebaikan: inti bisnis kontrak adalah kepercayaan, dan rendah hati adalah aset; jika TSMC terus mengadakan presentasi, kliennya tidak akan bisa tidur nyenyak. Kelompok lain berkata, diskonto narasi akan menyebar secara sistematis: perusahaan Taiwan dihargai rendah, kompensasi ikut rendah, bakat akan mengalir ke perusahaan yang bisa bercerita, dan produk generasi berikutnya justru lebih sulit diceritakan. Anda percaya pada kelompok mana, Anda akan tinggal di lingkaran setanpa itu. Kedua pendapat ini masih hidup dan belum pernah menang.

## Taiwan Bukan Tidak Bisa Bercerita

Orang Taiwan yang bisa bercerita memang ada.

Morris Chang pada 2021 menyebut TSMC sebagai "Puncak Pelindung Nasional"[^12]。Empat kata ini membuat seluruh Taiwan rela mengorbankan listrik, air, lahan, dan bakat untuk industri chip. Ini adalah penamaan tingkat tinggi dalam sejarah pemasaran: sejak saat itu, setiap berita tentang kekurangan air dan listrik otomatis menjadi iklan publik "Puncak Pelindung Nasional butuh Anda". Pada akhir 2024, buku memoir Morris Chang yang berusia hampir 90 tahun menjadi bestseller[^13b]。

Fakta bahwa buku memoar seorang pengusaha berusia hampir 90 tahun menjadi bestseller, sudah cukup menjelaskan: seorang pengusaha Taiwan yang menulis hidupnya dalam dua buku, orang Taiwan antre untuk membelinyya. Orang Taiwan suka mendengar cerita, suka membeli cerita, hanya ketika gilirannya sendiri untuk berbicara di atas panggung, mereka terdiam.

Para pencerita Taiwan ini memiliki latar belakang yang sama: Morris Chang bekerja di Texas Instruments selama 25 tahun, Jensen Huang memulai startupnya di Silicon Valley selama 30 tahun, dan Su Shihfeng memperoleh gelar doktor di MIT. Tidak satu pun dari mereka yang belajar keahlian ini di Taiwan. Tanah di Taiwan bisa melahirkan jenis-jenis manusia ini, namun lingkungan kerja di Taiwan tidak mengajarkan hal ini. Sekolah mengajarkan cara menggambar sirkuit dengan benar, namun tidak mengajarkan cara menggambar sirkuit sebagai simbol zaman.

Jadi masalahnya tidak pernah pada bakat. Masalahnya adalah struktur industri Taiwan mengirim orang-orang yang bisa bercerita ke luar negeri, atau ke dalam ruang rapat kontrak. Untuk memecahkan teka-teki ini, hanya dengan departemen pemasaran beberapa perusahaan tidak cukup, harus dimulai dari tata kelola perusahaan, struktur kompensasi, hingga sistem pendidikan sekolah.

![Morris Chang hadir dalam konferensi pemimpin ekonomi APEC 2021 melalui video konferensi, foto resmi Gedung Presiden](/article-images/technology/morris-chang-apec-2021.webp)
_Morris Chang hadir dalam Konferensi Pemimpin Ekonomi APEC 2021. Foto: Wang Yu Ching / Gedung Presiden, CC BY 2.0. [Lisensi melalui Wikimedia Commons](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg)._

Shi Zhenrong yang menggambar Kurva Senyum, juga sedang menjual konsep: satu konsep yang membuat filosofi manajemen perusahaannya dikutip oleh seluruh akademisi bisnis di dunia.

Jensen Huang lahir di Tainan, pindah ke AS pada usia 9 tahun[^13]。Su Shihfeng lahir di Tainan, pindah ke AS pada usia 3 tahun[^14]。Dua orang yang paling ahli berbicara tentang chip setengah pengarah di dunia, adalah benih Taiwan yang tumbuh di tanah AS.

![Jensen Huang berbicara di kursus CS 153 di Universitas Stanford, mengenakan jaket kulit ikoniknya, menggesture dengan tangannya](/article-images/technology/jensen-huang-stanford-2026.webp)
_Jensen Huang berbicara di kursus CS 153 di Universitas Stanford, April 2026. Foto: Anderseidesvik, CC BY-SA 4.0. [Lisensi melalui Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg)._

Di kalangan startup Taiwan juga ada yang bisa bercerita. Gogoro didirikan pada 2011, pada 2015 di CES, Gogoro mempromosikan stasiun penggantian baterai sebagai "jaringan energi", mengatakan bahwa mereka adalah perusahaan energi, sambil menjual skuter. Ceritanya begitu menarik hingga pada 2022, Gogoro berhasil listing di NASDAQ melalui SPAC, dan pada 2024, Castrol di bawah naungan BP mengumumkan investasi hingga $50 juta[^16]。Gogoro hingga kini masih mencari model bisnis yang berkelanjutan, namun contohnya membuktikan: yang bisa bercerita, setidaknya mendapatkan tiket untuk diuji oleh pasar. Yang tidak bisa bercerita, bahkan tidak bisa masuk ke pintu.

Aturan yang jelas: Taiwan tidak kekurangan bakat untuk bercerita, yang kurang adalah lingkungan yang memungkinkan cerita untuk diperbesar. Gen kontrak mengajarkan "klien adalah tokoh utama", sementara lingkungan yang bisa bercerita mengajarkan "aku bisa menjadi tokoh utama".

> 📝 **Catatan Kurator**
> Keajaiban dari empat kata "Puncak Pelindung Nasional" adalah: ketika Morris Chang mengatakannya, ia sedang berbicara kepada masyarakat Taiwan sebuah cerita yang perlu didukung: butuh listrik, air, lahan, dan bakat. Kemampuan bercerita bukanlah kesombongan, melainkan infrastruktur kebijakan industri. Fakta bahwa orang Taiwan mengerti empat kata ini, menunjukkan bahwa kekuatan narasi Taiwan tidak rusak, hanya jarang digunakan secara eksternal.

## Tabel Terjemahan Pesan Tersirat

Satu fakta teknis yang sama, dua cara berbicara. Eksplor pesan tersirat di balik kalimat, perbedaannya sendiri akan terlihat.

| Pembicara                            | Kalimat yang Terdengar                                                                                                                                                     | Terjemahan Pesan Tersirat                                                                                                                                                                                        |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Konferensi Pers TSMC                 | "Kapasitas utilizasikan terus meningkat, kami tetap yakin pada pertumbuhan jangka panjang."                                                                                | Chip paling canggih di dunia hanya bisa kami buat, namun mengatakan hal ini tidak terlihat seperti insinyur.                                                                                                     |
| Presentasi Insinyur Taiwan           | "Teknologi ini masih ada ruang untuk dioptimalkan."                                                                                                                        | Kami sudah menjadi nomor satu di dunia, mari kami diskon dulu agar tidak kecewa.                                                                                                                                 |
| Pitch Startup AS Halaman Pertama     | "Kami sedang membangun platform AI pertama di dunia untuk merevolusi industri senilai $5 triliun."                                                                         | Saat ini kami hanya punya tiga insinyur dan satu PPT, namun mimpi tidak terbatas, silakan beri kami uang.                                                                                                        |
| Pitch Startup Taiwan Halaman Pertama | "Anggota tim kami lulus dari Tsing Hua, National Taiwan University, dan National Chiao Tung University, pernah bekerja di MediaTek selama 8 tahun, dan memiliki 12 paten." | Kami tidak tahu cara berbicara tentang visi, jadi kami menggunakan latar belakang akademik dan pengalaman kerja sebagai pelindung.                                                                               |
| Jensen Huang                         | "Semakin Anda beli, semakin Anda hemat."                                                                                                                                   | Kartu ini mahal, namun jika Anda tidak membelinya, biaya listrik dan komputasi yang harus Anda bayar akan lebih mahal.                                                                                           |
| Qualcomm Snapdragon Summit           | "Era AI on-device dimulai sekarang."                                                                                                                                       | Kami akan berbicara tentang performanya setelah iPhone keluar, dulu biarkan Anda merasa seperti sedang menyaksikan sebuah zaman.                                                                                 |
| Iklan HTC 2010                       | "Quietly Brilliant"                                                                                                                                                        | Kami sangat brilliant, namun tidak enak untuk berteriak keras.                                                                                                                                                   |
| Iklan Samsung 2011                   | "The Next Big Thing is Already Here."                                                                                                                                      | Orang-orang yang mengantre di depan toko Apple tampak bodoh, jadi belilah kami.                                                                                                                                  |
| Elon Musk                            | "Kami akan membuat kehidupan menjadi multiplanet."                                                                                                                         | Roket kami kadang-kadang meledak, namun narasi harus terbang dulu.                                                                                                                                               |
| Morris Chang 2021                    | "Setengah pengarah adalah puncak pelindung nasional Taiwan."                                                                                                               | Empat kata ini membuat seluruh Taiwan rela mengorbankan lahan, air, dan listrik untuk industri chip. Kata-kata yang bisa bercerita dari seorang pria Taiwan setara dengan satu tahun presentasi konferensi pers. |

_Tabel di atas mengandung kutipan dari TSMC, insinyur Taiwan, dua startup, dan Qualcomm yang merupakan contoh khas, bukan kutipan langsung; kutipan dari Jensen Huang, HTC, Samsung, Musk, dan Morris Chang adalah slogan atau pernyataan publik yang sebenarnya[^17][^18][^12]。_

Setelah menerjemahkan, Anda akan menyadari: perbedaan antara bisa bercerita dan tidak bisa bercerita, seringkali hanya terletak pada dua cara berkata yang sama.

Tabel ini tidak untuk mengejek siapa pun. Kesopanan dalam teknologi sangat berguna: ia memungkinkan kolaborasi berjalan lancar, dan kontrol kualitas tidak boleh longgar. Namun kesopanan yang keluar dari ruang rapat akan berubah menjadi kupon diskon. Taiwan harus belajar: biarkan kesopanan tersisa di laboratorium, bawa kepercayaan ke panggung.

## Kembali ke GOR NTU

Setiap slide yang Jensen Huang presentasikan pada malam itu, fisiknya berada di ruang bersih di New Taipei, Taichung, dan Tainan. Setelah cerita selesai, seluruh dunia membayar. Orang-orang di ruang bersih terus bergiliran, konferensi pers terus konservatif.

Teknologi dengan skor 100 tidak akan otomatis menjadi narasi dengan skor 100. 40 poin itu membutuhkan seseorang yang berdiri di atas panggung, mengenakan jaket kulit sebagai pakaian perang, dan mengubah chip menjadi simbol zaman.

Puncak pelindung nasional Taiwan berikutnya, mungkin bukan chip baru apa pun, melainkan cerita baru apa yang diciptakan.

> ✦ Qualcomm mengubah satu chip SoC menjadi merek yang bisa berjalan di red carpet; Jensen Huang mengubah chip yang dibuat oleh TSMC menjadi simbol zaman; Morris Chang menggunakan empat kata untuk membuat seluruh Taiwan mengorbankan untuk industri chip. Teknologi Taiwan memiliki hal-hal dengan skor 100, yang kurang adalah seseorang yang rela berdiri di atas panggung dan mengubahnya menjadi narasi dengan skor 100.

---

**Bacaan Lanjutan:**

- [Industri Setengah Pengarah: Dari Transfer Teknologi RCA hingga Nitrid Gallium dan Kemasan Kuantum selama 50 tahun](/id/technology/taiwan-semiconductor-industry) — Narasi teknis lengkap puncak pelindung nasional, serta ikatan "NVIDIA menguasai kapasitas CoWoS"
- [Taiwan Enterprise: TSMC](/id/economy/tsmc) — Struktur tata kelola dan keuangan perusahaan yang menuliskan rendah hati sebagai model bisnis
- [Taiwan Enterprise: MediaTek](/id/economy/mediatek) — Pabrik chip seluler dengan volume pengiriman terbesar di dunia, mengapa narasi masih tertinggal
- [Taiwan Enterprise: HTC](/economy/台灣企業：宏達電) — Sejarah lengkap kematian "Quietly Brilliant"
- [Jensen Huang](/id/people/jensen-huang) — Lahir di Tainan, tumbuh di AS, orang yang paling ahli berbicara tentang chip setengah pengarah di dunia
- [NVIDIA di Taiwan](/id/technology/nvidia-in-taiwan) — Hubungan antara jaket kulit dan pasokan Taiwan
- [Computex: Tiga Pameran Komputer Internasional, Dua yang Diterima, yang Tersisa Berada di Taipei](/id/technology/computex) — Setiap Mei, para raksasa AI global bergiliran berbicara di Taipei dengan bahasa yang sama

## Sumber Gambar

Artikel ini menggunakan 5 gambar dengan lisensi CC, cache di `public/article-images/technology/`:

- [TSMC Fab 14B May 2025](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg) — Foto: 4300streetcar, CC BY 4.0, Wikimedia Commons
- [HTC One 03](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG) — Foto: Asmoth, CC BY-SA 4.0, Wikimedia Commons
- [HTC Dream opened](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg) — Foto: Marcus Sümnick, CC BY 3.0, Wikimedia Commons
- [Morris Chang at APEC 2021](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg) — Foto: Wang Yu Ching / Gedung Presiden, CC BY 2.0, Wikimedia Commons
- [Jensen Huang at Stanford CS 153](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg) — Foto: Anderseidesvik, CC BY-SA 4.0, Wikimedia Commons

## Referensi

[^1]: [The Free Library — HTC Market Cap Surpasses Nokia](https://www.thefreelibrary.com/HTC+Market+Cap+Surpasses+Nokia.-a0253461010) — Pada 7 April 2011, nilai pasar HTC sekitar $33,8 miliar, melebihi Nokia

[^2]: [Wikipedia — HTC](https://zh.wikipedia.org/wiki/%E5%AE%8F%E9%81%94%E5%9C%8B%E9%9A%9B%E9%9B%BB%E5%AD%90) — Pada 2011, pangsa pasar ponsel HTC sekitar 20%, nilai pasar melebihi triliun, harga saham pernah mencapai ribuan

[^3]: [Wikipedia — HTC Dream](https://en.wikipedia.org/wiki/HTC_Dream) — Ponsel Android pertama di dunia pada 2008

[^4]: [Wikipedia — Kurva Senyum](https://zh.wikipedia.org/wiki/%E5%BE%AE%E7%AC%91%E6%9B%B2%E7%B7%9A) — Shi Zhenrong mengusulkan konsep ini pada 1992 dalam buku "Membangun Acer"

[^4b]: [Wikipedia — MediaTek](https://zh.wikipedia.org/wiki/%E8%81%AF%E7%99%BC%E7%A7%91%E6%8A%80) — Salah satu pemasok chip seluler terbesar di dunia berdasarkan volume pengiriman; pangsa pasar TV chip sekitar 70%

[^5]: [Nvidia — Fourth Quarter and Fiscal 2026 Financial Results](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026) — Rilis resmi NVIDIA; FY2026 mencatatkan pendapatan $21,59 miliar dan laba bersih $12,01 miliar ( diverifikasi silang dengan laman keuangan Wikipedia: https://en.wikipedia.org/wiki/Nvidia）

[^6]: [TSMC — Quarterly Results Q4 2025](https://investor.tsmc.com/english/quarterly-results/2025/q4) — Halaman inveestor resmi TSMC; pada 2025, pendapatan total $12,242 miliar dan laba bersih $5,513 miliar ( diverifikasi silang dengan laman keuangan Wikipedia: https://en.wikipedia.org/wiki/TSMC）

[^7]: [Counterpoint — MediaTek Becomes Biggest Smartphone Chipset Vendor in Q3 2020](https://www.counterpointresearch.com/insights/mediatek-becomes-biggest-smartphone-chipset-vendor-q3-2020/) — Pada kuartal ketiga 2020, volume pengiriman chip seluler MediaTek berhasil melampaui Qualcomm, dengan pangsa pasar sekitar 31%

[^8]: [Wikipedia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — Platform SoC Snapdragon diluncurkan pada November 2006; penamaan merek berasal dari nama bunga (snapdragon flower), sedangkan Dimensity berasal dari bintang ketiga dari Bintang Kecil Urut (kedua penjelasan penamaan ini adalah data publik merek, menunggu sumber resmi dilengkapi)

[^9]: [MediaTek — Dimensity 9400 Press Release](https://corp.mediatek.com/news-events/press-releases/mediatek-launches-flagship-dimensity-9400-soc-for-advanced-capabilities) — Dimensity 9400 diluncurkan pada Oktober 2024; komunitas penguji umumnya memuji performanya dalam hal efisiensi (deskripsi induktif). Perangkat pertama yang dilengkapi dapat dilihat di [Wikipedia — Vivo X200](https://en.wikipedia.org/wiki/Vivo_X200)

[^10]: [Wikipedia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — Snapdragon Summit 2024 diselenggarakan di Hawai, meluncurkan Snapdragon 8 Elite (URL resmi sudah tidak valid, mengacu pada sumber sekunder Wikipedia)

[^11]: [Wikipedia — Foxconn](https://en.wikipedia.org/wiki/Foxconn) — ／ [Apple Inc.](https://en.wikipedia.org/wiki/Apple_Inc.) — Foxconn tahun fiskal 2025 mencatatkan pendapatan 8,103 triliun TWD dan laba bersih 1,893,5 miliar TWD (margin laba sekitar 2.3%); Apple FY2025 mencatatkan pendapatan $41,62 miliar dan laba bersih $11,2 miliar (margin laba sekitar 26.9%). Puncak persentase keuntungan iPhone pada masa-masa tertentu melebihi 80%: perkiraan Counterpoint (menunggu sumber dilengkapi)

[^12]: [Wikipedia — Puncak Pelindup Nasional](https://zh.wikipedia.org/wiki/%E8%AD%B7%E5%9C%8B%E7%A5%9E%E5%B1%B1) — Panggilan umum TSMC (juga dikenal sebagai "Pertiga"); "Setengah pengarah adalah puncak pelindup nasional Taiwan" adalah pernyataan publik Morris Chang pada 2021 (menunggu tautan sumber dilengkapi)

[^13]: [Wikipedia — Jensen Huang](https://zh.wikipedia.org/wiki/%E9%BB%83%E4%BB%81%E5%8B%B3) — Lahir pada 1963 di Tainan, imigrasi ke AS pada 1972 (usia 9 tahun)

[^13b]: Buku memoar kedua Morris Chang diluncurkan pada November 2024, menjadi bestseller (menunggu sumber dilengkapi)

[^14]: [Wikipedia — Su Shihfeng](https://zh.wikipedia.org/wiki/%E8%98%87%E5%A7%BF%E4%B8%B0) — Lahir pada 1969 di Tainan, pindah ke AS pada usia 3 tahun bersama keluarganya

[^15]: [Wikipedia — ASUS](https://zh.wikipedia.org/wiki/%E8%8F%AF%E7%A2%A9) — Pada 2006, ASUS mendirikan merek sekunder "Republic of Gamers" (ROG)

[^16]: [Wikipedia — Gogoro](https://en.wikipedia.org/wiki/Gogoro) — Didirikan pada 2011; pada 2015 di CES, Gogoro meluncurkan Gogoro Smartscooter dan jaringan energi; pada 2022, merger dengan Poema Global SPAC dan listing di NASDAQ; pada 2024, Castrol di bawah naungan BP mengumumkan investasi hingga $50 juta

[^17]: [NVIDIA GTC 2024 Keynote](https://www.youtube.com/watch?v=Y2F8yisiS6E) — "The more you buy, the more you save" adalah kutipan Jensen Huang dari video resmi acara ini

[^18]: "Quietly Brilliant" adalah slogan merek global HTC sejak 2009, "The Next Big Thing is Already Here" adalah slogan iklan Samsung Galaxy 2011, "We will make life multiplanetary" adalah pernyataan misi SpaceX (ketiganya adalah teks komersial publik)

[^19]: [NVIDIA at Computex 2024 — Video Presentasi Tema Resmi](https://www.youtube.com/watch?v=pKXDVsWZmUU) — Presentasi tema Jensen Huang pada 2 Juni 2024 di GOR NTU
