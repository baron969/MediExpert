# 🏥 Diagnova - Sistem Pakar Diagnosa Penyakit

**Diagnova** adalah aplikasi sistem pakar modern berbasis web yang dirancang untuk memberikan diagnosa awal terhadap berbagai jenis penyakit berdasarkan gejala yang dialami pengguna. Aplikasi ini menggunakan **Metode Forward Chaining** untuk memproses data gejala (fakta) menuju kesimpulan (diagnosa) secara akurat.

![Diagnova Preview](https://via.placeholder.com/1200x600.png?text=Diagnova+UI+Preview)

## ✨ Fitur Utama
- 🧠 **Forward Chaining Engine**: Logika inferensi cerdas dengan sistem scoring persentase kecocokan.
- 📊 **Statistik Real-time**: Visualisasi data diagnosa menggunakan Chart.js.
- 📜 **Riwayat Konsultasi**: Penyimpanan otomatis hasil diagnosa ke database SQLite.
- 📱 **Responsive & Modern UI**: Tampilan elegan dengan Dark Mode, animasi halus, dan sepenuhnya responsif.
- 📑 **Analisis Detail**: Penjelasan lengkap penyakit beserta saran penanganan medis.
- 🖨️ **Export PDF**: Fitur untuk mencetak atau menyimpan hasil diagnosa sebagai dokumen PDF.

## 🛠️ Tech Stack
- **Backend**: Python, Flask
- **Database**: SQLite
- **Frontend**: HTML5, Vanilla CSS3 (Modern UI), JavaScript (ES6+)
- **Charts**: Chart.js
- **Icons**: FontAwesome

## 📁 Struktur Folder
```
SISTEM PAKAR DETEKSI/
├── app.py                  # Entry point Flask & Database logic
├── metode.py               # Engine Forward Chaining
├── data_penyakit.py        # Basis Pengetahuan (Knowledge Base)
├── requirements.txt        # Dependensi Python
├── static/                 # File Asset (CSS, JS, Images)
└── templates/              # File HTML (Jinja2)
```

## 🚀 Cara Menjalankan
1. Clone repositori ini:
   ```bash
   git clone https://github.com/baron969/Diagnova.git
   ```
2. Masuk ke direktori proyek:
   ```bash
   cd Diagnova
   ```
3. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan aplikasi:
   ```bash
   python app.py
   ```
5. Buka di browser: `http://127.0.0.1:5000`

---
*Dibuat untuk keperluan akademis - Sistem Pakar.*
