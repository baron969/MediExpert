# =============================================================================
# metode.py — Forward Chaining Engine
# Sistem Pakar Diagnosa Penyakit — MediExpert
# =============================================================================

from data_penyakit import DATA_PENYAKIT, RULE_BASE, SEMUA_GEJALA


# ---------------------------------------------------------------------------
# KATEGORI GEJALA untuk tampilan UI (dikelompokkan)
# ---------------------------------------------------------------------------
KATEGORI_GEJALA = {
    "Gejala Umum": ["G01", "G02", "G05", "G06", "G07", "G08", "G31", "G32", "G34"],
    "Gejala Pernapasan": ["G03", "G04", "G09", "G10", "G11", "G12", "G13", "G14", "G15", "G33"],
    "Tenggorokan & Indra": ["G16", "G17", "G18", "G19", "G20", "G21", "G22", "G30"],
    "Pencernaan & Perut": ["G23", "G24", "G35", "G36", "G37", "G38", "G39", "G50"],
    "Kulit & Lainnya": ["G25", "G26", "G27", "G28", "G29", "G40", "G41", "G42", "G43", "G44", "G45", "G46", "G47", "G48", "G49"],
}


def get_semua_gejala_terformat() -> list:
    """Kembalikan daftar gejala terkelompok untuk ditampilkan di form UI."""
    result = []
    for kategori, gejala_ids in KATEGORI_GEJALA.items():
        gejala_list = []
        for gid in gejala_ids:
            if gid in SEMUA_GEJALA:
                gejala_list.append({"id": gid, "nama": SEMUA_GEJALA[gid]})
        if gejala_list:
            result.append({"kategori": kategori, "gejala": gejala_list})
    return result


# ---------------------------------------------------------------------------
# FORWARD CHAINING ENGINE
# ---------------------------------------------------------------------------

def hitung_skor_rule(rule: dict, gejala_pasien: set) -> dict:
    """
    Hitung skor kecocokan satu rule terhadap gejala pasien.

    Scoring:
    - Gejala wajib: bobot 60% dari total skor (harus terpenuhi semua)
    - Gejala pendukung: bobot 40% dari total skor
    """
    gejala_wajib     = set(rule["gejala_wajib"])
    gejala_pendukung = set(rule.get("gejala_pendukung", []))
    min_pendukung    = rule.get("min_pendukung", 1)

    # Cek apakah semua gejala wajib terpenuhi
    wajib_terpenuhi = gejala_wajib.issubset(gejala_pasien)
    if not wajib_terpenuhi:
        return {"cocok": False, "skor": 0.0}

    # Hitung gejala pendukung yang cocok
    pendukung_cocok = gejala_pendukung & gejala_pasien
    if len(pendukung_cocok) < min_pendukung:
        return {"cocok": False, "skor": 0.0}

    # Skor komponen wajib (60%)
    skor_wajib = 0.60

    # Skor komponen pendukung (40%), proporsional
    if gejala_pendukung:
        rasio_pendukung = len(pendukung_cocok) / len(gejala_pendukung)
    else:
        rasio_pendukung = 1.0
    skor_pendukung = 0.40 * rasio_pendukung

    skor_total = (skor_wajib + skor_pendukung) * 100  # dalam persen

    return {
        "cocok": True,
        "skor": round(skor_total, 2),
        "wajib_cocok": list(gejala_wajib),
        "pendukung_cocok": list(pendukung_cocok),
    }


def forward_chaining(gejala_ids: list) -> dict:
    """
    Jalankan algoritma Forward Chaining.

    Args:
        gejala_ids: List ID gejala yang dipilih pasien (e.g. ["G01", "G05"])

    Returns:
        dict berisi diagnosa_utama, kemungkinan_lain, gejala_tidak_cocok
    """
    gejala_pasien = set(gejala_ids)
    skor_penyakit: dict = {}  # penyakit_id -> skor tertinggi

    for rule in RULE_BASE:
        hasil = hitung_skor_rule(rule, gejala_pasien)
        if hasil["cocok"]:
            pid = rule["penyakit_id"]
            # Ambil skor tertinggi jika ada beberapa rule untuk penyakit yang sama
            if pid not in skor_penyakit or hasil["skor"] > skor_penyakit[pid]["skor"]:
                skor_penyakit[pid] = {
                    "penyakit_id": pid,
                    **hasil,
                    **DATA_PENYAKIT[pid],
                }

    # Urutkan dari skor tertinggi
    ranking = sorted(skor_penyakit.values(), key=lambda x: x["skor"], reverse=True)

    # Tentukan gejala yang tidak cocok dengan penyakit manapun
    semua_gejala_rules: set = set()
    for rule in RULE_BASE:
        semua_gejala_rules.update(rule["gejala_wajib"])
        semua_gejala_rules.update(rule.get("gejala_pendukung", []))
    gejala_tidak_cocok = [
        SEMUA_GEJALA.get(g, g)
        for g in gejala_pasien
        if g not in semua_gejala_rules
    ]

    if not ranking:
        return {
            "diagnosa_utama": None,
            "kemungkinan_lain": [],
            "gejala_dipilih": [SEMUA_GEJALA.get(g, g) for g in gejala_ids],
            "gejala_tidak_cocok": gejala_tidak_cocok,
            "total_gejala_dipilih": len(gejala_ids),
        }

    # Diagnosa utama: skor >= 75%
    THRESHOLD_UTAMA = 75.0
    diagnosa_utama  = ranking[0] if ranking[0]["skor"] >= THRESHOLD_UTAMA else None
    kemungkinan     = [r for r in ranking if r["skor"] < THRESHOLD_UTAMA]

    if diagnosa_utama:
        kemungkinan = [r for r in ranking[1:] if r["skor"] >= 40.0]
    else:
        kemungkinan = [r for r in ranking if r["skor"] >= 40.0]

    return {
        "diagnosa_utama": diagnosa_utama,
        "kemungkinan_lain": kemungkinan[:3],
        "gejala_dipilih": [SEMUA_GEJALA.get(g, g) for g in gejala_ids],
        "gejala_tidak_cocok": gejala_tidak_cocok,
        "total_gejala_dipilih": len(gejala_ids),
        "semua_hasil": ranking,
    }
