"""
================================================================
 SISTEM ADMINISTRASI DAPUR
================================================================
Aplikasi konsol untuk mengelola bahan baku dan peralatan dapur.

Memenuhi persyaratan teknis:
- Pilar OOP: Inheritance, Encapsulation, Polymorphism
- Magic Methods: __init__, __str__, __repr__, __len__, __eq__
- Instance Methods & Static Method
- Exception Handling + Custom Exception
- Input/Output interaktif via terminal
================================================================
"""

from datetime import datetime, date


# ============================================================
# CUSTOM EXCEPTIONS
# ============================================================
class DapurError(Exception):
    """Kelas dasar untuk semua exception khusus sistem dapur."""
    pass


class StokTidakCukupError(DapurError):
    """Dipicu saat stok tidak mencukupi untuk dikurangi/dipakai."""
    def __init__(self, nama_barang, diminta, tersedia):
        pesan = (f"Stok '{nama_barang}' tidak cukup! "
                 f"Diminta: {diminta}, tersedia: {tersedia}")
        super().__init__(pesan)


class BarangTidakDitemukanError(DapurError):
    """Dipicu saat kode barang tidak ditemukan di inventaris."""
    def __init__(self, kode):
        super().__init__(f"Barang dengan kode '{kode}' tidak ditemukan.")


class InputTidakValidError(DapurError):
    """Dipicu saat input pengguna tidak valid (mis. angka negatif)."""
    def __init__(self, pesan="Input tidak valid."):
        super().__init__(pesan)


# ============================================================
# BASE CLASS (ENCAPSULATION)
# ============================================================
class Barang:
    """Kelas dasar abstrak untuk semua item di dapur."""

    def __init__(self, kode, nama, harga_satuan, stok):
        self._kode = kode                      # protected
        self._nama = nama
        self.__harga_satuan = self._validasi_harga(harga_satuan)  # privat
        self.__stok = self._validasi_stok(stok)                   # privat

    # ---------- Properties (akses terkontrol / encapsulation) ----------
    @property
    def kode(self):
        return self._kode

    @property
    def nama(self):
        return self._nama

    @property
    def harga_satuan(self):
        return self.__harga_satuan

    @property
    def stok(self):
        return self.__stok

    # ---------- Static methods ----------
    @staticmethod
    def _validasi_harga(harga):
        if harga < 0:
            raise InputTidakValidError("Harga tidak boleh negatif.")
        return harga

    @staticmethod
    def _validasi_stok(stok):
        if stok < 0:
            raise InputTidakValidError("Stok tidak boleh negatif.")
        return stok

    @staticmethod
    def buat_kode(prefix, nomor_urut):
        """Static method: membuat kode barang otomatis, mis. BB-001."""
        return f"{prefix}-{nomor_urut:03d}"

    # ---------- Instance methods ----------
    def tambah_stok(self, jumlah):
        if jumlah <= 0:
            raise InputTidakValidError("Jumlah tambah stok harus > 0.")
        self.__stok += jumlah

    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            raise InputTidakValidError("Jumlah pakai harus > 0.")
        if jumlah > self.__stok:
            raise StokTidakCukupError(self._nama, jumlah, self.__stok)
        self.__stok -= jumlah

    def nilai_total(self):
        """Nilai total barang = harga satuan x stok."""
        return self.__harga_satuan * self.__stok

    def info(self):
        """Method ini di-override oleh subclass (POLYMORPHISM)."""
        return f"[{self._kode}] {self._nama} | Stok: {self.__stok} | Rp{self.__harga_satuan:,.0f}"

    # ---------- Magic methods ----------
    def __str__(self):
        return self.info()

    def __repr__(self):
        return f"Barang(kode={self._kode!r}, nama={self._nama!r})"

    def __eq__(self, other):
        if not isinstance(other, Barang):
            return NotImplemented
        return self._kode == other._kode


# ============================================================
# SUBCLASS 1 : BAHAN BAKU (INHERITANCE)
# ============================================================
class BahanBaku(Barang):
    def __init__(self, kode, nama, harga_satuan, stok, satuan, tanggal_kadaluarsa):
        super().__init__(kode, nama, harga_satuan, stok)
        self.satuan = satuan  # kg, liter, pcs, dll
        self.tanggal_kadaluarsa = tanggal_kadaluarsa  # objek date

    def sudah_kadaluarsa(self):
        return date.today() > self.tanggal_kadaluarsa

    # POLYMORPHISM: override info()
    def info(self):
        status = "KADALUARSA!" if self.sudah_kadaluarsa() else "Masih Layak"
        dasar = super().info()
        return (f"{dasar} {self.satuan} | Exp: "
                f"{self.tanggal_kadaluarsa.strftime('%d-%m-%Y')} ({status})")


# ============================================================
# SUBCLASS 2 : PERALATAN DAPUR (INHERITANCE)
# ============================================================
class Peralatan(Barang):
    def __init__(self, kode, nama, harga_satuan, stok, kondisi="Baik"):
        super().__init__(kode, nama, harga_satuan, stok)
        self.kondisi = kondisi  # Baik / Rusak / Perlu Servis

    # POLYMORPHISM: override info() dengan cara berbeda dari BahanBaku
    def info(self):
        dasar = super().info()
        return f"{dasar} unit | Kondisi: {self.kondisi}"


# ============================================================
# INVENTARIS DAPUR (KOMPOSISI + MAGIC METHODS)
# ============================================================
class InventarisDapur:
    def __init__(self, nama_dapur):
        self.nama_dapur = nama_dapur
        self._daftar_barang = {}   # kode -> objek Barang
        self._counter_bb = 0
        self._counter_pr = 0

    # ---------- Magic methods ----------
    def __len__(self):
        return len(self._daftar_barang)

    def __str__(self):
        return f"Inventaris Dapur '{self.nama_dapur}' ({len(self)} item terdaftar)"

    def __contains__(self, kode):
        return kode in self._daftar_barang

    # ---------- Instance methods ----------
    def tambah_bahan_baku(self, nama, harga, stok, satuan, tanggal_kadaluarsa):
        self._counter_bb += 1
        kode = Barang.buat_kode("BB", self._counter_bb)
        item = BahanBaku(kode, nama, harga, stok, satuan, tanggal_kadaluarsa)
        self._daftar_barang[kode] = item
        return item

    def tambah_peralatan(self, nama, harga, stok, kondisi="Baik"):
        self._counter_pr += 1
        kode = Barang.buat_kode("PR", self._counter_pr)
        item = Peralatan(kode, nama, harga, stok, kondisi)
        self._daftar_barang[kode] = item
        return item

    def cari_barang(self, kode):
        if kode not in self._daftar_barang:
            raise BarangTidakDitemukanError(kode)
        return self._daftar_barang[kode]

    def pakai_bahan(self, kode, jumlah):
        barang = self.cari_barang(kode)
        barang.kurangi_stok(jumlah)
        return barang

    def restock(self, kode, jumlah):
        barang = self.cari_barang(kode)
        barang.tambah_stok(jumlah)
        return barang

    def total_nilai_inventaris(self):
        return sum(b.nilai_total() for b in self._daftar_barang.values())

    def tampilkan_semua(self):
        if not self._daftar_barang:
            print(" (Belum ada barang di inventaris)")
            return
        for barang in self._daftar_barang.values():
            # POLYMORPHISM beraksi: print() memanggil __str__ -> info()
            # hasil berbeda tergantung tipe objek (BahanBaku / Peralatan)
            print(" -", barang)


# ============================================================
# FUNGSI BANTUAN INPUT (VALIDASI)
# ============================================================
def input_angka(prompt, tipe=float, boleh_nol=False):
    while True:
        try:
            nilai = tipe(input(prompt))
            if nilai < 0 or (nilai == 0 and not boleh_nol):
                raise InputTidakValidError("Nilai harus lebih dari 0.")
            return nilai
        except ValueError:
            print("  >> Input harus berupa angka, coba lagi.")
        except InputTidakValidError as e:
            print(f"  >> {e}")


def input_tanggal(prompt):
    while True:
        teks = input(prompt)
        try:
            return datetime.strptime(teks, "%d-%m-%Y").date()
        except ValueError:
            print("  >> Format tanggal salah, gunakan DD-MM-YYYY. Contoh: 31-12-2026")


# ============================================================
# PROGRAM UTAMA (MENU INTERAKTIF)
# ============================================================
def cetak_menu():
    print("\n" + "=" * 50)
    print(" SISTEM ADMINISTRASI DAPUR")
    print("=" * 50)
    print("1. Tambah Bahan Baku")
    print("2. Tambah Peralatan")
    print("3. Lihat Semua Barang")
    print("4. Pakai / Kurangi Stok Bahan")
    print("5. Restock Barang")
    print("6. Cari Barang berdasarkan Kode")
    print("7. Lihat Total Nilai Inventaris")
    print("0. Keluar")
    print("=" * 50)


def main():
    dapur = InventarisDapur("Dapur Utama Restoran")
    print(f"Selamat datang di {dapur}")

    while True:
        cetak_menu()
        pilihan = input("Pilih menu: ").strip()

        try:
            if pilihan == "1":
                nama = input("Nama bahan baku: ").strip()
                harga = input_angka("Harga per satuan (Rp): ")
                stok = input_angka("Jumlah stok awal: ")
                satuan = input("Satuan (kg/liter/pcs): ").strip()
                tgl = input_tanggal("Tanggal kadaluarsa (DD-MM-YYYY): ")
                item = dapur.tambah_bahan_baku(nama, harga, stok, satuan, tgl)
                print(f"\n✔ Berhasil ditambahkan: {item}")

            elif pilihan == "2":
                nama = input("Nama peralatan: ").strip()
                harga = input_angka("Harga per unit (Rp): ")
                stok = input_angka("Jumlah unit: ", tipe=int)
                kondisi = input("Kondisi (Baik/Rusak/Perlu Servis): ").strip() or "Baik"
                item = dapur.tambah_peralatan(nama, harga, stok, kondisi)
                print(f"\n✔ Berhasil ditambahkan: {item}")

            elif pilihan == "3":
                print(f"\nDaftar barang di {dapur.nama_dapur} (total {len(dapur)} item):")
                dapur.tampilkan_semua()

            elif pilihan == "4":
                kode = input("Kode barang: ").strip().upper()
                jumlah = input_angka("Jumlah yang dipakai: ")
                barang = dapur.pakai_bahan(kode, jumlah)
                print(f"\n✔ Stok dikurangi. Kondisi sekarang: {barang}")

            elif pilihan == "5":
                kode = input("Kode barang: ").strip().upper()
                jumlah = input_angka("Jumlah restock: ")
                barang = dapur.restock(kode, jumlah)
                print(f"\n✔ Stok ditambah. Kondisi sekarang: {barang}")

            elif pilihan == "6":
                kode = input("Masukkan kode barang: ").strip().upper()
                barang = dapur.cari_barang(kode)
                print(f"\nDitemukan: {barang}")

            elif pilihan == "7":
                total = dapur.total_nilai_inventaris()
                print(f"\n💰 Total nilai inventaris dapur: Rp{total:,.0f}")

            elif pilihan == "0":
                print("\nTerima kasih. Sampai jumpa!")
                break

            else:
                print("\n>> Pilihan tidak dikenali, silakan coba lagi.")

        # ---------- Exception Handling ----------
        except StokTidakCukupError as e:
            print(f"\n❌ ERROR STOK: {e}")
        except BarangTidakDitemukanError as e:
            print(f"\n❌ ERROR: {e}")
        except InputTidakValidError as e:
            print(f"\n❌ ERROR INPUT: {e}")
        except DapurError as e:
            print(f"\n❌ ERROR DAPUR: {e}")
        except Exception as e:
            print(f"\n⚠ Terjadi kesalahan tak terduga: {e}")


if __name__ == "__main__":
    main()