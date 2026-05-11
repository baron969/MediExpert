import json
from data_penyakit import DATA_PENYAKIT, SEMUA_GEJALA, BOBOT_UTAMA, BOBOT_PENDUKUNG

def get_semua_gejala_terformat() -> list:
    """
    Mengelompokkan gejala ke dalam kategori untuk UI.
    """
    kategori = {
        "Umum & Demam": ["G01", "G02", "G05", "G06", "G07", "G08", "G31", "G32"],
        "Pernapasan Utama": ["G03", "G04", "G12", "G13", "G14", "G15", "G33"],
        "Hidung & Tenggorokan": ["G09", "G10", "G11", "G16", "G17", "G18", "G19", "G20"],
        "Lainnya": ["G21", "G22", "G23", "G27", "G30", "G34"],
    }
    
    hasil = []
    for kat_nama, ids in kategori.items():
        gejala_kat = []
        for gid in ids:
            if gid in SEMUA_GEJALA:
                gejala_kat.append({"id": gid, "nama": SEMUA_GEJALA[gid]})
        hasil.append({"kategori": kat_nama, "gejala": gejala_kat})
    
    return hasil

def forward_chaining(gejala_dipilih: list, umur: int = None, jenis_kelamin: str = None) -> dict:
    """
    Melakukan proses diagnosa berdasarkan kombinasi gejala yang dipilih user.
    Algoritma baru menggunakan pembobotan gejala utama, gejala pendukung, 
    dan penyesuaian skor berdasarkan faktor risiko (umur/gender).
    """
    hasil_penyakit = []
    gejala_set = set(gejala_dipilih)

    for pid, p_data in DATA_PENYAKIT.items():
        # Hitung Bobot Maksimal Penyakit Ini
        max_score = (len(p_data["gejala_utama"]) * BOBOT_UTAMA) + (len(p_data["gejala_pendukung"]) * BOBOT_PENDUKUNG)
        
        if max_score == 0: continue
            
        current_score = 0.0
        gejala_cocok_utama = []
        gejala_cocok_pendukung = []

        # Cek Gejala Utama
        for g_utama in p_data["gejala_utama"]:
            if g_utama in gejala_set:
                current_score += BOBOT_UTAMA
                gejala_cocok_utama.append(SEMUA_GEJALA.get(g_utama, g_utama))

        # Cek Gejala Pendukung
        for g_pendukung in p_data["gejala_pendukung"]:
            if g_pendukung in gejala_set:
                current_score += BOBOT_PENDUKUNG
                gejala_cocok_pendukung.append(SEMUA_GEJALA.get(g_pendukung, g_pendukung))

        # Kalkulasi persentase awal
        persentase = (current_score / max_score) * 100

        # Penyesuaian Faktor Risiko Demografi (Opsional)
        if umur is not None:
            r_min = p_data["faktor_risiko"]["umur_min"]
            r_max = p_data["faktor_risiko"]["umur_max"]
            if r_min <= umur <= r_max:
                # Jika sesuai demografi risiko, berikan bonus kecil (maks 5%) agar lebih sensitif
                # Bonus diberikan hanya jika sudah ada gejala cocok
                if persentase > 0:
                    persentase += 5.0
                    
        # Pastikan tidak lebih dari 100
        persentase = min(persentase, 100.0)

        # Hanya rekam jika ada kecocokan signifikan
        if persentase > 0:
            hasil_penyakit.append({
                "id": pid,
                "nama": p_data["nama"],
                "deskripsi": p_data["deskripsi"],
                "penyebab": p_data["penyebab"],
                "saran": p_data["saran"],
                "icon": p_data["icon"],
                "warna": p_data["warna"],
                "skor": round(persentase, 2),
                "gejala_cocok_utama": gejala_cocok_utama,
                "gejala_cocok_pendukung": gejala_cocok_pendukung,
            })

    # Urutkan berdasarkan skor tertinggi
    hasil_penyakit = sorted(hasil_penyakit, key=lambda x: x["skor"], reverse=True)

    # Thresholds:
    # >= 50% = Diagnosa Utama
    # >= 20% = Kemungkinan Lain
    
    diagnosa_utama = None
    kemungkinan_lain = []
    
    for hp in hasil_penyakit:
        if hp["skor"] >= 50.0 and diagnosa_utama is None:
            diagnosa_utama = hp
        elif hp["skor"] >= 20.0:
            kemungkinan_lain.append(hp)

    gejala_detail = [{"id": gid, "nama": SEMUA_GEJALA.get(gid, gid)} for gid in gejala_dipilih]

    return {
        "gejala_terpilih": gejala_dipilih,
        "gejala_terpilih_detail": gejala_detail,
        "total_gejala": len(gejala_dipilih),
        "diagnosa_utama": diagnosa_utama,
        "kemungkinan_lain": kemungkinan_lain,
        "tidak_terdiagnosa": not diagnosa_utama and not kemungkinan_lain
    }
