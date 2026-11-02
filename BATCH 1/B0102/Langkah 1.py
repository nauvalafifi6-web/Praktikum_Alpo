# --- 1. DEKLARASI DATA DIRI MAHASISWA ---

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

#tampilkan data awal
print(f"Data Mahasiswa: {nama_mahasiswa} (NIM: {nim})")
print("Status Aktif :", is_aktif)
 