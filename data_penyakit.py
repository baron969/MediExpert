# =============================================================================
# data_penyakit.py — Basis Pengetahuan Sistem Pakar (Pernapasan)
# Referensi: WHO, Kemenkes RI, dan Jurnal Respirologi
# =============================================================================

SEMUA_GEJALA = {
    # ------------------------------------
    # KATEGORI 1: UMUM & DEMAM (G01 - G09)
    # ------------------------------------
    "G01": "Demam tinggi (> 38°C)",
    "G02": "Demam ringan (37–38°C)",
    "G03": "Menggigil",
    "G04": "Keringat berlebih, terutama di malam hari",
    "G05": "Nyeri otot dan sendi (Mialgia)",
    "G06": "Kelelahan ekstrem / badan lemas (Malaise)",
    "G07": "Sakit kepala",
    "G08": "Nafsu makan menurun drastis",
    "G09": "Penurunan berat badan drastis tanpa sebab",

    # ------------------------------------
    # KATEGORI 2: PERNAPASAN UTAMA (G10 - G19)
    # ------------------------------------
    "G10": "Batuk kering / tidak berdahak",
    "G11": "Batuk berdahak bening / putih",
    "G12": "Batuk berdahak kuning / hijau / kental",
    "G13": "Batuk berdarah (Hemoptisis)",
    "G14": "Batuk kronis (lebih dari 3 minggu)",
    "G15": "Batuk sering memburuk pada malam atau dini hari",
    "G16": "Sesak napas (Dyspnea) akut",
    "G17": "Napas pendek saat beraktivitas ringan",
    "G18": "Napas berbunyi ngik-ngik (Mengi / Wheezing)",
    "G19": "Dada terasa berat, perih, atau tertekan",

    # ------------------------------------
    # KATEGORI 3: HIDUNG & TENGGOROKAN (G20 - G29)
    # ------------------------------------
    "G20": "Hidung tersumbat",
    "G21": "Hidung berair (Pilek / Rinorea)",
    "G22": "Sering bersin-bersin",
    "G23": "Sakit tenggorokan (nyeri lokal)",
    "G24": "Nyeri hebat saat menelan makanan/minuman",
    "G25": "Amandel bengkak dan kemerahan",
    "G26": "Muncul bercak putih / nanah pada amandel",
    "G27": "Suara serak atau hilang sementara",

    # ------------------------------------
    # KATEGORI 4: SPESIFIK & LAINNYA (G30 - G39)
    # ------------------------------------
    "G30": "Hilang indra perasa (Ageusia)",
    "G31": "Hilang indra penciuman (Anosmia)",
    "G32": "Mual, muntah, atau sakit perut",
    "G33": "Pembengkakan kelenjar getah bening (di leher/rahang)",
    "G34": "Bibir atau ujung jari tampak kebiruan (Sianosis)",
}

# Bobot untuk sistem pakar
BOBOT_UTAMA = 3.0
BOBOT_PENDUKUNG = 1.0

DATA_PENYAKIT = {
    "P01": {
        "nama": "Influenza (Flu)",
        "deskripsi": "Infeksi virus pernapasan akut yang sangat menular. Flu datang tiba-tiba dengan gejala sistemik seperti demam tinggi dan nyeri otot.",
        "penyebab": "Virus Influenza tipe A, B, atau C.",
        "gejala_utama": ["G01", "G03", "G05", "G06", "G10"],
        "gejala_pendukung": ["G07", "G20", "G21", "G23", "G32"],
        "faktor_risiko": {"umur_min": 0, "umur_max": 150, "gender": "Semua"},
        "saran": [
            "Istirahat total (bed rest) dan hindari interaksi fisik.",
            "Perbanyak asupan cairan untuk mencegah dehidrasi.",
            "Konsumsi obat pereda gejala (Parasetamol) sesuai dosis.",
            "Waspadai komplikasi jika batuk tak kunjung sembuh."
        ],
        "warna": "blue",
        "icon": "fas fa-virus",
    },
    "P02": {
        "nama": "COVID-19 (Suspect)",
        "deskripsi": "Penyakit pernapasan yang disebabkan oleh SARS-CoV-2. Karakteristik uniknya adalah hilangnya kemampuan mencium bau dan mengecap rasa.",
        "penyebab": "Virus SARS-CoV-2.",
        "gejala_utama": ["G30", "G31", "G01", "G10", "G16", "G06"],
        "gejala_pendukung": ["G05", "G07", "G19", "G32", "G20"],
        "faktor_risiko": {"umur_min": 0, "umur_max": 150, "gender": "Semua"},
        "saran": [
            "Lakukan isolasi mandiri untuk memutus mata rantai penularan.",
            "Lakukan pengujian medis (Swab Antigen / PCR).",
            "Pantau saturasi oksigen darah secara berkala.",
            "Segera ke RS jika saturasi oksigen turun di bawah 95%."
        ],
        "warna": "rose",
        "icon": "fas fa-shield-virus",
    },
    "P03": {
        "nama": "Faringitis Akut (Radang Tenggorokan)",
        "deskripsi": "Peradangan akut pada mukosa faring. Seringkali merupakan bagian dari ISPA yang lebih luas.",
        "penyebab": "Infeksi virus (Rhinovirus) atau bakteri (Streptococcus).",
        "gejala_utama": ["G23", "G24", "G25", "G33"],
        "gejala_pendukung": ["G02", "G26", "G07", "G06", "G10"],
        "faktor_risiko": {"umur_min": 0, "umur_max": 150, "gender": "Semua"},
        "saran": [
            "Konsumsi cairan hangat seperti lemon dicampur madu.",
            "Gunakan obat kumur antiseptik atau air garam hangat.",
            "Jika ada demam tinggi dan bercak nanah, konsultasi ke dokter untuk antibiotik."
        ],
        "warna": "purple",
        "icon": "fas fa-head-side-cough",
    },
    "P04": {
        "nama": "Asma Bronkial",
        "deskripsi": "Gangguan inflamasi kronis pada jalan napas yang ditandai dengan mengi episodik, sesak napas, dan rasa berat di dada.",
        "penyebab": "Hipersensitivitas saluran napas akibat genetik atau alergi.",
        "gejala_utama": ["G16", "G18", "G19", "G15"],
        "gejala_pendukung": ["G10", "G06", "G22", "G17"],
        "faktor_risiko": {"umur_min": 0, "umur_max": 150, "gender": "Semua"},
        "saran": [
            "Jauhi pemicu alergi seperti debu, asap rokok, atau udara dingin.",
            "Gunakan inhaler pereda (SABA) saat serangan datang.",
            "Tetap tenang dan atur pernapasan secara perlahan.",
            "Ke IGD jika sesak tidak membaik dengan inhaler."
        ],
        "warna": "emerald",
        "icon": "fas fa-wind",
    },
    "P05": {
        "nama": "ISPA / Common Cold",
        "deskripsi": "Infeksi Saluran Pernapasan Akut yang ringan. Terutama berpusat pada rongga hidung tanpa gejala sistemik yang berat.",
        "penyebab": "Rhinovirus atau Coronavirus ringan.",
        "gejala_utama": ["G20", "G21", "G22", "G02"],
        "gejala_pendukung": ["G10", "G11", "G23", "G07", "G27"],
        "faktor_risiko": {"umur_min": 0, "umur_max": 150, "gender": "Semua"},
        "saran": [
            "Umumnya bersifat self-limiting (bisa sembuh sendiri).",
            "Tingkatkan istirahat dan konsumsi Vitamin C.",
            "Gunakan dekongestan jika hidung tersumbat mengganggu tidur."
        ],
        "warna": "cyan",
        "icon": "fas fa-head-side-mask",
    },
    "P06": {
        "nama": "Tuberkulosis (TBC) Paru",
        "deskripsi": "Infeksi kronis yang secara perlahan menghancurkan jaringan paru-paru. Karakteristik utamanya adalah batuk kronis dan keringat malam.",
        "penyebab": "Infeksi bakteri Mycobacterium tuberculosis.",
        "gejala_utama": ["G14", "G13", "G04", "G09", "G02"],
        "gejala_pendukung": ["G11", "G12", "G06", "G19", "G08", "G16"],
        "faktor_risiko": {"umur_min": 0, "umur_max": 150, "gender": "Semua"},
        "saran": [
            "PERHATIAN: Kondisi berisiko menular. Segera ke puskesmas/dokter spesialis paru.",
            "Lakukan pemeriksaan dahak (TCM) dan rontgen dada.",
            "Gunakan masker medis untuk melindungi keluarga di rumah.",
            "Pengobatan (OAT) membutuhkan waktu minimal 6 bulan tanpa putus."
        ],
        "warna": "amber",
        "icon": "fas fa-lungs",
    },
    "P07": {
        "nama": "Pneumonia (Paru Basah)",
        "deskripsi": "Peradangan pada kantung udara (alveolus) yang dapat terisi cairan pekat atau nanah.",
        "penyebab": "Infeksi Bakteri (Streptococcus pneumoniae) atau Virus.",
        "gejala_utama": ["G01", "G12", "G16", "G19", "G03", "G34"],
        "gejala_pendukung": ["G06", "G05", "G07", "G32", "G08"],
        "faktor_risiko": {"umur_min": 0, "umur_max": 150, "gender": "Semua"},
        "saran": [
            "KONDISI DARURAT MEDIS. Penderita seringkali membutuhkan bantuan oksigen.",
            "Segera cari fasilitas gawat darurat (IGD).",
            "Sangat mungkin membutuhkan terapi antibiotik intravena dan rawat inap."
        ],
        "warna": "indigo",
        "icon": "fas fa-lungs-virus",
    },
    "P08": {
        "nama": "Bronkitis Akut",
        "deskripsi": "Peradangan pada lapisan saluran bronkial (saluran napas utama). Sering berkembang setelah flu berat.",
        "penyebab": "Infeksi virus pernapasan atau paparan iritan.",
        "gejala_utama": ["G11", "G12", "G19", "G02"],
        "gejala_pendukung": ["G16", "G06", "G03", "G23", "G05"],
        "faktor_risiko": {"umur_min": 0, "umur_max": 150, "gender": "Semua"},
        "saran": [
            "Berhenti merokok dan hindari paparan asap.",
            "Minum ekspektoran untuk membantu membuang dahak.",
            "Gunakan pelembap udara (humidifier) di ruangan.",
            "Periksa ke dokter jika batuk lebih dari 3 minggu."
        ],
        "warna": "fuchsia",
        "icon": "fas fa-smoking-ban",
    },
    "P09": {
        "nama": "Laringitis Akut (Radang Pita Suara)",
        "deskripsi": "Peradangan pada kotak suara (laring). Gejala utamanya adalah suara yang serak atau hilang sama sekali.",
        "penyebab": "Infeksi virus, refluks lambung (GERD), atau penggunaan suara berlebihan.",
        "gejala_utama": ["G27", "G10", "G23"],
        "gejala_pendukung": ["G24", "G02", "G21", "G33", "G22"],
        "faktor_risiko": {"umur_min": 0, "umur_max": 150, "gender": "Semua"},
        "saran": [
            "Istirahatkan suara Anda sepenuhnya (vocal rest). Jangan berbisik karena membebani pita suara.",
            "Hindari konsumsi alkohol, kafein, dan makanan pedas.",
            "Minum banyak air putih bersuhu ruang."
        ],
        "warna": "teal",
        "icon": "fas fa-comment-slash",
    }
}
