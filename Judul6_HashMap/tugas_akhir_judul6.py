class Node:
    def __init__(self, key, value):
        self.key = key 
        self.value = value 
        self.next = None

class HashMapMahasiswa:
    def __init__(self, size=5):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def display(self):
        print("\n=== DAFTAR NILAI MAHASISWA (Hash Table) ===")
        for i in range(self.SIZE):
            print(f"Slot {i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"[NIM: {current.key} | {current.value}] -> ", end="")
                current = current.next
            print("NONE")

def main():
    mhs_map = HashMapMahasiswa()
    
    while True:
        print("\n=== Data Nilai Mahasiswa ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Tampilkan Hash Table")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            try:
                nim = int(input("Masukkan NIM (Angka): "))
                nama = input("Masukkan Nama: ")
                nilai = input("Masukkan Nilai: ")
                mhs_map.insert(nim, f"{nama} (Nilai: {nilai})")
                print("Data berhasil dimasukkan!")
            except ValueError:
                print("Input NIM harus berupa angka!")

        elif pilihan == "2":
            try:
                nim_cari = int(input("Masukkan NIM yang dicari: "))
                hasil = mhs_map.search(nim_cari)
                if hasil is not None:
                    print(f"\n[Ditemukan] NIM {nim_cari} -> {hasil.value}")
                else:
                    print(f"\n[Gagal] NIM {nim_cari} tidak ditemukan.")
            except ValueError:
                print("Input NIM harus berupa angka!")

        elif pilihan == "3":
            mhs_map.display()

        elif pilihan == "4":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()