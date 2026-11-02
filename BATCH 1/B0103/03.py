# 1. Variabel profil karakter game
nama_hero = "Arthur"
level = 15
hp = 100.0
is_alive = True
inventory = ["pedang besi", "Busur Kayu", "Tombak Perak", "Kapak", "Meriam"]
atribut = {"kekuatan": 90, "kelincahan": 75}

# 2. Tampilkan seluruh informasi karakter
print("=== Profil Karakter ===")
print("Nama Hero :", nama_hero)
print("Level     :", level)
print("HP        :", hp)
print("Is Alive  :", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)

# 3. Tampilkan tipe data masing-masing variabel
print("\n=== Tipe Data ===")
print("nama_hero :", type(nama_hero))
print("level     :", type(level))
print("hp        :", type(hp))
print("is_alive  :", type(is_alive))
print("inventory :", type(inventory))
print("atribut   :", type(atribut))

# 4. Aksi karakter
# a. Mendapatkan item baru
inventory.append("Ramuan HP")

# b. Naik level: konversi ke float lalu tambah 0.5
level = float(level)
level = level + 0.5

# 5. Cetak kembali informasi terbaru
print("\n=== Profil Karakter (Terbaru) ===")
print("Nama Hero :", nama_hero)
print("Level     :", level)
print("HP        :", hp)
print("Is Alive  :", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)