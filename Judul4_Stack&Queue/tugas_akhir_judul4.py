class QueueArray:
    def __init__(self, max_size=10):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self, x):
        if self.is_full():
            print("Antrean penuh!")
            return
        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN
        self.q[self.rear_idx] = x
        print(f"Pasien {x} berhasil mendaftar.")

    def dequeue(self):
        if self.is_empty():
            print("Antrean kosong!")
            return
        pasien = self.q[self.front_idx]
        print(f"Pasien {pasien} silakan masuk ke ruang periksa.")
        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("Antrean kosong!")
            return
        print(f"Pasien urutan depan: {self.q[self.front_idx]}")

    def display(self):
        if self.is_empty():
            print("Antrean kosong!")
            return
        print("Daftar tunggu (depan ke belakang): ", end="")
        i = self.front_idx
        while True:
            print(self.q[i], end=" ")
            if i == self.rear_idx:
                break
            i = (i + 1) % self.MAXN
        print()

def main():
    queue = QueueArray(max_size=10) 
    pilih = 0
    
    while pilih != 5:
        print("\n=== SISTEM ANTREAN RUMAH SAKIT ===")
        print("1. Pendaftaran Pasien")
        print("2. Panggilan Pasien")
        print("3. Lihat Pasien Terdepan")
        print("4. Tampilkan Seluruh Antrean")
        print("5. Keluar")
        
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
            
        if pilih == 1:
            val = input("Nama Pasien: ")
            queue.enqueue(val)
        elif pilih == 2:
            queue.dequeue()
        elif pilih == 3:
            queue.peek()
        elif pilih == 4:
            queue.display()
        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()