class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def __str__(self):
        return f"Produk: {self.nama} | Harga: Rp{self.harga:,} | Stok: {self.stok}"

    def __eq__(self, other):
        if isinstance(other, Produk):
            return self.harga == other.harga
        return False

    def __lt__(self, other):
        if isinstance(other, Produk):
            return self.harga < other.harga
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Produk):
            return self.harga > other.harga
        return NotImplemented

laptop = Produk("Laptop Asus", 15000000, 5)
smartphone = Produk("iPhone 15", 15000000, 10)
mouse = Produk("Logitech Mouse", 300000, 50)

print("=== Daftar Produk ===")
print(laptop)      
print(smartphone)  
print(mouse)       
print("-" * 30)

print("=== Hasil Perbandingan Harga ===")

print(f"Apakah {laptop.nama} > {mouse.nama}? {laptop > mouse}")

print(f"Apakah {mouse.nama} < {smartphone.nama}? {mouse < smartphone}")

print(f"Apakah harga {laptop.nama} sama dengan {smartphone.nama}? {laptop == smartphone}")