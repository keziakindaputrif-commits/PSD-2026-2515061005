**a. Judul Program**

Program Hash Map Data Nilai Mahasiswa Menggunakan Python


**b. Deskripsi Singkat**


Program ini dibuat untuk mengelola data nilai mahasiswa menggunakan struktur data Hash Map dengan bahasa pemrograman Python. Program ini memiliki fungsi untuk menambahkan data mahasiswa berdasarkan NIM, mencari data mahasiswa, serta menampilkan seluruh isi hash table. Data yang disimpan berupa NIM, nama mahasiswa, dan nilai mahasiswa. Dengan adanya program ini, proses penyimpanan dan pencarian data menjadi lebih mudah dan cepat dibandingkan pencarian biasa.

Struktur data yang digunakan pada program ini adalah Hash Map dengan metode chaining menggunakan linked list untuk menangani collision. Hash Map bekerja dengan cara mengubah key berupa NIM menjadi index tertentu menggunakan fungsi hash. Jika terdapat dua data dengan index yang sama, maka data akan disimpan menggunakan linked list pada slot tersebut. Penggunaan Hash Map membuat proses pencarian data menjadi lebih efisien karena data langsung diarahkan ke lokasi tertentu di dalam tabel hash.


**c. Source Code dan Penjelasan Program**

<img width="681" height="836" alt="image" src="https://github.com/user-attachments/assets/100f6f7b-d925-4ad3-8650-f0c989bfba21" />

<img width="829" height="729" alt="image" src="https://github.com/user-attachments/assets/570c9c6a-cd71-415c-9a28-3a4e535d422d" />

<img width="900" height="573" alt="image" src="https://github.com/user-attachments/assets/b5175ac1-2f0d-4a45-8b85-578a3c7eea74" />


Class Node digunakan untuk membuat node pada linked list. Pada class ini terdapat atribut key yang digunakan untuk menyimpan NIM mahasiswa, atribut value untuk menyimpan data nama dan nilai mahasiswa, serta atribut next yang digunakan untuk menghubungkan node berikutnya apabila terjadi collision pada hash table.

Class HashMapMahasiswa digunakan untuk membuat struktur Hash Map. Pada bagian constructor terdapat variabel SIZE yang berfungsi menentukan jumlah slot pada hash table. Selain itu terdapat variabel table yang berisi list kosong sesuai ukuran hash table yang digunakan untuk menyimpan data mahasiswa.

Fungsi hash_function() digunakan untuk menentukan index penyimpanan data pada hash table. Fungsi ini menggunakan operasi modulus % untuk menghasilkan index berdasarkan NIM mahasiswa. Contohnya jika NIM 12345 dibagi dengan ukuran tabel 5, maka hasilnya adalah 0, sehingga data akan disimpan pada slot ke-0.

Fungsi insert() digunakan untuk menambahkan data mahasiswa ke dalam hash table. Program pertama-tama menentukan index menggunakan fungsi hash, kemudian memeriksa apakah key sudah ada atau belum. Jika key sudah ada maka data akan diperbarui, sedangkan jika belum ada maka program akan membuat node baru dan menyimpannya pada linked list di slot tersebut.

Fungsi search() digunakan untuk mencari data mahasiswa berdasarkan NIM. Program akan menuju slot hasil hash, kemudian memeriksa linked list pada slot tersebut satu per satu. Jika data ditemukan maka program akan mengembalikan data mahasiswa tersebut, sedangkan jika tidak ditemukan maka program akan menghasilkan nilai None.

Fungsi display() digunakan untuk menampilkan seluruh isi hash table. Program akan menampilkan semua slot beserta data mahasiswa yang tersimpan pada masing-masing slot. Jika suatu slot kosong maka program akan menampilkan tulisan NONE.

Fungsi main() merupakan fungsi utama yang menjalankan program secara interaktif. Pada fungsi ini terdapat menu pilihan seperti menambah data mahasiswa, mencari data mahasiswa, menampilkan hash table, dan keluar dari program. Program menggunakan perulangan while True sehingga menu akan terus muncul sampai pengguna memilih keluar dari program.



**d. Output Program**

<img width="414" height="948" alt="image" src="https://github.com/user-attachments/assets/55253e3e-5087-43c1-ac88-0eb4723db72c" />

<img width="646" height="698" alt="image" src="https://github.com/user-attachments/assets/691c9993-0e17-4596-b47f-e26bfe05af63" />


**e. Link YouTube**

https://youtu.be/33mnxngi6Eo
