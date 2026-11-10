# 1. Panggil library untuk membuat model AI
from sklearn.tree import DecisionTreeClassifier

# 2. Siapkan Data Latih (Data historis dari pabrik)
# Fitur (X): [Suhu, Getaran]
X_latih = [
    [85, 2.1],   # Aman
    [92, 3.5],   # Aman
    [110, 5.8],  # Rusak
    [78, 1.5],   # Aman
    [105, 4.2],  # Rusak
    [115, 6.0]   # Rusak
]

# Label (y): 0 = Aman, 1 = Rusak
y_latih = [0, 0, 1, 0, 1, 1]

# 3. Buat "Otak" AI dan Latih dia!
print("Sedang melatih AI...")
model_ai = DecisionTreeClassifier()
model_ai.fit(X_latih, y_latih) # <-- INI PROSES BELAJARNYA

print("AI selesai dilatih!\n")

# 4. Uji Coba AI dengan data mesin baru yang belum pernah dia lihat
mesin_baru = [
    [88, 2.0],   # Mesin A (Suhu normal, getaran normal)
    [108, 5.5],  # Mesin B (Suhu tinggi, getaran tinggi)
    [95, 4.5]    # Mesin C (Suhu sedang, getaran agak tinggi)
]

# Minta AI memprediksi!
prediksi = model_ai.predict(mesin_baru)

# 5. Tampilkan hasilnya
for i in range(len(mesin_baru)):
    data_mesin = mesin_baru[i]
    hasil = prediksi[i]
    
    status = "RUSAK" if hasil == 1 else "AMAN"
    
    print(f"Mesin dengan Suhu {data_mesin[0]} dan Getaran {data_mesin[1]} -> Prediksi: {status}")