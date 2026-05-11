# =============================================================================
# data_penyakit.py — Basis Pengetahuan Sistem Pakar (Pernapasan)
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

DATA_PENYAKIT = {
    "P01": {
        "nama": "Influenza (Flu)",
        "deskripsi": "Influenza adalah infeksi virus akut saluran pernapasan. Penyakit ini datang tiba-tiba dengan gejala berat seperti demam tinggi, nyeri otot hebat, dan kelelahan.",
        "penyebab": "Virus Influenza A, B, atau C.",
        "gejala_utama": ["G01", "G05", "G06", "G07", "G08"],
        "gejala_pendukung": ["G03", "G04", "G09", "G10", "G16", "G23"],
        "saran": [
            "Istirahat total minimal 5–7 hari.",
            "Perbanyak minum air putih dan cairan hangat.",
            "Parasetamol untuk menurunkan demam dan meredakan nyeri.",
            "Ke dokter jika demam > 39°C lebih dari 3 hari atau sesak napas."
        ],
        "warna": "#3B82F6",
        "icon": "fas fa-virus",
    },
    "P02": {
        "nama": "COVID-19",
        "deskripsi": "COVID-19 disebabkan virus SARS-CoV-2. Ciri khas: hilangnya penciuman (anosmia) dan perasa (ageusia).",
        "penyebab": "Virus SARS-CoV-2.",
        "gejala_utama": ["G01", "G03", "G12", "G21", "G22", "G06"],
        "gejala_pendukung": ["G05", "G07", "G14", "G23", "G04"],
        "saran": [
            "Isolasi mandiri minimal 10 hari sejak gejala pertama.",
            "Lakukan tes antigen/PCR untuk konfirmasi.",
            "Pantau saturasi oksigen — ke IGD jika SpO₂ < 94%.",
            "Konsumsi vitamin C, D, zinc sesuai anjuran dokter."
        ],
        "warna": "#EF4444",
        "icon": "fas fa-biohazard",
    },
    "P04": {
        "nama": "Radang Tenggorokan (Faringitis)",
        "deskripsi": "Peradangan faring akibat bakteri Streptococcus atau virus. Ditandai nyeri tenggorokan dan amandel bengkak.",
        "penyebab": "Bakteri Streptococcus pyogenes atau virus.",
        "gejala_utama": ["G16", "G17", "G18", "G19", "G02", "G30"],
        "gejala_pendukung": ["G20", "G07", "G06", "G11", "G27"],
        "saran": [
            "Berkumur air garam hangat 3× sehari.",
            "Minum cairan hangat (teh madu lemon, sup kaldu).",
            "Jika karena bakteri, habiskan antibiotik dari dokter."
        ],
        "warna": "#8B5CF6",
        "icon": "fas fa-lungs",
    },
    "P05": {
        "nama": "Asma Bronkial",
        "deskripsi": "Asma adalah peradangan kronis yang menyebabkan penyempitan saluran udara. Mengi dan sesak napas adalah tanda khas.",
        "penyebab": "Hipersensitivitas saluran napas dipicu alergen/polutan.",
        "gejala_utama": ["G12", "G13", "G14", "G03", "G15", "G06"],
        "gejala_pendukung": ["G04", "G07", "G11", "G16"],
        "saran": [
            "Hindari pemicu: debu, asap rokok, polusi, bulu hewan.",
            "Selalu bawa inhaler pelega (bronchodilator).",
            "Gunakan inhaler pencegah rutin.",
            "Ke IGD jika sesak berat atau inhaler tidak membantu."
        ],
        "warna": "#10B981",
        "icon": "fas fa-wind",
    },
    "P06": {
        "nama": "Batuk Pilek (Common Cold)",
        "deskripsi": "Infeksi virus ringan pada saluran pernapasan atas. Biasanya sembuh sendiri dalam 7–10 hari.",
        "penyebab": "Rhinovirus, adenovirus.",
        "gejala_utama": ["G09", "G10", "G11", "G04", "G16", "G02"],
        "gejala_pendukung": ["G03", "G06", "G07", "G20"],
        "saran": [
            "Istirahat cukup dan tidur minimal 8 jam.",
            "Perbanyak minum air putih dan jus jeruk.",
            "Gunakan dekongestan nasal jika perlu."
        ],
        "warna": "#06B6D4",
        "icon": "fas fa-head-side-cough",
    },
    "P07": {
        "nama": "Tuberkulosis (TBC)",
        "deskripsi": "Penyakit infeksi bakteri kronis paru-paru. Ditandai batuk > 2 minggu, keringat malam, dan berat badan turun.",
        "penyebab": "Bakteri Mycobacterium tuberculosis.",
        "gejala_utama": ["G03", "G33", "G31", "G32", "G06", "G34"],
        "gejala_pendukung": ["G01", "G04", "G12", "G07", "G08", "G30"],
        "saran": [
            "Segera ke dokter untuk pemeriksaan dahak (BTA) dan rontgen.",
            "Jalani pengobatan OAT minimal 6 bulan tanpa henti.",
            "Gunakan masker dan pastikan ventilasi rumah baik."
        ],
        "warna": "#DC2626",
        "icon": "fas fa-bacterium",
    },
    "P08": {
        "nama": "Pneumonia",
        "deskripsi": "Peradangan pada kantung udara (alveoli) paru-paru akibat infeksi. Gejalanya berat dengan sesak napas signifikan.",
        "penyebab": "Bakteri (Streptococcus pneumoniae), virus, atau jamur.",
        "gejala_utama": ["G01", "G04", "G12", "G14", "G06", "G08"],
        "gejala_pendukung": ["G03", "G05", "G07", "G23", "G27"],
        "saran": [
            "Segera ke dokter — pneumonia membutuhkan antibiotik/antiviral.",
            "Foto rontgen dada diperlukan untuk konfirmasi.",
            "Rawat inap diperlukan jika gejala berat."
        ],
        "warna": "#7C3AED",
        "icon": "fas fa-lungs-virus",
    },
}

RULE_BASE = [
    # --- P01: Influenza ---
    {"id": "R01", "penyakit_id": "P01",
     "gejala_wajib": ["G01", "G05", "G06"],
     "gejala_pendukung": ["G03", "G07", "G08", "G04", "G09", "G10", "G16", "G23"],
     "min_pendukung": 2},

    # --- P02: COVID-19 ---
    {"id": "R02", "penyakit_id": "P02",
     "gejala_wajib": ["G21", "G22"],
     "gejala_pendukung": ["G01", "G03", "G12", "G06", "G05", "G07", "G14", "G04"],
     "min_pendukung": 2},
    {"id": "R03", "penyakit_id": "P02",
     "gejala_wajib": ["G01", "G12", "G03"],
     "gejala_pendukung": ["G06", "G05", "G07", "G14", "G21", "G22", "G04", "G23"],
     "min_pendukung": 3},

    # --- P04: Faringitis ---
    {"id": "R06", "penyakit_id": "P04",
     "gejala_wajib": ["G16", "G17", "G18"],
     "gejala_pendukung": ["G19", "G02", "G30", "G20", "G07", "G06"],
     "min_pendukung": 2},
    {"id": "R07", "penyakit_id": "P04",
     "gejala_wajib": ["G16", "G19"],
     "gejala_pendukung": ["G17", "G18", "G02", "G07", "G30"],
     "min_pendukung": 2},

    # --- P05: Asma ---
    {"id": "R08", "penyakit_id": "P05",
     "gejala_wajib": ["G12", "G13"],
     "gejala_pendukung": ["G14", "G03", "G15", "G06", "G04", "G11"],
     "min_pendukung": 2},
    {"id": "R09", "penyakit_id": "P05",
     "gejala_wajib": ["G12", "G14", "G15"],
     "gejala_pendukung": ["G13", "G03", "G06", "G04", "G07"],
     "min_pendukung": 2},

    # --- P06: Common Cold ---
    {"id": "R10", "penyakit_id": "P06",
     "gejala_wajib": ["G09", "G10", "G11"],
     "gejala_pendukung": ["G04", "G16", "G02", "G03", "G06", "G07", "G20"],
     "min_pendukung": 2},
    {"id": "R11", "penyakit_id": "P06",
     "gejala_wajib": ["G09", "G04", "G16"],
     "gejala_pendukung": ["G10", "G11", "G02", "G06", "G07"],
     "min_pendukung": 2},

    # --- P07: TBC ---
    {"id": "R12", "penyakit_id": "P07",
     "gejala_wajib": ["G03", "G31", "G32"],
     "gejala_pendukung": ["G33", "G34", "G06", "G01", "G04", "G30"],
     "min_pendukung": 2},
    {"id": "R13", "penyakit_id": "P07",
     "gejala_wajib": ["G33", "G06", "G34"],
     "gejala_pendukung": ["G03", "G31", "G32", "G01", "G12", "G08"],
     "min_pendukung": 2},

    # --- P08: Pneumonia ---
    {"id": "R14", "penyakit_id": "P08",
     "gejala_wajib": ["G01", "G04", "G12"],
     "gejala_pendukung": ["G14", "G06", "G08", "G03", "G05", "G07"],
     "min_pendukung": 2},
    {"id": "R15", "penyakit_id": "P08",
     "gejala_wajib": ["G01", "G14", "G06"],
     "gejala_pendukung": ["G04", "G12", "G08", "G03", "G23"],
     "min_pendukung": 3},
]
