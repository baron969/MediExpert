# =============================================================================
# data_penyakit.py — Basis Pengetahuan Sistem Pakar (Pernapasan)
# Berdasarkan referensi medis umum
# =============================================================================

SEMUA_GEJALA = {
    # Gejala Umum
    "G01": "Demam tinggi (> 38°C)",
    "G02": "Demam ringan (37–38°C)",
    "G03": "Batuk kering",
    "G04": "Batuk berdahak",
    "G05": "Nyeri otot dan sendi",
    "G06": "Kelelahan / badan lemas",
    "G07": "Sakit kepala",
    "G08": "Menggigil",
    # Pernapasan
    "G09": "Hidung tersumbat",
    "G10": "Hidung berair / pilek",
    "G11": "Bersin-bersin",
    "G12": "Sesak napas / sulit bernapas",
    "G13": "Napas berbunyi (mengi)",
    "G14": "Dada terasa berat / sesak",
    "G15": "Batuk memburuk malam hari",
    # Tenggorokan & Mulut
    "G16": "Sakit tenggorokan",
    "G17": "Nyeri saat menelan",
    "G18": "Amandel bengkak / merah",
    "G19": "Bercak putih pada amandel",
    "G20": "Suara serak",
    "G21": "Hilang indra perasa (ageusia)",
    "G22": "Hilang indra penciuman (anosmia)",
    # Pencernaan/Lainnya yang terkait
    "G23": "Mual dan muntah",
    "G27": "Mata merah / perih",
    "G30": "Kelenjar getah bening bengkak",
    "G31": "Keringat berlebih / keringat malam",
    "G32": "Penurunan berat badan drastis",
    "G33": "Batuk darah (hemoptisis)",
    "G34": "Nafsu makan menurun",
}

# Bobot untuk sistem pakar
BOBOT_UTAMA = 3.0
BOBOT_PENDUKUNG = 1.0

DATA_PENYAKIT = {
    "P01": {
        "nama": "Influenza (Flu)",
        "deskripsi": "Infeksi virus pernapasan yang menyerang hidung, tenggorokan, dan paru-paru. Flu datang secara tiba-tiba dan dapat menyebabkan komplikasi pada kelompok rentan.",
        "penyebab": "Virus Influenza (A, B, atau C).",
        "gejala_utama": ["G01", "G05", "G06", "G08", "G03"],
        "gejala_pendukung": ["G07", "G09", "G10", "G16", "G23"],
        "faktor_risiko": {
            "umur_min": 0, "umur_max": 100, "gender": "Semua" # Berisiko pada balita dan lansia, tapi umum terjadi di semua umur
        },
        "saran": [
            "Istirahat total dan hindari aktivitas berat.",
            "Perbanyak minum air putih untuk menghindari dehidrasi.",
            "Konsumsi obat penurun panas (seperti parasetamol) jika demam mengganggu.",
            "Segera ke dokter jika demam tidak turun setelah 3 hari atau muncul sesak napas."
        ],
        "warna": "blue",
        "icon": "fas fa-virus",
    },
    "P02": {
        "nama": "COVID-19",
        "deskripsi": "Penyakit menular yang disebabkan oleh virus SARS-CoV-2. Gejalanya sangat bervariasi, namun kehilangan indra perasa dan penciuman adalah tanda yang sangat spesifik.",
        "penyebab": "Virus SARS-CoV-2.",
        "gejala_utama": ["G21", "G22", "G01", "G03", "G12", "G06"],
        "gejala_pendukung": ["G05", "G07", "G14", "G23", "G04"],
        "faktor_risiko": {
            "umur_min": 45, "umur_max": 100, "gender": "Semua" # Lansia memiliki risiko komplikasi lebih besar
        },
        "saran": [
            "Lakukan isolasi mandiri untuk mencegah penularan ke orang lain.",
            "Lakukan tes Antigen atau PCR untuk konfirmasi pasti.",
            "Pantau saturasi oksigen menggunakan oximeter secara berkala.",
            "Segera hubungi fasilitas kesehatan jika napas terasa sesak atau saturasi < 94%."
        ],
        "warna": "red",
        "icon": "fas fa-shield-virus",
    },
    "P04": {
        "nama": "Radang Tenggorokan (Faringitis)",
        "deskripsi": "Peradangan pada saluran tenggorokan yang biasanya ditandai dengan rasa sakit, gatal, dan kesulitan saat menelan.",
        "penyebab": "Infeksi virus (paling umum) atau infeksi bakteri (Streptococcus pyogenes).",
        "gejala_utama": ["G16", "G17", "G18", "G19", "G30"],
        "gejala_pendukung": ["G02", "G20", "G07", "G06", "G11"],
        "faktor_risiko": {
            "umur_min": 0, "umur_max": 100, "gender": "Semua"
        },
        "saran": [
            "Berkumur dengan air garam hangat atau cairan antiseptik mulut.",
            "Minum cairan hangat (seperti teh dengan madu dan lemon) untuk melegakan tenggorokan.",
            "Hindari makanan pedas, asam, atau berminyak yang dapat memicu iritasi.",
            "Jika disebabkan oleh bakteri (biasanya ditandai demam tinggi dan bercak putih), dokter mungkin akan meresepkan antibiotik."
        ],
        "warna": "purple",
        "icon": "fas fa-head-side-cough",
    },
    "P05": {
        "nama": "Asma Bronkial",
        "deskripsi": "Penyakit kronis pada saluran pernapasan yang menyebabkan penyempitan dan peradangan. Kerap ditandai dengan napas berbunyi (mengi) dan batuk di malam hari.",
        "penyebab": "Faktor genetik dan hipersensitivitas terhadap pemicu (alergen, udara dingin, stres).",
        "gejala_utama": ["G12", "G13", "G14", "G15"],
        "gejala_pendukung": ["G03", "G06", "G04", "G11", "G07"],
        "faktor_risiko": {
            "umur_min": 0, "umur_max": 100, "gender": "Semua"
        },
        "saran": [
            "Jauhi faktor pemicu (seperti debu, asap rokok, polusi, atau bulu hewan).",
            "Gunakan inhaler pereda cepat (reliever) sesuai anjuran dokter saat serangan datang.",
            "Tetap tenang dan atur napas secara perlahan saat merasa sesak.",
            "Segera ke IGD jika sesak tidak membaik setelah menggunakan inhaler."
        ],
        "warna": "emerald",
        "icon": "fas fa-wind",
    },
    "P06": {
        "nama": "Batuk Pilek (Common Cold)",
        "deskripsi": "Infeksi virus ringan pada saluran pernapasan atas (hidung dan tenggorokan). Biasanya tidak berbahaya dan dapat sembuh dengan sendirinya.",
        "penyebab": "Berbagai jenis virus, paling sering Rhinovirus.",
        "gejala_utama": ["G09", "G10", "G11", "G02", "G16"],
        "gejala_pendukung": ["G03", "G04", "G06", "G07", "G20"],
        "faktor_risiko": {
            "umur_min": 0, "umur_max": 100, "gender": "Semua"
        },
        "saran": [
            "Perbanyak istirahat untuk membantu tubuh melawan virus.",
            "Jaga kelembapan udara di ruangan.",
            "Minum air putih yang cukup untuk mengencerkan lendir.",
            "Gunakan obat dekongestan tetes atau oral jika hidung tersumbat sangat mengganggu."
        ],
        "warna": "cyan",
        "icon": "fas fa-thermometer",
    },
    "P07": {
        "nama": "Tuberkulosis (TBC)",
        "deskripsi": "Penyakit menular mematikan yang menyerang paru-paru. Ditandai dengan batuk kronis yang tak kunjung sembuh, penurunan berat badan, dan keringat malam.",
        "penyebab": "Infeksi bakteri Mycobacterium tuberculosis.",
        "gejala_utama": ["G03", "G33", "G31", "G32", "G06"],
        "gejala_pendukung": ["G34", "G01", "G04", "G12", "G30"],
        "faktor_risiko": {
            "umur_min": 15, "umur_max": 100, "gender": "Semua"
        },
        "saran": [
            "TBC adalah kondisi medis serius. SEGERA periksakan diri ke dokter spesialis paru (pulmonologi).",
            "Lakukan tes dahak (BTA) dan rontgen dada untuk memastikan diagnosis.",
            "Gunakan masker medis saat berinteraksi dengan orang lain untuk mencegah penularan.",
            "Pastikan ruangan di rumah memiliki ventilasi dan pencahayaan matahari yang baik."
        ],
        "warna": "rose",
        "icon": "fas fa-lungs",
    },
    "P08": {
        "nama": "Pneumonia",
        "deskripsi": "Peradangan serius pada kantung udara di salah satu atau kedua paru-paru (paru-paru basah). Kantung udara bisa berisi cairan atau nanah.",
        "penyebab": "Infeksi bakteri (Streptococcus pneumoniae), virus, atau jamur.",
        "gejala_utama": ["G01", "G04", "G12", "G14", "G08"],
        "gejala_pendukung": ["G06", "G03", "G05", "G07", "G23"],
        "faktor_risiko": {
            "umur_min": 60, "umur_max": 100, "gender": "Semua" # Lansia sangat berisiko
        },
        "saran": [
            "Pneumonia berpotensi mengancam jiwa, segera cari pertolongan medis.",
            "Pemeriksaan dokter fisik dan rontgen dada sangat diperlukan.",
            "Dokter mungkin akan meresepkan antibiotik atau antiviral, dan dalam kasus berat memerlukan rawat inap.",
            "Perbanyak asupan cairan dan istirahat total."
        ],
        "warna": "indigo",
        "icon": "fas fa-lungs-virus",
    },
}
