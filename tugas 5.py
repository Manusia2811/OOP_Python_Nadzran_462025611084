class DompetDigital:
    def __init__(self, pemilik, pin, saldo_awal):
        # 1. Minimal 3 Private Attributes (Menggunakan __)
        self.__pemilik = pemilik
        self.__pin = pin
        self.__saldo = saldo_awal
        print(f"Akun Dompet Digital atas nama '{self.__pemilik}' berhasil dibuat.")

    # 2. Metode Getter untuk mengakses data secara aman
    def get_pemilik(self):
        return self.__pemilik

    # Getter saldo dengan proteksi (Hanya bisa dilihat jika PIN benar)
    def lihat_saldo(self, input_pin):
        if self.__verifikasi_pin(input_pin):
            return f"Saldo saat ini: Rp{self.__saldo}"
        else:
            return "Akses Ditolak: PIN Salah!"

    # 3. Metode Validasi (Private Method untuk pengecekan internal)
    def __verifikasi_pin(self, input_pin):
        return input_pin == self.__pin

    # Metode untuk mengubah data (Tarik Tunai) dengan validasi
    def tarik_tunai(self, jumlah, input_pin):
        print(f"\n--- Mencoba tarik tunai sebesar Rp{jumlah} ---")
        if self.__verifikasi_pin(input_pin):
            if jumlah <= self.__saldo:
                self.__saldo -= jumlah
                print(f"Penarikan berhasil! Sisa saldo: Rp{self.__saldo}")
            else:
                print("Transaksi Gagal: Saldo tidak mencukupi.")
        else:
            print("Transaksi Gagal: PIN salah!")

# --- Instansiasi dan Pengujian ---

# Membuat Object
dompet_budi = DompetDigital("Nadzran", "281105", 500000)

# A. PEMBUKTIAN AKSES PRIVAT
# Baris di bawah ini akan menyebabkan AttributeError jika diaktifkan
# print(dompet_budi.__saldo) 
# Komentar: Kode di atas error karena __saldo bersifat private dan tidak bisa diakses langsung dari luar class.

# B. PENGUJIAN METODE VALIDASI (PIN Salah)
print(dompet_budi.lihat_saldo("000000"))
dompet_budi.tarik_tunai(100000, "111111")

# C. PENGUJIAN METODE VALIDASI (PIN Benar)
print(f"\nNama Pemilik: {dompet_budi.get_pemilik()}") # Menggunakan Getter
print(dompet_budi.lihat_saldo("281105"))
dompet_budi.tarik_tunai(200000, "281105")