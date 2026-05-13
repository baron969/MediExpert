# AGENTS.md — Diagnova (Sistem Pakar Diagnosa Penyakit)

## Stack

- **Backend:** Python 3 + Flask (no typecheck/lint/formatter configured)
- **Database:** Supabase (primary) with SQLite fallback at `riwayat.db` (gitignored)
- **Frontend:** Jinja2 server-rendered HTML, Chart.js, FontAwesome
- **Deploy:** Vercel (serverless) via `api/index.py` wrapper; `gunicorn` in requirements but unused locally

## Run locally

```powershell
pip install -r requirements.txt
python app.py
# → http://localhost:5000
```

No build step, no codegen, no migration needed. SQLite table auto-creates on first run.

## Architecture

| File | Role |
|---|---|
| `app.py` | Flask entrypoint, routes, DB layer (Supabase + SQLite fallback), session auth |
| `metode.py` | Certainty Factor inference engine — `cf_combine_sequential` formula (`cf1 + cf2 × (1 - cf1)`); thresholds: ≥0.40 = main diagnosis, ≥0.10 = other possibilities |
| `data_penyakit.py` | Knowledge base: 9 diseases (P01–P09), 34 symptoms (G01–G34), all respiratory; also `DESKRIPSI_GEJALA` dict (medical explanations + icons per G-code) |
| `data_artikel.py` | Education content: 8 articles with id/judul/ringkasan/gambar/isi/sumber |
| `api/index.py` | Vercel serverless entrypoint — `from app import app` |
| `supabase_schema.sql` | Reference DDL; not auto-applied |
| `templates/` | Jinja2 templates (base, index, hasil, riwayat, login, tentang, tentang-kami, edukasi) |
| `static/` | CSS, JS, images |

## Key conventions

- Symptom IDs use G-prefix codes (`G01`–`G34`), disease IDs use P-prefix codes (`P01`–`P09`)
- Form field naming: each symptom's confidence is sent as `keyakinan_G01`, `keyakinan_G02`, etc. with values `0.0`, `0.4`, `0.7`, `1.0` (matching `KEYAKINAN_USER` in `metode.py`). Symptoms with value `0.0` are ignored by backend.
- Admin routes (`/riwayat`, `/riwayat/hapus/<id>`, `/api/statistik`) require session auth; credentials from `ADMIN_USERNAME`/`ADMIN_PASSWORD` env vars (default: `admin`/`admin123`)
- Rating system: `/api/rating` POST accepts `{id, rating}` (1–5). Star rating displayed on `hasil.html` and admin table shows average in stat cards
- `.env` file has Supabase creds + `FLASK_SECRET_KEY` + `FLASK_DEBUG`; not committed (gitignored). Supabase failure silently falls back to SQLite
- No test framework, no CI, no test commands available
- Commit style uses `type: description` prefixes (`feat:`, `Fix:`, `Refactor:`, `UI:`, etc.)
