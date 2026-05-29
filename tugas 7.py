# polymorphism_lab.py

# Parent Class
class AlatPembayaran:
    def proses_bayar(self):
        print("Memproses pembayaran...")


# Child Class 1
class KartuKredit(AlatPembayaran):
    def proses_bayar(self):
        print("Pembayaran berhasil menggunakan Kartu Kredit 💳")


# Child Class 2
class EWallet(AlatPembayaran):
    def proses_bayar(self):
        print("Pembayaran berhasil menggunakan E-Wallet 📱")


# Child Class tambahan (opsional biar lebih bagus)
class TransferBank(AlatPembayaran):
    def proses_bayar(self):
        print("Pembayaran berhasil menggunakan Transfer Bank 🏦")


# Fungsi Duck Typing
def jalankan_transaksi(objek):
    objek.proses_bayar()


# Program utama
print("=== Sistem Pembayaran ===")

# Membuat objek dari class berbeda
kartu = KartuKredit()
ewallet = EWallet()
transfer = TransferBank()

# Menjalankan transaksi (Duck Typing)
jalankan_transaksi(kartu)
jalankan_transaksi(ewallet)
jalankan_transaksi(transfer)