import pandas as pd

# Data yang tadi kita buat diubah menjadi DataFrame (Tabel)
data_mesin = [
    {"id": "M-001", "nama": "Pompa", "suhu": 85},
    {"id": "M-002", "nama": "Kompresor", "suhu": 92},
    {"id": "M-003", "nama": "Turbin", "suhu": 110},
    {"id": "M-004", "nama": "Bearing", "suhu": 78}
]

# Mengubah List of Dictionaries menjadi Tabel
tabel_mesin = pd.DataFrame(data_mesin)

print("--- 1. TABEL DATA MESIN ---")
print(tabel_mesin)

print("\n--- 2. MENCARI MESIN YANG OVERHEAT ---")
# Filter data tanpa for loop!
mesin_overheat = tabel_mesin[tabel_mesin["suhu"] > 100]
print(mesin_overheat)

print("\n--- 3. STATISTIKA DESKRIPTIF ---")
# Menghitung rata-rata secara instan
rata_rata_suhu = tabel_mesin["suhu"].mean()
suhu_tertinggi = tabel_mesin["suhu"].max()

print(f"Rata-rata suhu mesin: {rata_rata_suhu:.3f} C")
print(f"Suhu tertinggi: {suhu_tertinggi} C")