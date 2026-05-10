# =============================================================================
# app.py — Flask + Supabase Backend
# Sistem Pakar Diagnosa Penyakit — MediExpert
# =============================================================================

import json
import os
import sqlite3
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request, url_for
from supabase import create_client, Client

from data_penyakit import DATA_PENYAKIT, SEMUA_GEJALA
from metode import forward_chaining, get_semua_gejala_terformat

# ---------------------------------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------------------------------
load_dotenv()

# ---------------------------------------------------------------------------
# Inisialisasi Flask
# ---------------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "mediexpert_secret_2025")

# ---------------------------------------------------------------------------
# Supabase Client + SQLite Fallback
# ---------------------------------------------------------------------------
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
DB_PATH      = os.path.join(BASE_DIR, "riwayat.db")

_supabase: Client = None
_use_sqlite = False   # Will switch to True if Supabase unavailable


def get_supabase() -> Client:
    global _supabase
    if _supabase is None and SUPABASE_URL and SUPABASE_KEY:
        _supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    return _supabase


def init_sqlite():
    """Buat tabel SQLite sebagai fallback."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS riwayat_konsultasi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_pasien TEXT NOT NULL DEFAULT 'Anonim',
            gejala TEXT NOT NULL,
            diagnosa TEXT,
            skor REAL DEFAULT 0,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


init_sqlite()


def simpan_riwayat(nama_pasien: str, gejala_ids: list, diagnosa: str, skor: float):
    """Simpan ke Supabase; fallback ke SQLite jika gagal."""
    data = {
        "nama_pasien": nama_pasien,
        "gejala": json.dumps(gejala_ids),
        "diagnosa": diagnosa,
        "skor": round(skor, 2),
        "timestamp": datetime.now().strftime("%d %B %Y, %H:%M:%S"),
    }
    try:
        db = get_supabase()
        if db:
            db.table("riwayat_konsultasi").insert(data).execute()
            return
    except Exception as e:
        print(f"[WARNING] Supabase gagal, fallback SQLite: {e}")
    # Fallback SQLite
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO riwayat_konsultasi (nama_pasien,gejala,diagnosa,skor,timestamp) VALUES (?,?,?,?,?)",
        (data["nama_pasien"], data["gejala"], data["diagnosa"], data["skor"], data["timestamp"])
    )
    conn.commit()
    conn.close()


def ambil_riwayat(limit: int = 50) -> list:
    """Ambil riwayat dari Supabase; fallback ke SQLite jika gagal."""
    try:
        db = get_supabase()
        if db:
            resp = (
                db.table("riwayat_konsultasi")
                .select("*")
                .order("id", desc=True)
                .limit(limit)
                .execute()
            )
            rows = resp.data or []
            for item in rows:
                try:
                    gejala_ids = json.loads(item.get("gejala", "[]"))
                    item["gejala_nama"] = [SEMUA_GEJALA.get(g, g) for g in gejala_ids]
                except Exception:
                    item["gejala_nama"] = []
            return rows
    except Exception as e:
        print(f"[WARNING] Supabase gagal, fallback SQLite: {e}")
    # Fallback SQLite
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM riwayat_konsultasi ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
    conn.close()
    hasil = []
    for row in rows:
        item = dict(row)
        try:
            gejala_ids = json.loads(item.get("gejala", "[]"))
            item["gejala_nama"] = [SEMUA_GEJALA.get(g, g) for g in gejala_ids]
        except Exception:
            item["gejala_nama"] = []
        hasil.append(item)
    return hasil


def ambil_statistik() -> dict:
    """Hitung statistik diagnosa; fallback ke SQLite jika Supabase gagal."""
    try:
        db = get_supabase()
        if db:
            resp = db.table("riwayat_konsultasi").select("diagnosa").execute()
            rows = resp.data or []
            counter: dict = {}
            for row in rows:
                label = row.get("diagnosa") or "Tidak Terdiagnosa"
                counter[label] = counter.get(label, 0) + 1
            sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
            return {"labels": [k for k, _ in sorted_items], "data": [v for _, v in sorted_items], "total": len(rows)}
    except Exception as e:
        print(f"[WARNING] Supabase statistik gagal, fallback SQLite: {e}")
    # Fallback SQLite
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("SELECT diagnosa, COUNT(*) FROM riwayat_konsultasi GROUP BY diagnosa ORDER BY 2 DESC").fetchall()
    total = sum(r[1] for r in rows)
    conn.close()
    return {
        "labels": [r[0] or "Tidak Terdiagnosa" for r in rows],
        "data": [r[1] for r in rows],
        "total": total,
    }


def hapus_riwayat_by_id(item_id: int):
    """Hapus riwayat dari Supabase; fallback ke SQLite."""
    try:
        db = get_supabase()
        if db:
            db.table("riwayat_konsultasi").delete().eq("id", item_id).execute()
            return
    except Exception as e:
        print(f"[WARNING] Supabase hapus gagal, fallback SQLite: {e}")
    # Fallback SQLite
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DELETE FROM riwayat_konsultasi WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()


# ===========================================================================
# ROUTES
# ===========================================================================

@app.route("/")
def index():
    kategori_gejala = get_semua_gejala_terformat()
    return render_template(
        "index.html",
        kategori_gejala=kategori_gejala,
        total_gejala=len(SEMUA_GEJALA),
        total_penyakit=len(DATA_PENYAKIT),
        daftar_penyakit=DATA_PENYAKIT,
    )


@app.route("/diagnosa", methods=["POST"])
def diagnosa():
    nama_pasien    = request.form.get("nama_pasien", "Anonim").strip() or "Anonim"
    gejala_dipilih = request.form.getlist("gejala")

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

    hasil = forward_chaining(gejala_dipilih)

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
    data_riwayat = ambil_riwayat(limit=50)
    statistik    = ambil_statistik()
    return render_template("riwayat.html", riwayat=data_riwayat, statistik=statistik)


@app.route("/riwayat/hapus/<int:item_id>", methods=["POST"])
def hapus_riwayat(item_id: int):
    hapus_riwayat_by_id(item_id)
    return redirect(url_for("riwayat"))


@app.route("/api/statistik")
def api_statistik():
    return jsonify(ambil_statistik())


@app.route("/tentang")
def tentang():
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
    print("  MediExpert — Sistem Pakar Diagnosa Penyakit")
    print("  Backend: Flask + Supabase")
    print("=" * 60)
    print(f"  Penyakit : {len(DATA_PENYAKIT)}")
    print(f"  Gejala   : {len(SEMUA_GEJALA)}")
    print(f"  Supabase : {SUPABASE_URL or 'BELUM DIKONFIGURASI'}")
    print("=" * 60)
    print("  Buka browser: http://127.0.0.1:5000")
    print("=" * 60)
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(debug=debug_mode, host="0.0.0.0", port=5000)
