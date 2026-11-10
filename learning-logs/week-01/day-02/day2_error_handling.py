# Simulasi data dari lapangan (ada yang rusak/berupa teks)
data_sensor = ["85.5", "92.0", "ERROR", "78.1"]

print("--- 1. CARA YANG SALAH (Tanpa Pengaman) ---")
# Jika kita paksa membagi teks "ERROR", Python akan crash di sini
# (Kita beri komentar agar tidak menghentikan program)
# suhu = float("ERROR") 

print("\n--- 2. CARA YANG BENAR (Dengan Try-Except) ---")

def olah_data_sensor(data):
    try:
        # KITA COBA (try) ubah teks menjadi angka desimal
        suhu = float(data) 
        # Jika berhasil, hitung sesuatu
        tegangan = suhu * 1.5
        return f"Sukses: Suhu {suhu} C -> Tegangan {tegangan:.2f} Pa"
        
    except ValueError:
        # JIKA GAGAL (misal inputnya "ERROR"), lakukan ini:
        return "Gagal: Data tidak valid (bukan angka)!"

# Mari kita uji fungsi kita ke semua data
for data in data_sensor:
    hasil = olah_data_sensor(data)
    print(f"Input: {data:<5} | Output: {hasil}")