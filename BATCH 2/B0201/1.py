import time

# Catat waktu mulai
waktu_mulai = time.perf_counter()

# --- KODE YANG INGIN DIUKUR ---
# Contoh: Proses perulangan hingga 5 juta kali
total = 0
for i in range(5_000_000):
    total += i
    #print(i)
# ------------------------------

# Catat waktu selesai
waktu_selesai = time.perf_counter()

# Hitung selisih waktu
lama_eksekusi = waktu_selesai - waktu_mulai

print(f"Hasil perhitungan: {total}")
print(f"Lama waktu eksekusi: {lama_eksekusi:.6f}) detik")