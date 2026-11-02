#--- 1. DEKLARASI DATA DIRI MAHASISWA ---

nim="61080200042" 
nama_mahasiswa="Naufal"
semester= 1
is_aktif= True #status registrasi ulang


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

# Penentuan status kelulusan semester (boolean)
# Lulus jika rata-rata >= 75.0 dan status mahasiswa aktif
is_lulus_semester = (rata_rata_nilai >= 75.0) and is_aktif

print("\n- HASIL EVALUASI AVAL ---")
print("Total Nilai      :", total_nilai)
print("Rata-rata Nilai  :", round(rata_rata_nilai, 2))
print("Total SKS        :", total_sks_diambil)
print("Status Lulus     :", is_lulus_semester)