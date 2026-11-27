# Day 48 · portfolio_tabs

Kode yang dipakai di deck Day 48 (versi "kode dulu, lalu hasilnya").

| Folder / file | Dipakai di | Isi |
|---|---|---|
| `fundamentals/01_text.py` … `06_layout.py` | Bagian 02 · Core Components | Satu file per topik: teks, data, grafik bawaan, Plotly, widget, layout |
| `app.py` | Bagian 03 · Portfolio | Satu app dengan tiga tab: Home, ML Predictor, EDA Dashboard |
| `assets/foto.png` | Tab Home | Foto placeholder; ganti dengan foto kalian |
| `requirements.txt` | Deploy | Versi library yang dipin |
| `screenshots/` | Slide "Hasilnya: ..." | Screenshot hasil setiap langkah |

## Menjalankan

```bash
python -m venv portfolio-env
source portfolio-env/bin/activate        # Windows: portfolio-env\Scripts\activate
pip install -r requirements.txt

streamlit run fundamentals/01_text.py    # contoh bagian 02
streamlit run app.py                     # portfolio lengkap
```

Nomor baris di slide bagian 03 sama dengan nomor baris di `app.py`.

`trendline="ols"` di tab EDA butuh `statsmodels`. Library ini sudah ada di `requirements.txt`; jangan dihapus sebelum deploy.
