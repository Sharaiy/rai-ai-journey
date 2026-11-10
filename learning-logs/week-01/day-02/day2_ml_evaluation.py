import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Siapkan dataset yang lebih banyak (kita buat 10 data mainan)
data = {
    'suhu': [85, 92, 110, 78, 105, 115, 80, 88, 102, 90],
    'getaran': [2.1, 3.5, 5.8, 1.5, 4.2, 6.0, 1.8, 2.0, 4.8, 2.5],
    'status': [0, 0, 1, 0, 1, 1, 0, 0, 1, 0] # 0 = Aman, 1 = Rusak
}
df = pd.DataFrame(data)

# 2. Pisahkan Fitur (X) dan Label (y)
X = df[['suhu', 'getaran']]
y = df['status']

# 3. TRAIN/TEST SPLIT (Ini kuncinya!)
# test_size=0.2 artinya 20% data disembunyikan untuk ujian
# random_state=42 agar hasil acaknya konsisten setiap kali dijalankan
X_latih, X_uji, y_latih, y_uji = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Total data asli: {len(df)}")
print(f"Data untuk belajar (Train): {len(X_latih)}")
print(f"Data untuk ujian (Test): {len(X_uji)}\n")

# 4. Latih AI HANYA dengan data latih
model = DecisionTreeClassifier(random_state=42)
model.fit(X_latih, y_latih)

# 5. Uji AI dengan data ujian yang belum pernah dia lihat
prediksi_ai = model.predict(X_uji)

# 6. Hitung Akurasi (berapa persen jawaban AI yang benar)
akurasi = accuracy_score(y_uji, prediksi_ai)

print("--- HASIL UJIAN AI ---")
print(f"Jawaban Asli (Kunci): {list(y_uji)}")
print(f"Tebakan AI           : {list(prediksi_ai)}")
print(f"Akurasi AI           : {akurasi * 100:.1f}%")