# 1. LIST (berurutan,bisa diubah / mutable)
hobi = ["Membaca", "Koding", "Berenang"]
print("List Hobi:", hobi)
print("Tipe:", (hobi))

#2. TUPLE (Berurutan, TIDAK bisa diubah / immutable)
koordinat = (-6.1751, 106.8650)
print("Tuple Koordinat:", koordinat)
print("Tipe:", type(koordinat))

# 3. DICTIONARY (pasangan key : value
mahasiswa = {
    "nama": "Naufal",
    "nim": 261080200042,
    "ipk": 4.00
}
print("Dict Mahasiswa:", mahasiswa)
print("Nama Mahasiswa:", mahasiswa["nama"])
print("Tipe:", type(mahasiswa))

#4. SET (Nilai unik,tidak berurutan, tidak ada duplikat)
angka_unik = {1, 2, 3, 4, 5,}
print("Set Angka unik (otomatis menghapus duplikat):", angka_unik)
print("Tipe:", type(angka_unik))