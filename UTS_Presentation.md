# Materi Presentasi UTS: Diagnova - Sistem Pakar Kesehatan Pernapasan

## 1. Identitas Proyek
- **Nama Aplikasi**: Diagnova
- **Tagline**: "Your Intelligent First Response for Respiratory Health"
- **Platform**: Web-based (Flask & Supabase)
- **Domain Masalah**: Deteksi dini penyakit sistem pernapasan (Influenza, COVID-19, Bronkitis, dll).

---

## 2. Latar Belakang & Masalah
- **Masalah**: Kurangnya kesadaran masyarakat untuk melakukan deteksi dini terhadap gejala penyakit pernapasan yang seringkali dianggap sepele (misal: batuk biasa vs gejala awal COVID/Bronkitis).
- **Solusi**: Menyediakan sistem pakar yang dapat memberikan diagnosa awal berdasarkan gejala yang dirasakan pengguna secara cepat, akurat (berbasis data medis), dan mudah diakses.

---

## 3. Teknologi yang Digunakan (Tech Stack)
- **Backend**: Python dengan framework **Flask**.
- **Database**: **Supabase** (PostgreSQL) untuk penyimpanan data pasien dan riwayat diagnosa secara real-time.
- **Frontend**: HTML5, CSS3 (Vanilla), dan JavaScript untuk pengalaman pengguna yang responsif dan premium.
- **Metodologi**: **Forward Chaining** (Inferensi dari gejala menuju kesimpulan penyakit).
- **Deployment**: **Vercel** untuk akses publik yang cepat dan andal.

---

## 4. Landasan Teori: Forward Chaining
Sistem ini menggunakan algoritma **Forward Chaining**, yaitu:
1. **Fact-Driven**: Dimulai dari sekumpulan fakta (gejala yang dipilih user).
2. **Inference Engine**: Mencocokkan fakta tersebut dengan aturan (*rules*) yang ada di basis pengetahuan.
3. **Goal**: Menghasilkan kesimpulan berupa penyakit yang paling mungkin diderita beserta tingkat keyakinannya.

*Contoh Rule:*
> "IF demam (G01) AND batuk kering (G10) AND hilang penciuman (G30) THEN COVID-19 (P02)"

---

## 5. Fitur Utama
1. **Dynamic Diagnosis**: Form gejala yang interaktif.
2. **Demographic Filtering**: Mempertimbangkan faktor usia dan jenis kelamin untuk akurasi lebih tinggi.
3. **Professional Report**: Hasil diagnosa dilengkapi dengan deskripsi penyakit, penyebab, dan saran medis yang praktis.
4. **Admin Dashboard**: Terintegrasi dengan Supabase untuk mencatat riwayat konsultasi.
5. **Modern UI/UX**: Desain "Soft Blue" yang memberikan kesan tenang dan profesional layaknya aplikasi kesehatan modern.

---

## 6. Alur Penggunaan (User Flow)
1. **Landing Page**: Pengguna membaca cara kerja sistem.
2. **Identitas**: Pengguna memasukkan nama, usia, dan gender.
3. **Seleksi Gejala**: Pengguna memilih gejala yang dirasakan dari daftar yang tersedia.
4. **Hasil Diagnosa**: Sistem menampilkan penyakit, tingkat kecocokan, dan langkah selanjutnya (saran).

---

## 7. Kesimpulan & Pengembangan Masa Depan
- **Kesimpulan**: Diagnova berhasil mengimplementasikan sistem pakar berbasis web yang fungsional untuk membantu screening awal kesehatan.
- **Next Steps**: Integrasi dengan AI (LLM) untuk konsultasi lebih lanjut dan penambahan data penyakit yang lebih luas.
