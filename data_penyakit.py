# =============================================================================
# data_penyakit.py — Basis Pengetahuan Sistem Pakar (Pernapasan)
# Referensi: WHO, Kemenkes RI, dan Jurnal Respirologi
# Metode: Certainty Factor (CF)
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

DESKRIPSI_GEJALA = {
    "G01": {"penjelasan": "Suhu tubuh meningkat di atas 38°C, menandakan sistem imun sedang melawan infeksi. Semakin tinggi demam, semakin aktif respons peradangan tubuh.", "ikon": "fa-temperature-high"},
    "G02": {"penjelasan": "Kenaikan suhu tubuh ringan antara 37–38°C. Sering muncul pada tahap awal infeksi atau saat sistem imun mulai bereaksi.", "ikon": "fa-temperature-low"},
    "G03": {"penjelasan": "Gemetar hebat akibat kontraksi otot yang tidak terkendali, biasanya menyertai demam tinggi sebagai respons tubuh terhadap infeksi.", "ikon": "fa-snowflake"},
    "G04": {"penjelasan": "Produksi keringat berlebih terutama saat tidur malam, sering dikaitkan dengan infeksi kronis seperti TBC atau gangguan hormon.", "ikon": "fa-tint"},
    "G05": {"penjelasan": "Rasa nyeri dan pegal pada otot serta sendi di seluruh tubuh, umum terjadi saat tubuh melawan infeksi virus sistemik.", "ikon": "fa-bone"},
    "G06": {"penjelasan": "Rasa lelah luar biasa yang tidak hilang meski sudah istirahat, menandakan tubuh menggunakan banyak energi untuk melawan penyakit.", "ikon": "fa-battery-quarter"},
    "G07": {"penjelasan": "Nyeri atau tekanan di area kepala, bisa disebabkan oleh peradangan sinus, demam, atau dehidrasi saat sakit.", "ikon": "fa-head-side-virus"},
    "G08": {"penjelasan": "Hilangnya keinginan untuk makan secara signifikan, sering menyertai infeksi akut karena tubuh mengalihkan energi ke sistem imun.", "ikon": "fa-utensils"},
    "G09": {"penjelasan": "Berat badan turun drastis tanpa program diet, bisa menandakan infeksi kronis atau gangguan metabolisme yang serius.", "ikon": "fa-weight"},
    "G10": {"penjelasan": "Batuk tanpa dahak, biasanya akibat iritasi saluran napas oleh virus atau alergen. Sering terjadi pada awal infeksi.", "ikon": "fa-cough"},
    "G11": {"penjelasan": "Batuk yang mengeluarkan dahak berwarna bening atau putih, umumnya menandakan infeksi virus tahap awal atau alergi.", "ikon": "fa-tint"},
    "G12": {"penjelasan": "Batuk dengan dahak kental berwarna kuning atau hijau, menandakan adanya infeksi bakteri yang membutuhkan perhatian medis.", "ikon": "fa-tint"},
    "G13": {"penjelasan": "Batuk yang disertai bercak darah, kondisi serius yang memerlukan pemeriksaan segera karena bisa menandakan infeksi parah.", "ikon": "fa-biohazard"},
    "G14": {"penjelasan": "Batuk yang berlangsung lebih dari 3 minggu tanpa henti, bisa menjadi tanda infeksi kronis seperti TBC atau bronkitis.", "ikon": "fa-clock"},
    "G15": {"penjelasan": "Batuk yang memburuk pada malam atau dini hari, sering terkait dengan kondisi alergi atau asma yang dipicu perubahan suhu.", "ikon": "fa-moon"},
    "G16": {"penjelasan": "Kesulitan bernapas yang muncul tiba-tiba, kondisi darurat yang membutuhkan penanganan segera karena bisa mengancam jiwa.", "ikon": "fa-lungs"},
    "G17": {"penjelasan": "Napas terasa pendek dan cepat meski hanya melakukan aktivitas ringan seperti berjalan, menandakan penurunan fungsi paru.", "ikon": "fa-walking"},
    "G18": {"penjelasan": "Suara napas berbunyi ngik-ngik atau siulan, menandakan penyempitan saluran napas seperti pada asma atau bronkitis.", "ikon": "fa-music"},
    "G19": {"penjelasan": "Rasa berat, perih, atau tertekan di area dada, bisa menandakan peradangan paru atau bronkus yang memerlukan evaluasi.", "ikon": "fa-heartbeat"},
    "G20": {"penjelasan": "Hidung terasa penuh dan sulit bernapas melalui hidung akibat pembengkakan pembuluh darah di rongga hidung.", "ikon": "fa-nose"},
    "G21": {"penjelasan": "Cairan encer keluar dari hidung, mekanisme tubuh untuk mengeluarkan virus atau partikel asing dari saluran napas.", "ikon": "fa-water"},
    "G22": {"penjelasan": "Refleks alami tubuh untuk mengeluarkan iritan dari rongga hidung. Bersin berulang bisa menandakan alergi atau flu.", "ikon": "fa-sneeze"},
    "G23": {"penjelasan": "Rasa nyeri atau gatal di tenggorokan, sering merupakan gejala awal infeksi virus yang menyebabkan peradangan mukosa.", "ikon": "fa-hand-holding-heart"},
    "G24": {"penjelasan": "Nyeri tajam saat menelan makanan atau minuman, menandakan peradangan berat di faring yang bisa disebabkan infeksi bakteri.", "ikon": "fa-ban"},
    "G25": {"penjelasan": "Amandel (tonsil) tampak membesar dan merah, biasanya disertai nyeri tenggorokan, tanda radang amandel akut.", "ikon": "fa-chevron-circle-up"},
    "G26": {"penjelasan": "Bercak putih atau nanah pada permukaan amandel, menandakan infeksi bakteri seperti streptococcus yang butuh antibiotik.", "ikon": "fa-circle"},
    "G27": {"penjelasan": "Perubahan suara menjadi serak atau hilang sama sekali, akibat peradangan pita suara karena infeksi atau pemakaian berlebih.", "ikon": "fa-volume-mute"},
    "G30": {"penjelasan": "Hilangnya kemampuan mengecap rasa, gejala khas COVID-19 namun juga bisa terjadi pada infeksi sinus berat.", "ikon": "fa-tongue"},
    "G31": {"penjelasan": "Hilangnya kemampuan mencium bau, sering menyertai COVID-19 atau infeksi hidung berat yang mengganggu saraf olfaktori.", "ikon": "fa-nose"},
    "G32": {"penjelasan": "Mual, muntah, atau nyeri perut yang menyertai gejala pernapasan, bisa menandakan infeksi sistemik yang mempengaruhi pencernaan.", "ikon": "fa-face-dizzy"},
    "G33": {"penjelasan": "Pembengkakan kelenjar getah bening di leher atau rahang, menandakan sistem imun sedang melawan infeksi aktif.", "ikon": "fa-dot-circle"},
    "G34": {"penjelasan": "Bibir atau ujung jari tampak kebiruan akibat kekurangan oksigen dalam darah. KONDISI DARURAT yang memerlukan bantuan medis segera.", "ikon": "fa-hand"},
}

# Setiap gejala pada penyakit memiliki nilai CF (Certainty Factor) pakar
# CF_expert berkisar 0.0 – 1.0, merepresentasikan seberapa kuat gejala
# tersebut mengindikasikan penyakit. (MB = CF, MD = 0 untuk semua gejala)

DATA_PENYAKIT = {
    "P01": {
        "nama": "Influenza (Flu)",
        "deskripsi": "Infeksi virus pernapasan akut yang sangat menular. Flu datang tiba-tiba dengan gejala sistemik seperti demam tinggi dan nyeri otot.",
        "penyebab": "Virus Influenza tipe A, B, atau C.",
        "gejala_utama": [("G01", 0.9), ("G03", 0.7), ("G05", 0.8), ("G06", 0.6), ("G10", 0.6)],
        "gejala_pendukung": [("G07", 0.4), ("G20", 0.3), ("G21", 0.3), ("G23", 0.3), ("G32", 0.3)],
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
        "gejala_utama": [("G30", 0.9), ("G31", 0.9), ("G01", 0.8), ("G10", 0.7), ("G16", 0.8), ("G06", 0.6)],
        "gejala_pendukung": [("G05", 0.4), ("G07", 0.3), ("G19", 0.4), ("G32", 0.3), ("G20", 0.3)],
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
        "gejala_utama": [("G23", 0.9), ("G24", 0.8), ("G25", 0.8), ("G33", 0.6)],
        "gejala_pendukung": [("G02", 0.3), ("G26", 0.5), ("G07", 0.3), ("G06", 0.2), ("G10", 0.3)],
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
        "gejala_utama": [("G16", 0.9), ("G18", 0.9), ("G19", 0.8), ("G15", 0.7)],
        "gejala_pendukung": [("G10", 0.3), ("G06", 0.3), ("G22", 0.2), ("G17", 0.4)],
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
        "gejala_utama": [("G20", 0.8), ("G21", 0.8), ("G22", 0.7), ("G02", 0.6)],
        "gejala_pendukung": [("G10", 0.3), ("G11", 0.3), ("G23", 0.3), ("G07", 0.3), ("G27", 0.3)],
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
        "gejala_utama": [("G14", 0.9), ("G13", 0.9), ("G04", 0.8), ("G09", 0.8), ("G02", 0.6)],
        "gejala_pendukung": [("G11", 0.3), ("G12", 0.4), ("G06", 0.3), ("G19", 0.3), ("G08", 0.4), ("G16", 0.4)],
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
        "gejala_utama": [("G01", 0.8), ("G12", 0.7), ("G16", 0.9), ("G19", 0.8), ("G03", 0.6), ("G34", 0.9)],
        "gejala_pendukung": [("G06", 0.3), ("G05", 0.3), ("G07", 0.3), ("G32", 0.3), ("G08", 0.3)],
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
        "gejala_utama": [("G11", 0.7), ("G12", 0.8), ("G19", 0.7), ("G02", 0.6)],
        "gejala_pendukung": [("G16", 0.4), ("G06", 0.3), ("G03", 0.3), ("G23", 0.3), ("G05", 0.3)],
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
        "gejala_utama": [("G27", 0.9), ("G10", 0.6), ("G23", 0.6)],
        "gejala_pendukung": [("G24", 0.4), ("G02", 0.3), ("G21", 0.3), ("G33", 0.3), ("G22", 0.3)],
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
