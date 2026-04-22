class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None  # lagu yang sedang diputar

    # tambah lagu
    def tambah_lagu(self, lagu):
        new_node = Node(lagu)

        if self.head is None:
            self.head = self.tail = self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        print(f"Lagu '{lagu}' berhasil ditambahkan")

    # putar lagu sekarang
    def putar(self):
        if self.current is None:
            print("Playlist kosong")
        else:
            print(f"Sedang memutar: {self.current.data}")

    # lagu berikutnya
    def next_lagu(self):
        if self.current is None:
            print("Playlist kosong")
        elif self.current.next is None:
            print("Sudah di lagu terakhir")
        else:
            self.current = self.current.next
            print(f"Pindah ke lagu berikutnya: {self.current.data}")

    # lagu sebelumnya
    def prev_lagu(self):
        if self.current is None:
            print("Playlist kosong")
        elif self.current.prev is None:
            print("Sudah di lagu pertama")
        else:
            self.current = self.current.prev
            print(f"Kembali ke lagu sebelumnya: {self.current.data}")

    # tampilkan semua lagu
    def tampilkan(self):
        if self.head is None:
            print("Playlist kosong")
        else:
            temp = self.head
            no = 1
            print("Daftar Lagu:")
            while temp:
                tanda = " <-- sedang diputar" if temp == self.current else ""
                print(f"{no}. {temp.data}{tanda}")
                temp = temp.next
                no += 1


def main():
    playlist = Playlist()

    while True:
        print("\n=== MENU PLAYER ===")
        print("1. Tambah Lagu")
        print("2. Putar Lagu Sekarang")
        print("3. Lagu Berikutnya (Next)")
        print("4. Lagu Sebelumnya (Previous)")
        print("5. Lihat Playlist")
        print("6. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            lagu = input("Masukkan judul lagu: ")
            playlist.tambah_lagu(lagu)

        elif pilih == "2":
            playlist.putar()

        elif pilih == "3":
            playlist.next_lagu()

        elif pilih == "4":
            playlist.prev_lagu()

        elif pilih == "5":
            playlist.tampilkan()

        elif pilih == "6":
            print("Keluar...")
            break

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()