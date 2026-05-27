# Definisi Class
class Laptop:
    def __init__(self, merk, prosesor, ram):
        # Minimal 3 Attributes
        self.merk = merk
        self.prosesor = prosesor
        self.ram = ram

    def deskripsi(self):
        return f"Laptop {self.merk} dengan prosesor {self.prosesor} dan RAM {self.ram}GB."

# Pembuatan minimal 2 Object dari Class yang sama
laptop_1 = Laptop("ASUS ROG", "Intel i9", 32)
laptop_2 = Laptop("MacBook Air", "Apple M2", 16)

# Menampilkan ke konsol menggunakan 1 print untuk 1 object
print(laptop_1.deskripsi())
print(laptop_2.deskripsi())