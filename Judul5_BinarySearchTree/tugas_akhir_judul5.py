class Node:
    def __init__(self, npm, nama):
        self.npm = npm
        self.nama = nama
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, npm, nama):
        if root is None:
            return Node(npm, nama)
        if npm < root.npm:
            root.left = self.insert(root.left, npm, nama)
        else:
            root.right = self.insert(root.right, npm, nama)
        return root
    
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(f"NPM : {root.npm} | Nama : {root.nama}")
            self.inorder(root.right)
        return

    def search(self, root, npm):
        while root is not None:
            if npm == root.npm:
                print("\nData Mahasiswa Ditemukan")
                print(f"NPM  : {root.npm}")
                print(f"Nama : {root.nama}")
                break
            elif npm < root.npm:
                root = root.left
            else:
                root = root.right
        else:
            print("\nData mahasiswa tidak ditemukan")
        return
    
def main():
    bst = BinarySearchTree()
    while True:
        print("\n===== Sistem Pengelolaan Data Mahasiswa =====")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Cari Data Mahasiswa")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan menu : ")
        if pilihan == "1":
            try:
                jumlah = int(input("\nMasukkan jumlah mahasiswa : "))
                for i in range(jumlah):
                    print(f"\nData Mahasiswa ke-{i+1}")
                    npm = int(input("Masukkan NPM  : "))
                    nama = input("Masukkan Nama : ")
                    bst.root = bst.insert(bst.root, npm, nama)
                print("\nData mahasiswa berhasil ditambahkan")
            except ValueError:
                print("\nInput tidak valid! Masukkan angka.")
                continue
        elif pilihan == "2":
            if bst.root is None:
                print("\nData mahasiswa masih kosong")
            else:
                print("\n===== DATA MAHASISWA =====")
                bst.inorder(bst.root)
        elif pilihan == "3":
            try:
                cari = int(input("\nMasukkan NPM yang ingin dicari : "))
                bst.search(bst.root, cari)
            except ValueError:
                print("\nInput tidak valid! NPM harus angka.")
                continue
        elif pilihan == "4":
            print("\nProgram selesai...")
            break
        else:
            print("\nMenu tidak tersedia, silakan pilih menu yang benar")
    return

if __name__ == "__main__":
    main()