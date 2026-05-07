**JUDUL PROGRAM**
"Sistem Pencarian Kontak Telepon"

**DESKRIPSI SINGKAT**
Program ini dirancang untuk mensimulasikan pencarian informasi nomor telepon dalam sebuah daftar kontak digital secara cepat dan efisien. Fokus utama program ini adalah memudahkan pengguna menemukan detail kontak (nama dan nomor telepon) hanya dengan memasukkan nama yang dicari sebagai kata kunci.Algoritma struktur data yang diterapkan dalam program ini adalah Binary Search (pencarian biner). Algoritma ini bekerja dengan cara membagi daftar data menjadi dua bagian secara berulang hingga data ditemukan. Syarat utama agar algoritma ini berfungsi adalah data harus dalam keadaan terurut (sorted). Dalam kasus ini, daftar kontak telah diurutkan berdasarkan abjad nama dari A ke Z untuk memastikan efisiensi pencarian sebesar O(log n).

**SOURCE CODE & PENJELASAN LOGIKA**
Program ini dimulai dengan mendefinisikan sebuah fungsi pencarian bernama binarySearch yang membutuhkan dua input, yaitu kumpulan data kontak dan nama yang ingin dicari. Di dalam fungsi ini, kita menyiapkan dua penanda, yaitu batas bawah di angka nol dan batas atas di ujung akhir daftar kontak. Selama batas bawah belum melewati batas atas, program akan terus menghitung titik tengah dari daftar tersebut. Program kemudian membandingkan nama di titik tengah dengan nama yang kita cari; agar tidak terjadi kesalahan karena perbedaan huruf kapital, keduanya diubah menjadi huruf kecil terlebih dahulu. Jika ternyata cocok, program langsung mengembalikan urutan indeksnya. Namun, jika nama di tengah secara abjad lebih besar dari target, area pencarian dipersempit dengan menggeser batas atas ke sebelah kiri titik tengah. Sebaliknya, jika lebih kecil, batas bawah digeser ke sebelah kanan titik tengah. Jika pencarian selesai tanpa menemukan kecocokan, fungsi ini akan mengirimkan nilai -1 sebagai tanda bahwa data tidak ada.

Pada bagian utama program atau fungsi main, kita menyiapkan daftar kontak berisi nama dan nomor telepon yang sudah disusun rapi secara berurutan sesuai abjad agar algoritma pencarian biner bisa bekerja dengan benar. Program akan mencetak seluruh daftar nama yang tersedia ke layar agar pengguna tahu siapa saja yang ada di dalam kontak. Setelah itu, program meminta pengguna mengetikkan nama yang ingin dicari melalui perintah input. Nama tersebut kemudian diproses oleh fungsi binarySearch yang sudah dibuat sebelumnya. Terakhir, program akan mengecek hasil dari fungsi tersebut; jika hasilnya bukan -1, maka detail lengkap berupa nama, nomor telepon, dan posisi indeksnya akan ditampilkan di layar. Jika hasilnya adalah -1, program akan memberi tahu pengguna dengan sopan bahwa nama yang dicari tidak ditemukan dalam daftar.

**CODE**
<img width="1035" height="836" alt="image" src="https://github.com/user-attachments/assets/adc7e895-743e-4153-bd26-a852be3474a4" />
<img width="822" height="287" alt="image" src="https://github.com/user-attachments/assets/86920b2e-4e18-43af-acad-dc712994e2c6" />

**OUTPUT**
<img width="940" height="685" alt="image" src="https://github.com/user-attachments/assets/1186672a-f7e8-4d59-8bc6-087e660ed632" />

**LINK YOUTUBE**
https://youtu.be/YD1iBHsqPmY
