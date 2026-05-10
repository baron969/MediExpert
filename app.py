# =============================================================================
# app.py
# Entry point Flask aplikasi Sistem Pakar Diagnosa Penyakit
# =============================================================================

import json
import os
import sqlite3
from datetime import datetime

from flask import Flask, jsonify, redirect, render_template, request, session, url_for

from data_penyakit import DATA_PENYAKIT, SEMUA_GEJALA
from metode import forward_chaining, get_semua_gejala_terformat

# ---------------------------------------------------------------------------
# Inisialisasi Aplikasi Flask
# ---------------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = "sistem_pakar_diagnosa_secret_key_2024"

# ---------------------------------------------------------------------------
# Konfigurasi Database SQLite
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, "riwayat.db")


def init_db():
    """Inisialisasi database SQLite untuk menyimpan riwayat konsultasi."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS riwayat_konsultasi (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_pasien TEXT    NOT NULL DEFAULT 'Anonim',
            gejala      TEXT    NOT NULL,
            diagnosa    TEXT,
            skor        REAL    DEFAULT 0,
            timestamp   TEXT    NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def simpan_riwayat(nama_pasien: str, gejala_ids: list, diagnosa: str, skor: float):
    """Menyimpan hasil konsultasi ke database SQLite."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO riwayat_konsultasi (nama_pasien, gejala, diagnosa, skor, timestamp) VALUES (?, ?, ?, ?, ?)",
        (
            nama_pasien,
            json.dumps(gejala_ids),
            diagnosa,
            skor,
            datetime.now().strftime("%d %B %Y, %H:%M:%S"),
        ),
    )
    conn.commit()
    conn.close()


def ambil_riwayat(limit: int = 20) -> list:
    """Mengambil riwayat konsultasi dari database, diurutkan terbaru."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM riwayat_konsultasi ORDER BY id DESC LIMIT ?", (limit,)
    )
    rows = cursor.fetchall()
    conn.close()

    hasil = []
    for row in rows:
        item = dict(row)
        # Parse JSON gejala menjadi list nama gejala
        try:
            gejala_ids = json.loads(item["gejala"])
            item["gejala_nama"] = [SEMUA_GEJALA.get(g, g) for g in gejala_ids]
        except Exception:
            item["gejala_nama"] = []
        hasil.append(item)
    return hasil


def ambil_statistik() -> dict:
    """Mengambil statistik diagnosa dari database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT diagnosa, COUNT(*) as jumlah FROM riwayat_konsultasi GROUP BY diagnosa ORDER BY jumlah DESC"
    )
    rows = cursor.fetchall()
    total = sum(r[1] for r in rows)
    conn.close()

    return {
        "labels" : [r[0] if r[0] else "Tidak Terdiagnosa" for r in rows],
        "data"   : [r[1] for r in rows],
        "total"  : total,
    }


# Inisialisasi database saat startup
init_db()


# ===========================================================================
# ROUTES
# ===========================================================================


@app.route("/")
def index():
    """Halaman utama — form checklist gejala."""
    kategori_gejala = get_semua_gejala_terformat()
    return render_template(
        "index.html",
        kategori_gejala=kategori_gejala,
        total_gejala=len(SEMUA_GEJALA),
        total_penyakit=len(DATA_PENYAKIT),
    )


@app.route("/diagnosa", methods=["POST"])
def diagnosa():
    """Endpoint diagnosa — menerima gejala dari form dan menjalankan forward chaining."""
    nama_pasien   = request.form.get("nama_pasien", "Anonim").strip() or "Anonim"
    gejala_dipilih = request.form.getlist("gejala")

    # -----------------------------------------------------------------------
    # Validasi input
    # -----------------------------------------------------------------------
    if not gejala_dipilih:
        return render_template(
            "index.html",
            kategori_gejala=get_semua_gejala_terformat(),
            total_gejala=len(SEMUA_GEJALA),
            total_penyakit=len(DATA_PENYAKIT),
            error="Harap pilih minimal 1 gejala sebelum melakukan diagnosa.",
        )

    if len(gejala_dipilih) < 3:
        return render_template(
            "index.html",
            kategori_gejala=get_semua_gejala_terformat(),
            total_gejala=len(SEMUA_GEJALA),
            total_penyakit=len(DATA_PENYAKIT),
            error="Untuk hasil diagnosa yang akurat, pilih minimal 3 gejala.",
            gejala_terpilih=gejala_dipilih,
        )

    # -----------------------------------------------------------------------
    # Jalankan Forward Chaining
    # -----------------------------------------------------------------------
    hasil = forward_chaining(gejala_dipilih)

    # -----------------------------------------------------------------------
    # Simpan riwayat ke database
    # -----------------------------------------------------------------------
    nama_diagnosa = "Tidak Terdiagnosa"
    skor_diagnosa = 0.0

    if hasil.get("diagnosa_utama"):
        nama_diagnosa = hasil["diagnosa_utama"]["nama"]
        skor_diagnosa = hasil["diagnosa_utama"]["skor"]
    elif hasil.get("kemungkinan_lain"):
        nama_diagnosa = f"Kemungkinan: {hasil['kemungkinan_lain'][0]['nama']}"
        skor_diagnosa = hasil["kemungkinan_lain"][0]["skor"]

    simpan_riwayat(nama_pasien, gejala_dipilih, nama_diagnosa, skor_diagnosa)

    return render_template(
        "hasil.html",
        hasil=hasil,
        nama_pasien=nama_pasien,
        timestamp=datetime.now().strftime("%d %B %Y, %H:%M"),
    )


@app.route("/riwayat")
def riwayat():
    """Halaman riwayat konsultasi."""
    data_riwayat = ambil_riwayat(limit=50)
    statistik    = ambil_statistik()
    return render_template(
        "riwayat.html",
        riwayat=data_riwayat,
        statistik=statistik,
    )


@app.route("/riwayat/hapus/<int:item_id>", methods=["POST"])
def hapus_riwayat(item_id: int):
    """Menghapus satu entri riwayat berdasarkan ID."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DELETE FROM riwayat_konsultasi WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("riwayat"))


@app.route("/api/statistik")
def api_statistik():
    """API endpoint untuk data chart statistik diagnosa."""
    return jsonify(ambil_statistik())


@app.route("/tentang")
def tentang():
    """Halaman tentang sistem pakar."""
    return render_template(
        "tentang.html",
        total_penyakit=len(DATA_PENYAKIT),
        total_gejala=len(SEMUA_GEJALA),
        daftar_penyakit=DATA_PENYAKIT,
    )


# ===========================================================================
# MAIN
# ===========================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("  Sistem Pakar Diagnosa Penyakit")
    print("  Forward Chaining Method")
    print("=" * 60)
    print(f"  Database: {DB_PATH}")
    print(f"  Penyakit: {len(DATA_PENYAKIT)} penyakit terdaftar")
    print(f"  Gejala  : {len(SEMUA_GEJALA)} gejala tersedia")
    print("=" * 60)
    print("  Buka browser: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(debug=True, host="0.0.0.0", port=5000)
