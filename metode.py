from data_penyakit import DATA_PENYAKIT, SEMUA_GEJALA


# ---------------------------------------------------------------------------
# Tingkat keyakinan pengguna (CF User)
# ---------------------------------------------------------------------------
KEYAKINAN_USER = {
    "tidak_tahu": 0.0,
    "mungkin": 0.4,
    "kemungkinan_besar": 0.7,
    "pasti_ya": 1.0,
}


def get_label_keyakinan(cf: float) -> str:
    for label, val in KEYAKINAN_USER.items():
        if abs(val - cf) < 0.01:
            return label.replace("_", " ").title()
    return "Tidak Tahu"


# ---------------------------------------------------------------------------
# Helper kombinasi CF berurutan (semua CF positif)
# CF_combine(cf1, cf2) = cf1 + cf2 * (1 - cf1)
# ---------------------------------------------------------------------------
def cf_combine_sequential(cf_values: list) -> float:
    if not cf_values:
        return 0.0
    result = cf_values[0]
    for cf in cf_values[1:]:
        result = result + cf * (1 - result)
    return result


# ---------------------------------------------------------------------------
# Format gejala ber-kategori untuk UI
# ---------------------------------------------------------------------------
def get_semua_gejala_terformat() -> list:
    kategori = {
        "Umum & Demam": ["G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08", "G09"],
        "Pernapasan Utama": ["G10", "G11", "G12", "G13", "G14", "G15", "G16", "G17", "G18", "G19"],
        "Hidung & Tenggorokan": ["G20", "G21", "G22", "G23", "G24", "G25", "G26", "G27"],
        "Lainnya": ["G30", "G31", "G32", "G33", "G34"],
    }

    hasil = []
    for kat_nama, ids in kategori.items():
        gejala_kat = []
        for gid in ids:
            if gid in SEMUA_GEJALA:
                gejala_kat.append({"id": gid, "nama": SEMUA_GEJALA[gid]})
        hasil.append({"kategori": kat_nama, "gejala": gejala_kat})

    return hasil


# ---------------------------------------------------------------------------
# Certainty Factor Method — Diagnosa berbasis CF
# ---------------------------------------------------------------------------
def certainty_factor_method(
    gejala_dipilih: dict, umur: int = None, jenis_kelamin: str = None
) -> dict:
    """
    gejala_dipilih: {kode_gejala: cf_user, ...}
    cf_user adalah nilai keyakinan pengguna (0.0, 0.4, 0.7, atau 1.0)

    Untuk setiap penyakit:
      1. Cocokkan gejala yang dipilih dengan daftar gejala penyakit
      2. Hitung CF tiap kecocokan: CF_expert × CF_user
      3. Gabungkan semua CF secara sekuensial
      4. Konversi ke persentase untuk ditampilkan
    """
    hasil_penyakit = []

    for pid, p_data in DATA_PENYAKIT.items():
        cf_list = []
        gejala_cocok_utama = []
        gejala_cocok_pendukung = []

        # Gabung utama + pendukung jadi satu untuk pengecekan
        semua_gejala_penyakit = []
        for gid, cf_expert in p_data["gejala_utama"]:
            semua_gejala_penyakit.append((gid, cf_expert, True))
        for gid, cf_expert in p_data["gejala_pendukung"]:
            semua_gejala_penyakit.append((gid, cf_expert, False))

        for gid, cf_expert, is_utama in semua_gejala_penyakit:
            if gid in gejala_dipilih:
                cf_user = gejala_dipilih[gid]
                cf_combined = cf_expert * cf_user
                if cf_combined > 0:
                    cf_list.append(cf_combined)
                    nama_gejala = SEMUA_GEJALA.get(gid, gid)
                    if is_utama:
                        gejala_cocok_utama.append(nama_gejala)
                    else:
                        gejala_cocok_pendukung.append(nama_gejala)

        if not cf_list:
            continue

        cf_total = cf_combine_sequential(cf_list)
        skor_persen = round(cf_total * 100, 1)

        hasil_penyakit.append({
            "id": pid,
            "nama": p_data["nama"],
            "deskripsi": p_data["deskripsi"],
            "penyebab": p_data["penyebab"],
            "saran": p_data["saran"],
            "icon": p_data["icon"],
            "warna": p_data["warna"],
            "skor": skor_persen,
            "cf": round(cf_total, 4),
            "gejala_cocok_utama": gejala_cocok_utama,
            "gejala_cocok_pendukung": gejala_cocok_pendukung,
        })

    # Urutkan berdasarkan CF tertinggi
    hasil_penyakit = sorted(hasil_penyakit, key=lambda x: x["cf"], reverse=True)

    # Thresholds:
    # CF >= 0.40 (40%) → Diagnosa Utama
    # CF >= 0.10 (10%) → Kemungkinan Lain
    diagnosa_utama = None
    kemungkinan_lain = []

    for hp in hasil_penyakit:
        if hp["cf"] >= 0.40 and diagnosa_utama is None:
            diagnosa_utama = hp
        elif hp["cf"] >= 0.10:
            if len(kemungkinan_lain) < 2:
                kemungkinan_lain.append(hp)

    # Buat detail gejala dengan keyakinan user
    gejala_detail = []
    for gid, cf_user in gejala_dipilih.items():
        gejala_detail.append({
            "id": gid,
            "nama": SEMUA_GEJALA.get(gid, gid),
            "keyakinan": cf_user,
            "label_keyakinan": get_label_keyakinan(cf_user),
        })

    return {
        "gejala_terpilih": list(gejala_dipilih.keys()),
        "gejala_terpilih_detail": gejala_detail,
        "total_gejala": len(gejala_dipilih),
        "diagnosa_utama": diagnosa_utama,
        "kemungkinan_lain": kemungkinan_lain,
        "tidak_terdiagnosa": not diagnosa_utama and not kemungkinan_lain,
    }
