# =============================================================================
# metode.py
# Implementasi algoritma Forward Chaining untuk Sistem Pakar Diagnosa Penyakit
# =============================================================================
#
# KONSEP FORWARD CHAINING:
# Forward Chaining (Penalaran Maju) adalah strategi inferensi yang dimulai dari
# fakta-fakta yang diketahui (gejala yang dipilih pengguna) kemudian secara
# sistematis menerapkan aturan (rules) untuk menyimpulkan fakta baru hingga
# mencapai suatu kesimpulan (diagnosa penyakit).
#
# Alur:
#   Fakta (Gejala) → Mesin Inferensi → Evaluasi Rule → Kesimpulan (Diagnosa)
#
# =============================================================================

from data_penyakit import RULE_BASE, DATA_PENYAKIT, SEMUA_GEJALA


def forward_chaining(gejala_terpilih: list) -> dict:
    """
    Fungsi utama Forward Chaining Sistem Pakar.

    Proses:
    1. Inisialisasi working memory dengan fakta (gejala yang dipilih user)
    2. Evaluasi setiap rule dalam rule base terhadap working memory
    3. Hitung skor kecocokan setiap penyakit
    4. Kembalikan hasil diagnosa terurut berdasarkan persentase kecocokan

    Args:
        gejala_terpilih (list): Daftar ID gejala yang dipilih pengguna (e.g. ["G01", "G03"])

    Returns:
        dict: Hasil diagnosa berisi:
              - diagnosa_utama: Penyakit dengan kecocokan tertinggi (jika lolos threshold)
              - kemungkinan_lain: Penyakit dengan kecocokan 30-70%
              - semua_hasil: Seluruh hasil evaluasi terurut
              - gejala_terpilih_detail: Detail gejala yang dipilih
              - total_gejala: Jumlah gejala yang dipilih
    """

    # -------------------------------------------------------------------------
    # LANGKAH 1: Inisialisasi Working Memory
    # Working memory berisi semua fakta yang diketahui (gejala yang dipilih user)
    # -------------------------------------------------------------------------
    working_memory = set(gejala_terpilih)
    gejala_count = len(working_memory)

    if gejala_count == 0:
        return {
            "error": "Tidak ada gejala yang dipilih.",
            "diagnosa_utama": None,
            "kemungkinan_lain": [],
            "semua_hasil": [],
            "gejala_terpilih_detail": [],
            "total_gejala": 0,
        }

    # -------------------------------------------------------------------------
    # LANGKAH 2: Evaluasi Setiap Rule (Forward Chaining Inference Engine)
    # Mesin inferensi akan memeriksa setiap rule:
    #   - Apakah semua gejala WAJIB terpenuhi? (kondisi AND)
    #   - Berapa banyak gejala PENDUKUNG yang cocok?
    # -------------------------------------------------------------------------
    skor_penyakit = {}  # { penyakit_id: skor_tertinggi }
    detail_cocok  = {}  # { penyakit_id: { detail rule yang cocok } }

    for rule in RULE_BASE:
        penyakit_id     = rule["penyakit_id"]
        gejala_wajib    = set(rule["gejala_wajib"])
        gejala_dukung   = set(rule["gejala_pendukung"])
        min_pendukung   = rule["min_pendukung"]

        # --- Cek apakah SEMUA gejala wajib ada di working memory ---
        wajib_terpenuhi = gejala_wajib.issubset(working_memory)
        if not wajib_terpenuhi:
            continue  # Rule tidak aktif → lewati

        # --- Hitung gejala pendukung yang cocok ---
        cocok_pendukung = gejala_dukung & working_memory
        jumlah_pendukung_cocok = len(cocok_pendukung)

        # --- Cek apakah syarat minimum pendukung terpenuhi ---
        if jumlah_pendukung_cocok < min_pendukung:
            continue  # Rule tidak cukup kuat → lewati

        # ---------------------------------------------------------------
        # LANGKAH 3: Hitung Skor Kecocokan
        # Skor dihitung berdasarkan:
        #   - Persentase gejala wajib (bobot 60%)
        #   - Persentase gejala pendukung (bobot 40%)
        # ---------------------------------------------------------------
        total_gejala_rule = len(gejala_wajib) + len(gejala_dukung)
        total_gejala_cocok = len(gejala_wajib) + jumlah_pendukung_cocok

        # Komponen skor gejala wajib (selalu 100% jika rule aktif)
        skor_wajib = (len(gejala_wajib) / len(gejala_wajib)) * 60

        # Komponen skor gejala pendukung
        skor_dukung = (jumlah_pendukung_cocok / max(len(gejala_dukung), 1)) * 40

        skor_total = round(skor_wajib + skor_dukung, 2)

        # Jika penyakit sudah ada, simpan skor tertinggi
        if penyakit_id not in skor_penyakit or skor_total > skor_penyakit[penyakit_id]:
            skor_penyakit[penyakit_id] = skor_total
            detail_cocok[penyakit_id] = {
                "rule_id"               : rule["id"],
                "gejala_wajib_cocok"    : list(gejala_wajib),
                "gejala_pendukung_cocok": list(cocok_pendukung),
                "gejala_tidak_cocok"    : list(gejala_dukung - working_memory),
                "jumlah_wajib"          : len(gejala_wajib),
                "jumlah_pendukung_cocok": jumlah_pendukung_cocok,
                "jumlah_pendukung_total": len(gejala_dukung),
            }

    # -------------------------------------------------------------------------
    # LANGKAH 4: Normalisasi & Penentuan Kategori Diagnosa
    # Urutkan penyakit berdasarkan skor kecocokan (tertinggi ke terendah)
    # -------------------------------------------------------------------------
    hasil_terurut = sorted(skor_penyakit.items(), key=lambda x: x[1], reverse=True)

    semua_hasil = []
    for penyakit_id, skor in hasil_terurut:
        info = DATA_PENYAKIT.get(penyakit_id, {})
        detail = detail_cocok.get(penyakit_id, {})

        # Resolusi nama gejala dari ID
        wajib_nama    = [SEMUA_GEJALA[g] for g in detail.get("gejala_wajib_cocok", []) if g in SEMUA_GEJALA]
        dukung_nama   = [SEMUA_GEJALA[g] for g in detail.get("gejala_pendukung_cocok", []) if g in SEMUA_GEJALA]
        tidakcocok_nm = [SEMUA_GEJALA[g] for g in detail.get("gejala_tidak_cocok", []) if g in SEMUA_GEJALA]

        semua_hasil.append({
            "penyakit_id"           : penyakit_id,
            "nama"                  : info.get("nama", ""),
            "deskripsi"             : info.get("deskripsi", ""),
            "penyebab"              : info.get("penyebab", ""),
            "saran"                 : info.get("saran", []),
            "warna"                 : info.get("warna", "#6B7280"),
            "icon"                  : info.get("icon", "fas fa-notes-medical"),
            "skor"                  : skor,
            "rule_id"               : detail.get("rule_id", ""),
            "gejala_wajib_cocok"    : wajib_nama,
            "gejala_pendukung_cocok": dukung_nama,
            "gejala_tidak_cocok"    : tidakcocok_nm,
            "jumlah_wajib"          : detail.get("jumlah_wajib", 0),
            "jumlah_pendukung_cocok": detail.get("jumlah_pendukung_cocok", 0),
            "jumlah_pendukung_total": detail.get("jumlah_pendukung_total", 0),
        })

    # Klasifikasi hasil
    diagnosa_utama    = None
    kemungkinan_lain  = []
    tidak_terdiagnosa = len(semua_hasil) == 0

    if semua_hasil:
        top = semua_hasil[0]
        if top["skor"] >= 70:
            diagnosa_utama = top
            kemungkinan_lain = [h for h in semua_hasil[1:] if h["skor"] >= 40]
        elif top["skor"] >= 40:
            # Tidak cukup yakin → semua jadi kemungkinan
            kemungkinan_lain = semua_hasil
        else:
            tidak_terdiagnosa = True

    # Detail gejala yang dipilih user
    gejala_terpilih_detail = [
        {"id": gid, "nama": SEMUA_GEJALA.get(gid, gid)}
        for gid in sorted(gejala_terpilih)
        if gid in SEMUA_GEJALA
    ]

    return {
        "diagnosa_utama"       : diagnosa_utama,
        "kemungkinan_lain"     : kemungkinan_lain,
        "semua_hasil"          : semua_hasil,
        "gejala_terpilih_detail": gejala_terpilih_detail,
        "total_gejala"         : gejala_count,
        "tidak_terdiagnosa"    : tidak_terdiagnosa,
        "error"                : None,
    }


def get_semua_gejala_terformat() -> list:
    """
    Mengembalikan daftar semua gejala yang diformat untuk form checklist.
    Mengelompokkan gejala berdasarkan kategori.
    """
    from data_penyakit import SEMUA_GEJALA

    kategori = {
        "Gejala Umum": {
            "icon" : "fas fa-thermometer-half",
            "warna": "#F59E0B",
            "gejala": {k: v for k, v in SEMUA_GEJALA.items() if k in
                       ["G01","G02","G03","G04","G05","G06","G07","G08"]},
        },
        "Gejala Pernapasan": {
            "icon" : "fas fa-lungs",
            "warna": "#3B82F6",
            "gejala": {k: v for k, v in SEMUA_GEJALA.items() if k in
                       ["G09","G10","G11","G12","G13","G14","G15"]},
        },
        "Gejala Tenggorokan & Mulut": {
            "icon" : "fas fa-head-side-virus",
            "warna": "#8B5CF6",
            "gejala": {k: v for k, v in SEMUA_GEJALA.items() if k in
                       ["G16","G17","G18","G19","G20","G21","G22"]},
        },
        "Gejala Lainnya": {
            "icon" : "fas fa-stethoscope",
            "warna": "#10B981",
            "gejala": {k: v for k, v in SEMUA_GEJALA.items() if k in
                       ["G23","G24","G25","G26","G27","G28","G29","G30"]},
        },
    }
    return kategori
