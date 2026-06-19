# =====================================================================
# 1. PEMBUATAN CUSTOM EXCEPTION
# =====================================================================
class GagalLoginError(Exception):
    """Custom Exception yang dipicu ketika percobaan login gagal."""
    def __init__(self, pesan="Username atau password salah!"):
        self.pesan = pesan
        super().__init__(self.pesan)


# =====================================================================
# 2. CLASS UTAMA DENGAN LOGIKA VALIDASI
# =====================================================================
class SistemAkses:
    def __init__(self):
        # Data kredensial yang tersimpan di sistem
        self.username_terdaftar = "admin"
        self.password_terdaftar = "rahasia123"

    def validasi_login(self, username, password):
        """Metode untuk memvalidasi input menggunakan kata kunci 'raise'"""
        if username != self.username_terdaftar or password != self.password_terdaftar:
            # Memicu custom exception jika input tidak cocok
            raise GagalLoginError("Peringatan: Akses ditolak! Kredensial tidak valid.")
        
        print("Login Berhasil! Selamat datang di sistem.")


# =====================================================================
# 3. IMPLEMENTASI TRY-EXCEPT-FINALLY
# =====================================================================
if __name__ == "__main__":
    sistem = SistemAkses()
    
    print("--- Simulasi Percobaan Login (Akan Error) ---")
    input_user = "user_salah"
    input_pass = "password_ngawur"
    
    # Membungkus pemanggilan metode di dalam blok try-except
    try:
        sistem.validasi_login(input_user, input_pass)
        
    except GagalLoginError as error:
        # Menangkap custom exception yang berhasil dipicu
        print(f"Terjadi Kesalahan: {error}")
        
    finally:
        # Blok yang akan selalu dieksekusi di akhir proses
        print("Proses pemeriksaan login telah selesai dilakukan.")