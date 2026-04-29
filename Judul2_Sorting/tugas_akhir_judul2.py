def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            # Membandingkan elemen pertama (ketebalan) dari tiap sub-list
            if arr[j][0] > arr[j + 1][0]:
                tukar(arr, j, j + 1)

def main():
    try:
        n = int(input("Masukkan jumlah buku di rak: "))
    except ValueError:
        print("Input tidak valid! Harap masukkan angka")
        return
    
    arr = []
    print("\nMasukkan data buku (Judul dan Ketebalan dalam mm):")
    for i in range(n):
        print(f"Buku ke-{i+1}:")
        judul = input(" Judul Buku: ")
        while True:
            try:
                tebal = int(input(" Ketebalan (mm): "))
                arr.append([tebal, judul]) 
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")

    print(f"\nKondisi rak sebelum diurutkan: {arr}")
    
    bubble_sort(arr, len(arr))
    
    print("\nUrutan buku sesuai ketebalan:")
    for buku in arr:
        # buku[0] adalah tebal, buku[1] adalah judul
        print(f"- {buku[1]} ({buku[0]} mm)")

if __name__ == "__main__":
    main()