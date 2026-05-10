# =============================================================================
# data_penyakit.py
# Modul data penyakit, gejala, dan basis pengetahuan sistem pakar
# Sistem Pakar Diagnosa Penyakit - Forward Chaining
# =============================================================================

# ---------------------------------------------------------------------------
# BASIS PENGETAHUAN: Data semua gejala yang diketahui sistem
# ---------------------------------------------------------------------------
SEMUA_GEJALA = {
    # --- Gejala Umum ---
    "G01": "Demam tinggi (> 38°C)",
    "G02": "Demam ringan (37–38°C)",
    "G03": "Batuk kering",
    "G04": "Batuk berdahak",
    "G05": "Nyeri otot dan sendi",
    "G06": "Kelelahan / badan lemas",
    "G07": "Sakit kepala",
    "G08": "Menggigil",

    # --- Gejala Pernapasan ---
    "G09": "Hidung tersumbat",
    "G10": "Hidung berair / pilek",
    "G11": "Bersin-bersin",
    "G12": "Sesak napas / sulit bernapas",
    "G13": "Napas berbunyi (mengi/wheezing)",
    "G14": "Dada terasa berat / sesak",
    "G15": "Batuk memburuk malam hari",

    # --- Gejala Tenggorokan & Mulut ---
    "G16": "Sakit tenggorokan",
    "G17": "Nyeri saat menelan",
    "G18": "Amandel bengkak / merah",
    "G19": "Bercak putih pada amandel",
    "G20": "Suara serak",
    "G21": "Hilang indra perasa (ageusia)",
    "G22": "Hilang indra penciuman (anosmia)",

    # --- Gejala Kulit & Lainnya ---
    "G23": "Mual dan muntah",
    "G24": "Nyeri perut",
    "G25": "Ruam / bintik merah pada kulit",
    "G26": "Perdarahan gusi atau hidung",
    "G27": "Mata merah / perih",
    "G28": "Penurunan trombosit (tanda lab)",
    "G29": "Nyeri di belakang mata",
    "G30": "Kelenjar getah bening membengkak",
}

# ---------------------------------------------------------------------------
# BASIS PENGETAHUAN: Data detail setiap penyakit
# ---------------------------------------------------------------------------
DATA_PENYAKIT = {
    "P01": {
        "nama": "Influenza (Flu)",
        "deskripsi": (
            "Influenza adalah infeksi virus akut pada saluran pernapasan yang disebabkan oleh "
            "virus Influenza tipe A, B, atau C. Penyakit ini sangat menular dan menyerang sistem "
            "pernapasan atas maupun bawah. Berbeda dengan flu biasa, influenza datang tiba-tiba "
            "dengan gejala yang lebih berat."
        ),
        "penyebab": "Virus Influenza A, B, atau C yang menyebar melalui droplet udara.",
        "gejala_utama": ["G01", "G03", "G05", "G06", "G07", "G08"],
        "gejala_pendukung": ["G04", "G09", "G10", "G16", "G23"],
        "saran": [
            "Istirahat total minimal 5–7 hari dan hindari aktivitas berat.",
            "Perbanyak minum air putih dan cairan hangat (sup, teh herbal).",
            "Konsumsi obat pereda gejala: parasetamol untuk demam, dekongestan untuk hidung.",
            "Segera ke dokter jika demam > 39°C lebih dari 3 hari atau sesak napas.",
            "Vaksinasi flu tahunan untuk pencegahan di masa mendatang.",
            "Hindari kontak dengan orang sehat selama masih bergejala.",
        ],
        "warna": "#3B82F6",  # Biru
        "icon": "fas fa-virus",
    },

    "P02": {
        "nama": "COVID-19",
        "deskripsi": (
            "COVID-19 adalah penyakit infeksi saluran pernapasan yang disebabkan oleh virus "
            "SARS-CoV-2. Gejala bervariasi dari ringan hingga kritis. Ciri khas yang membedakan "
            "COVID-19 dari penyakit lain adalah hilangnya kemampuan mencium bau (anosmia) dan "
            "merasakan rasa (ageusia), serta potensi komplikasi pada paru-paru."
        ),
        "penyebab": "Virus SARS-CoV-2 yang menyebar melalui droplet, aerosol, dan kontak langsung.",
        "gejala_utama": ["G01", "G03", "G12", "G21", "G22", "G06"],
        "gejala_pendukung": ["G05", "G07", "G14", "G23", "G04"],
        "saran": [
            "Isolasi mandiri minimal 10 hari sejak gejala pertama muncul.",
            "Lakukan tes antigen/PCR untuk konfirmasi diagnosis.",
            "Pantau saturasi oksigen — segera ke IGD jika SpO₂ < 94%.",
            "Konsumsi vitamin C, D, zinc, dan obat sesuai resep dokter.",
            "Hubungi hotline COVID setempat atau telemedicine untuk panduan lebih lanjut.",
            "Pastikan ventilasi ruangan baik dan gunakan masker N95.",
        ],
        "warna": "#EF4444",  # Merah
        "icon": "fas fa-biohazard",
    },

    "P03": {
        "nama": "Demam Berdarah Dengue (DBD)",
        "deskripsi": (
            "Demam Berdarah Dengue (DBD) adalah penyakit infeksi yang disebabkan oleh virus Dengue "
            "yang ditularkan melalui gigitan nyamuk Aedes aegypti betina. DBD ditandai dengan "
            "demam tinggi mendadak, nyeri hebat di belakang mata, ruam kulit, dan penurunan "
            "trombosit yang dapat mengancam jiwa jika tidak ditangani segera."
        ),
        "penyebab": "Virus Dengue (DENV 1–4) yang ditularkan nyamuk Aedes aegypti.",
        "gejala_utama": ["G01", "G05", "G07", "G25", "G26", "G29"],
        "gejala_pendukung": ["G08", "G06", "G23", "G24", "G28", "G27"],
        "saran": [
            "SEGERA ke dokter atau IGD rumah sakit — DBD bisa fatal tanpa penanganan.",
            "Lakukan pemeriksaan darah lengkap (trombosit, hematokrit) setiap hari.",
            "Perbanyak minum cairan: air putih, jus jambu biji, cairan isotonik.",
            "Jangan konsumsi aspirin atau ibuprofen karena dapat memperparah perdarahan.",
            "Istirahat total dan hindari aktivitas fisik apapun.",
            "Berantas sarang nyamuk di sekitar rumah (3M Plus).",
        ],
        "warna": "#F59E0B",  # Kuning/Amber
        "icon": "fas fa-mosquito",
    },

    "P04": {
        "nama": "Radang Tenggorokan (Faringitis)",
        "deskripsi": (
            "Radang tenggorokan atau faringitis adalah peradangan pada faring (bagian belakang "
            "tenggorokan) yang dapat disebabkan oleh infeksi bakteri (umumnya Streptococcus) "
            "atau virus. Kondisi ini sangat umum dan biasanya ditandai dengan rasa sakit, "
            "gatal, atau terbakar di tenggorokan, terutama saat menelan."
        ),
        "penyebab": "Bakteri Streptococcus pyogenes atau infeksi virus (adenovirus, rhinovirus).",
        "gejala_utama": ["G16", "G17", "G18", "G19", "G02", "G30"],
        "gejala_pendukung": ["G20", "G07", "G06", "G11", "G27"],
        "saran": [
            "Berkumur dengan air garam hangat (1/2 sdt garam + 240 ml air) 3x sehari.",
            "Minum banyak cairan hangat seperti teh madu lemon atau sup kaldu.",
            "Konsumsi obat pereda nyeri tenggorokan (lozenges, parasetamol).",
            "Jika bakteri (ada bercak putih), dokter akan meresepkan antibiotik — habiskan.",
            "Hindari makanan dan minuman dingin, pedas, atau asam.",
            "Gunakan humidifier untuk menjaga kelembaban udara.",
        ],
        "warna": "#8B5CF6",  # Ungu
        "icon": "fas fa-lungs",
    },

    "P05": {
        "nama": "Asma Bronkial",
        "deskripsi": (
            "Asma bronkial adalah penyakit peradangan kronis pada saluran napas yang "
            "menyebabkan penyempitan dan pembengkakan saluran udara. Hal ini membuat "
            "penderita sulit bernapas dan memicu batuk, mengi (wheezing), dan dada sesak. "
            "Asma dapat dipicu oleh alergen, polutan udara, aktivitas fisik, atau stres."
        ),
        "penyebab": "Hipersensitivitas saluran napas dipicu alergen, polutan, infeksi, atau aktivitas fisik.",
        "gejala_utama": ["G12", "G13", "G14", "G03", "G15", "G06"],
        "gejala_pendukung": ["G04", "G07", "G11", "G16"],
        "saran": [
            "Hindari pemicu asma: debu, asap rokok, polusi, bulu hewan, serbuk bunga.",
            "Selalu bawa inhaler pelega (short-acting bronchodilator) ke mana pun.",
            "Gunakan inhaler pencegah (kortikosteroid inhalasi) secara rutin sesuai resep.",
            "Buat rencana tindakan asma bersama dokter dan ikuti dengan disiplin.",
            "Lakukan olahraga ringan dengan pemanasan yang cukup (renang disarankan).",
            "Segera ke IGD jika sesak napas berat, bibir/ujung jari membiru, atau inhaler tidak membantu.",
        ],
        "warna": "#10B981",  # Hijau
        "icon": "fas fa-wind",
    },

    "P06": {
        "nama": "Batuk Pilek (Common Cold)",
        "deskripsi": (
            "Batuk pilek atau common cold adalah infeksi virus yang sangat umum pada saluran "
            "pernapasan atas. Biasanya disebabkan oleh rhinovirus dan menyebar melalui kontak "
            "tangan atau droplet. Umumnya sembuh sendiri dalam 7–10 hari dan jarang menyebabkan "
            "komplikasi serius pada orang dewasa sehat."
        ),
        "penyebab": "Rhinovirus (penyebab tersering), coronavirus, adenovirus, RSV.",
        "gejala_utama": ["G09", "G10", "G11", "G04", "G16", "G02"],
        "gejala_pendukung": ["G03", "G06", "G07", "G20"],
        "saran": [
            "Istirahat cukup dan tidur minimal 8 jam per malam.",
            "Perbanyak minum air putih, jus jeruk (vitamin C), dan cairan hangat.",
            "Gunakan obat bebas: dekongestan nasal, antihistamin, atau pereda nyeri.",
            "Semprotkan saline nasal untuk membersihkan hidung tersumbat.",
            "Cuci tangan sering untuk mencegah penularan ke orang lain.",
            "Biasanya sembuh sendiri; konsultasi dokter jika gejala > 10 hari atau memburuk.",
        ],
        "warna": "#06B6D4",  # Cyan
        "icon": "fas fa-head-side-cough",
    },
}

# ---------------------------------------------------------------------------
# RULE BASE: Aturan forward chaining (kondisi → kesimpulan)
# Setiap rule memiliki bobot untuk akurasi scoring
# ---------------------------------------------------------------------------
RULE_BASE = [
    {
        "id": "R01",
        "penyakit_id": "P01",
        "gejala_wajib": ["G01", "G05", "G06"],        # Harus ada semua
        "gejala_pendukung": ["G03", "G07", "G08", "G04", "G09", "G10", "G16", "G23"],
        "min_pendukung": 2,                            # Minimal 2 dari pendukung
    },
    {
        "id": "R02",
        "penyakit_id": "P02",
        "gejala_wajib": ["G21", "G22"],               # Anosmia + ageusia = ciri khas COVID
        "gejala_pendukung": ["G01", "G03", "G12", "G06", "G05", "G07", "G14", "G04"],
        "min_pendukung": 2,
    },
    {
        "id": "R03",
        "penyakit_id": "P02",
        "gejala_wajib": ["G01", "G12", "G03"],
        "gejala_pendukung": ["G06", "G05", "G07", "G14", "G21", "G22", "G04", "G23"],
        "min_pendukung": 3,
    },
    {
        "id": "R04",
        "penyakit_id": "P03",
        "gejala_wajib": ["G01", "G29", "G25"],        # Demam + nyeri bola mata + ruam = DBD
        "gejala_pendukung": ["G26", "G05", "G07", "G08", "G23", "G24", "G28", "G27"],
        "min_pendukung": 2,
    },
    {
        "id": "R05",
        "penyakit_id": "P03",
        "gejala_wajib": ["G01", "G26", "G28"],
        "gejala_pendukung": ["G29", "G25", "G05", "G07", "G23", "G24"],
        "min_pendukung": 2,
    },
    {
        "id": "R06",
        "penyakit_id": "P04",
        "gejala_wajib": ["G16", "G17", "G18"],        # Sakit + nyeri menelan + amandel bengkak
        "gejala_pendukung": ["G19", "G02", "G30", "G20", "G07", "G06"],
        "min_pendukung": 2,
    },
    {
        "id": "R07",
        "penyakit_id": "P04",
        "gejala_wajib": ["G16", "G19"],               # Sakit + bercak putih = bakteri
        "gejala_pendukung": ["G17", "G18", "G02", "G07", "G30"],
        "min_pendukung": 2,
    },
    {
        "id": "R08",
        "penyakit_id": "P05",
        "gejala_wajib": ["G12", "G13"],               # Sesak + mengi = ciri khas asma
        "gejala_pendukung": ["G14", "G03", "G15", "G06", "G04", "G11"],
        "min_pendukung": 2,
    },
    {
        "id": "R09",
        "penyakit_id": "P05",
        "gejala_wajib": ["G12", "G14", "G15"],
        "gejala_pendukung": ["G13", "G03", "G06", "G04", "G07"],
        "min_pendukung": 2,
    },
    {
        "id": "R10",
        "penyakit_id": "P06",
        "gejala_wajib": ["G09", "G10", "G11"],        # Tersumbat + berair + bersin = pilek
        "gejala_pendukung": ["G04", "G16", "G02", "G03", "G06", "G07", "G20"],
        "min_pendukung": 2,
    },
    {
        "id": "R11",
        "penyakit_id": "P06",
        "gejala_wajib": ["G09", "G04", "G16"],
        "gejala_pendukung": ["G10", "G11", "G02", "G06", "G07"],
        "min_pendukung": 2,
    },
]
