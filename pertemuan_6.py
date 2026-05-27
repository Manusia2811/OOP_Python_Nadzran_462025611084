# =================================================================
# Nama File : inheritance_lab.py
# Deskripsi : Demonstrasi Multiple Inheritance dan Diamond Problem
#             Menggunakan super() dan Method Resolution Order (MRO)
# =================================================================

class Karyawan:
    """Kelas Basis Utama (Top of the Diamond)"""
    def __init__(self, nama, id_karyawan):
        self.nama = nama
        self.id_karyawan = id_karyawan
        print(f"[{self.nama}] Menginisialisasi data dasar Karyawan.")

    def kerja(self):
        return f"{self.nama} sedang melakukan tugas umum."


class Developer(Karyawan):
    """Kelas Turunan Pertama - Kiri"""
    def __init__(self, nama, id_karyawan, bahasa_pemrograman, **kwargs):
        # super() di sini akan mengarah ke Manager jika dipanggil melalui TimLeader
        super().__init__(nama=nama, id_karyawan=id_karyawan, **kwargs)
        self.bahasa_pemrograman = bahasa_pemrograman
        print(f"[{self.nama}] Menginisialisasi keahlian Developer: {self.bahasa_pemrograman}.")

    def kerja(self):
        tugas_asal = super().kerja()
        return f"{tugas_asal}\n-> Menulis kode program dalam bahasa {self.bahasa_pemrograman}."


class Manager(Karyawan):
    """Kelas Turunan Pertama - Kanan"""
    def __init__(self, nama, id_karyawan, departemen, **kwargs):
        # super() di sini akan mengarah ke Karyawan
        super().__init__(nama=nama, id_karyawan=id_karyawan, **kwargs)
        self.departemen = departemen
        print(f"[{self.nama}] Menginisialisasi tanggung jawab Manager departemen: {self.departemen}.")

    def kerja(self):
        tugas_asal = super().kerja()
        return f"{tugas_asal}\n-> Mengelola tim dan proyek di departemen {self.departemen}."


class TimLeader(Developer, Manager):
    """Kelas Turunan Kedua (Bottom of the Diamond - Multiple Inheritance)"""
    def __init__(self, nama, id_karyawan, bahasa_pemrograman, departemen, jumlah_anggota):
        # Menggunakan kwargs untuk mendistribusikan argumen dengan aman lewat super()
        super().__init__(
            nama=nama, 
            id_karyawan=id_karyawan, 
            bahasa_pemrograman=bahasa_pemrograman, 
            departemen=departemen
        )
        self.jumlah_anggota = jumlah_anggota
        print(f"[{self.nama}] Menginisialisasi peran Tim Leader dengan {self.jumlah_anggota} anggota tim.")

    def kerja(self):
        # Memanggil metode kerja() berdasarkan urutan MRO
        tugas_gabungan = super().kerja()
        return f"{tugas_gabungan}\n-> Memimpin rapat evaluasi harian bersama {self.jumlah_anggota} anggota."


# =================================================================
# Eksekusi dan Pengujian
# =================================================================
if __name__ == "__main__":
    print("--- 1. Proses Instansiasi Objek (Perhatikan urutan pemanggilan __init__) ---")
    leader = TimLeader(
        nama="Budi Santoso", 
        id_karyawan="TL-001", 
        bahasa_pemrograman="Python", 
        departemen="Teknologi Informasi", 
        jumlah_anggota=5
    )
    
    print("\n--- 2. Eksekusi Metode kerja() ---")
    print(leader.kerja())
    
    print("\n--- 3. Urutan Method Resolution Order (MRO) ---")
    # Menampilkan urutan pencarian kelas oleh Python
    for index, kelas in enumerate(TimLeader.__mro__, start=1):
        print(f"{index}. {kelas.__name__}")