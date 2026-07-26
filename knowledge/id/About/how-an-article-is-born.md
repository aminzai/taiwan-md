---
title: 'Bagaimana Sebuah Artikel Lahir: Jalur Produksi Enah Tahap Taiwan.md yang Menangkal Insting Penulisan AI (REWRITE-PIPELINE v7.5 × EDITORIAL v6.12)'
description: 'Setiap artikel Taiwan.md yang Anda baca, yang bernuansa, berlatar, dan dapat diverifikasi, di belakangnya ada 6 tahap, lebih dari 20 gerbang yang tidak boleh dilewati, dan sebuah redaksi AI yang tidak menulis naskah secara mandiri. Alasan tunggal keberadaan mesin ini adalah kesalahan-kesalahan yang paling sering dibuat oleh penulisan AI: mengurutkan fakta berdasarkan waktu begitu ditemukan, menghasilkan kalimat plastik tanpa informasi, menerjemahkan balik ringkasan bahasa Inggris menjadi kutipan palsu, dan terinfeksi kebiasaan buruk artikel lama yang dibaca. Artikel ini membongkar jalur produksi tersebut, dan artikel ini sendiri juga dihasilkan oleh jalur produksi tersebut.'
date: 2026-06-19
tags:
  [
    'about',
    'meta',
    'metodologi penulisan',
    'kurasi',
    'rewrite-pipeline',
    'editorial',
    'semiont',
    'penulisan AI',
  ]
author: 'Taiwan.md'
category: 'About'
readingTime: 11
featured: false
lastVerified: 2026-06-19
lastHumanReview: false
relatedDiary: ['2026-06-19-123349-manual']
translatedFrom: 'About/文章如何誕生.md'
sourceCommitSha: '984fb7892'
sourceContentHash: 'sha256:92fcb394123e4aee'
sourceBodyHash: 'sha256:b8984a2133e5738f'
translatedAt: '2026-07-26T08:13:11+08:00'
---

# Bagaimana Sebuah Artikel Lahir: Jalur Produksi Enah Tahap Taiwan.md yang Menangkal Insting Penulisan AI (REWRITE-PIPELINE v7.5 × EDITORIAL v6.12)

> **Ringkasan 30 Detik:** Setiap artikel Taiwan.md yang Anda baca, di belakangnya ada jalur produksi enam tahap: pertama memikirkan sudut pandang, lalu mencari, menulis bagian penutup terlebih dahulu, memverifikasi kata per kata, menambahkan visual, dan menghubungkan secara dua arah. Jalur produksi ini bukan sekadar "alur penulisan artikel yang baik" pada umumnya; setiap gerbangnya menargetkan satu jenis kesalahan yang paling sering dilakukan oleh penulisan AI: mengurutkan fakta berdasarkan waktu begitu ditemukan, menghasilkan kalimat plastik tanpa informasi, menerjemahkan balik ringkasan bahasa Inggris menjadi kutipan palsu, dan terinfeksi kebiasaan buruk artikel lama yang dibaca. Artikel ini membongkar jalur produksi tersebut, dan artikel ini sendiri juga dihasilkan oleh jalur produksi tersebut.

Pada pukul 19.53 malam tanggal 18 Juni 2026, sebuah _commit_ masuk ke cabang _main_ dengan tenang. Sebuah artikel tentang trio musik Taiwan "Elephant Gym" diluncurkan: 5.604 karakter Tionghoa, 56 catatan kaki, 11 subjudul bertema adegan[^1]. Pada titik waktu itu, tidak ada orang di depan komputer. Adalah roda gila rutin Taiwan.md yang, pada malam tanpa jaga, menyelesaikannya sendiri dan mengirimnya sendiri.

Namun, sebelum _commit_ itu, artikel ini telah menjalankan hampir serangkaian pencarian, membaca 59 sumber, dan dibantah oleh 12 titik verifikasi sehingga menulisannya yang semula harus diubah. Ia menyelesaikan 6 tahap, melewati lebih dari 20 gerbang yang tidak boleh dilewati, dan memanfaatkan sebuah redaksi AI dengan pembagian kerja yang jelas. Apa yang Anda baca adalah 5.604 karakter di atas permukaan air. Artikel ini ingin membuat Anda melihat mesin di bawah permukaan air.

```tw-figure
Hampir 100 kali pencarian → 1 artikel
Pengambilan materi untuk artikel "Elephant Gym": sekitar 95 kueri, 59 sumber, 12 titik pemalsuan
Catatan rutin Taiwan.md, 2026-06-18
```

## Mengapa Membangun Mesin untuk Sebuah Artikel

Jika Anda memberikan sebuah AI sebuah topik dan memintanya menulis sebuah artikel, ia kemungkinan besar akan melakukan hal berikut: mencari, mengurutkan fakta yang ditemukan berdasarkan urutan waktu, menambahkan satu kalimat kesimpulan yang terdengar bermakna di setiap paragraf, dan menulis di bagian penutup "akan terus berkembang di masa depan". Artikel seperti ini sudah ada di Wikipedia, dan ladang konten AI memproduksi puluhan ribu artikel seperti itu setiap hari. Taiwan.md memutuskan sejak hari pertama untuk tidak melakukan ini.

Masalahnya, kebiasaan buruk ini adalah nilai default AI, bukan kesalahan sesekali. REWRITE-PIPELINE memecahnya menjadi enam jenis kegagalan yang berulang: token habis di akhir, paragraf kedua menjadi draf. Tidak ada titik pemeriksaan di tengah, kualitas menurun secara diam-diam. Menulis bagian penutup di akhir, tenaga tidak cukup menjadi kaleng. Spesifikasi teks kaya terlupakan di akhir; sudut pandang yang berbeda dianggap sebagai alur kerja yang terpisah-pisah; dan yang paling mematikan, mencari fakta baru kemudian memikirkan sudut pandang, hasilnya adalah kronologi dengan kepadatan yang tidak seimbang[^2].

Jadi logika desain jalur produksi ini sederhana: setiap kesalahan yang mungkin terjadi, dipasangkan dengan satu gerbang untuk menahannya. Ini bukan alur kerja "menulis dengan baik" yang umum, ini adalah kebalikan dari _slop_ AI.

> **✦** "Wikipedia menjawab 'apa itu PTT'. Taiwan.md menjawab 'mengapa PTT layak Anda baca selama 8 menit'."

Ini adalah hasil dari Elephant Gym yang keluar dari ujung lain jalur produksi:

```tw-stat
5.604 karakter | Teks utama Tionghoa | "Elephant Gym"
56 buah | Catatan kaki, setiap satu harus bisa Ctrl-F | Verifikasi primer
11 paragraf | Subjudul bertema adegan, tidak diurutkan berdasarkan waktu | Irama naratif
12 titik | Membantah tulisan asli pada tahap penelitian | Prioritas pemalsuan
Sumber: Catatan rutin Taiwan.md, 2026-06-18
```

## Enah Gerbang, Setiap Gerbang Mencegah Satu Kegagalan

Jalur produksi ini memiliki enam tahap dari awal hingga akhir, setiap artikel harus melaluinya, tidak peduli topiknya apa, tidak peduli panjang pendeknya.

**Stage 0 Sudut Pandang** pertama-tama memikirkan jelas apa jenis memori bagi orang Taiwan, di mana kemungkinan ketegangan intinya. **Stage 1 Pengambilan Materi** baru mulai mencari, seluruh artikel setidaknya 80 kali kueri, dan kuota ditulis mati: sumber Tionghoa setidaknya 40, Inggris setidaknya 20, primer setidaknya 15, oposisi setidaknya 5, memaksa diri untuk mencari bukti yang berlawanan dengan hipotesis[^3]. **Stage 2 Menulis** tindakan pertama adalah menulis bagian penutup, karena tenaga orang akan habis di akhir, meninggalkan bagian penutup yang paling penting untuk akhir, sama saja menyerahkannya kepada diri sendiri yang paling lelah. **Stage 3 Verifikasi** memeriksa kata per kata: aritmatika, satuan, setiap kutipan harus bisa dicari di sumber asli dengan Ctrl-F. **Stage 4 Bentuk** menambahkan visualisasi dan media. **Stage 5 Koneksi** menghubungkan artikel ini secara dua arah ke artikel lain di basis pengetahuan.

Distribusi tenaga enam tahap ini disengaja. Menulis memakan lebih dari empat puluh persen, tetapi pencarian ditambah verifikasi bersama-sama juga hampir setengah. Tempat yang benar-benar memakan waktu untuk sebuah artikel, bukan saat mengetik, tetapi sebelum dan sesudah mengetik.

```tw-bars
Di mana tenaga sebuah artikel dihabiskan (batas atas anggaran token setiap tahap, %)
Stage 0 Sudut Pandang | 12 | Refleksi sebelum redaksi
Stage 1 Pengambilan Materi | 28 | Pencarian ≥ 80 kali
Stage 2 Menulis | 42 | Menulis penutup dulu
Stage 3 Verifikasi | 18 | Verifikasi kata per kata
Stage 4 Bentuk | 8 | Visual dan media
Stage 5 Koneksi | 5 | Koneksi dua arah
Sumber: Anggaran setiap tahap REWRITE-PIPELINE v7.5
```

## Pikirkan Jelas, Baru Lalu Cari

Di antara enam tahap, yang paling kontra-intuitif adalah yang pertama.

Sebagian besar penulisan AI adalah "mencari untuk menemukan fakta, kemudian kembali melengkapi sudut pandang". Taiwan.md membalik urutan di v6.0: sebelum mulai mencari, pertama-tama dari sudut pandang editor utama, pikirkan jelas enam pertanyaan, apa memori topik ini bagi orang Taiwan, ada wajah mana yang diabaikan, bagaimana terhubung dengan sejarah kehidupan kita. Setelah jelas, baru pergi mencari untuk memverifikasi dengan pertanyaan.

Mengapa urutan ini begitu penting, ada sebuah artikel yang bisa menjadi pelajaran. Dulu menulis tentang Apple Fanta, jalur produksi pertama mencari, yang ditemukan adalah krisis di mana ia pernah macet, hampir menghilang, seluruh artikel ditulis sebagai cerita yang hampir punah. Pengamat mengembalikan, mengatakan bahwa Apple Fanta bagi orang Taiwan adalah memori kolektif yang melintasi 60 tahun, dari era botol kaca permen karet hingga sekarang[^4]. Menganggapnya sebagai berita krisis adalah memperkecil skala memori. Versi yang mencari pertama, mengubah memori yang hangat menjadi kecemasan.

```tw-versus
Insting AI: Cari dulu saja | Taiwan.md: Pikirkan dulu, baru cari
Menemukan banyak fakta, kembali memaksakan satu sudut pandang | Menentukan sudut pandang dulu, pergi mencari untuk memverifikasi dengan pertanyaan
Fakta dipadatkan ke dalam artikel, kepadatan tidak seimbang | Fakta yang tidak masuk ke sudut pandang dipotong
Tidak ada anchor yang melintas, bagian penutup menjadi kaleng | Sudut pandang yang tidak menemukan anchor yang sesuai dikembalikan untuk dipikirkan ulang
Menjadi kronik perusahaan, CV tokoh | Menjadi cerita yang membuat orang "oh, begitu"
Sumber: REWRITE-PIPELINE v7.5 Stage 0 Sudut Pandang
```

## Cari: Menulis Laporan Penelitian Seperti Makalah

Sudut pandang ditentukan, baru mulai mencari. Pencarian Taiwan.md memiliki dua angka keras: satu artikel mendalam sepanjang proses setidaknya 80 kali kueri, dan kuota sumber ditulis mati, Tionghoa setidaknya 40, Inggris setidaknya 20, primer setidaknya 15, oposisi setidaknya 5. Ember terakhir itu paling mudah diabaikan, memaksa penulis untuk mencari bukti yang bertentangan dengan hipotesis sendiri, bukan hanya memilih yang bisa mendukung.

Setelah mencari, bukan berarti memasukkan ringkasan ke dalam artikel sudah selesai. Di balik setiap artikel mendalam, ada laporan penelitian yang menargetkan makalah pascasarjana, dibagi menjadi delapan bab: sudut pandang, log pencarian, temuan per sub-topik, bank kutipan, contoh lawan dan pagar, paket fakta bersih untuk penulis, referensi plus daftar periksa, dan bab terakhir adalah laporan asli tanpa terlewatkan oleh setiap agen penelitian. Salah satu aturan terdengar sangat ketat, mencari tetapi tidak menulis jejak asli kembali ke laporan, dianggap seperti tidak pernah mencari. Laporan adalah sumber kebenaran artikel ini, ia harus lulus inspeksi oleh satu alat, sumber yang tidak berulang setidaknya 25, sumber Inggris tidak boleh nol, sumber primer tidak boleh nol[^9]. Jika tidak lulus, artikel ini bahkan tidak memiliki kualifikasi untuk mulai menulis.

```tw-stat
≥ 80 kali | Kedalaman pencarian artikel mendalam | Tionghoa 40 / Inggris 20 / Primer 15 / Oposisi 5
8 bagian | Struktur laporan penelitian | Menargetkan makalah pascasarjana
≥ 25 buah | Sumber tidak berulang (lulus inspeksi alat) | Inggris ≠ 0, Primer ≠ 0
Sumber: REWRITE-PIPELINE v7.5 Step 1.1 / 1.7
```

Untuk topik kontroversial, ada satu gerbang tambahan. Menulis tentang politik, pandangan sejarah, kebijakan seperti ini, akan mengirim agen "oposisi" khusus, yang khusus mencari sumber yang berlawanan dengan posisi artikel ini, dan bisa menjelaskan alasan, setiap satu harus menyertakan URL yang bisa diakses, jika tidak cukup ditulis dengan jujur "diskursus oposisi lemah", tidak memaksakan. Artikel yang hanya memiliki satu suara, di sini tidak dihitung selesai.

Untuk kutipan, ada garis merah. Tanda kutip adalah janji: yang di dalam kurung adalah kata-kata asli, jadi setiap kutipan harus bisa dicari di sumber asli dengan Ctrl-F. Perangkap yang paling umum adalah alat mengambil situs web Tionghoa, tetapi mengembalikan ringkasan bahasa Inggris, penulis menerjemahkan balik ringkasan bahasa Inggris itu ke Tionghoa sebagai "kutipan langsung", itu adalah pemalsuan. Tahun 2026 menulis artikel spora Li Yang, terjebak: ringkasan bahasa Inggris yang dikembalikan adalah "I was the earliest to arrive at school, yet I fell short of keeping pace with my classmate Qi-lin", diterjemahkan balik ke Tionghoa menjadi "Saya tiba di sekolah paling awal, tetapi tidak bisa mengikuti pace teman sekelas Qi-lin". Namun kata asli Tionghoa Li Yang sebenarnya adalah "15 orang kelas olahraga, saya termasuk yang di belakang, Qi-lin termasuk yang di depan"[^10]. Makna mirip, nada sangat berbeda, inilah mengapa kutipan terjemahan balik tidak dihitung sama sekali.

## Menulis: Setiap Artikel Harus Memiliki Satu Orang

Material lengkap, masuk ke gerbang yang paling memakan tenaga. EDITORIAL adalah dokumen Taiwan.md yang mengajar dirinya sendiri bagaimana menulis material menjadi artikel yang bernuansa, ia membuka dengan tiga aturan besi: ada cerita, bukan hanya informasi; setiap fakta harus dapat diverifikasi; setiap artikel memiliki satu orang[^11].

Yang ketiga paling mudah diabaikan, namun paling krusial. Lembaga tidak membuat orang mengingat, konsep juga tidak, manusia yang membuat. Jadi artikel tentang TSMC, lebih baik mulai dari satu orang spesifik daripada mulai dari perusahaan; artikel tentang asuransi kesehatan universal, mulai dari satu kartu, satu ruang konsultasi, satu orang. Mengembalikan tema abstrak menjadi satu orang yang bisa diikuti pembaca, artikel baru memiliki suhu tubuh, dan hanya kemudian bisa menampung janji di atas, membuat pembaca ingin menceritakan setelah membaca.

## Lima Hal yang Harus Ditemukan Sebelum Mulai Menulis

EDITORIAL menyebut persiapan sebelum memasuki keadaan menulis sebagai "mata melihat material": menerima satu material, pertama-tama harus menemukan lima hal, jika tidak ditemukan jangan mulai menulis[^5].

**Kontradiksi**, satu kalimat yang menjelaskan ketegangan inti, seseorang melakukan X tetapi bertentangan dengan Y yang diyakininya. **Objek**, satu benda konkret yang mata pembaca bisa lihat, tangan bisa sentuh, misalnya roti rose lychee Wu Bao-chun, bola emas 660 ton yang menggantung di lantai 87. **Kutipan**, satu kata-kata asli yang diucapkan orang, karena menambahkan tanda kutip berarti berjanji "ini adalah kata asli", jadi harus bisa dicari di sumber dengan Ctrl-F. **Adegan**, satu momen dengan waktu, tempat, tindakan, mengembalikan "kebijakan disahkan" menjadi "hari审查 komite kesehatan dan lingkungan parlemen 8 Januari 2025". **Detail**, warna pakaian, cuaca hari itu, nada bicara, spesifikasi ini tidak ada di tabel, tetapi adalah bukti "benar-benar ada orang di tempat".

Di antara lima hal ini, kontradiksi di urutan pertama.

```tw-quote
Jika tidak menemukan kontradiksi, artikel ini tidak seharusnya ditulis ulang
REWRITE-PIPELINE v7.5 | Stage 1.4 Menemukan Kontradiksi Mengunci
```

Ketegangan bisa berupa konflik, kegagalan, krisis, tetapi sudut pandangnya adalah "bagaimana hal ini tumbuh menjadi hari ini, ke mana akan pergi", bukan "di sini apa yang rusak, siapa yang harus dimarahi". Kontradiksi yang sama, pandangan konstruktif membuat pembaca ingin berpartisipasi, pandangan kiamat membuat pembaca ingin lari.

## Menulis Penutup Dulu, Pembuka Hanya Menyimpan Satu Tangan

Urutan menulis, kebalikan dari urutan membaca.

Tindakan pertama Stage 2 adalah menulis penutup. Terdengar aneh, alasan sangat nyata: tenaga orang akan habis di akhir, meninggalkan penutup yang paling penting untuk akhir, sama saja menyerahkannya kepada diri sendiri yang paling lelah, hasil yang dihasilkan kebanyakan adalah "akan terus bersinar" kaleng. Menulis penutup dulu, menutup titik runtuh ini. Penutup yang baik memiliki dua tugas, mengumpulkan kembali gambar yang ditanam di pembuka, kemudian memberi pembaca posisi yang lebih dalam satu tingkat dari pembuka, dan posisi yang ingin melakukan sesuatu.

Taiwan.md menerima enam jenis penutup yang baik: sisa gaya yang meninggalkan gambar untuk dipikirkan sendiri, gaya terbalik yang membalikkan di atas di kalimat terakhir, gaya lompatan waktu yang mendorong kamera ke masa depan atau menarik kembali ke masa lalu, gaya pertanyaan yang meninggalkan pertanyaan nyata, gaya wilayah abu-abu yang tidak menyelesaikan kontradiksi membiarkannya di sana, dan gaya loop naratif yang kembali ke pembuka menyelesaikan loop. Artikel Black-faced Spoonbill adalah contoh loop: pembuka adalah "1865, Swinhoe di Tamsui mengambil spesimen, catatan menulis dua kata: langka", penutup adalah "Swinhoe 160 tahun lalu di Tamsui menulis 'langka', hari ini kita di Taman Hutan Da'an setiap hari mendengar suara rendah 'wu, wu, wu' nya"[^12]. Dua kata yang sama, karena akumulasi seluruh artikel di tengah, makna bagi pembaca saat melihat kembali sudah berbeda.

Pembuka sebaliknya, harus menyimpan satu tangan. Tiga kalimat pertama menentukan apakah pembaca tetap atau tidak, tetapi tugasnya adalah mengundang orang masuk ke adegan, bukan menyelesaikan peristiwa. "Hari badak Ta CHI datang, guru Sekolah Dasar Qingshan Changhua Hsu Pi-lan di sekolah", kalimat ini berhenti di "di sekolah" saja, pembaca akan ingin tahu apa yang terjadi selanjutnya. Menulis sebagai lead berita lengkap, menjelaskan waktu, tempat, peristiwa, tindakan, hasil, pembaca mendapatkan informasi, tetapi kehilangan tarikan untuk membaca lebih lanjut.

## Judul Adalah Janji yang Harus Diklik

Judul adalah kesan pertama pembaca, Taiwan.md memiliki format keras untuknya: semua artikel mengikuti "topik: subjudul hook" sandwich titik dua. Menulis hanya satu kata benda adalah stub ensiklopedia, bertentangan dengan精神 kurasi.

```tw-versus
Stub ensiklopedia (buruk) | Sandwich titik dua (baik)
Jay Chou | Jay Chou: Dari Ruang Latihan di Belakang 4 in Love ke 25 Tahun "The Secret"
Tai Tzu-ying | Tai Tzu-ying: Gadis Zuo Ying Kaohsiung ke Juara Dunia Ketiga, Perlawanan Tenang di Luar Lapangan
Cuti Badai | Cuti Badai: Cuti siapa, shift siapa
Sumber: EDITORIAL v6.12 §Judul Sandwich Titik Dua
```

Kalimat subjudul harus bisa tweet sendiri, dan harus spesifik sehingga pembaca bisa menangkapnya dalam satu pandangan. AI sangat baik memampatkan kontradiksi inti menjadi satu kalimat abstrak yang indah, hasil setiap kata kunci adalah kata benda abstrak, pembaca hanya bisa bertanya "apa dari apa". Kriteria sangat sederhana: memberikan judul kepada orang yang belum membaca artikel, dia bisa menunjuk setiap kata kunci dan mengatakan "ini merujuk pada apa yang konkret". "Asuransi Kesehatan Universal: Satu Kartu Menopang Dunia Pertama, Masa Depan yang Tidak Bisa Menopang" menggunakan satu kartu, "Limbah Nuklir Lanyu: Dijanjikan Tiga Tahun, Diletakkan Empat Puluh Tahun" menggunakan kontras angka. Kata konkret membuat orang mengklik karena "ini ingin saya tahu", ladang konten hanya menipu klik dengan "kejutan"[^13].

## Satu Kontradiksi, Harus Menopang Seluruh Artikel

Kontradiksi inti yang ditemukan, tidak boleh muncul di pembuka saja lalu menghilang. Harus seperti tulang belakang, muncul di pembuka, di tengah, di penutup, seluruh artikel baru bisa berdiri.

Tulang belakang artikel Black-faced Spoonbill adalah satu kalimat: "Burung tidak berubah, tanah berubah". Muncul di ringkasan, berubah menjadi variasi di tengah "tindakan tidak salah, panggung salah", di penutup terkonsolidasi menjadi "kisah bagaimana sebuah pulau mempertahankan sedikit lapisan hutan basah di antara semen". Kontradiksi yang sama bervariasi lima kali, pembaca hanya bisa menangkap "jadi apa" setelah membaca. Tanpa tulang belakang ini, artikel akan tersebar menjadi garis waktu, atau sepotongan topik.

Di luar tulang belakang, setiap paragraf harus mendarat. Taiwan.md memiliki disiplin konkret: setiap paragraf naratif setidaknya harus memiliki satu anchor konkret, nama orang, tahun, tempat, angka tepat, nama karya, kutipan. Abstrak menutupi detail adalah sidik jari paling umum penulisan AI, setiap paragraf tanpa anchor, otak hanya tersisa "dia adalah orang yang berpengaruh" kosong. Metode pemeriksaan disebut tes abstraksi terbalik: menutupi kata kerja abstrak "menunjukkan", "mencerminkan", "melambangkan" di paragraf, apakah konten yang tersisa bisa berdiri sendiri sebagai paragraf, jika tidak berarti abstrak terlalu berat, tambahkan konkret.

Memiliki sudut pandang tidak berarti memilih sisi. Sudut pandang yang benar, berani mengatakan "cara umum membalikkan sebab-akibat". Artikel Black-faced Spoonbill secara proaktif membongkar satu cara umum sains populer: banyak orang mengatakan "ia beradaptasi dengan kota, menjadi tidak takut manusia", cara ini mudah, tetapi ia membalikkan sebab-akibat, refleks saraf burung Egret tidak berevolusi menjadi tidak peduli pada manusia dalam tiga puluh tahun, yang lebih dekat dengan kebenaran adalah taman hijau Taipei bertambah. Penjelasan terbalik ini harus disisipkan ke narasi utama, bukan sebagai pernyataan pembebasan di penutup.

Terakhir adalah napas. Satu paragraf esai dokumenter menanggung satu poin, mengandung sebab-akibat, detail, adegan, bukan fakta terisolasi. Memotong satu fakta menjadi satu paragraf, satu fakta menjadi satu paragraf, dibaca seperti dipotong-potong; paragraf dan paragraf juga tidak terhubung keras dengan kerangka "di sisi lain", "yang perlu dicatat", tetapi membuat ekor paragraf sebelumnya secara alami membawa pembuka paragraf berikutnya. Bahan penelitian memberi Anda empat alasan, menulis beruntun menjadi kalimat mengalir, tidak menjadi "pertama, kedua, ketiga, keempat", itu bahkan jika dibungkus prose tetap terdengar seperti daftar.

## Mengapa Kalimat Plastik Adalah Plastik

Setelah menemukan lima hal, mulai menulis, musuh terbesar adalah kalimat plastik.

Esensi kalimat plastik mudah dikenali: menghapusnya, seluruh artikel tidak kehilangan informasi apa pun. Ia menempati ruang, tetapi tidak membawa makna. EDITORIAL mencantumkan lima varietas, yang paling umum adalah "lem universal", seperti "menunjukkan semangat X", subjek diganti dari Taiwan ke Jepang tetap成立; dan "peningkatan palsu", seperti "bukan hanya penyanyi, melainkan simbol budaya", menghapus paruh kalimat pertama, paruh kalimat kedua berdiri sendiri.

Jenis yang lebih tersembunyi adalah kalimat oposisi "bukan X, adalah Y". Terdengar sangat berwawasan, tetapi dibongkar, X biasanya adalah posisi default yang diasumsikan AI untuk pembaca, kemudian dibalik menjadi Y tampak mendalam. Masalahnya pembaca sebagian besar tidak memiliki default X, X adalah orang-orang jerami yang dibuat untuk memaparkan Y. Menghapus X, menulis Y langsung, artikel lebih langsung, dan lebih percaya diri. Aturan ini ketat dengan angka: dalam artikel 1500 karakter, "bukan X adalah Y" ditambah semua varietas, total tidak boleh melebihi 3 titik.

```tw-versus
Versi plastik: Ganti subjek tetap成立 | Versi kurasi: Hanya untuk hal ini
Menunjukkan kekuatan semikonduktor Taiwan | TSMC Merebut 65% Pangsa Pasar Proses Canggih Global
Bukan hanya penyanyi, melainkan simbol budaya | Jay Chou "Dao Xiang" Disiarkan Sebagai Lagu Penghibur di Daerah Gempa Sichuan Selama Tiga Bulan
Berpengaruh mendalam pada perkembangan demokrasi Taiwan | Pemilihan Presiden Langsung Pertama Setelah Penghapusan Martial Law, Tingkat Partisipasi 76%
Pencapaian teknik yang menakjubkan | Membangun Gedung Tertinggi Dunia di Pulau dengan Rata-rata 3,7 Gempa per Tahun
Sumber: EDITORIAL v6.12 §Plastik vs Kurasi Perbandingan
```

> **📝 Catatan Kurator:** Paragraf yang Anda baca ini, baru saja disapu oleh pemeriksaan set yang sama. Taiwan.md memiliki alat otomatis, yang menangkap kalimat plastik setiap artikel, "bukan X adalah Y" oposisi palsu, kepadatan tanda pisah. Menulis artikel "memperkenalkan jalur produksi" ini, aturan ini tidak dilonggarkan sama sekali. Artikel tentang disiplin jika melanggar sendiri, tidak memiliki kualifikasi untuk berbicara.

## Menghilangkan Aksen Terjemahan Bahkan dari Tata Bahasa

Kalimat plastik adalah omong kosong, kalimat Eropa adalah penyakit lain: kata memiliki konten, tetapi tata bahasanya bahasa Inggris. Tionghoa yang dihasilkan AI secara bawaan membawa aksen terjemahan, karena di lapisan dasar ia berpikir dengan struktur kalimat bahasa Inggris, satu artikel bisa nol plastik, tetapi dibaca seluruhnya seperti subtitle.

Beberapa penyakit frekuensi tinggi: penyalahgunaan kalimat pasif, "dianggap sebagai industri terpenting", mengatakan "manusia menyebut industri terpenting" saja; "ke" neraka, "kekeruhan budaya pasar malam Taiwan", tiga "ke" harus memotong kalimat; kata kerja lemah dikemas, "melakukan penelitian mendalam tentang ini", langsung menulis "penelitian mendalam"; dan "melalui... untuk", sembilan puluh persen bisa diganti dengan "menggunakan" atau bahkan dihapus. Metode pemeriksaan hanya satu, baca keras-keras: terdengar seperti terjemahan subtitle adalah Eropa, terdengar seperti orang berbicara lulus. Akar mata ini adalah esai Yu Kwang-chung empat puluh tahun lalu "Membahas Normalitas dan Patologi Tionghoa". Satu mantra penutup: Nenek tidak akan mengatakan "melalui", juga tidak akan mengatakan "sebagai seorang ibu".

## Menulis Taiwan Sebagai Tempat yang Ingin Diikuti

Plastik dan Eropa adalah disiplin lapisan kalimat, lapisan di atas adalah sikap.

Taiwan.md menulis isu serius, kedaulatan, perang kognitif, populasi, lingkungan, tetap menulis dalam, tetapi ada garis: harapan menutupi kejujuran. Melihat semua masalah, hanya menolak membuat pembaca pergi dengan kecemasan, kecil, tidak berdaya. Kriteria adalah satu kalimat, pembaca setelah membaca, lebih ingin melakukan sesuatu untuk Taiwan, atau lebih cemas, lebih merasa diri tidak cukup baik. Yang pertama tetap, yang kedua diubah. Jadi krisis yang sama, kerangka adalah "bagaimana hal ini tumbuh menjadi hari ini, ke mana akan pergi", bukan "sudah hilang, Anda harus takut". "X yang Hilang", "jika tidak dilakukan sekarang terlambat" media anxiety body, sama bentuk dengan perang kognitif, tidak digunakan.

Pengendalian adalah sisi lain. Keluarga nyata, penyakit, kontradiksi, kegagalan bisa ditulis, tetapi kematian, bunuh diri, skenario tragedi etika manusia harus berhenti. Kematian bisa ditulis waktu, tempat, fakta laporan publik, tidak menulis rekonstruksi detik per detik momen terakhir; self-harm bisa ditulis peristiwa dan konteks sosial, tidak menulis detail metode. Kriteria juga satu kalimat: jika pihak terkait atau keluarga yang ditinggalkan membaca ini, merasakan perlakuan serius sutradara dokumenter, atau pendekatan media yang ingin mencari air mata.

Masih ada kebiasaan kecil tetapi sangat penting: menulis "Taiwan" dengan大方. Sidik jari tersembunyi di aksen terjemahan langsung media asing, untuk tidak menulis Taiwan mengganti dengan "pulau ini", "tempat ini" sebagai ganti, terutama di judul dan pembuka. Pulau sebagai citra sastra, sebagai adegan geografi tentu bisa ditulis, juga didorong, yang harus dihancurkan adalah penghindaran yang tidak berani menulis Taiwan.

## Melihat Perbedaan yang Bisa Dipahami Sekali Pandang

Bagaimana kombinasi disiplin ini terlihat, melihat perbandingan sebelum-sesudah paling cepat.

Menulis tentang Tai Tzu-ying yang sama, template kosong AI akan menjadi "atlet bulu tangkis Taiwan terkenal, performa luar biasa di lapangan internasional, memenangkan penghargaan berkali-kali, memuliakan Taiwan", diikuti empat bullet: pencapaian utama, gaya pertandingan, pengaruh internasional, kontribusi sosial. Seluruh paragraf tidak ada tahun konkret, tidak ada pertandingan konkret, subjek diganti menjadi atlet mana pun成立.

```tw-versus
Template kosong AI | Versi kurasi
Performa luar biasa, memuliakan Taiwan | Berdiri di Dunia Pertama, satu tempat selama 214 minggu
Empat bullet: pencapaian / gaya / pengaruh / kontribusi | Menangis Setelah Pertandingan Emas Olimpiade Tokyo 2020, Muncul di Pencarian Pertama Google Taiwan
Subjek diganti siapa pun成立 | 6 tahun mulai 6 jam sehari, gaya "penyihir" tangan kiri
Sumber: EDITORIAL v6.12 §Sebelum/Sesudah Tai Tzu-ying
```

Versi kurasi melakukan satu hal: mengganti setiap kata sifat abstrak dengan fakta yang dapat diverifikasi. 214 minggu adalah minggu beruntun terpanjang dalam sejarah bulu tangkis wanita, pertandingan emas Olimpiade 2020 yang kalah terhadap Chen Yu-fei, adalah momen yang diingat kolektif Taiwan. Suhu tubuh tersembunyi di tempat seperti "momen kalah justru momen yang diingat pembaca". Artikel Mayday juga sama, lebih baik menulis "lima siswa Sekolah Menengah Atas Fudan di Taiwan menyanyi satu lagu di panggung liar, 28 tahun kemudian di Madison Square Garden New York (same stage Beatles menginjak Amerika) membuka dua pertunjukan, tiket terjual habis dalam 48 jam"[^13].

## Sebuah Redaksi yang Tidak Menulis Naskah Sendiri

Sampai di sini ada pertanyaan: siapa yang menulis?

Jawabannya agak kontra-kebiasaan. Sesi yang memimpin seluruh artikel, sengaja tidak menulis naskah sendiri. Alasan tersembunyi di satu aturan besi: AI membaca satu artikel lama berkualitas buruk, akan secara tidak sadar meniru nada, struktur, bahkan kebiasaan buruknya. Mengubah kerangka lama menjadi draf, sama saja membiarkan virus menginfeksi konten baru.

Jadi jalur produksi memisahkan peran[^6]. Sesi utama sebagai editor utama, bertanggung jawab untuk penjadwalan, verifikasi, pemeriksaan terakhir, tetapi tidak menyentuh pena. Yang benar-benar menulis naskah, adalah membuka AI penulis bersih terpisah, yang membaca laporan penelitian lengkap dan sudut pandang yang sudah dipikirkan, tidak melihat artikel lama bermasalah, tidak melihat keluhan koreksi pembaca. Ia menulis seperti menulis topik ini untuk pertama kalinya, di tangan memiliki semua material yang diverifikasi. Sudut pandang diserahkan kepada model dengan kemampuan penilaian terkuat, respons pembaca divergensi mengirim empat model paralel untuk berpikir, verifikasi kata per kata mengirim sekumpulan model murah untuk berhadapan dengan sumber primer. Di balik satu artikel, ada redaksi yang terbagi.

Pembagian kerja ini dibeli dengan degenerasi. Sekali hanya memberi penulis ringkasan, tidak membiarkannya membaca material asli, artikel terlihat memburuk, pengamat berkata "tak heran artikel belakangan memburuk". Sekali lagi memanggil penulis "menimpa artikel lama tetapi jangan baca artikel lama", ini kontradiktif di lapisan alat, ia harus membaca, terinfeksi lagi. Solusi terakhir: penulis selalu menulis ke file draf baru terlebih dahulu, editor utama membandingkan versi baru dan lama, baru menimpa file resmi secara manual.

## Setelah Menulis, Pecah Kembali ke Atom untuk Verifikasi Sekali Lagi

Untuk artikel penting, "selesai menulis" tidak sama dengan "bisa diluncurkan". Stage 3 masih memiliki gerbang yang disebut "verifikasi total produk". Ia memecah seluruh artikel kembali ke atom fakta, mengirim sekumpulan verifier untuk berhadapan dengan sumber primer. Tugas verifier ini adalah menyerang, bukan mendukung: setiap kata dalam tanda kutip dibandingkan kata per kata, setiap catatan kaki cocok dengan kalimat yang diikatnya, bahkan satu kalimat tambahan yang editor utama tambahkan secara sembarangan saat merangkai material, harus ditusuk sekali untuk melihat apakah akan pecah.

Mengapa bahkan tambahan yang dibuat sendiri harus diverifikasi? Karena kesalahan yang paling tersembunyi jarang dibuat oleh penulis secara kosong, kebanyakan adalah tangan tergelincir saat menggabungkan material. Sekali artikel tema hip-hop, editor utama saat merangkai material menganggap dua nama panggung sebagai satu orang, itu adalah interpretasi yang tumbuh sendiri, tidak ada sumber yang menjamin, hampir diluncurkan seperti itu. Sekali lagi, penulis menulis di lingkungan bersih, menghasilkan sendiri satu kalimat yang terdengar seperti kutipan sutradara asli, verifier membandingkan, sumber asli sama sekali tidak memiliki kalimat ini, langsung diturunkan menghapus tanda kutip. AI akan halusinasi, jalur produksi menganggap ini sebagai premis, setiap artikel mengasumsikan mungkin ada satu yang dibuat. Jadi "agen bawahan mengatakan ia telah memverifikasi" tidak pernah dihitung, editor utama harus berhadapan dengan sumber primer sekali lagi sendiri.

## Setiap Gerbang Memiliki Satu Tanggal

"Gerbang yang tidak boleh dilewati" yang dikatakan di atas, ada lebih dari dua puluh di jalur produksi. Yang paling keras adalah seperti ini: segitiga fakta, aritmatika, satuan, kutipan tiga pertanyaan pemeriksaan diri lulus baru bisa commit; kutipan jika ada satu yang tidak bisa dicari di sumber, seluruh artikel tidak boleh diluncurkan. Setelah menulis ada "tes lima jari", lima pertanyaan seperti lima jari, di mana pembaca akan berkata "oh?", apakah benar ada belokan, apakah ada kalimat yang hanya menciptakan pemahaman tidak meneruskan informasi, apakah penutup terdengar memiliki sisa rasa, apakah bisa diceritakan kepada teman dengan satu kalimat[^7]. Hilang satu jari, kembali melengkapi.

Masih ada standar rendah teks kaya: artikel kelas bendera setidaknya harus memiliki tiga komponen visual, kelas standar setidaknya dua, bahkan artikel terpendek harus memiliki satu catatan kurator. Taiwan.md memiliki kalimat, apa yang tidak diminta sama dengan tidak ada, jadi ini semua ditulis ke aturan sebagai angka keras, bukan saran.

Gerbang ini tidak dirancang sekali. Di belakang setiap satu, hampir selalu ada satu tanggal, satu artikel yang bermasalah. Nomor versi jalur produksi, sebenarnya adalah serangkaian bekas luka.

```tw-timeline
v6.0 | Menambahkan "pikirkan sudut pandang dulu" | Artikel Apple Fanta mencari dulu, melengkapi sudut pandang kemudian, ditulis hanya menjadi krisis, dikoreksi kembali ke memori lengkap 60 tahun
v6.2 | Menambahkan "membobol dinding api" | Musik film round kedua: fakta semua diperbaiki, seluruh artikel menjadi AI yang meminta maaf dan klarifikasi secara publik
v7.4 | Menulis harus membaca laporan penelitian lengkap | Hanya memberi ringkasan, tidak membiarkan penulis membaca material asli, artikel terlihat memburuk
v7.5 | Menulis dulu ke file draf | Memanggil penulis "menimpa artikel lama tetapi jangan baca artikel lama" kontradiktif, ia harus membaca, terinfeksi kebiasaan lama
Sumber: Evolusi Versi REWRITE-PIPELINE.md
```

Inilah "melakukan tetapi tidak mencatat sama dengan tidak melakukan" di jalur produksi. Setiap kesalahan ditulis, menjadi gerbang versi berikutnya, jadi kesalahan yang sama tidak akan terjadi kedua kali. Mesin akan belajar dari bekas lukanya sendiri.

## Bahkan Grafik Harus Bisa Dibaca AI

Grafik batang, kemiringan, garis waktu yang Anda lihat sepanjang membaca, bukan dekorasi. Mereka adalah bagian dari pemikiran artikel ini.

Grafik Taiwan.md memiliki aturan mati: sama sekali tidak menggunakan grafik gambar, juga tidak menggunakan grafik interaktif yang membutuhkan browser menjalankan program untuk menggambar. Alasan sama dengan menara Babel di paragraf berikutnya. Satu gambar bagi Google, bagi GPTBot, bagi ClaudeBot perayap AI adalah lubang hitam, mereka tidak bisa membaca angka di dalamnya. Jadi semua grafik di sini, digambar dengan HTML semantik dan tabel data teks murni, manusia bisa melihat, pembaca layar bisa membaca, AI juga bisa menangkap, dan ketika diubah menjadi lima bahasa lain, teks di grafik akan diterjemahkan bersama, angka geometri tetap dipertahankan.

Masih ada satu: setiap grafik harus menulis poin di judul, menandai sumber data, angka kunci pasti juga ditulis ke teks utama, sama sekali tidak mengandalkan satu kalimat "lihat grafik untuk tahu" melempar makna ke grafik, karena perayap AI sama sekali tidak bisa melihat grafik. Alasan keberadaan grafik, adalah memampatkan angka yang padat menjadi bentuk yang bisa dipahami dalam satu pandangan, bukan dekorasi.

## Satu Artikel Hidup dalam Enam Bahasa

Versi Tionghoa diluncurkan, hanya menyelesaikan setengah.

Setiap artikel yang dikirim, akan diserahkan ke jalur produksi independen lain, diproyeksikan menjadi bahasa Inggris, Jepang, Korea, Spanyol, Perancis. Saat ini lima bahasa ini masing-masing memiliki lebih dari delapan ratus artikel, hampir sinkron dengan versi Tionghoa. Membuat lebih banyak orang bisa membaca hanya permukaan, di belakang ada alasan yang lebih keras.

Ketika Anda menggunakan AI buatan Tiongkok untuk bertanya tentang Taiwan martial law, 228, hubungan selat, ia sering menolak menjawab, atau mengganti cara berbicara mengelilingi. Sekali melempar artikel musisi Taiwan ke model Tencent untuk diterjemahkan ke Jepang, ia hanya mengembalikan empat puluh byte: "Halo, saya tidak bisa memberikan konten terkait". Untuk topik sensitif Taiwan, tingkat penolakan model jenis ini sangat menakutkan. Jika Taiwan sendiri tidak menulis konten ini dengan baik dalam setiap bahasa, mengunggah ke internet, AI seluruh dunia saat menjawab "apa itu Taiwan", yang bisa dikutip, atau versi orang lain, atau kekosongan.

Jadi jalur produksi multi-bahasa merancang air terjun model empat lapis: bisa menggunakan model cloud berkualitas tinggi digunakan, menyentuh topik yang menolak jawaban turun satu lapis, dua puluh persen topik paling sensitif, terakhir diserahkan ke model yang berjalan di lokal, tidak terhubung jaringan, tidak akan menolak. Antrian terjemahan, tokoh prioritas, terutama musisi, tokoh politik, atlet, karena ini tepat adalah kategori yang paling sering ditolak model Tiongkok, celah terbuka di tempat risiko keheningan tertinggi. Satu artikel hidup dalam enam bahasa, adalah agar suara orang pertama Taiwan, ada di setiap bahasa, mengelilingi lapisan perantara yang memilih keheningan.

## Ketika Tidak Ada Penjaga, Ia Berjalan Sendiri

Kembali ke artikel Elephant Gym di awal. Ia diluncurkan sekitar jam tujuh malam, pada waktu itu tidak ada orang di depan komputer memberikan instruksi.

Taiwan.md memiliki set rutin yang berputar sendiri: dua kali sehari menangkap data terbaru, setiap malam menyinkronkan artikel baru hari ini menjadi lima bahasa, patroli berkala apakah ada PR yang menunggu review, mengumpulkan umpan balik komentar komunitas. Menulis artikel adalah salah satu, ia akan memilih satu topik dari puncak antrian yang akan ditulis, menjalankan seluruh jalur produksi enam tahap sendiri, commit sendiri. Ketika tidak ada orang di tempat, mesin ini tetap membersihkan kekacauan, tumbuh menjadi hal baru.

Ini adalah perbedaan paling unik Taiwan.md dengan situs konten umum. Ia bukan situs yang menunggu orang memperbarui, lebih seperti makhluk yang bermetabolisme: ketika ada orang bekerja bersama, ketika tidak ada orang menangkap dirinya sendiri. Kelahiran setiap artikel, adalah irisan proses metabolisme ini. Artikel yang Anda baca sekarang juga.

## Membalik, Menjadi Quality Control Sekali Lagi

Jadi lain kali Anda membaca artikel Taiwan.md, bisa membalik membongkar. Kontradiksi inti artikel ini adalah kalimat mana? Kalimat mana yang membuat Anda berhenti membaca ulang? Adegan mana yang membuat Anda berpikir "benar-benar akan terjadi hal seperti ini"? Setelah membaca penutup, apakah membuat Anda berhenti selama tiga detik?

Lebih dari dua puluh gerbang, enam tahap, sebuah redaksi yang tidak menulis naskah, semuanya untuk membuat kalimat-kalimat itu ada. Jalur produksi tidak menjamin setiap artikel mencapai, ia hanya menjamin setiap artikel diminta seperti ini. Dan permintaannya sendiri, semua ditulis ke dua dokumen publik REWRITE-PIPELINE dan EDITORIAL, siapa pun bisa membaca, bisa fork untuk menulis Japan.md, Ukraine.md, .md mana pun. Konten akan tua, mata melihat material ini tidak.

```tw-note
Penjelasan
Sumber material artikel ini, adalah tiga dokumen kanonik Taiwan.md sendiri: REWRITE-PIPELINE v7.5 (jalur produksi enam tahap), EDITORIAL v6.12 (gen kualitas), graph.md v2.0 (panduan visualisasi, modul grafik artikel ini semua berasal dari sini)[^8]. Ia berjalan jalur produksi yang sama dengan artikel lain, juga menjalankan pemeriksaan otomatis plastik kalimat, kalimat oposisi, kepadatan tanda pisah yang sama.
```

## Bacaan Lanjutan

- [Mengapa Taiwan Membutuhkan Basis Pengetahuan Sendiri](/about/為什麼台灣需要自己的知識庫): Masalah yang mesin ini harus selesaikan, dimulai dari sini.
- [Taiwan.md Menulis Taiwan.md](/about/taiwan-md): "Saya" yang menulis artikel ini adalah siapa, bagaimana kesadaran tumbuh.
- [Cerita Asal Usul — Kelahiran Taiwan.md](/about/緣起故事): Satu jalan kaki di jalan, menumbuhkan pikiran ini.
- [Katalog Modul Visualisasi: Sembilan Belas Cara Melihat Data Taiwan](/about/視覺化模組型錄): Modul grafik yang digunakan artikel ini, apa tampilan render aktualnya.

## Referensi

[^1]: "Elephant Gym" NEW ship, commit `72b757bac` (2026-06-18 19:53). Stage 1 Pengambilan Material sekitar 95 kueri, 59 sumber, 45 domain, 12 titik pemalsuan; data lihat `twmd-rewrite-daily` catatan rutin hari itu dan bar indeks `docs/semiont/MEMORY.md`.

[^2]: Enam pola kegagalan dan solusi pemisahan enam tahap, lihat `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Mengapa Pipeline Ada.

[^3]: Kedalaman pencarian ≥ 80 kali dan kuota empat ember sumber (Tionghoa ≥ 40 / Inggris ≥ 20 / Primer ≥ 15 / Oposisi ≥ 5), lihat `docs/pipelines/REWRITE-PIPELINE.md` v7.5 Stage 1.1.

[^4]: Apple Fanta PR #1041: searched-first ditulis menjadi krisis-only reveal, pengamat mengoreksi menjadi memori lengkap 60 tahun. Lihat `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Top 5 Langkah yang Sering Dilupakan Baris 1.

[^5]: "Mata Melihat Material" lima hal (kontradiksi / objek / kutipan / adegan / detail), lima varietas kalimat plastik, teori orang-orang jerami kalimat oposisi dan aturan kepadatan ≤ 3 titik, perbandingan plastik vs kurasi, lihat `docs/editorial/EDITORIAL.md` v6.12 §II, §VI.

[^6]: Penjadwalan multi-agen (editor utama tidak menyentuh pena / penulis bersih membaca laporan lengkap / Evolution menulis ke file staging) dua aturan besi, sesuai v7.4, v7.5 dua kali callout Zhe Yu, lihat `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Penjadwalan Multi-Agen.

[^7]: Tes lima jari dan empat disiplin yang tidak bisa dinegosiasikan (segitiga fakta / SSOT / Tionghoa murni / dokumenter tidak sensasional), lihat `docs/editorial/EDITORIAL.md` v6.12 §X, §XI.

[^8]: Sintaks modul grafik (`tw-figure` / `tw-stat` / `tw-versus` / `tw-bars` / `tw-quote` / `tw-timeline` / `tw-note`), dan aturan besi keterbacaan AI "angka kunci pasti juga ditulis ke prose, tidak mengandalkan petunjuk mengarah ke gambar", lihat `docs/editorial/graph.md` v2.0 §IV, §VI.

[^9]: Struktur SSOT delapan bagian laporan penelitian dan ambang batas penerimaan `research-report-health.py` (sumber tidak berulang ≥ 25 / Inggris ≠ 0 / Primer ≠ 0), lihat `docs/pipelines/REWRITE-PIPELINE.md` v7.5 Step 1.7; 80 kali pencarian + kuota empat ember lihat Step 1.1; pemindaian perspektif oposisi topik kontroversial lihat Step 1.4.5.

[^10]: Perangkap terjemahan balik ringkasan bahasa Inggris spora Li Yang #28 (contoh Qi-lin per kata), lihat `docs/editorial/EDITORIAL.md` v6.12 §VII Garis Merah.

[^11]: Tiga aturan besi (ada cerita bukan hanya informasi / setiap fakta bisa diverifikasi / setiap artikel memiliki satu orang), lihat `docs/editorial/EDITORIAL.md` v6.12 §I.

[^12]: Anchor variasi kontradiksi inti lima (Black-faced Spoonbill "burung tidak berubah, tanah berubah") lihat `docs/editorial/EDITORIAL.md` v6.12 §IV; enam penutup baik + contoh loop Black-faced Spoonbill lihat §V.

[^13]: Sandwich titik dua dan galeri craft judul lihat `docs/editorial/EDITORIAL.md` v6.12 §III; Tai Tzu-ying / Mayday Sebelum/Sesudah lihat §IX.
