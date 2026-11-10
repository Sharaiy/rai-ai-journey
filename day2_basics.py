# 1. LIST (Daftar) - Bayangkan ini seperti rak tempat menyimpan banyak data
gaya_uji = [1500, 2500, 8000, 1200]  # List berisi 4 nilai gaya (Newton)
luas_konstan = 0.05 # Luas penampang 0.05 m^2

print("--- 1. MENGUJI LIST ---")
print(f"Data gaya uji yang dimasukkan: {gaya_uji}")
print(f"Jumlah data uji: {len(gaya_uji)} buah\n") # len() untuk menghitung panjang list

# 2. LOOP (Perulangan) - Bayangkan ini seperti mesin otomatis
# Daripada kita hitung tegangan satu per satu secara manual, kita suruh Python mengulanginya
print("--- 2. MENGHITUNG TEGANGAN (LOOP) ---")
for g in gaya_uji:
    tegangan = g / luas_konstan
    print(f"Gaya {g} N -> Tegangan: {tegangan} Pascal")

print("\n--- 3. FUNCTION (Fungsi) ---")
# 3. FUNCTION - Bayangkan ini seperti "alat" yang bisa dipakai berulang kali
# Kita buat alat bernama 'cek_keamanan'
def cek_keamanan(tegangan, batas_maksimal):
    if tegangan > batas_maksimal:
        return "BAHAYA! Melebihi batas aman."
    else:
        return "AMAN."

# Mari kita uji fungsi tersebut dengan data dari perhitungan loop tadi
batas_aman_material = 100000 # Misal batas amannya 100.000 Pascal
print(f"Batas aman material: {batas_aman_material} Pascal")

# Kita uji salah satu gaya (misal gaya 8000 N)
tegangan_uji = 8000 / luas_konstan
status = cek_keamanan(tegangan_uji, batas_aman_material)

print(f"Tegangan 8000 N: {tegangan_uji} Pascal -> Status: {status}")