def binarySearch(data, target):
    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if data[mid]['nama'].lower() == target.lower():
            return mid 
        elif data[mid]['nama'].lower() > target.lower():
            high = mid - 1
        else:
            low = mid + 1
            
    return -1 # Data tidak ditemukan

def main():
    # Data harus terurut (Sorted) agar Binary Search bisa jalan
    buku_telepon = [
        {"nama": "Alex", "no": "0812345"},
        {"nama": "Boni", "no": "0823456"},
        {"nama": "Cristal", "no": "0834567"},
        {"nama": "Daniel", "no": "0845678"},
        {"nama": "Exel", "no": "0856789"}
    ]
    
    print("--- DAFTAR KONTAK ---")
    for kontak in buku_telepon:
        print(f"Nama: {kontak['nama']}")
    
    print("\n---------------------")
    cari = input("Masukkan nama yang ingin dicari: ")
    
    # Memanggil fungsi Binary Search
    hasil = binarySearch(buku_telepon, cari)
    
    # Menampilkan hasil
    if hasil != -1:
        print(f"\n[HASIL] Data ditemukan!")
        print(f"Nama    : {buku_telepon[hasil]['nama']}")
        print(f"No Telp : {buku_telepon[hasil]['no']}")
        print(f"Indeks  : {hasil}")
    else:
        print(f"\n[HASIL] Nama '{cari}' tidak ditemukan dalam daftar.")

if __name__ == "__main__":
    main()