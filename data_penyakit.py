# =============================================================================
# data_penyakit.py — Basis Pengetahuan Sistem Pakar (10 Penyakit)
# Sumber: WHO, Kemenkes RI, Harrison's Principles of Internal Medicine
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
    "G13": "Napas berbunyi (mengi/wheezing)",
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
    # Kulit & Perut
    "G23": "Mual dan muntah",
    "G24": "Nyeri perut / kram",
    "G25": "Ruam / bintik merah pada kulit",
    "G26": "Perdarahan gusi atau hidung",
    "G27": "Mata merah / perih",
    "G28": "Penurunan trombosit (tanda lab)",
    "G29": "Nyeri di belakang mata",
    "G30": "Kelenjar getah bening membengkak",
    # Tambahan Penyakit Baru
    "G31": "Keringat berlebih / keringat malam",
    "G32": "Penurunan berat badan drastis",
    "G33": "Batuk darah (hemoptisis)",
    "G34": "Nafsu makan menurun",
    "G35": "Diare cair / encer",
    "G36": "Lidah kotor / berselaput putih",
    "G37": "Nyeri ulu hati / epigastrium",
    "G38": "Kembung / perut terasa penuh",
    "G39": "Sendawa berlebihan",
    "G40": "Tekanan darah tinggi (> 140/90 mmHg)",
    "G41": "Sakit kepala bagian belakang / tengkuk",
    "G42": "Pusing / vertigo",
    "G43": "Detak jantung tidak teratur / berdebar",
    "G44": "Sesak napas saat beraktivitas",
    "G45": "Kulit dan mata menguning (jaundice)",
    "G46": "Urine berwarna gelap (seperti teh)",
    "G47": "Nyeri perut kanan atas",
    "G48": "Demam naik-turun (step-ladder fever)",
    "G49": "Rose spots (bintik merah pucat di perut)",
    "G50": "Konstipasi / sembelit",
}

DATA_PENYAKIT = {
    "P01": {
        "nama": "Influenza (Flu)",
        "deskripsi": (
            "Influenza adalah infeksi virus akut saluran pernapasan yang disebabkan virus "
            "Influenza A, B, atau C. Penyakit ini datang tiba-tiba dengan gejala berat "
            "seperti demam tinggi, nyeri otot hebat, dan kelelahan ekstrem."
        ),
        "penyebab": "Virus Influenza A, B, atau C (menyebar via droplet udara).",
        "gejala_utama": ["G01", "G05", "G06", "G07", "G08"],
        "gejala_pendukung": ["G03", "G04", "G09", "G10", "G16", "G23"],
        "saran": [
            "Istirahat total minimal 5–7 hari.",
            "Perbanyak minum air putih dan cairan hangat.",
            "Parasetamol untuk menurunkan demam dan meredakan nyeri.",
            "Ke dokter jika demam > 39°C lebih dari 3 hari atau sesak napas.",
            "Vaksinasi flu tahunan untuk pencegahan.",
        ],
        "warna": "#3B82F6",
        "icon": "fas fa-virus",
    },
    "P02": {
        "nama": "COVID-19",
        "deskripsi": (
            "COVID-19 disebabkan virus SARS-CoV-2. Ciri khas: hilangnya penciuman (anosmia) "
            "dan perasa (ageusia). Gejala bervariasi dari ringan hingga kritis dengan "
            "potensi komplikasi pneumonia berat."
        ),
        "penyebab": "Virus SARS-CoV-2 (droplet, aerosol, kontak langsung).",
        "gejala_utama": ["G01", "G03", "G12", "G21", "G22", "G06"],
        "gejala_pendukung": ["G05", "G07", "G14", "G23", "G04"],
        "saran": [
            "Isolasi mandiri minimal 10 hari sejak gejala pertama.",
            "Lakukan tes antigen/PCR untuk konfirmasi.",
            "Pantau saturasi oksigen — ke IGD jika SpO₂ < 94%.",
            "Konsumsi vitamin C, D, zinc sesuai anjuran dokter.",
            "Hubungi hotline COVID atau layanan telemedicine.",
        ],
        "warna": "#EF4444",
        "icon": "fas fa-biohazard",
    },
    "P03": {
        "nama": "Demam Berdarah Dengue (DBD)",
        "deskripsi": (
            "DBD disebabkan virus Dengue yang ditularkan nyamuk Aedes aegypti. "
            "Ditandai demam tinggi mendadak, nyeri hebat di belakang mata, ruam kulit, "
            "dan penurunan trombosit yang dapat mengancam jiwa."
        ),
        "penyebab": "Virus Dengue (DENV 1–4) via nyamuk Aedes aegypti.",
        "gejala_utama": ["G01", "G05", "G07", "G25", "G26", "G29"],
        "gejala_pendukung": ["G08", "G06", "G23", "G24", "G28", "G27"],
        "saran": [
            "SEGERA ke IGD — DBD bisa fatal tanpa penanganan cepat.",
            "Periksa darah lengkap (trombosit, hematokrit) setiap hari.",
            "Perbanyak minum: air putih, jus jambu biji, cairan isotonik.",
            "JANGAN konsumsi aspirin/ibuprofen (memperparah perdarahan).",
            "Berantas sarang nyamuk (3M Plus).",
        ],
        "warna": "#F59E0B",
        "icon": "fas fa-mosquito",
    },
    "P04": {
        "nama": "Radang Tenggorokan (Faringitis)",
        "deskripsi": (
            "Faringitis adalah peradangan faring akibat bakteri Streptococcus atau virus. "
            "Ditandai nyeri tenggorokan, sulit menelan, dan amandel bengkak. "
            "Bakteri Streptococcus membutuhkan antibiotik agar tuntas."
        ),
        "penyebab": "Bakteri Streptococcus pyogenes atau virus (adenovirus, rhinovirus).",
        "gejala_utama": ["G16", "G17", "G18", "G19", "G02", "G30"],
        "gejala_pendukung": ["G20", "G07", "G06", "G11", "G27"],
        "saran": [
            "Berkumur air garam hangat 3× sehari.",
            "Minum cairan hangat (teh madu lemon, sup kaldu).",
            "Jika bakteri (bercak putih), habiskan antibiotik dari dokter.",
            "Hindari makanan dingin, pedas, atau asam.",
            "Gunakan humidifier untuk menjaga kelembaban udara.",
        ],
        "warna": "#8B5CF6",
        "icon": "fas fa-lungs",
    },
    "P05": {
        "nama": "Asma Bronkial",
        "deskripsi": (
            "Asma adalah peradangan kronis saluran napas yang menyebabkan penyempitan "
            "saluran udara. Mengi (wheezing), sesak napas, dan batuk malam hari adalah "
            "tanda khas. Dipicu alergen, polutan, atau aktivitas fisik."
        ),
        "penyebab": "Hipersensitivitas saluran napas dipicu alergen, polutan, atau infeksi.",
        "gejala_utama": ["G12", "G13", "G14", "G03", "G15", "G06"],
        "gejala_pendukung": ["G04", "G07", "G11", "G16"],
        "saran": [
            "Hindari pemicu: debu, asap rokok, polusi, bulu hewan.",
            "Selalu bawa inhaler pelega (bronchodilator).",
            "Gunakan inhaler pencegah (kortikosteroid) rutin.",
            "Ke IGD jika sesak berat, bibir membiru, atau inhaler tidak membantu.",
            "Renang adalah olahraga yang direkomendasikan untuk penderita asma.",
        ],
        "warna": "#10B981",
        "icon": "fas fa-wind",
    },
    "P06": {
        "nama": "Batuk Pilek (Common Cold)",
        "deskripsi": (
            "Common cold adalah infeksi virus ringan pada saluran pernapasan atas, "
            "umumnya disebabkan rhinovirus. Menyebar via kontak tangan atau droplet. "
            "Biasanya sembuh sendiri dalam 7–10 hari."
        ),
        "penyebab": "Rhinovirus (tersering), coronavirus, adenovirus, RSV.",
        "gejala_utama": ["G09", "G10", "G11", "G04", "G16", "G02"],
        "gejala_pendukung": ["G03", "G06", "G07", "G20"],
        "saran": [
            "Istirahat cukup dan tidur minimal 8 jam.",
            "Perbanyak minum air putih dan jus jeruk (vitamin C).",
            "Gunakan dekongestan nasal atau antihistamin.",
            "Cuci tangan sering untuk mencegah penularan.",
            "Konsultasi dokter jika gejala > 10 hari atau memburuk.",
        ],
        "warna": "#06B6D4",
        "icon": "fas fa-head-side-cough",
    },
    "P07": {
        "nama": "Tuberkulosis (TBC)",
        "deskripsi": (
            "TBC adalah penyakit infeksi bakteri kronis yang terutama menyerang paru-paru. "
            "Disebabkan Mycobacterium tuberculosis dan menyebar lewat udara. "
            "Ditandai batuk kronik > 2 minggu, keringat malam, dan penurunan berat badan."
        ),
        "penyebab": "Bakteri Mycobacterium tuberculosis (aerosol/droplet).",
        "gejala_utama": ["G03", "G33", "G31", "G32", "G06", "G34"],
        "gejala_pendukung": ["G01", "G04", "G12", "G07", "G08", "G30"],
        "saran": [
            "Segera ke dokter untuk pemeriksaan dahak (BTA) dan foto rontgen.",
            "Jalani pengobatan OAT (Obat Anti Tuberkulosis) minimal 6 bulan.",
            "JANGAN berhenti minum OAT sebelum selesai — cegah resistensi.",
            "Gunakan masker dan ventilasi rumah yang baik.",
            "Anggota keluarga serumah perlu diperiksa (kontak tracing).",
        ],
        "warna": "#DC2626",
        "icon": "fas fa-bacterium",
    },
    "P08": {
        "nama": "Pneumonia",
        "deskripsi": (
            "Pneumonia adalah infeksi yang menyebabkan peradangan pada kantung udara (alveoli) "
            "di paru-paru. Bisa disebabkan bakteri, virus, atau jamur. Gejalanya mirip flu "
            "namun lebih berat dengan sesak napas dan nyeri dada signifikan."
        ),
        "penyebab": "Streptococcus pneumoniae (tersering), virus (influenza, COVID-19), jamur.",
        "gejala_utama": ["G01", "G04", "G12", "G14", "G06", "G08"],
        "gejala_pendukung": ["G03", "G05", "G07", "G23", "G27"],
        "saran": [
            "Segera ke dokter — pneumonia membutuhkan antibiotik/antiviral.",
            "Foto rontgen dada diperlukan untuk konfirmasi diagnosis.",
            "Istirahat total dan hindari aktivitas fisik.",
            "Perbanyak minum cairan untuk mencegah dehidrasi.",
            "Rawat inap diperlukan jika saturasi oksigen < 95% atau gejala berat.",
        ],
        "warna": "#7C3AED",
        "icon": "fas fa-lungs-virus",
    },
    "P09": {
        "nama": "Tifoid (Demam Tifus)",
        "deskripsi": (
            "Tifoid disebabkan bakteri Salmonella typhi yang ditularkan melalui makanan/air "
            "yang terkontaminasi. Ciri khas: demam naik bertahap (step-ladder fever), "
            "lidah kotor berselaput, dan gangguan pencernaan."
        ),
        "penyebab": "Bakteri Salmonella typhi (fecal-oral, makanan/air terkontaminasi).",
        "gejala_utama": ["G48", "G36", "G01", "G06", "G34"],
        "gejala_pendukung": ["G23", "G24", "G35", "G50", "G49", "G07", "G08"],
        "saran": [
            "Periksakan diri ke dokter untuk tes Widal atau kultur darah.",
            "Konsumsi antibiotik (kloramfenikol/siprofloksasin) sesuai resep dokter.",
            "Istirahat total dan makan makanan lunak mudah dicerna.",
            "Hindari makanan pedas, berserat, dan berlemak.",
            "Jaga kebersihan tangan dan sanitasi makanan/minuman.",
        ],
        "warna": "#D97706",
        "icon": "fas fa-disease",
    },
    "P10": {
        "nama": "Gastritis (Maag)",
        "deskripsi": (
            "Gastritis adalah peradangan pada lapisan lambung yang disebabkan infeksi "
            "H. pylori, penggunaan NSAID, atau pola makan buruk. Ditandai nyeri ulu hati, "
            "kembung, dan mual yang memburuk saat perut kosong."
        ),
        "penyebab": "Helicobacter pylori, NSAID (ibuprofen/aspirin), stres, alkohol.",
        "gejala_utama": ["G37", "G38", "G23", "G39", "G24"],
        "gejala_pendukung": ["G34", "G06", "G07", "G02"],
        "saran": [
            "Makan teratur dan hindari perut kosong terlalu lama.",
            "Hindari makanan pedas, asam, berlemak, dan minuman berkafein.",
            "Konsumsi antasida sesuai petunjuk untuk meredakan nyeri.",
            "Ke dokter untuk pemeriksaan H. pylori jika gejala berulang.",
            "Kelola stres dengan olahraga teratur dan istirahat cukup.",
        ],
        "warna": "#059669",
        "icon": "fas fa-stomach",
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

    # --- P03: DBD ---
    {"id": "R04", "penyakit_id": "P03",
     "gejala_wajib": ["G01", "G29", "G25"],
     "gejala_pendukung": ["G26", "G05", "G07", "G08", "G23", "G24", "G28", "G27"],
     "min_pendukung": 2},
    {"id": "R05", "penyakit_id": "P03",
     "gejala_wajib": ["G01", "G26", "G28"],
     "gejala_pendukung": ["G29", "G25", "G05", "G07", "G23", "G24"],
     "min_pendukung": 2},

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

    # --- P09: Tifoid ---
    {"id": "R16", "penyakit_id": "P09",
     "gejala_wajib": ["G48", "G36", "G06"],
     "gejala_pendukung": ["G01", "G34", "G23", "G24", "G35", "G50", "G07"],
     "min_pendukung": 2},
    {"id": "R17", "penyakit_id": "P09",
     "gejala_wajib": ["G01", "G36", "G34"],
     "gejala_pendukung": ["G48", "G06", "G23", "G24", "G35", "G49", "G08"],
     "min_pendukung": 3},

    # --- P10: Gastritis ---
    {"id": "R18", "penyakit_id": "P10",
     "gejala_wajib": ["G37", "G38", "G23"],
     "gejala_pendukung": ["G39", "G24", "G34", "G06", "G02"],
     "min_pendukung": 2},
    {"id": "R19", "penyakit_id": "P10",
     "gejala_wajib": ["G37", "G39"],
     "gejala_pendukung": ["G38", "G23", "G24", "G34", "G06"],
     "min_pendukung": 2},
]
