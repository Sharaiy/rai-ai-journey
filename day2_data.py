# 1. DICTIONARY (Kamus) - Menyimpan data dengan format "Kunci: Nilai" (Key: Value)
# Bayangkan ini seperti buku telepon, atau spesifikasi teknis suatu komponen.
mesin_pompa = {
    "id": "M-001",
    "nama": "Pompa Air Sentrifugal",
    "suhu": 85,         # dalam Celcius
    "getaran": 2.5      # dalam mm/s
}

print("--- 1. MENGUJI DICTIONARY ---")
# Cara memanggil isinya adalah dengan memanggil "Kunci"-nya (Key)
print(f"Mesin: {mesin_pompa['nama']}")
print(f"Suhu saat ini: {mesin_pompa['suhu']} C")

# 2. LIST OF DICTIONARIES - Kumpulan data (Ini format data yang paling sering dipakai AI!)
daftar_mesin = [
    {"id": "M-001", "nama": "Pompa", "suhu": 85},
    {"id": "M-002", "nama": "Kompresor", "suhu": 92},
    {"id": "M-003", "nama": "Turbin", "suhu": 110}
]

print("\n--- 2. LAPORAN KONDISI MESIN ---")
# Kita gunakan Loop (for) untuk mengecek satu per satu
for mesin in daftar_mesin:
    # Kita gunakan If-Else untuk mengambil keputusan
    if mesin["suhu"] > 100:
        status = "BAHAYA (OVERHEAT)"
    else:
        status = "AMAN"
        
    # Cetak laporannya
    print(f"ID: {mesin['id']} | Nama: {mesin['nama']} | Suhu: {mesin['suhu']} C | Status: {status}")