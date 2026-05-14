**a. Judul Program**
Aplikasi Antrean Klinik / Rumah Sakit dengan Metode Circular Queue

**b. Deskripsi Singkat**
Program ini dibuat untuk mensimulasikan sistem antrean pasien di rumah sakit atau klinik secara digital. Konsep utamanya memakai prinsip FIFO (First-In, First-Out), jadi pasien yang datang dan mendaftar duluan bakal dilayani lebih dulu oleh dokter.

Untuk struktur datanya, program ini mengimplementasikan Circular Queue (antrean melingkar) berbasis array. Alasan pakai circular queue dibanding antrean biasa adalah untuk menghemat memori. Dengan memanfaatkan operasi modulo (%), slot array yang sudah kosong karena pasiennya sudah dipanggil bisa dipakai lagi buat pasien baru yang baru daftar. Jadi tidak ada memori yang mubazir atau error antrean penuh padahal sebetulnya masih ada slot kosong di depan.

**c. Source Code dan Penjelasan Logika**
<img width="743" height="880" alt="image" src="https://github.com/user-attachments/assets/cb8e8533-aa70-4899-a268-0ee97a207254" />
<img width="937" height="885" alt="image" src="https://github.com/user-attachments/assets/682739aa-1b9d-44ab-b648-497b9002058b" />
<img width="665" height="388" alt="image" src="https://github.com/user-attachments/assets/9eb297bc-5ed9-45a6-a47a-b70375b28345" />




Penjelasan Alur Kode:
Bagian awal program dimulai dengan fungsi __init__ yang gunanya untuk menyiapkan antrean baru. Di sini, ukuran maksimal array ditentukan (standarnya 10 slot) dan posisi front_idx (indeks depan) beserta rear_idx (indeks belakang) diset ke angka -1. Angka -1 ini jadi penanda kalau antrean masih benar-benar kosong dan belum ada pasien sama sekali.

Untuk memantau kondisi antrean, ada dua fungsi cek yaitu is_empty dan is_full. Fungsi is_empty cuma ngecek apakah front_idx masih di angka -1 atau tidak. Sedangkan is_full pakai rumus matematika (rear_idx + 1) % MAXN. Kalau hasil rumus itu sama dengan posisi front_idx, artinya antrean melingkarnya sudah mentok alias penuh.

Saat ada pasien baru yang mau daftar lewat fungsi enqueue, program bakal cek dulu pakai is_full. Kalau penuh, sistem langsung menolak dan memunculkan pesan peringatan. Kalau ternyata antrean masih kosong, posisi front_idx dan rear_idx bakal diubah jadi 0. Tapi kalau antreannya sudah terisi sebagian, program tinggal memajukan posisi rear_idx satu langkah ke depan pakai rumus modulo tadi, baru setelah itu nama pasiennya dimasukkan ke dalam array.

Lalu untuk proses manggil pasien, kita pakai fungsi dequeue. Pertama, program memastikan dulu kalau antrean tidak kosong. Kalau aman, nama pasien yang ada di posisi front_idx akan dipanggil untuk masuk ke ruang periksa. Setelah dipanggil, program bakal ngecek apakah dia pasien terakhir atau bukan. Kalau indeks depan dan belakangnya sama (front_idx == rear_idx), berarti antrean sudah habis dan kedua indeks di-reset lagi ke -1. Kalau masih ada pasien lain di belakangnya, program tinggal menggeser posisi front_idx maju satu langkah.

Terakhir, ada fungsi peek dan display buat monitoring. Fungsi peek fungsinya simpel, cuma buat mengintip siapa pasien yang ada di urutan paling depan tanpa mengubah antrean. Sementara fungsi display dipakai buat mencetak semua nama pasien yang lagi nyantre. Di sini dipakai perulangan while True yang bakal jalan terus dari posisi front_idx sampai ketemu rear_idx. Indeks perulangannya juga sengaja dimajukan pakai rumus % self.MAXN supaya kalau posisinya sudah di ujung array, dia bisa berputar balik ke indeks 0 dengan lancar.

**d.Output**
<img width="507" height="870" alt="image" src="https://github.com/user-attachments/assets/549eee2b-c407-4767-88bc-d594fee9ff49" />
<img width="485" height="552" alt="image" src="https://github.com/user-attachments/assets/89b4b9db-5b86-4f12-b417-6bb457507a22" />

**e.Link Youtube**
https://youtu.be/6wxyiheUJUA?si=NSuYqXDNbJ6VKztK
