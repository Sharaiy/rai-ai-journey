import pandas as pd
import numpy as np # Kita butuh numpy untuk logika if-else cepat

print("--- 1. MEMBACA FILE CSV ---")
# AI Engineer membaca data asli dari file, bukan mengetik manual
data = pd.read_csv("data_sensor.csv")

print("Lima data teratas:")
print(data.head()) # Hanya menampilkan 5 baris teratas

print("\n--- 2. FILTERING MULTI-KONDISI ---")
# Skenario: Cari mesin yang suhunya di atas 100 ATAU getarannya di atas 4
# Tanda | artinya "ATAU" (OR).
mesin_kritis = data[(data["suhu"] > 100) | (data["getaran"] > 4)]
print("Daftar Mesin Kritis (Suhu > 100 ATAU Getaran > 4):")
print(mesin_kritis)

print("\n--- 3. MENAMBAH KOLOM BARU (FEATURE ENGINEERING) ---")
# Jika suhu > 100 DAN getaran > 4, statusnya 'RUSAK BERAT'. Jika tidak, 'NORMAL'.
# Tanda & artinya "DAN" (AND).
data["status_kesehatan"] = np.where((data["suhu"] > 100) & (data["getaran"] > 4), "RUSAK BERAT", "NORMAL")

print("\nTabel Akhir dengan Status Kesehatan:")
print(data)