---
title: 'Industri Semikonduktor: Revolusi Material 50 Tahun dari Transfer Teknologi RCA hingga GaN dan Paket Kuantum'
description: 'Gunung suci pelindung Taiwan menguasai proses manufaktur canggih global melalui model foundry, tetapi medan perang material science 50 tahun berikutnya — GaN di pengisi daya cepat, CoWoS di bawah chip AI, dan dilusi freezer di atas qubit kuantum — baru saja dibuka.'
date: 2026-03-17
category: 'Technology'
tags:
  [
    'semikonduktor',
    'TSMC',
    'Taiwan Semiconductor Manufacturing Company',
    'gallium nitride',
    'paket 3D',
    'CoWoS',
    'komputer kuantum',
    'proses manufaktur canggih',
    'perisai silikon',
    'ilmu material',
  ]
subcategory: '半導體與硬體'
author: 'Taiwan.md'
featured: true
lastVerified: 2026-05-19
lastHumanReview: true
difficulty: 'intermediate'
readingTime: 22
image: '/article-images/technology/silicon-vs-gan-charger-2025.webp'
imageCredit: '4300streetcar'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg'
sporeLinks:
  [
    "{'id': 87, 'platform': 'threads', 'date': '2026-05-25', 'url': 'https://www.threads.com/@taiwandotmd/post/DYvqEURgXm-'}",
    "{'id': 88, 'platform': 'x', 'date': '2026-05-25', 'url': 'https://x.com/taiwandotmd/status/2058735515021783190'}",
  ]
translatedFrom: 'Technology/半導體產業.md'
sourceCommitSha: '6ffd92f94'
sourceContentHash: 'sha256:575572d1dd581d19'
sourceBodyHash: 'sha256:d37164a7592bd08a'
translatedAt: '2026-08-03T16:36:44.361859+00:00'
---

# Industri Semikonduktor: Revolusi Material 50 Tahun dari Transfer Teknologi RCA hingga GaN dan Paket Kuantum

![Dua kepala pengisi daya USB-C cepat 30W dengan daya sama yang disusun berdampingan, produk material silikon di sebelah kiri memiliki volume yang jelas lebih besar, produk gallium nitride di sebelah kanan menyusut hampir setengahnya, mencerminkan bagaimana ilmu material menekan kepadatan energi ke dalam telapak tangan](/article-images/technology/silicon-vs-gan-charger-2025.webp)
_Volume pengisi daya USB-C dengan daya sama antara Si dan GaN. Foto: 4300streetcar, 2025-12-25. [Lisensi melalui Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg)._

> **Ringkasan 30 detik:** Taiwan Semiconductor Manufacturing Company (TSMC) memulai produksi massal 2 nanometer (nm) di Fab 22 Kaohsiung pada kuartal keempat 2025, memimpin 2-3 generasi lebih maju dari seluruh dunia[^2]. Namun, ceritanya tidak hanya terjadi pada transistor yang semakin kecil: pengisi daya cepat di tasmu diisi dengan gallium nitride (GaN), GlobalWafers memproduksi wafer silikon karbida (SiC) 8 inci di Zhongli, dan GPU Blackwell NVIDIA sepenuhnya bergantung pada paket CoWoS TSMC untuk dikirim ke pusat data. Dari tahun 1973 di mana Institut Penelitian Industri (IRIS) mengeluarkan 4,5 juta dolar AS untuk membeli teknologi dari RCA[^5], hingga kuartal kedua 2026 di mana chip kuantum superkonduktor 20 qubit Institut Academia Sinica (IAS) terhubung ke internet[^6], Taiwan telah melewati sungai panjang ilmu material dari fisika celah pita (bandgap) hingga deposisi lapisan atom (ALD) hingga qubit topologis. Gunung suci pelindung mengandalkan pengalaman 50 tahun, tetapi posisi foundry di era kuantum belum bisa direbut oleh Taiwan.

Pada suatu sore tahun 1985, Komisien Politik Li Kuo-tung (李國鼎) menemui Morris Chang (張忠謀) yang baru kembali ke Taiwan untuk menjabat sebagai Presiden IRIS di Dewan Eksekutif Yuan. Li Kuo-tung langsung mengatakan: "Kami ingin membuat perusahaan manufaktur sirkuit terintegrasi skala besar, Anda yang memimpin."

Morris Chang terkejut sejenak. Ia pikir ia hanya datang untuk menjadi presiden, namun dua minggu kemudian ia ditarik untuk mendirikan perusahaan dengan model bisnis yang belum pernah dicoba siapa pun.

Percakapan ini mengubah dunia. Namun, 40 tahun kemudian, "dunia" jauh lebih tebal daripada yang dibayangkan pada sore itu. Ini termasuk pengisi daya cepat 65 watt seukuran dua ruas jari di samping ponselmu, termasuk setiap GPU Blackwell yang dimakan oleh NVIDIA di pusat data, termasuk qubit kuantum di laboratorium IAS yang perlu didinginkan hingga mendekati nol mutlak agar "bangun".

## Taruhan Foundry 1987

![Tampak luar pabrik Fab 5 TSMC di Taman Sains Hsinchu, bangunan industri berlapis-lapis terhubung dengan Jalan Fuguo, merupakan salah satu area pabrik representatif dari periode ekspansi TSMC di tahun 1990-an](/article-images/technology/tsmc-fab5-hsinchu-2010.webp)
_Pabrik Fab 5 TSMC di Taman Sains Hsinchu, 2010. Foto: Peellden. [Lisensi melalui Wikimedia Commons](https://commons.wikimedia.org/wiki/File:TSMC_Fab5.JPG)._

Ceritanya harus dimulai lebih awal. Pada tahun 1973, IRIS mengeluarkan 4,5 juta dolar AS untuk membeli teknologi sirkuit terintegrasi dari perusahaan Amerika RCA, dan mengirim 19 insinyur ke Amerika untuk pelatihan[^5]. Saat itu, tidak ada yang menyangka bahwa "biaya sekolah" ini akan menjadi batu fondasi pertama kerajaan semikonduktor Taiwan. Pada tahun 1980, teknologi transfer IRIS mendirikan United Microelectronics Corporation (UMC), Taiwan memiliki perusahaan semikonduktor pertama. Namun, Li Kuo-tung tidak puas: skala UMC terlalu kecil, teknologi tidak dapat mengejar standar internasional, Taiwan membutuhkan terobosan yang lebih besar.

Pada 21 Februari 1987, Morris Chang mendirikan Taiwan Semiconductor Manufacturing Company (TSMC) di Taman Sains Hsinchu, menciptakan model bisnis yang belum pernah ada sebelumnya: **foundry murni**.

Ide ini terdengar sangat gila pada saat itu. Seluruh perusahaan semikonduktor di dunia adalah terintegrasi vertikal, dari desain hingga manufaktur dalam satu garis, bagaimana mungkin hanya melakukan manufaktur, tidak melakukan desain? Apakah pelanggan akan menyerahkan gambar desain paling rahasia kepada Anda?

Logika Morris Chang sederhana: industri semikonduktor semakin kompleks, desain dan manufaktur adalah dua keahlian yang sangat berbeda. Daripada melakukan segalanya tetapi tidak ahli dalam apa pun, lebih baik fokus pada satu hal, membuat manufaktur chip menjadi yang terbaik di seluruh dunia.

Struktur saham awal TSMC sangat cerdik: pemerintah berinvestasi 48,3%, swasta 24,2%, Philips Belanda memegang 27,6% saham[^1]. Keterlibatan Philips adalah kunci. Saat itu industri semikonduktor didominasi oleh Amerika dan Jepang, Eropa membutuhkan pemasok alternatif. Philips tidak hanya berinvestasi, tetapi juga menyerahkan pesanan chip-nya ke TSMC, menjadi pelanggan pertama yang penting.

Model foundry memicu pembagian kerja besar dalam industri semikonduktor: perusahaan desain IC fokus pada desain chip (Qualcomm, NVIDIA, MediaTek), perusahaan foundry fokus pada manufaktur (TSMC, UMC, GlobalFoundries), pabrik paket dan pengujian bertanggung jawab untuk proses akhir (ASE Group, Silicon Power). Dulu hanya raksasa seperti Intel dan IBM yang dapat menanggung investasi astronomis pabrik wafer, sekarang startup dengan ide bagus dapat merancang chip, lalu menyerahkannya kepada TSMC untuk diproduksi.

Inti model foundry adalah kepercayaan. Pelanggan harus percaya bahwa TSMC tidak akan mencuri desain mereka, tidak akan membocorkan rahasia dagang, tidak akan bersaing dengan mereka. TSMC membangun "aturan kepercayaan" dengan empat prinsip: netralitas teknologi (tidak pernah merancang chip sendiri), kesetaraan pelanggan (semua pelanggan menikmati teknologi dan layanan yang sama), perjanjian kerahasiaan tingkat tertinggi, alokasi kapasitas produksi yang adil. Aturan ini telah dijalankan selama hampir 40 tahun, tanpa pengecualian.

> 📝 **Catatan Kurator**: Pada tahun 1987, 19 insinyur yang dikirim IRIS ke RCA baru berusia awal 40-an. Mereka belajar proses silikon Amerika tahun 1960-an, saat itu tidak ada yang menyangka bahwa 30 tahun kemudian mereka akan menjadi klien utama teknologi paket dunia. Klausul "pengebirian sukarela" di mana TSMC memutuskan untuk tidak merancang chip sendiri, ternyata menjadi ikatan yang membuat Jensen Huang, Tim Cook, dan Lisa Su tidak dapat lepas. Kehebatan model foundry bukan pada apa yang dilakukannya, tetapi pada apa yang **pilih untuk tidak dilakukan**. Jika ditarik lebih jauh ke hulu, penemuan transistor oleh Bell Labs pada tahun 1947, chip terintegrasi oleh Texas Instruments dan Fairchild pada tahun 1958, migrasi pemerintah Nasionalis ke Taiwan pada tahun 1949 membawa serta sekelompok birokrat teknis berlatar belakang sains dan teknik (tulang punggung IRIS masa depan) — transfer teknologi RCA 4,5 juta dolar ini adalah tongkat estafet, bukan titik awal.

## Ben J. Lin dan ASML: Taruhan Dua Anak Kecil dalam Paparan Air

Foundry bukan hanya urusan TSMC. Pembaca [@malathrone_21k_running](https://www.threads.com/@malathrone_21k_running) menambahkan garis sejarah kunci ini di kolom komentar: akar darah Philips TSMC juga berakar pada ASML — perusahaan mesin litografi yang dipisahkan dari Philips Belanda pada tahun 1984, hari ini adalah satu-satunya pemasok mesin EUV (extreme ultraviolet) di seluruh dunia. Kedua perusahaan ini 30 tahun yang lalu adalah "anak kecil" yang tidak diperhatikan oleh raksasa industri[^asml-philips].

Kunci cerita ini adalah insinyur Taiwan bernama Ben J. Lin (林本堅). Ia bekerja di Pusat Penelitian Watson IBM sejak 1992 mengenai teknologi litografi, dan kembali ke Taiwan pada tahun 2000 untuk bergabung dengan TSMC sebagai Kepala Departemen R&D[^lin-bio]. Pada era itu, perdebatan rute berikutnya untuk mesin litografi adalah 157 nm deep ultraviolet (DUV), Nikon dan Intel bertaruh pada jalur ini, tetapi 157nm terus bermasalah: lensa kalsium fluorida memiliki masalah birefringensi, film menyerap terlalu kuat pada panjang gelombang ini, integrasi proses sulit[^157nm-fail].

Pada tahun 2002, Ben J. Lin mengusulkan ide gila di Konferensi Optik SPIE: "Pertahankan sumber cahaya 193 nm, tetapi isi air di antara lensa dan wafer." Indeks bias air 1,44, cahaya 193 nm setara dengan resolusi sekitar 134 nm di dalam air — lebih halus dari 157nm, dan tidak perlu mengganti sumber cahaya, tidak perlu mengganti lensa[^immersion-litho].

Nikon tidak percaya, terus bertaruh pada 157nm. ASML bersedia bertaruh — ia juga "anak kecil", sama seperti TSMC yang mencari tuas fisika untuk membalikkan keadaan. Pada tahun 2003, ASML mulai mengembangkan mesin litografi 193nm immersion (193i), pada tahun 2007 pertama kali memproduksi massal, menopang **enam generasi** dari proses 65 nm hingga penerus EUV hari ini[^immersion-litho][^cw-lin-interview].

"Nikon takut panas sehingga tidak melakukan immersion, ASML dan kami hanya bisa melakukannya sendiri", jalur teknologi ini mendorong Nikon turun dari takhta mesin litografi[^cw-lin-interview]. 30 tahun yang lalu, dua anak kecil bertaruh masing-masing, hari ini satu adalah pabrik mesin EUV satu-satunya di dunia, yang lain adalah foundry 2 nm satu-satunya di dunia. Dua benih yang disebarkan Philips Belanda bertanding di abad ke-21.

## Garis Waktu Material 50 Tahun: Dari Silikon ke GaN ke Superkonduktor Topologis

Untuk memahami medan perang semikonduktor 2025, pertama-tama harus memahami garis fisika yang belum pernah dijelaskan dengan jelas.

Silikon (Si) adalah titik awal garis ini. "Celah pita" (bandgap) nya adalah 1,1 elektronvolt (eV), ini adalah tiket energi minimum yang harus dibayar agar elektron melompat dari pita konduksi ke pita valensi. Celah pita kecil, chip mudah dibuat, tetapi memiliki dua langit-langit: tegangan tinggi akan runtuh, frekuensi tinggi akan menghasilkan panas. PanSci menjelaskan batas ini dengan sangat jelas: "Semikonduktor berbasis silikon memiliki batas frekuensi kerja hanya di bawah 100 kHz, jika melebihi 100 kHz, efisiensi konversi akan turun drastis, ada masalah pembuangan energi yang serius."[^7]

Celah pita gallium nitride (GaN) adalah 3,4 eV, 3 kali silikon. Batas tegangan runtuh adalah 10 kali silikon. Frekuensi kerja dapat ditarik hingga 1000 kHz, satu orde magnitudo lebih tinggi dari silikon[^7]. Angka fisika ini diterjemahkan ke kehidupan sehari-hari: daya yang sama, transformator induktor GaN dapat jauh lebih kecil, persyaratan pendinginan juga lebih rendah, sehingga kepala pengisi daya cepat yang menekan kepadatan energi ke telapak tangan lahir.

Silikon karbida (SiC) mengambil jalur lain. Ini juga celah pita lebar (celah pita 3,26 eV), tetapi lebih tahan terhadap suhu dan tegangan tinggi. PanSci secara langsung menunjukkan medan perangnya: "Silikon karbida memiliki stabilitas yang baik di bawah suhu tinggi dan tegangan tinggi, terutama dengan meningkatnya kebutuhan pengisian daya cepat kendaraan listrik di masa depan, kebutuhan pengisian daya di atas 1000 volt akan membuat semikonduktor silikon yang hanya dapat menahan 600 volt tidak mampu menanggung, diharapkan akan mengambil alih komponen kunci dalam kendaraan listrik."[^7]

> 💡 **Tahukah Anda**: "Celah pita" semikonduktor menentukan seberapa tinggi tegangan yang dapat ditahannya, seberapa cepat frekuensi yang dapat dijalankan, dan berapa banyak panas yang dihasilkan. Silikon 1,1 eV adalah dasar elektronik konsumen selama 50 tahun; GaN 3,4 eV menopang pengisi daya cepat ponsel 240 watt; SiC 3,26 eV memasuki inverter kendaraan listrik 800 volt; langkah berikutnya mungkin adalah semikonduktor berlian (5,5 eV). Seluruh garis waktu material adalah tangga "menaikkan kepadatan energi", Taiwan harus menawar sekali dengan batas fisika ilmu material setiap kali naik satu anak tangga.

Langkah berikutnya belum dinamai: mungkin berlian (C, celah pita 5,5 eV), gallium oksida (Ga₂O₃, 4,8 eV), atau memasuki mekanisme fisika yang sama sekali berbeda, seperti superkonduktor topologis (topological superconductor), ini adalah jalur yang diambil oleh prosesor kuantum Majorana 1 yang diumumkan Microsoft pada Februari 2025[^15]. Fisika berubah, seluruh rantai industri akan ditulis ulang.

## GaN di Pengisi Daya Cepat Anda

Kembalikan lensa ke tas Anda.

Pengisi daya Nokia 3310 berdaya 4,56 watt, pengisi daya cepat 2025 berdaya 240 watt. Bedanya 52 kali. PanSci menguraikan garis waktu ini: "Pengisi daya cepat GaN yang paling populer saat ini memiliki daya hingga 65 watt, berbeda 13 kali, secara ideal waktu pengisian juga akan dipersingkat menjadi satu per tiga belas."[^7] Lebih dahsyat lagi, merek Tiongkok realme meluncurkan GT Neo5 pengisi daya超 cepat 240 watt pada awal 2023, mendorong angka ini ke atas 50.

Kurva pertumbuhan ini secara fisika bergantung pada beralih ke GaN, ketebalan kawat tembaga dan volume baterai justru menyusut. Untuk meningkatkan daya dan memperkecil volume, metode paling langsung adalah meningkatkan frekuensi kerja, tetapi "semikonduktor berbasis silikon memiliki batas frekuensi kerja hanya di bawah 100 kHz"[^7], inilah yang dikatakan PanSci sebagai "batas silikon". GaN menarik frekuensi kerja ke atas 1 MHz, transformator dan induktor menyusut secara bersamaan, seluruh kepala pengisi daya dapat dimasukkan ke dalam saku.

Masalahnya: ketika pasar pengisi daya cepat Taiwan baru meledak, TSMC mengumumkan satu hal, **menarik diri dari foundry GaN pada Juli 2027**[^8].

Di balik keputusan ini ada dua tekanan. Pertama, pabrik GaN Tiongkok (China Resources Microelectronics, Silan Microelectronics, Ruineng, dll.) memperluas produksi secara massal, menekan harga foundry ke level yang tidak ingin diambil oleh TSMC. Kedua, profit chip AI terlalu menggoda, TSMC ingin mengubah pabrik GaN menjadi lini produksi paket canggih (CoWoS). Teknologi dilisensikan ke World Semiconductor (VIS) dan GlobalFoundries, beban foundry GaN Taiwan diserahkan kepada厂商 yang telah bertaruh sejak sepuluh tahun lalu seperti稳懋 (3163) dan 宏捷科 (8086)[^8].

> ⚠️ **Pandangan Kontroversial**: TSMC menarik diri dari foundry GaN, ada dua interpretasi di luar. Satu pihak menganggap ini adalah pilihan rasional "menyisihkan kapasitas untuk AI", profit per wafer 3 nm lebih dari 20 kali lipat dari GaN 6 inci, alokasi kapasitas tentu berorientasi pada tingkat pengembalian yang tinggi. Pihak lain mempertanyakan: Taiwan melepaskan GaN berarti menyerahkan basis generasi berikutnya elektronik konsumen (ponsel / laptop / pengisi daya) kepada pabrik Tiongkok, apakah "perisai" perisai silikon hanya tersisa di ujung AI? Perbedaan kedua pihak adalah: apakah Anda menganggap nilai Gunung Suci Pelindung adalah "proses manufaktur canggih yang tidak dapat digantikan", atau "klaster rantai pasok yang lengkap".

Baik TSMC, raksasa wafer GlobalWafers, maupun berbagai raksasa semikonduktor domestik dan asing, sudah naik ke kereta ini[^7]. Tetapi naik gerbong mana adalah dua hal yang berbeda.

## Wafer 8 Inci SiC GlobalWafers

Jika GaN adalah cerita pengisi daya cepat ponsel, SiC adalah cerita kendaraan listrik.

Pabrik inti garis SiC Taiwan adalah GlobalWafers (环球晶), bukan TSMC. Pada tahun 2024, kapasitas produksi bulanan wafer SiC 6 inci GlobalWafers ditarik hingga sekitar 20.000 keping, furnace kristalisasi mandiri diperluas dari 3 menjadi 20, yield melampaui 50%[^9]. Pada tahun 2025, wafer SiC 8 inci diproduksi massal, ini adalah yang pertama di Taiwan.

CEO GlobalWafers, Hsu Hsiu-lan (徐秀兰), selalu berbicara langsung: "Zhongmei Crystal membentuk 'Grup IDM Virtual', menargetkan kebutuhan SiC 5 tahun ke depan! Kami mengejar dengan cepat."[^9] Strategi adalah mengikat kristalisasi (GlobalWafers), epitaksi (Pengcheng), modul (Hongyang Semiconductor) di bawah induk Zhongmei Crystal menjadi satu rantai.

Namun, SiC bukan cerita garis lurus. Pada paruh kedua 2025, pabrik SiC Tiongkok (San'an Optoelectronics, Tianke Heda, dll.) memperluas produksi secara gila, kelebihan pasokan global, utilisasi kapasitas wafer SiC 6 inci dan 8 inci GlobalWafers一度 di bawah 50%[^10]. Ini menambahkan lembah pada naskah prediksi optimis PanSci tahun 2023 "kebutuhan kendaraan listrik mengambil alih".

Sinyal pemulihan datang dari NVIDIA. Ada rumor bahwa platform GPU Rubin generasi berikutnya NVIDIA akan menggunakan SiC pada lapisan interposer, dipasangkan dengan arsitektur pusat data tegangan tinggi DC 800 volt, produksi massal menyeluruh pada tahun 2027[^10]. Jika rumor ini benar, kapasitas wafer SiC 8 inci GlobalWafers akan beralih dari kendaraan listrik ke pusat data AI, seluruh cerita menyala kembali.

> 📝 **Catatan Kurator**: GaN dan SiC sering disebut bersama sebagai "Semikonduktor Kelas Ketiga", tetapi klasifikasi ini memiliki makna industri di Taiwan yang lebih dari sekadar label "material generasi berikutnya" — ini mewakili bidang pertama di mana Taiwan memiliki rantai pasok lengkap **tanpa melewati TSMC**. Kristalisasi GlobalWafers, manufaktur Hanle, packaging 稳懋, desain 宏捷科: di luar Gunung Suci Pelindung, ada "gunung kelas ketiga" yang lebih rendah profil tetapi independen yang sedang tumbuh.

## Ikatan Jensen Huang dengan CoWoS+

Kembali ke medan perang AI.

GPU H100 NVIDIA menggunakan proses 4 nm TSMC, ditambah paket CoWoS-S mengintegrasikan memori bandwidth tinggi HBM3. Blackwell B200 upgrade ke CoWoS-L, mengintegrasikan dua GPU Blackwell ditambah satu CPU Grace, kecepatan pelatihan AI 4 kali lebih cepat dari H100[^11]. Rubin generasi berikutnya diperkirakan rilis tahun 2026.

Inti setiap generasi GPU adalah "proses manufaktur canggih + paket canggih" dual engine. Proses membuat transistor semakin kecil, paket menumpuk die yang berbeda semakin dekat. PanSci menggunakan perbandingan Jalan Taiji dan Terowongan Xueshan untuk menjelaskan hal ini: "Paket tradisional harus melewati Jalan Taiji yang berkelok-kelok, paket canggih memotong tikungan untuk mengambil jalan lurus, menembus Terowongan Xueshan yang menghubungkan dua tempat, membuat lalu lintas data lebih nyaman dan cepat."[^12]

Inti CoWoS (Chip-on-Wafer-on-Substrate) adalah "through-silicon via" (TSV): menumpuk die yang berbeda, menembus substrat silikon dengan saluran vertikal mikro, membuat dua sirkuit yang terpisah menjadi terhubung secara 3D. PanSci menggambarkan dengan jelas: "Tumpukan 3D dapat menempatkan chip C di atas chip A, menembus substrat silikon yang telah di-thin-out melalui teknologi TSV, menghubungkan dua sirkuit dengan kabel konduksi vertikal kepadatan tinggi, jarak keduanya berubah dari ujung dunia menjadi dekat."[^12]

Angka kapasitas lebih menusuk. Kapasitas bulanan CoWoS TSMC akhir 2024 sekitar 35.000 keping, target akhir 2025 mencapai 75.000 keping, 2028 akan maju ke 150.000 keping, CAGR hampir 80%[^13]. NVIDIA langsung memesan kapasitas CoWoS TSMC hingga 2027, dan **semua chip, terlepas dari pabrik TSMC mana yang memproduksinya (termasuk Arizona), harus dikirim kembali ke Taiwan untuk paket CoWoS**[^13].

Inilah duopoli Jensen Huang dan TSMC. NVIDIA di ujung desain, TSMC di ujung manufaktur dan paket, kedua perusahaan bersama-sama mengunci simpul kunci pusat data AI.

Pada 2 Juni 2024, dalam pidato tema Computex di Gymnasium Universitas Nasional Taiwan, Jensen Huang secara terbuka menjelaskan ikatan ini kepada seluruh dunia — slide yang ditampilkan adalah roadmap Blackwell dan Rubin, tetapi di balik setiap slide adalah lini produksi CoWoS TSMC.

<div class="video-embed" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;">
   <iframe src="https://www.youtube.com/embed/pKXDVsWZmUU" title="NVIDIA CEO Jensen Huang Keynote at COMPUTEX 2024" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

_Saluran resmi NVIDIA: Pidato tema Computex "The Era of AI" oleh Jensen Huang pada 2 Juni 2024 di Gymnasium Universitas Nasional Taiwan. Selama dua jam penuh, ia membongkar GPU Blackwell, NVLink, Spectrum-X satu per satu — tetapi现场 fisik setiap slide ada di Hsinchu Baoshan. "Tanpa TSMC, tidak ada NVIDIA" tidak diucapkannya, tetapi setiap gambar kapasitas mengatakan itu._

Biaya fisik paket 3D juga tidak kecil. PanSci menunjukkan kesulitan: "Paket canggih menuntut planarity die dan kecocokan chip yang sangat tinggi, jika tumpukan tidak hati-hati dan koneksi tidak berhasil, akan menyebabkan kehilangan yield. Selain itu, sirkuit terintegrasi menghasilkan disipasi energi saat komputasi menyebabkan kenaikan suhu, paket canggih mendekatkan jarak antara die, konduksi termal saling mempengaruhi, saling menghangatkan, membuat pendinginan lebih sulit."[^12]

Tahap berikutnya adalah SoIC (System on Integrated Chips) dan SoW-X (System on Wafer). SoIC adalah "3D sejati", wafer terhadap wafer ditumpuk langsung, tanpa bumping (bumping-free). SoW-X diperkirakan produksi massal tahun 2027, ukuran retikula adalah 9,5 kali CoWoS saat ini, mengintegrasikan lebih dari 16 chip komputasi besar, kemampuan komputasi 40 kali lebih tinggi dari CoWoS saat ini[^13]. Chip AI semakin panjang dan besar, lini paket TSMC semakin seperti pabrik-pabrik mini.

## ALD: Atom Tumbuh Lapis demi Lapis

![Lemari pajangan museum menampilkan beberapa sampel wafer silikon dengan ukuran berbeda berdampingan, yang terbesar berdiameter sekitar 12 inci, kilau seperti cermin menunjukkan bahan inti manufaktur semikonduktor](/article-images/technology/silicon-wafers-museum-2017.webp)
_Pameran sampel wafer silikon, 2017. Foto: ArticCynda. [Lisensi melalui Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Silicon_wafers.jpg)._

4 nm, 2 nm, 1,6 nm. Di balik angka-angka ini ada teknologi manufaktur yang rendah profil tetapi kritis: Atomic Layer Deposition (ALD).

ALD ditemukan oleh orang Finlandia, tetapi menjadi langkah inti yang tidak dapat dilewati oleh setiap wafer proses manufaktur canggih Taiwan.

Ceritanya harus dimulai dari Finlandia. Pada tahun 1974, ahli material Tuomo Suntola (图奥莫．松托拉) mulai mengembangkan ALD di perusahaan Instrumentarium Oy Finlandia. Pada tahun 1977 teknologi terbentuk, dan pertama kali muncul dalam pameran industri[^14]. Saat itu teknologi ini hanya untuk membuat display elektroluminescent, Suntola sendiri tidak menyangka 30 tahun kemudian ini akan menjadi urat nadi proses nanometer. Pada tahun 1999, ia menjual teknologi ALD ke perusahaan peralatan semikonduktor Belanda ASM. Hari ini ASM memiliki lebih dari 55% pangsa pasar di pasar ALD[^14].

PanSci menjelaskan prinsip ALD dengan bersih: "Deposisi lapisan atom adalah teknologi deposisi uap kimia yang ditingkatkan, membagi proses deposisi menjadi dua langkah. Pertama, injeksi prekursornya pertama, bereaksi dengan permukaan substrat... Ketika permukaan jenuh, injeksi prekursornya kedua, bereaksi dengan prekursor yang telah menempel, membentuk material target, menyelesaikan proses film."[^14] Dua prekursor injeksi bergantian, setiap putaran hanya tumbuh film setebal satu lapisan atom.

Mengapa ini penting? Karena ketebalan gate transistor proses 2 nm hanya tersisa beberapa atom, dan lapisan isolasi gate harus mencapai planarity tingkat atom, kontrol ketebalan tingkat atom. Deposisi uap kimia tradisional (CVD) tidak bisa, deposisi fisik (PVD) tidak bisa, hanya ALD yang dapat "tumbuh lapis demi lapis". Setiap pabrik proses manufaktur canggih TSMC memasang mesin ALD ASM, rantai yang terdiri dari peralatan Belanda, teknologi Finlandia, dan proses Taiwan adalah dasar fisik di mana 2 nm dapat diproduksi massal.

> 💡 **Tahukah Anda**: Ukuran fitur minimum proses 2 nm sekitar lebar 20 atom silikon berbaris. Jika atom silikon diperbesar menjadi bola biliar, transistor 2 nm sekitar panjang meja pingpong. Pekerjaan ALD adalah "menutupi bola biliar satu per satu" di meja ini dengan material isolasi.

ASM tidak terdaftar di Taiwan, tetapi hampir semua pelanggan terbesar mesin ALD 12 inci-nya ada di Taiwan. **Rantai pasok ini tersembunyi tetapi tidak dapat digantikan**, jika produksi massal 2 nm TSMC tidak lancar, tidak ada pabrik ALD kedua di dunia yang dapat mengisi posisi.

## Setelah 2nm adalah Kuantum

Setelah tingkat Angstrom (angstrom, 1 nm = 10 Angstrom), cerita TSMC belum selesai.

Kuartal keempat 2025, TSMC memulai produksi massal 2 nm di Fab 22 Kaohsiung, Fab 20 Hsinchu Baoshan mengikuti[^2]. 2 nm pertama kali menggunakan arsitektur transistor nanosheet GAA (Gate-All-Around), meninggalkan transistor FinFET yang digunakan dari 22 nm hingga 3 nm[^16]. 2 nm setara dengan lebar 20 atom silikon, sudah mendekati batas teori fisika. Pelanggan pertama termasuk chip seri A Apple dan chip AI NVIDIA, kapasitas produksi proses 2 nm akan diperluas setiap kuartal[^3].

Langkah berikutnya adalah 1,6 nm (A16), diperkirakan produksi massal kuartal keempat 2026, pertama kali memperkenalkan "Jaringan Pengiriman Daya Sisi Belakang" (Backside Power Delivery Network), dinamai sendiri oleh TSMC sebagai Super Power Rail[^16]. Daya yang sama 10% lebih cepat dari N2P, efisiensi daya 15-20% lebih hemat pada kinerja yang sama.

Tapi setelah 1,6 nm? Node proses semakin mahal. Biaya R&D proses 28 nm sekitar 1 miliar dolar AS, 7 nm melonjak ke 3 miliar, 3 nm meledak ke 10 miliar, 2 nm diperkirakan lebih dari 20 miliar[^4]. Kurva eksponensial Hukum Moore mengubah biaya R&D tahap akhir menjadi angka astronomis, inilah yang dikatakan PanSci sebagai "kompleksitas pengembangan proses manufaktur canggih dan dana investasi meningkat secara eksponensial, dan investasi dan pengembalian sering tidak sebanding"[^12].

Jadi industri semikonduktor mengubah strategi: ekspansi horizontal menjadi tumpukan vertikal (paket 3D), silikon menjadi material baru (GaN/SiC), akhirnya mungkin beralih ke fisika komputasi yang sama sekali berbeda, seperti komputasi kuantum.

Garis waktu IAS berjalan seperti ini. Oktober 2023, komputer kuantum superkonduktor 5 qubit selesai dikembangkan. 29 Januari 2024, Presiden Tsai Ing-wen (蔡英文) melakukan inspeksi, komputer kuantum resmi terhubung ke internet[^6]. PanSci menulis: "Januari 2024, komputer kuantum pertama yang dikembangkan secara mandiri di Taiwan lahir di Institut Academia Sinica, meskipun hanya memiliki 5 qubit, ini membuka babak di mana Taiwan menempati posisi di arena kompetitif komputer kuantum global."[^17]

Desember 2025, chip kuantum superkonduktor 20 qubit selesai. Januari 2026 diumumkan terhubung untuk digunakan[^6]. Waktu koherensi (coherence time T1) melompat dari 15-30 mikrodetik era 5 qubit menjadi 530 mikrodetik 20 qubit. Waktu koherensi adalah durasi qubit mempertahankan keadaan superposisi, semakin panjang berarti "lebih sedikit noise, dapat melakukan komputasi yang lebih kompleks".

Tim nasional kuantum lintas kementerian resmi dibentuk pada Maret 2022, anggaran 5 tahun 8 miliar NTD, 17 tim penelitian[^18]. Departemen Ekonomi kemudian mendirikan "Kantor Pendorong Teknologi Industri Kuantum" pada April 2026, menjembatani R&D akademik dengan industri.

Apa yang dilakukan IRIS sangat menarik: menggunakan proses 28 nm TSMC untuk membuat "chip kontrol qubit". Berita Pusat Tiongkok Maret 2024 mengutip pernyataan IRIS: "Memanfaatkan desain IC microwave yang dikuasai Taiwan dan proses 28 nm TSMC, membuat chip kontrol dan modul suhu rendah (4K, yaitu -269°C)... Memperkecil instrumen kontrol, memasukkannya ke dalam lemari pendingin suhu rendah, mengurangi volume keseluruhan peralatan 40%, menyederhanakan kabel, memiliki keunggulan komersialisasi... Konsumsi daya modul ini berkurang lebih dari 50% dibandingkan data yang diterbitkan oleh raksasa internasional."[^19]

> 📝 **Catatan Kurator**: Strategi kuantum Taiwan bukan membuat qubit sendiri (itu wilayah IBM, Google, IAS), tetapi mengecilkan sirkuit kontrol hingga dapat dimasukkan ke dalam dilution freezer. Dari 5 qubit ke 20 qubit, chip kontrol IRIS dari mendukung 1 qubit, 2 qubit, 8 qubit, diperkirakan mencapai 20 qubit pada 2026-2027. **Langkah berikutnya Gunung Suci Pelindung ingin menjadi foundry era kuantum, bukan berebut hegemoni kuantum secara langsung**. Namun posisi foundry ini, saat ini belum ada yang memaku "serahkan pada Taiwan".

## Tiga Jalur Kuantum: Superkonduktor, Jebakan Ion, Topologis

Komputer kuantum bukan hanya satu jalan.

**Qubit superkonduktor** (superconducting qubits) adalah jalur yang diambil oleh IBM, Google, IAS. Keuntungannya adalah proses kompatibel dengan fab semikonduktor saat ini (inilah posisi Taiwan yang memiliki harapan), kecepatan kontrol cepat. Kerugiannya adalah membutuhkan dilution freezer mendekati nol mutlak (15 mK, sekitar -273°C), noise tinggi. Google pada 2019 menggunakan "Wutong" (Sycamore) 53 qubit mengumumkan mencapai hegemoni kuantum, menyelesaikan tugas yang membutuhkan 10.000 tahun komputer super tradisional dalam 200 detik[^20].

**Qubit jebakan ion** (trapped ion qubits) mengambil jalur laser yang mengontrol atom tunggal. PanSci menguraikan perbedaan jalur ini: "Teknik jebakan ion menggunakan laser untuk mengontrol atom tunggal untuk melakukan komputasi, teknik ini memiliki presisi dan stabilitas yang sangat tinggi, tetapi juga menghadapi masalah kompleksitas teknologi dan biaya."[^17] Pabrik representatif adalah IonQ dan Quantinuum. Keuntungannya presisi tinggi, stabilitas baik, tidak perlu suhu sangat rendah. Kerugiannya kecepatan kontrol lambat, sulit diperluas ke banyak qubit.

**Qubit topologis** (topological qubits) adalah taruhan generasi berikutnya Microsoft. Februari 2025, Microsoft merilis prosesor kuantum topologis Majorana 1, mengklaim dapat diperluas hingga satu juta qubit[^15]. Secara teori qubit topologis sangat tahan gangguan, tetapi jalur ini paling tidak matang, keberadaan partikel Majorana sendiri masih dalam tahap verifikasi di fisika.

Ketiga jalur ini memiliki risiko masing-masing. Strategi Taiwan adalah "**memastikan bahwa terlepas dari jalur mana yang menang, Taiwan memiliki simpul rantai pasok**", dan tidak bertaruh pada satu jalur yang menang. Jalur superkonduktor mengandalkan chip kontrol 28 nm TSMC. Jalur jebakan ion membutuhkan optik presisi yang kompatibel dengan industri optoelektronik Taiwan; jika jalur topologis berhasil, masih membutuhkan film kemurnian ekstrem, kembali ke wilayah ALD.

## Fab Luar Negeri: Ekspansi atau Ekspor

Globalisasi TSMC mulai berakselerasi dari 2020-an.

**Fab 21 Arizona Amerika Serikat**: Fase 1 proses 4 nm produksi massal paruh pertama 2025; Fase 2 proses 3 nm/2 nm produksi massal paruh kedua 2027; Fase 3 proses 2 nm/A16 diperkirakan sebelum 2030. Total pengeluaran modal sekitar 165 miliar dolar AS[^21]. Namun ada "tetapi" penting: paket CoWoS semua chip AI masih hanya di Taiwan, wafer yang diproduksi di pabrik Arizona akan dikirim kembali ke Taiwan untuk paket[^13].

**Fab 1 Kumamoto Jepang**: Proses 22-28 nm, produksi massal 2024, berkolaborasi dengan Sony dan Toyota. Rencana Fab 2 (12-16 nm) ketidakpastian kemajuan, sebagian sumber daya dialihkan ke Arizona.

**ESMC Dresden Jerman** (TSMC memegang 40% saham): Chip mobil 28/22/16/12 nm, perpindahan peralatan paruh kedua 2025, produksi massal 2027, kapasitas bulanan sekitar 40.000 keping[^22].

Pabrik luar negeri ini memiliki "Prinsip N-2" yang sama — **selalu tertinggal dua generasi dari Taiwan本土**. Ketika Taiwan本土 melakukan 2 nm, yang paling canggih di luar negeri adalah 4 nm; ketika Taiwan mendorong 1,6 nm, luar negeri baru mencapai 3 nm. Garis merah ini ditulis dalam etika teknik geopolitik, bukan dalam klausul kontrak.

> ⚠️ **Pandangan Kontroversial**: Fab luar negeri adalah perluasan atau pengenceran Perisai Silikon? Pendukung mengatakan: teknologi tetap di Taiwan, kapasitas luar, mengubah Perisai Silikon dari "satu pulau" menjadi "satu rantai", de-risking lebih menyeluruh. Penentang mengatakan: setiap pabrik luar negeri yang dikirim, mengirimkan sekumpulan insinyur terlatih, satu SOP produksi massal, satu hubungan pelanggan. 30 tahun kemudian ketika Arizona atau Kumamoto menumpuk ke batas N-2, "dua generasi paling canggih" itu mungkin akan dikompresi secara perlahan. Prinsip N-2 saat ini adalah janji TSMC, bukan hukum fisika.

Sejalan dengan fab luar negeri adalah "ekspor talenta desain". Desain chip AI tidak hanya membutuhkan Taiwan, Silicon Valley, Tel Aviv, New Delhi memiliki pusat desain sendiri. Ekosistem foundry TSMC sedang berubah dari "insinyur seluruh pulau" menjadi campuran "insinyur global + manufaktur seluruh pulau".

## Biaya Lingkungan: Sisi Lain Gunung Suci Pelindung

Gunung Suci Pelindung memiliki berat.

Sumber daya air adalah yang paling intuitif. Tiga taman sains TSMC mengonsumsi lebih dari 208.000 ton air per hari, kelompok lingkungan memperkirakan setelah 2025 pabrik baru beroperasi, konsumsi air mungkin meningkat 4 kali lipat menjadi 770.000 ton/hari[^23]. Tanggapan TSMC: rata-rata setiap tetes air digunakan 3,5 kali, tingkat daur ulang mencapai 87%, target pabrik baru 90%;新增 penghematan air 5,54 juta meter kubik tahun 2024.

Listrik adalah soal kedua. Satu fab 3 nm mengonsumsi sekitar 2,1 miliar kWh per tahun, setara dengan penggunaan listrik 20.000 rumah di seluruh Taiwan selama satu tahun. Konsumsi listrik 2 nm dan 1,6 nm akan terus naik. TSMC berjanji mencapai RE100 (100% energi terbarukan) tahun 2050, tetapi pasokan listrik hijau Taiwan tidak mengikuti kecepatan ekspansi semikonduktor, timeline ini terus diuji tekanan.

Jam kerja adalah soal ketiga. Jam kerja, harga rumah, tingkat kelahiran insinyur Taman Sains Hsinchu adalah topik artikel lain. Tetapi sama seperti ilmu material adalah masalah fisika: waktu dan energi manusia juga memiliki "celah pita", melewati ambang batas akan runtuh.

Eksistensi Gunung Suci Pelindung, selain bergantung pada teknologi TSMC, kebijakan pemerintah, peluang geopolitik, juga termasuk biaya yang ditanggung bersama oleh 170.000 insinyur taman sains, seluruh pabrik rantai pasok, dan setiap penduduk Taiwan yang menggunakan air dan listrik.

## Ekosistem Lengkap: Taiwan Bukan Hanya TSMC

Kompetisi industri semikonduktor Taiwan berasal dari seluruh klaster, bukan TSMC sendirian. Ujung desain IC ada MediaTek (top 3 global), Novatek, Realtek, Himax; selain TSMC, ada UMC, World Semiconductor, UMC; paket dan pengujian oleh ASE Group (top dunia), Silicon Power, Kyung Yuan Electric menangani tahap akhir. Semikonduktor Kelas Ketiga didukung oleh GlobalWafers (kristalisasi SiC), Hanle, 稳懋 (GaN), 宏捷科; memori oleh Nan Ya Technology, Winbond; peralatan dan material oleh Jade Mountain Precision, Sin-E, Chongyue厂商 tersembunyi mengisi posisi.

Satu chip dari desain hingga selesai, mungkin berputar di Taiwan dan selesai, tidak perlu transportasi lintas negara. "Keunggulan rantai pendek" ini terlihat oleh seluruh dunia selama COVID, sejak itu ditulis dalam buku putih rantai pasok setiap raksasa teknologi.

Taman Sains Hsinchu didirikan tahun 1980, 40+ tahun menumpuk hingga lebih dari 500 perusahaan, 170.000 personel. Insinyur mungkin di TSMC selama 5 tahun, melompat ke MediaTek untuk merancang chip, kemudian beralih ke ASE untuk menangani paket — siklus talenta lintas perusahaan ini membuat tingkat teknologi seluruh industri menyebar secara efektif.

Siapa pesaingnya? Strategi terintegrasi vertikal Samsung Korea Selatan berinvestasi 230 miliar dolar AS 2022-2026, tetapi yield proses manufaktur canggih masih tertinggal TSMC[^4]. Intel macet di 10 nm selama bertahun-tahun,提出 IDM 2.0 tahun 2021 ingin兼营 desain dan foundry, tetapi hingga 2025 bisnis foundry belum mendapatkan klien utama — yang paling ironis adalah beberapa chip tingkat tinggi Intel sendiri, justru di-foundry-kan oleh TSMC.

## Posisi Era Kuantum Masih Kosong

Daya pengisi daya Nokia 3310 sebesar 4,56 watt, sedangkan pengisi cepat tahun 2025 mencapai 240 watt. Selisihnya 52 kali lipat. Jalur ini ditempuh silikon selama 30 tahun, sedangkan nitida galium (GaN) mengejar ketinggalan dalam 5 tahun.

Di laboratorium kuantum Akademi Sinica, chip kuantum superkonduktor memerlukan suhu 15 millikelvin (sekitar −273 °C) untuk beroperasi. ITRI menggunakan proses 28 nanometer TSMC untuk menghasilkan chip kontrol, yang memampatkan «volume instrumen kontrol» yang dibutuhkan di suhu ekstrem rendah tersebut dari seukuran gedung menjadi ukuran kotak kecil. Kemampuan semikonduktor Taiwan, sedang sedikit demi sedikit menggeser batas komputer kuantum.

Namun tidak ada yang bisa menjelaskan dengan jelas batas itu di mana. Waktu koherensi bit kuantum berkisar dari 15 mikrodetik hingga 530 mikrodetik — ini baru permulaan. 19 insinyur yang dikirim RCA 50 tahun lalu mungkin juga tidak mengetahui bahwa tahun 1973 mereka akan mengkristalisasi menjadi 2 nanometer tahun 2025.

Gunung Penyelamat Negara (TSMC) berkuasa saat ini berkat pengalaman 50 tahun industri. Untuk 50 tahun ke depan, posisi foundry era kuantum, belum diraih oleh Taiwan.

> ✦ Blackwell buatan Jensen Huang berinferensi di awan di atas kepalamu, wafer SiC GlobalWafers memanaskan stasiun pengisian kendaraan listrik di depan rumahmu, film tipis ALD pertama buatan Suntola 1974 di Finlandia mengunci lapisan isolasi gerbang di chip ponselmu — semikonduktor sejak dulu memang seluruh spektrum material memanjat tahap demi tahap mengikuti fisika band gap selama 50 tahun, bukan milik TSMC semata. Di mana tahap selanjutnya, fisika yang akan memberitahu, tapi apakah mau dipanjat, itu pilihan Taiwan.

---

**Baca Lanjutan**:

- [Perusahaan Taiwan: TSMC](/id/economy/tsmc) — Tata kelola perusahaan, struktur keuangan, skala belanja modal Gunung Penyelamat Negara
- [Perusahaan Taiwan: MediaTek](/id/economy/mediatek) — Bagaimana raja desain IC menempati posisi di chip ponsel dan komputasi tepi AI
- [Perusahaan Taiwan: ASE Semiconductor](/economy/台灣企業：日月光半導體) — Industri _assembly_ dan _testing_ nomor satu global, ekosistem proses pasca-CoWoS
- [Pembangun Gunung: Taruhan Abad](/id/art/mountain-makers-tsmc-documentary) — Film dokumenter 2025 karya Hsiao Ju-chen, lima tahun wawancara 80+ veteran semikonduktor, 2026 masuk ke tiga lokasi investasi CHIPS Act utama: Purdue, Wisconsin, Michigan
- [Wu Ta-you](/people/吳大猷) — Pada era 1980-an Taiwan berjuang bangun semikonduktor, ia sebagai ketua Akademi Sinica menegaskan pentingnya sains fundamental, meletakkan fondasi sistem penelitian Taiwan
- [Huang Chung-jen](/people/黃崇仁) — Pendiri Powerchip/Powerchip Technology, jalan DRAM Taiwan yang membangun pabrik sendiri di atas lisensi proses orang lain: pangsa pasar turun dari 23,2% ke 6,3%, kisah paling jarang dibicarakan industri ini
- [Industri Robot Taiwan](/id/technology/taiwan-robotics-industry) — Pulau nomor satu semikonduktor dunia, kenapa jadi murid belajar di era robot? Melihat keterbukaan NCAIR dan celah industri
- [Bursa Saham dan Pasar Modal Taiwan](/economy/台灣股市與資本市場) — Bagaimana seluruh ekosistem rantai pasokan yang menopang identitas bursa Taiwan 2026 sebagai global ke-6 terwujud di pasar modal
- [Rantai Pasokan Tungsten Taiwan](/id/technology/taiwan-tungsten-supply-chain) — Hexafluorida tungsten mengisi jendela kontak dan _word line_ 3D NAND, Taiwan tak punya tambang tungsten tapi berkat daur ulang dan pemurnian menempati posisi hulu rantai pasokan ini
- [Sekolah Kecerdasan Buatan Taiwan](/id/technology/taiwan-ai-academy) — Sepuluh ribu insinyur AI latih AIA delapan tahun, bagaimana kembali ke rantai ICT semikonduktor既有, memperkuat sisi perangkat lunak Taiwan
- [Computex: Tiga Pameran Komputer Internasional Tutup Dua, Sisanya Berada di Taipei](/id/technology/computex) — CoWoS dan proses mutakhir TSMC, setiap akhir Mei berjabat tangan dengan raksasa AI global di pameran Taipei berusia 45 tahun ini
- [Taman Sains Taiwan](/id/technology/science-park-development) — Tiga taman: Hsinchu, Tainan, Taichung, badan fisik kluster semikonduktor, juga pusat geografis _Silicon Shield_

## Sumber Gambar

Artikel ini menggunakan 3 gambar berlisensi CC/PD, cache di `public/article-images/technology/` untuk menghindari server sumber link panas:

- [Silicon vs GaN 30W USB-C chargers](https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg) — Foto: 4300streetcar, 2025-12-25, CC BY 4.0, Wikimedia Commons file Silicon_vs_GaN_30W_USB-C_chargers.jpg
- [TSMC Fab 5 Hsinchu](https://commons.wikimedia.org/wiki/File:TSMC_Fab5.JPG) — Foto: Peellden, 2010-09-05, CC BY-SA 3.0, Wikimedia Commons file TSMC_Fab5.JPG
- [Silicon wafers museum display](https://commons.wikimedia.org/wiki/File:Silicon_wafers.jpg) — Foto: ArticCynda, 2017-10-23, CC0 public domain, Wikimedia Commons file Silicon_wafers.jpg

## Referensi

[^1]: [Semiwiki — How Philips Saved TSMC](https://semiwiki.com/semiconductor-history/307560-how-philips-saved-tsmc/) — Saham Philips menurut Semiwiki seharusnya 27,6%; pemegang saham kunci teknologi dan klien awal TSMC

[^2]: [Focus Taiwan 2025/12/30 — TSMC 2nm production](https://focustaiwan.tw/business/202512300012) — Produksi massal 2 nm TSMC dimulai dengan Fab 22 Kaohsiung sebagai prioritas, Fab 20 Hsinchu Baoshan mengikuti

[^3]: [数位时代 — TSMC 2nm officially mass production](https://www.bnext.com.tw/article/89663/tsmc-2nm-volume-production) — TSMC mulai produksi massal 2 nm Q4 2025; angka kapasitas bulanan spesifik adalah estimasi industri eksternal, resmi tidak公布

[^4]: [科技新報 — TSMC 3nm utilization reaches 100%](https://technews.tw/2025/05/26/tsmcs-2nm-process-is-expected-to-reach-full-capacity-in-four-seasons/) — Yield proses manufaktur canggih TSMC estimasi industri lebih baik dari pesaing; angka yield spesifik adalah estimasi pihak ketiga, bukan pengungkapan resmi

[^5]: [天下雜誌 — Li Kuo-tung and birth of TSMC](https://www.cw.com.tw/article/5095492) — Morris Chang mendirikan TSMC 1987, menetapkan model "foundry murni", meletakkan fondasi pembagian kerja industri semikonduktor global; latar belakang transfer teknologi RCA 4,5 juta dolar 1973

[^6]: [中央研究院 — 20 qubit superconducting quantum chip announcement](https://www.sinica.edu.tw/News_Content/56/2375) — IAS menyelesaikan chip kuantum superkonduktor 20 qubit Desember 2025, terhubung Januari 2026; waktu koherensi T1 mencapai 530 mikrodetik

[^7]: [泛科學（PanSci） — Gallium Nitride: Use 1/3 time, get same power](https://pansci.asia/archives/362660) — Penulis: Redaksi PanSci. Celah pita GaN 3,4 eV, tegangan runtuh 10 kali, frekuensi kerja 1 MHz vs silikon 100 kHz; aplikasi pengisian daya cepat kendaraan listrik 1000 volt SiC. Mitra Kurasi Konten per MOU 2026-05-05

[^8]: [TrendForce — TSMC exits GaN foundry by July 2027](https://www.trendforce.com/news/2025/08/22/news-tsmc-reportedly-exits-gan-foundry-business-by-2027/) — TSMC menarik diri dari foundry GaN Juli 2027, lisensi teknologi ke World Semiconductor (VIS) dan GlobalFoundries; 稳懋 (3163) pengiriman bulanan sekitar 500 keping GaN 6 inci

[^9]: [富果直送 — GlobalWafers SiC 8-inch wafer 2025 mass production](https://www.fugle.tw/news/article/1234567) — Kapasitas bulanan wafer SiC 6 inci GlobalWafers akhir 2024 mencapai 20.000 keping, furnace kristalisasi mandiri 3 → 20 unit, yield > 50%; strategi "Grup IDM Virtual" Hsu Hsiu-lan

[^10]: [科技新報 — SiC supply chain under pressure](https://technews.tw/2025/11/sic-market-oversupply) — Ekspansi pabrik SiC Tiongkok 2025 menyebabkan utilisasi kapasitas wafer SiC 6/8 inci GlobalWafers di bawah 50%; GPU Rubin NVIDIA rumor menggunakan lapisan interposer SiC + pusat data DC tegangan tinggi 800V produksi massal 2027

[^11]: [SemiAnalysis — NVIDIA Blackwell CoWoS-L Analysis](https://www.semianalysis.com/p/nvidia-blackwell-b200-cowos-l) — NVIDIA Blackwell B200 menggunakan CoWoS-L mengintegrasikan 2 GPU Blackwell + 1 CPU Grace; kecepatan pelatihan AI 4 kali lebih cepat dari H100; NVIDIA memesan kapasitas CoWoS TSMC hingga 2027

[^12]: [泛科學（PanSci） — 3D Stacking: How Advanced Packaging Makes Chips Enter Xueshan Tunnel](https://pansci.asia/archives/367588) — Penulis: Redaksi PanSci. Prinsip CoWoS/SoIC/TSV; metafora Jalan Taiji vs Terowongan Xueshan; tantangan yield dan pendinginan paket 3D. Mitra Kurasi Konten per MOU 2026-05-05

[^13]: [Digitimes — TSMC CoWoS capacity expansion plan](https://www.digitimes.com.tw/iot/article.asp?cat=158&id=0000696823_X1D7L8XB6JNL2Y8XLPZJK) — Kapasitas bulanan CoWoS TSMC akhir 2024 35.000 keping, akhir 2025 75.000 keping, target 2028 150.000 keping; NVIDIA memesan kapasitas hingga 2027; wafer Arizona dikirim kembali ke Taiwan untuk paket

[^14]: [泛科學（PanSci） — ALD Atomic Layer Deposition: 50 Years of Film Revolution](https://pansci.asia/archives/377669) — Penulis: Redaksi PanSci. ALD 1974 Suntola di Instrumentarium Oy dikembangkan, teknologi terbentuk 1977, dijual ke ASM 1999; 55% pangsa pasar ASM; prinsip dua prekursor deposisi uap kimia. Mitra Kurasi Konten per MOU 2026-05-05

[^15]: [科技新報 — Microsoft Majorana 1 Topological Quantum Processor Released](https://technews.tw/2025/02/20/microsoft-majorana-1-topological-qubit/) — Microsoft Februari 2025 merilis prosesor kuantum topologis Majorana 1 pertama di dunia, mengklaim dapat diperluas hingga satu juta qubit

[^16]: [TSMC官网 — A16 (1.6nm) Process Announcement](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm) — 2 nm pertama kali menggunakan transistor nanosheet GAA (tinggalkan FinFET); A16 pertama kali memperkenalkan jaringan pengiriman daya sisi belakang (Super Power Rail), produksi massal Q4 2026, 10% lebih cepat dari N2P pada daya yang sama, hemat daya 15-20% pada kinerja yang sama

[^17]: [泛科學（PanSci） — Taiwan Quantum Tech: From 5 Qubits to Mass Production Era](https://pansci.asia/archives/377923) — Penulis: Redaksi PanSci. IAS Januari 2024 komputer kuantum 5 qubit lahir; tiga jalur superkonduktor vs jebakan ion vs topologis; Google Wutong 53 qubit 200 detik menyelesaikan masalah 10.000 tahun. Mitra Kurasi Konten per MOU 2026-05-05

[^18]: [iThome — Quantum National Team 5 Years 8 Billion Budget](https://www.ithome.com.tw/news/151234) — Tim nasional kuantum lintas kementerian resmi dibentuk Maret 2022, 5 tahun 8 miliar NTD, 17 tim penelitian; April 2026 Departemen Ekonomi mendirikan Kantor Pendorong Teknologi Industri Kuantum

[^19]: [中央社 2024/03/06 — IRIS Quantum Control Chip](https://www.cna.com.tw/news/ait/202403060123.aspx) — IRIS menggunakan proses 28 nm TSMC membuat chip kontrol kuantum suhu rendah 4K (-269°C), volume berkurang 40%, konsumsi daya berkurang lebih dari 50% dibandingkan raksasa internasional; jalur pengembangan 2024 1 qubit → 2026-2027 20 qubit

[^20]: [TechNews — Google Sycamore Quantum Supremacy](https://technews.tw/2019/10/24/google-sycamore-quantum-supremacy/) — 2019 Google 53 qubit Wutong komputer kuantum mencapai hegemoni kuantum, 200 detik menyelesaikan tugas komputasi 10.000 tahun komputer super tradisional

[^21]: [SemiAnalysis — TSMC Arizona Fab 21 Investment Plan](https://www.semianalysis.com/p/tsmc-arizona-1650b-capex) — Investasi tiga fase Fab 21 Arizona TSMC 165 miliar dolar AS; Fase 1 (4nm) produksi massal 2025, Fase 2 (3nm/2nm) 2027, Fase 3 (2nm/A16) sebelum 2030; Prinsip N-2 luar negeri selalu tertinggal dua generasi dari Taiwan

[^22]: [Digitimes — ESMC Dresden 2027 Mass Production](https://www.digitimes.com.tw/news/esmc-dresden-2027) — Saham ESMC TSMC 40%; pabrik chip mobil 28/22/16/12 nm Dresden Jerman perpindahan peralatan paruh kedua 2025, produksi massal 2027, kapasitas bulanan sekitar 40.000 keping

[^23]: [天下雜誌 — TSMC Water Resource Consumption](https://www.cw.com.tw/article/5128456) — Tiga taman sains TSMC mengonsumsi lebih dari 208.000 ton air per hari; kelompok lingkungan memperkirakan setelah 2025 pabrik baru beroperasi air meningkat menjadi 770.000 ton/hari; tanggapan TSMC setiap tetes air digunakan 3,5 kali, tingkat daur ulang 87% (pabrik baru 90%),新增 penghematan air 5,54 juta meter kubik 2024

[^asml-philips]: [Wikipedia — ASML Holding](https://en.wikipedia.org/wiki/ASML_Holding) — ASML didirikan 1 April 1984 dari joint venture 50/50 Philips Belanda (Philips) dan ASM International (ASMI) ASM Lithography; setelah saham listing 1995 ASMI keluar, hari ini ASML adalah satu-satunya pemasok mesin litografi EUV di dunia

[^lin-bio]: [Wikipedia — Burn-Jeng Lin](https://en.wikipedia.org/wiki/Burn-Jeng_Lin) — Ben J. Lin lahir 1942 di Vietnam, mulai bekerja di Pusat Penelitian Watson IBM mengenai teknologi litografi 1970-an, kembali ke Taiwan bergabung dengan TSMC sebagai Kepala Departemen R&D 2000; dianugerahi SPIE Frits Zernike Award 2008; disebut "Bapak Litografi Immersion"

[^157nm-fail]: [Electronics Weekly — Immersion litho sidelines 157nm](https://www.electronicsweekly.com/news/research-news/process-rd/immersion-litho-sidelines-157nm-2005-05/) — Jalur 157nm ditinggalkan karena lensa kalsium fluorida (CaF₂) birefringensi, film menyerap terlalu kuat pada 157nm, kesulitan integrasi proses, digantikan oleh 193nm immersion setelah 2002-2003; taruhan Intel + Nikon gagal

[^immersion-litho]: [Wikipedia — Immersion lithography](https://en.wikipedia.org/wiki/Immersion_lithography) — Ben J. Lin 2002 SPIE mengusulkan litografi immersion 193nm; indeks bias air 1,44使 193nm setara resolusi sekitar 134nm; ASML produksi massal 2007, dari 65nm menopang hingga 7nm, memperpanjang Hukum Moore enam generasi

[^cw-lin-interview]: [天下雜誌 CommonWealth — Interview with the Father of Immersion Lithography Who Put TSMC on the Map](https://english.cw.com.tw/article/article.action?id=3720) — Wawancara Ben J. Lin 2024-06-18 — Latar belakang sejarah "Nikon takut melakukan immersion"; Ben J. Lin kembali ke TSMC 2000 mendorong adopsi litografi immersion, garis darah kolaborasi teknologi 30 tahun TSMC dan ASML
