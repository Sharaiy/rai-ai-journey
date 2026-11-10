import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

print("--- 1. MEMBACA DATA KOTOR ---")
# pd.to_numeric dengan errors='coerce' akan mengubah teks/error menjadi NaN (angka kosong)
# Ini adalah trik Pandas untuk menangani data rusak secara massal
data = pd.read_csv("data_ujian.csv")
data['suhu_f'] = pd.to_numeric(data['suhu_f'], errors='coerce')
data['getaran'] = pd.to_numeric(data['getaran'], errors='coerce')

print("Data setelah dibersihkan (yang error jadi NaN):")
print(data)

print("\n--- 2. MENGHAPUS DATA YANG TIDAK LENGKAP ---")
# dropna() akan membuang baris yang memiliki nilai kosong (NaN)
data_bersih = data.dropna().copy()
print(f"Data awal: {len(data)} baris. Setelah dibersihkan: {len(data_bersih)} baris.")

print("\n--- 3. konversi suhu ---")

data_bersih['suhu_c'] = (data_bersih['suhu_f'] - 32) * 5 / 9
data_bersih['status_bahaya'] = np.where((data_bersih['suhu_c'] > 100) & (data_bersih['getaran'] > 4), 1, 0)

print(data_bersih[['id_mesin', 'suhu_f', 'getaran', 'suhu_c', 'status_bahaya']])

print("\n--- 4. MELATIH AI DENGAN DATA BERSIH ---")
# Fitur yang dipakai AI sekarang bukan cuma suhu & getaran, tapi Severity Index!
X = data_bersih[['suhu_f', 'getaran']]
y = data_bersih['status_bahaya']

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

print("AI berhasil dilatih dengan data industri yang sudah dibersihkan!")

# Data baru dari lapangan (Masih Fahrenheit)
mesin_baru = pd.DataFrame({
    'suhu_f': [185.0, 226.4], 
    'getaran': [2.0, 5.5]
})

# Kita harus lakukan proses yang SAMA seperti data latih
mesin_baru['suhu_c'] = (mesin_baru['suhu_f'] - 32) * 5 / 9

print("\n--- 4. MELATIH AI DENGAN DATA BERSIH ---")
# Gunakan suhu_c agar konsisten dengan apa yang akan diprediksi nanti
X = data_bersih[['suhu_c', 'getaran']]
y = data_bersih['status_bahaya']

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)
print("AI berhasil dilatih!")

# Data baru dari lapangan (Masih Fahrenheit)
mesin_baru = pd.DataFrame({
    'suhu_f': [185.0, 226.4], 
    'getaran': [2.0, 5.5]
})

# Konversi data baru ke Celsius
mesin_baru['suhu_c'] = (mesin_baru['suhu_f'] - 32) * 5 / 9

# Prediksi HANYA menggunakan kolom yang dilatih (suhu_c dan getaran)
prediksi = model.predict(mesin_baru[['suhu_c', 'getaran']])

print("\n--- 5. PREDIKSI MESIN BARU ---")
for i, hasil in enumerate(prediksi):
    status_teks = "RUSAK" if hasil == 1 else "AMAN"
    # Cetak menggunakan nama kolom yang benar (suhu_c)
    print(f"Mesin baru {i+1} (Suhu {mesin_baru['suhu_c'][i]:.1f} C, Getaran {mesin_baru['getaran'][i]}) -> {status_teks}")