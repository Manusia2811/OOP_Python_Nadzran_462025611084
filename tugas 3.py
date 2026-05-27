class Lingkaran:
    # Atribut unik untuk setiap objek
    def __init__(self, nama, jari_jari):
        self.nama = nama
        self.jari_jari = jari_jari

    # --- INSTANCE METHODS ---
    # Memerlukan 'self' karena mengakses atribut objek (self.jari_jari)
    
    def hitung_luas(self):
        luas = 3.14 * (self.jari_jari ** 2)
        return f"Luas {self.nama}: {luas}"

    def tampilkan_info(self):
        return f"Objek: {self.nama} | Jari-jari: {self.jari_jari}"

    # --- STATIC METHOD ---
    # Tidak butuh 'self' karena fungsinya bersifat umum/pendukung
    
    @staticmethod
    def sapa_pengguna():
        return "Selamat datang di Kalkulator Geometri v1.0"

# --- INSTANSIASI DAN PENGUJIAN ---

# 1. Panggil Static Method (Melalui Nama Class)
print(Lingkaran.sapa_pengguna())
print("-" * 30)

# 2. Buat minimal 2 Object
lingkaran_a = Lingkaran("Lingkaran Kecil", 7)
lingkaran_b = Lingkaran("Lingkaran Besar", 21)

# 3. Panggil dan tampilkan hasil Instance Method
print(lingkaran_a.tampilkan_info())
print(lingkaran_a.hitung_luas())

print(lingkaran_b.tampilkan_info())
print(lingkaran_b.hitung_luas())

# 4. Panggil Static Method (Melalui salah satu Object)
print("-" * 30)
print(f"Pesan sistem: {lingkaran_a.sapa_pengguna()}")
