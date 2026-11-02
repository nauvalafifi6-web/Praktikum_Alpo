 
# --- 2. DATA NILAI MENTAH (Simulasi input dari form web / Database) ---
# Catatan : Input dari form seringkali terbaca sebagai String
str_nilai_algoritma = "85.5"
str_nilai_basis_data = "78.0"
str_nilai_pemrograman_web = "90.2"
sks_per_matkul = 3 # Integer


# --- 3. KONVERSI TIPE DATA (Type Casting) ---
nilai_algo = float(str_nilai_algoritma)
nilai_bd = float(str_nilai_basis_data)
nilai_web = float(str_nilai_pemrograman_web)

# --- 4. KALKULASI MENGGUNAKAN VARIABEL ---
total_nilai = nilai_algo + nilai_bd + nilai_web
jumlah_matkul = 3
rata_rata_nilai = total_nilai / jumlah_matkul
total_sks_diambil = jumlah_matkul * sks_per_matkul


# --- # TIPE DATA KOLEKSI ---
# List daftar mata kuliah yang diambil
daftar_matkul = ["Algoritma dan Pemrograman", "Basis Data", "Pemrograman Web"]

# Dictionary untuk menyimpan Nilai Mutu (KRS/KHS)
transkrip_nilai = {
    "Algoritma dan pemrograman": 4.0,    # Nilai A
    "Basis Data": 3.0,                   # Nilai B
    "Pemrograman Web": 4.0               # Nilai A
}
 
# --- 6. UPDATE VARIABEL DINAMIS ---
# Misal mahasiswa mengambil 1 mata kuliah tambahan
matkul_baru = "jaringan komputer"
nilai_matkul_baru_str = "88.0"
mutu_matkul_baru = 3.5 # Nilai AB

# a. Tambahkan ke List
daftar_matkul.append(matkul_baru)

# B. Tambahkan ke Dictionary
transkrip_nilai[matkul_baru] = mutu_matkul_baru

# C. Rekalkulasi variabel Total & dan rata-rata
nilai_jk = float(nilai_matkul_baru_str)
total_nilai = total_nilai + nilai_jk  #Memperbarui nilai variabel total_nilai
jumlah_matkul = len(daftar_matkul)     #Me matkul menggunakan len(
rata_rata_terbaru = total_nilai / jumlah_matkul

#D. Hitung Indeks Prestasi Kumulatif (IPK) dari Dictionary Mutu
total_bobot_mutu = sum(transkrip_nilai.values())
ipk_sementara = total_bobot_mutu / jumlah_matkul

print("\n--- HASIL REKALKULASI SETELAH PENAMBAHAN MATKUL ---")
print("Daftar Matkul Terbaru :", daftar_matkul)
print("Jumlah Matkul Total   :", jumlah_matkul)
print("Rata-rata Angka Baru  :", round(rata_rata_terbaru, 2))
print("IPK Sementara (Skala 4) :",round(ipk_sementara, 2))
      