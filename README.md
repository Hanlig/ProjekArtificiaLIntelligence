# ProjekArtificiaLIntelligence

1. Sebutkan 1 topik yang akan dikerjakan untuk Proyek Akhir Mata Kuliah

Projek Akhir: Pembuatan Chatbot Penjualan Kue

2. Jelaskan hasil akhir sistem yang akan dibangun (min. 100 kata)
   
Chatbot ini bertujuan untuk membantu pelanggan dalam memberikan informasi produk,
menerima pesanan, dan menjawab pertanyaan pelanggan. Chatbot ini akan berperan sebagai
admin yang dapat melayani pelanggan diluar jam operasional. Chatbot akan berinteraksi dengan
pelanggan melakukan tanya jawab dengan menggunakan penggunaan bahasa indonesia yang
digunakan sehari-hari. Chatbot yang telah diprogram untuk mengerti setiap kata dengan melihat
kata - kata utama dari kalimat yang diberikan pelanggan. Selain memahami kalimat sehari - hari
dari pelanggan, Chatbot juga membalas dengan bahasa sehari hari. Hal ini untuk memberikan
komunikasi yang lebih natural, santai, mudah dan tetap ramah digunakan untuk pengguna.
Chatbot akan memberikan informasi mengenai jenis kue, ukuran kue, dan harga kue yang
dimiliki oleh Toko Kue. Setelah memberikan informasi produk dan menjawab pertanyaan
pelanggan, Chatbot akan menanyakan kelanjutan pelanggan untuk melakukan pemesanan.
Maka dari itu hasil akhir yang akan dibangun dari Chatbot penjualan kue, seperti:
Chatbot: “Hai Sobat Manies! Selamat datang di Toko Kuempat. Ada yang bisa aku bantu? Mau
cari kue apa hari ini Manies?”
Pelanggan: “saya butuh kue coklat, ada apa aja?”
Chatbot: “Wah, cocok banget. Kuempat punya Fudge Brownies dengan topping almond, keju,
dan oreo. Kamu bisa request coklat huruf sebagai topper loh. Gimana kamu tertarik?”
Pelanggan: “Berapa ya harganya?”
Chatbot: “Fudge Brownies ukuran 20x20 cuma Rp. 75.000 aja per kotak, sudah termasuk
request coklat huruf.”
Pelanggan: “boleh itu saja”
Chatbot: “Sip! kamu boleh mengisi form pembelian ini dan akan diproses pada saat jam kerja.”
Chatbot: “Nama:
No. WA:
Pesanan:
Tgl. Pengiriman:”

3. Jelaskan, pengetahuan apa yang akan menjadi knowledge base sistem?

Knowledge base sistem pada program Chatbot Penjualan Kue ini mengenai informasi
produk yang dijual dan urutan pemesanan yang membantu Chatbot dalam menjalankan tugas
sebagai admin. Sistem ini yang akan membalas pengguna menggunakan bahasa formal
maupun non formal. Sehingga komunikasi yang terjadi antara pelanggan dan Sistem Chatbot
menjadi lebih natural, santai, ramah, dan dapat memberikan pengalaman interaksi yang lebih
nyaman, seolah - olah pelanggan sedang berbicara dengan admin manusia.


**RANCANGAN PEMBANGUNAN CHATBOT ADMIN TOKO KUE**

**1. Tentukan Fungsionalitas Utama Admin Toko Kue**
Beberapa fitur dasar yang biasanya ditangani admin toko kue:

a. Menjawab pertanyaan tentang menu kue.

b. Memberi informasi harga.

c. Menangani pesanan.

d. Menjawab jam buka-tutup toko.

e. Menjawab lokasi toko.

f. Menyapa dan menanggapi ucapan.

g. Menangani pertanyaan umum (FAQ).


**2. Teknologi Inti yang Kamu Butuhkan:**

a. Natural Language Processing (NLP)
    
    Untuk memproses dan memahami bahasa manusia.
    Tools: nltk, spaCy, atau transformers (HuggingFace).

b. Machine Learning / Deep Learning

    Untuk mengklasifikasi maksud (intent) dan menanggapi sesuai konteks.
    Tools: scikit-learn, TensorFlow, atau PyTorch.

c. Intent Recognition & Response Generation

    Intent: mengenali maksud dari input pengguna (seperti “pesan”, “tanya harga”, “ucapan salam”).
    Entity extraction: mengambil detail (seperti jenis kue, jumlah, tanggal).

**3. Arah Pembuatan Chatbot NLP:**

🔹 A. Bangun Sendiri dari Nol (lebih fleksibel, butuh lebih banyak coding)

a. NLP preprocessing (tokenizing, stemming, vectorizing)
b. Intent classification (ML model)
c. Entity recognition
d. Response handling


🔹 B. Pakai Framework NLP (lebih cepat)

a. Rasa (open-source chatbot framework)
b. Dialogflow (Google)
c. Botpress, Microsoft Bot Framework, dll.

