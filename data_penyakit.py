# =============================================================================
# data_penyakit.py — Basis Pengetahuan Sistem Pakar (Pernapasan)
# Referensi: WHO, Kemenkes RI, dan Jurnal Respirologi
# =============================================================================

SEMUA_GEJALA = {
    # Gejala Umum & Demam
    "G01": "Demam tinggi (> 38°C)",
    "G02": "Demam ringan (37–38°C)",
    "G05": "Nyeri otot dan sendi (Mialgia)",
    "G06": "Kelelahan ekstrem / badan lemas (Malaise)",
    "G07": "Sakit kepala",
    "G08": "Menggigil",
    "G31": "Keringat berlebih, terutama di malam hari",
    "G32": "Penurunan berat badan drastis tanpa sebab",
    "G34": "Nafsu makan menurun drastis",

    # Pernapasan & Batuk
    "G03": "Batuk kering / tidak berdahak",
    "G04": "Batuk berdahak bening / putih",
    "G40": "Batuk berdahak kuning / hijau / kental",
    "G33": "Batuk berdarah (Hemoptisis)",
    "G41": "Batuk kronis (lebih dari 3 minggu)",
    "G12": "Sesak napas (Dyspnea) akut",
    "G42": "Napas pendek saat beraktivitas ringan",
    "G13": "Napas berbunyi ngik-ngik (Mengi / Wheezing)",
    "G14": "Dada terasa berat, perih, atau tertekan",
    "G15": "Batuk sering memburuk pada malam atau dini hari",

    # Hidung, Tenggorokan & Kepala
    "G09": "Hidung tersumbat",
    "G10": "Hidung berair (Pilek / Rinorea)",
    "G11": "Sering bersin-bersin",
    "G16": "Sakit tenggorokan (nyeri lokal)",
    "G17": "Nyeri hebat saat menelan makanan/minuman",
    "G18": "Amandel bengkak dan kemerahan",
    "G19": "Muncul bercak putih / nanah pada amandel",
    "G20": "Suara serak atau hilang sementara",

    # Gejala Spesifik / Lanjutan
    "G21": "Hilang indra perasa (Ageusia)",
    "G22": "Hilang indra penciuman (Anosmia)",
    "G23": "Mual, muntah, atau sakit perut",
    "G30": "Pembengkakan kelenjar getah bening (di leher/rahang)",
    "G43": "Bibir atau ujung jari tampak kebiruan (Sianosis)",
}

# Bobot untuk sistem pakar
BOBOT_UTAMA = 3.0
BOBOT_PENDUKUNG = 1.0

DATA_PENYAKIT = {
    "P01": {
        "nama": "Influenza (Flu)",
        "deskripsi": "Infeksi virus pernapasan akut yang sangat menular. Berbeda dengan batuk pilek biasa, flu datang tiba-tiba dengan gejala sistemik seperti demam tinggi dan nyeri otot.",
        "penyebab": "Virus Influenza tipe A, B, atau C.",
        "gejala_utama": ["G01", "G05", "G06", "G08", "G03"],
        "gejala_pendukung": ["G07", "G09", "G10", "G16", "G23"],
        "faktor_risiko": {"umur_min": 0, "umur_max": 100, "gender": "Semua"},
        "saran": [
            "Istirahat total (bed rest) dan hindari interaksi fisik.",
            "Perbanyak asupan cairan untuk mencegah dehidrasi akibat demam.",
            "Gunakan obat analgetik/antipiretik (Parasetamol) sesuai dosis.",
            "Waspadai komplikasi pada anak di bawah 5 tahun atau lansia di atas 65 tahun."
        ],
        "warna": "blue",
        "icon": "fas fa-virus",
    },
    "P02": {
        "nama": "COVID-19 (Suspect)",
        "deskripsi": "Penyakit pernapasan yang disebabkan oleh infeksi virus SARS-CoV-2. Spektrum gejalanya sangat luas, dengan karakteristik unik pada hilangnya kemampuan mencium bau dan mengecap rasa.",
        "penyebab": "Virus SARS-CoV-2.",
        "gejala_utama": ["G21", "G22", "G01", "G03", "G12", "G06"],
        "gejala_pendukung": ["G05", "G07", "G14", "G23", "G09"],
        "faktor_risiko": {"umur_min": 45, "umur_max": 100, "gender": "Semua"}, # Usia lanjut rentan komplikasi
        "saran": [
            "SEGERA lakukan isolasi mandiri untuk memutus mata rantai penularan.",
            "Lakukan pengujian medis (Swab Antigen / PCR) untuk diagnosis pasti.",
            "Pantau saturasi oksigen darah menggunakan oximeter secara rutin.",
            "Segera hubungi faskes terdekat jika saturasi oksigen turun di bawah 95%."
        ],
        "warna": "red",
        "icon": "fas fa-shield-virus",
    },
    "P03": {
        "nama": "Faringitis Akut (Radang Tenggorokan)",
        "deskripsi": "Peradangan akut pada dinding mukosa faring. Seringkali merupakan bagian dari infeksi saluran pernapasan atas (ISPA) yang lebih luas.",
        "penyebab": "70% infeksi virus (Rhinovirus, Adenovirus), 30% infeksi bakteri (Streptococcus grup A).",
        "gejala_utama": ["G16", "G17", "G18", "G30"],
        "gejala_pendukung": ["G02", "G19", "G07", "G06", "G03"],
        "faktor_risiko": {"umur_min": 0, "umur_max": 100, "gender": "Semua"},
        "saran": [
            "Konsumsi banyak cairan hangat, seperti air lemon dicampur madu.",
            "Gunakan obat kumur antiseptik ringan atau air garam hangat 3 kali sehari.",
            "Jika terdapat demam tinggi dan bercak nanah (G19), konsultasikan dengan dokter untuk kemungkinan perlunya antibiotik."
        ],
        "warna": "purple",
        "icon": "fas fa-head-side-cough",
    },
    "P04": {
        "nama": "Asma Bronkial",
        "deskripsi": "Gangguan inflamasi kronis pada jalan napas yang ditandai dengan mengi episodik, sesak napas, rasa berat di dada, dan batuk. Bersifat reversibel, dapat memburuk di malam hari.",
        "penyebab": "Hipersensitivitas saluran napas (Genetik, Alergi, Lingkungan, atau Stres).",
        "gejala_utama": ["G12", "G13", "G14", "G15"],
        "gejala_pendukung": ["G03", "G06", "G11", "G42"],
        "faktor_risiko": {"umur_min": 0, "umur_max": 100, "gender": "Semua"},
        "saran": [
            "Identifikasi dan hindari alergen pemicu (debu, serbuk sari, asap rokok, udara dingin).",
            "Gunakan inhaler pereda (reliever) golongan SABA (seperti salbutamol) jika serangan datang.",
            "Praktikkan teknik pernapasan relaksasi (pursed-lip breathing).",
            "Segera cari pertolongan medis di IGD jika napas tidak membaik setelah 2 kali penggunaan inhaler."
        ],
        "warna": "emerald",
        "icon": "fas fa-wind",
    },
    "P05": {
        "nama": "ISPA / Common Cold",
        "deskripsi": "Infeksi Saluran Pernapasan Akut yang ringan. Berpusat pada rongga hidung (Rinitis) tanpa gejala sistemik yang berat.",
        "penyebab": "Rhinovirus atau Coronavirus ringan.",
        "gejala_utama": ["G09", "G10", "G11", "G02"],
        "gejala_pendukung": ["G03", "G04", "G16", "G07", "G20"],
        "faktor_risiko": {"umur_min": 0, "umur_max": 100, "gender": "Semua"},
        "saran": [
            "Umumnya bersifat self-limiting (sembuh sendiri) dalam 7-10 hari.",
            "Tingkatkan kualitas istirahat dan nutrisi (Vitamin C & Zink).",
            "Gunakan dekongestan nasal jika hidung mampet mengganggu kualitas tidur."
        ],
        "warna": "cyan",
        "icon": "fas fa-head-side-mask",
    },
    "P06": {
        "nama": "Tuberkulosis (TBC) Paru Aktif",
        "deskripsi": "Infeksi kronis mematikan jika tidak diobati, yang secara bertahap menghancurkan jaringan paru-paru. Karakteristik utamanya adalah batuk lama disertai keringat malam tanpa sebab.",
        "penyebab": "Infeksi bakteri Mycobacterium tuberculosis.",
        "gejala_utama": ["G41", "G33", "G31", "G32", "G02"],
        "gejala_pendukung": ["G04", "G40", "G06", "G14", "G34", "G12"],
        "faktor_risiko": {"umur_min": 15, "umur_max": 100, "gender": "Semua"},
        "saran": [
            "KONDISI SERIUS: Segera buat janji dengan dokter spesialis paru (Sp.P).",
            "Lakukan pemeriksaan dahak (BTA / TCM) dan rontgen dada (Thorax).",
            "Wajib menggunakan masker N95/bedah untuk melindungi keluarga di rumah.",
            "Jika terdiagnosis, pengobatan (OAT) memakan waktu minimal 6 bulan tanpa terputus."
        ],
        "warna": "rose",
        "icon": "fas fa-lungs",
    },
    "P07": {
        "nama": "Pneumonia",
        "deskripsi": "Peradangan dan konsolidasi pada kantung udara (alveolus) paru-paru akibat infeksi, menyebabkan kesulitan oksigen masuk ke dalam darah.",
        "penyebab": "Bakteri (Streptococcus pneumoniae), Virus, atau Jamur.",
        "gejala_utama": ["G01", "G40", "G12", "G14", "G08", "G43"],
        "gejala_pendukung": ["G06", "G05", "G07", "G23", "G34"],
        "faktor_risiko": {"umur_min": 60, "umur_max": 100, "gender": "Semua"}, # Ekstra berisiko untuk lansia
        "saran": [
            "KONDISI DARURAT MEDIS, terutama bagi lansia atau bayi.",
            "Pemeriksaan penunjang seperti rontgen dada dan tes darah sangat krusial.",
            "Sangat mungkin membutuhkan terapi antibiotik intravena dan bantuan oksigen di rumah sakit.",
            "Jangan mencoba mengobati sendiri jika napas terasa dangkal dan cepat."
        ],
        "warna": "indigo",
        "icon": "fas fa-lungs-virus",
    },
    "P08": {
        "nama": "Bronkitis Akut",
        "deskripsi": "Peradangan pada lapisan saluran bronkial (saluran yang membawa udara ke paru-paru). Seringkali berkembang setelah flu atau infeksi virus ringan.",
        "penyebab": "Infeksi virus pernapasan, paparan iritan (asap rokok, debu kimia).",
        "gejala_utama": ["G04", "G40", "G14", "G02"],
        "gejala_pendukung": ["G12", "G06", "G08", "G16", "G05"],
        "faktor_risiko": {"umur_min": 0, "umur_max": 100, "gender": "Semua"},
        "saran": [
            "Berhenti merokok dan hindari paparan asap rokok pasif atau debu.",
            "Gunakan humidifier udara di dalam kamar.",
            "Minum cairan ekspektoran atau mukolitik ringan untuk membantu mengeluarkan dahak.",
            "Hubungi dokter jika batuk berlangsung lebih dari 3 minggu (berisiko menjadi bronkitis kronis)."
        ],
        "warna": "fuchsia",
        "icon": "fas fa-smoking-ban",
    },
    "P09": {
        "nama": "Laringitis Akut (Radang Pita Suara)",
        "deskripsi": "Peradangan pada laring (kotak suara) akibat penggunaan suara berlebihan, iritasi, atau infeksi. Gejala paling spesifik adalah hilangnya suara.",
        "penyebab": "Infeksi virus akut, refluks asam lambung (GERD), atau vokalisasi berlebihan.",
        "gejala_utama": ["G20", "G03", "G16"],
        "gejala_pendukung": ["G17", "G02", "G10", "G30", "G11"],
        "faktor_risiko": {"umur_min": 0, "umur_max": 100, "gender": "Semua"},
        "saran": [
            "Istirahatkan suara Anda secara total (vocal rest) — jangan berbisik, karena berbisik justru lebih menegangkan pita suara.",
            "Hindari konsumsi kafein, alkohol, dan makanan pedas yang bisa memicu asam lambung naik ke laring.",
            "Minum banyak air putih suhu ruang."
        ],
        "warna": "teal",
        "icon": "fas fa-comment-slash",
    }
}
