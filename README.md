# DSML Batch 43 · Day 48 — Portfolio Building with Streamlit

Repo hands-on untuk Day 48 (Sabtu, 12 Desember 2026). Kita menulis kode Streamlit mengikuti slide
(kode dulu, lalu hasilnya), merakit portfolio satu `app.py` dengan tiga tab, lalu men-deploy-nya ke
Streamlit Community Cloud.

**Mulai dari sini:** [`lab/README.md`](lab/README.md) (bagian "Sebelum kelas" wajib dikerjakan H-1).

📘 **Buku panduan peserta (PDF):** [`docs/Buku-Panduan-Peserta-Day-48.pdf`](docs/Buku-Panduan-Peserta-Day-48.pdf), versi lengkap langkah demi langkah dengan gambar dan lembar kerja.

| Folder / file | Isi |
|---|---|
| `lab/README.md` | Panduan hands-on: setup, Bagian 01–04, deploy, kalau macet |
| `lab/portfolio_tabs/fundamentals/` | Bagian 02 · satu file per topik: teks, data, grafik bawaan, Plotly, widget, layout |
| `lab/portfolio_tabs/app.py` | Bagian 03 · portfolio tiga tab: Home, ML Predictor, EDA Dashboard (nomor baris = slide) |
| `lab/portfolio_tabs/assets/foto.png` | Foto placeholder; ganti dengan foto kalian |
| `lab/portfolio_tabs/requirements.txt` | Versi library yang dipin (Python 3.11) |
| `lab/portfolio_tabs/screenshots/` | Hasil yang benar untuk setiap langkah |
| `docs/Buku-Panduan-Peserta-Day-48.pdf` | Buku panduan peserta (PDF) |
| `assignment.md` | Assignment Day 48: brief, rubric, cara mengumpulkan (deadline Sabtu, 19 Desember 2026) |

## Yang perlu disiapkan

- Python 3.11, VS Code + extension Python, Git, akun GitHub
- Login ke https://share.streamlit.io dengan akun GitHub

## Jalan cepat

```bash
cd lab/portfolio_tabs
python -m venv portfolio-env
source portfolio-env/bin/activate        # Windows: portfolio-env\Scripts\activate
pip install -r requirements.txt
streamlit run app.py                     # http://localhost:8501
```

Data di tab EDA adalah dataset Iris dan prediksi di tab ML Predictor masih rumus demo. Untuk
assignment, ganti keduanya dengan data dan model kalian sendiri (lihat `assignment.md`).
