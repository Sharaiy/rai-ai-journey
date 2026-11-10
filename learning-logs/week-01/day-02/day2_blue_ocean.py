import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

print("--- 1. MEMBACA DATA KOTOR ---")
# pd.to_numeric dengan errors='coerce' akan mengubah teks/error menjadi NaN (angka kosong)
# Ini adalah trik Pandas untuk menangani data rusak secara massal
data = pd.read_csv("data_pabrik_kotor.csv")
data['suhu'] = pd.to_numeric(data['suhu'], errors='coerce')
data['getaran'] = pd.to_numeric(data['getaran'], errors='coerce')
data['tekanan'] = pd.to_numeric(data['tekanan'], errors='coerce')

print("Data setelah dibersihkan (yang error jadi NaN):")
print(data)

print("\n--- 2. MENGHAPUS DATA YANG TIDAK LENGKAP ---")
# dropna() akan membuang baris yang memiliki nilai kosong (NaN)
data_bersih = data.dropna().copy()
print(f"Data awal: {len(data)} baris. Setelah dibersihkan: {len(data_bersih)} baris.")

print("\n--- 3. FEATURE ENGINEERING (Logika Teknik Mesin) ---")
# AI tidak tahu fisika. Kita harus bantu dengan membuat fitur 'Severity Index'
# Logika: Suhu di atas 100 C berbahaya. Getaran di atas 4.0 mm/s berbahaya.
# Kita buat rumus sederhana: (Suhu * 0.5) + (Getaran * 10)
data_bersih['severity_index'] = (data_bersih['suhu'] * 0.5) + (data_bersih['getaran'] * 10)

# Kita beri label (0 = Aman, 1 = Rusak) berdasarkan logika severity index > 80
data_bersih['status'] = np.where(data_bersih['severity_index'] > 80, 1, 0)

print(data_bersih[['id_mesin', 'suhu', 'getaran', 'severity_index', 'status']])

print("\n--- 4. MELATIH AI DENGAN DATA BERSIH ---")
# Fitur yang dipakai AI sekarang bukan cuma suhu & getaran, tapi Severity Index!
X = data_bersih[['suhu', 'getaran', 'severity_index']]
y = data_bersih['status']

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

print("AI berhasil dilatih dengan data industri yang sudah dibersihkan!")

# Uji dengan mesin baru
mesin_baru = pd.DataFrame({
    'suhu': [85.0, 108.0],
    'getaran': [2.0, 5.5]
})
# Kita harus hitung severity index untuk mesin baru sebelum ditebak AI
mesin_baru['severity_index'] = (mesin_baru['suhu'] * 0.5) + (mesin_baru['getaran'] * 10)

prediksi = model.predict(mesin_baru)
print("\n--- 5. PREDIKSI MESIN BARU ---")
for i, hasil in enumerate(prediksi):
    status_teks = "RUSAK" if hasil == 1 else "AMAN"
    print(f"Mesin baru {i+1} (Suhu {mesin_baru['suhu'][i]}, Getaran {mesin_baru['getaran'][i]}) -> {status_teks}")