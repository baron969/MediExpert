-- =============================================================================
-- supabase_schema.sql
-- Jalankan SQL ini di Supabase Dashboard > SQL Editor
-- =============================================================================

-- Buat tabel riwayat_konsultasi
CREATE TABLE IF NOT EXISTS riwayat_konsultasi (
    id          BIGSERIAL PRIMARY KEY,
    nama_pasien TEXT      NOT NULL DEFAULT 'Anonim',
    gejala      TEXT      NOT NULL,
    diagnosa    TEXT,
    skor        REAL      DEFAULT 0,
    timestamp   TEXT      NOT NULL,
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- Aktifkan Row Level Security (RLS)
ALTER TABLE riwayat_konsultasi ENABLE ROW LEVEL SECURITY;

-- Policy: izinkan semua operasi (untuk development)
-- Ganti dengan policy lebih ketat untuk production
CREATE POLICY "Allow all operations"
ON riwayat_konsultasi
FOR ALL
USING (true)
WITH CHECK (true);

-- Index untuk performa query
CREATE INDEX IF NOT EXISTS idx_riwayat_created_at
ON riwayat_konsultasi(created_at DESC);

CREATE INDEX IF NOT EXISTS idx_riwayat_diagnosa
ON riwayat_konsultasi(diagnosa);
