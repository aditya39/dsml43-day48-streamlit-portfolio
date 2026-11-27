# Lab Day 48 — Portfolio Streamlit: kode dulu, lalu hasilnya

Hari ini kalian menulis kode yang sama dengan di slide, menjalankannya, lalu mencocokkan hasilnya
dengan screenshot. Di akhir, kalian punya satu `app.py` dengan tiga tab (**Home**, **ML Predictor**,
**EDA Dashboard**) yang siap di-deploy ke Streamlit Community Cloud.

```
lab/
├── README.md                  ← panduan ini
└── portfolio_tabs/
    ├── fundamentals/          # Bagian 02: satu file per topik (01_text.py … 06_layout.py)
    ├── app.py                 # Bagian 03: portfolio tiga tab (nomor baris = nomor baris di slide)
    ├── assets/foto.png        # foto placeholder, ganti dengan foto kalian
    ├── requirements.txt       # versi dipin, dipakai di laptop dan saat deploy
    ├── .gitignore
    └── screenshots/           # hasil yang benar untuk setiap langkah (hasil_01 … hasil_09)
```

Versi lengkap dengan gambar dan lembar kerja ada di **Buku Panduan Peserta Day 48** (PDF).

---

## Sebelum kelas (wajib, ±15 menit)

1. **Python 3.11** (`python --version` di Windows, `python3 --version` di macOS), **VS Code** +
   extension Python, **Git** (`git --version`), akun **GitHub**.
2. Login ke **https://share.streamlit.io** dengan akun GitHub.
3. Susun folder seperti ini:

```
Documents/dsml-day48/
├── materi/          ← repo hands-on dari mentor (berisi lab/portfolio_tabs)
└── my-portfolio/    ← folder kerja kalian → nanti jadi repo GitHub sendiri
```

4. Buat venv dan install library dari folder `my-portfolio`:

**macOS / Linux**

```bash
cd ~/Documents/dsml-day48/my-portfolio
python3 -m venv portfolio-env
source portfolio-env/bin/activate
pip install -r ../materi/lab/portfolio_tabs/requirements.txt
```

**Windows (PowerShell)**

```powershell
cd ~\Documents\dsml-day48\my-portfolio
python -m venv portfolio-env
portfolio-env\Scripts\activate
pip install -r ..\materi\lab\portfolio_tabs\requirements.txt
```

> Library-nya sama dengan slide "Instalasi dan aplikasi pertama"
> (`pip install streamlit pandas plotly scikit-learn statsmodels`), tapi versinya dikunci supaya
> sama dengan yang nanti dipakai saat deploy.
>
> PowerShell menolak `activate` ("running scripts is disabled")? Jalankan sekali:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, lalu coba lagi.

✅ **Cek:** `streamlit version` mencetak `Streamlit, version 1.67.0`.

---

## Bagian 01 — Aplikasi pertama dan aturan rerun

Buat `my-portfolio/app.py`:

```python
import streamlit as st
st.title("Hello, Streamlit!")
st.write("My first Streamlit app.")
st.balloons()
```

```bash
streamlit run app.py
```

Browser terbuka di `http://localhost:8501`. Ubah teks di `app.py`, simpan, lalu lihat app
ikut berubah. Hentikan app dengan `Ctrl + C` di terminal.

**Coba rerun:** tambahkan dua baris ini, simpan, lalu geser slider tiga kali dan lihat terminal.

```python
x = st.slider("Geser aku", 0, 10, 5)
print("script jalan, x =", x)
```

✅ **Checkpoint:** setiap geseran mencetak satu baris baru. Setiap interaksi = script dijalankan
ulang dari atas ke bawah.

---

## Bagian 02 — Core Components (kode dulu, lalu hasilnya)

Jalankan satu per satu dari folder `my-portfolio` (`Ctrl + C` sebelum menjalankan file berikutnya).
Windows: ganti `/` dengan `\`.

| Slide | Perintah | Hasil yang benar |
|---|---|---|
| Teks: `st.title` sampai `st.caption` | `streamlit run ../materi/lab/portfolio_tabs/fundamentals/01_text.py` | `screenshots/hasil_01_teks.png` |
| Data: tabel, metrik, dan JSON | `streamlit run ../materi/lab/portfolio_tabs/fundamentals/02_data.py` | `screenshots/hasil_02_data.png` |
| Grafik bawaan: line dan bar chart | `streamlit run ../materi/lab/portfolio_tabs/fundamentals/03_charts.py` | `screenshots/hasil_03_grafik_bawaan.png` |
| Plotly: grafik yang bisa di-hover | `streamlit run ../materi/lab/portfolio_tabs/fundamentals/04_plotly.py` | `screenshots/hasil_04_plotly.png` |
| Setiap widget mengembalikan nilai | `streamlit run ../materi/lab/portfolio_tabs/fundamentals/05_widgets.py` | `screenshots/hasil_05_widget.png` |
| Layout: sidebar, kolom, tab, expander | `streamlit run ../materi/lab/portfolio_tabs/fundamentals/06_layout.py` | `screenshots/hasil_06_layout.png` |

Mau mengetik sendiri? Salin isi file ke `my-portfolio/latihan.py` lalu `streamlit run latihan.py`.

✅ **Checkpoint:** kalian bisa menjawab: apa beda `st.dataframe` dan `st.table`? Kenapa
`st.plotly_chart` bisa di-hover? Nilai apa yang dikembalikan `st.multiselect`?

---

## Bagian 03 — Portfolio tiga tab, langkah demi langkah

1. Salin foto placeholder ke folder kerja:

```bash
mkdir assets
cp ../materi/lab/portfolio_tabs/assets/foto.png assets/      # Windows: copy ..\materi\lab\portfolio_tabs\assets\foto.png assets\
```

2. Kosongkan `my-portfolio/app.py`, lalu ketik kode mengikuti slide. Nomor baris di slide sama
   dengan nomor baris di `portfolio_tabs/app.py`:

| Slide | Baris `app.py` | Isi |
|---|---|---|
| Baris 1–16: page config dan tiga tab | 1–16 | import, `st.set_page_config(layout="wide")`, `st.tabs` |
| Home 1/3: judul, foto, dan bio | 18–35 | `st.title`, `st.columns([1, 3])`, `st.image`, bio |
| Home 2/3: angka singkat | 37–49 | empat `st.metric`, judul Featured Projects |
| Home 3/3: dua kartu project | 51–71 | `st.container(border=True)` |
| ML Predictor 1/3: input luas | 73–89 | dua kolom, `st.number_input` luas tanah |
| ML Predictor 2/3: slider dan tombol | 90–103 | `st.slider`, `st.selectbox` sertifikat, `st.button` |
| ML Predictor 3/3: hitung dan tampilkan | 105–125 | rumus demo, `st.metric` |
| EDA 1/6: muat data sekali (cache) | 127–147 | `@st.cache_data`, dataset Iris |
| EDA 2/6: filter spesies dan sumbu X | 149–168 | `st.multiselect`, `st.selectbox` |
| EDA 3/6: sumbu Y dan data terfilter | 169–181 | filter DataFrame, `st.stop()` kalau kosong |
| EDA 4/6: bar chart rata-rata fitur | 183–203 | `px.bar` |
| EDA 5/6: pie chart jumlah sampel | 205–214 | `px.pie` |
| EDA 6/6: scatter plot dan data mentah | 216–233 | `px.scatter(trendline="ols")`, `st.checkbox` + `st.dataframe` |

3. Simpan dan lihat hasilnya setelah setiap tab selesai:

```bash
streamlit run app.py
```

✅ **Checkpoint tab Home:** sama dengan `screenshots/hasil_07_tab_home.png`.

✅ **Checkpoint tab ML Predictor:** isi luas tanah 100, luas bangunan 80, 3 kamar tidur,
2 kamar mandi, SHM → klik **Prediksi Harga** → `Rp 2.14 M`. Geser slider lagi: hasilnya hilang
karena `st.button` hanya bernilai `True` pada rerun tepat setelah diklik.

✅ **Checkpoint tab EDA:** sama dengan `screenshots/hasil_09_tab_eda.png`; hapus semua spesies →
muncul peringatan, grafik di bawahnya tidak dibuat.

> Tertinggal? Salin `../materi/lab/portfolio_tabs/app.py` ke `my-portfolio/app.py`, lalu lanjut
> dari slide yang sedang dibahas.

---

## Bagian 04 — Deploy ke Streamlit Community Cloud

1. **Siapkan repo.** Isi folder `my-portfolio` harus seperti ini:

```
my-portfolio/
├── app.py
├── assets/
│   └── foto.png
├── requirements.txt
└── .gitignore
```

```bash
cp ../materi/lab/portfolio_tabs/requirements.txt ../materi/lab/portfolio_tabs/.gitignore .
```

(Windows: `copy ..\materi\lab\portfolio_tabs\requirements.txt .` lalu
`copy ..\materi\lab\portfolio_tabs\.gitignore .`)

`requirements.txt` berisi versi dipin, termasuk `statsmodels==0.15.0` yang dibutuhkan
`trendline="ols"`. `.gitignore` menolak `portfolio-env/`, `venv/`, `.venv/`, `__pycache__/`, dan
`.streamlit/secrets.toml`, jadi venv dan rahasia tidak ikut ter-push.

2. **Uji di venv bersih** (opsional tapi disarankan): buat venv baru, `pip install -r requirements.txt`,
   `streamlit run app.py`. Error yang muncul di sini akan muncul juga di Cloud.

3. **Push ke GitHub.** Buat repo **public** baru `my-portfolio` (tanpa README bawaan), lalu:

```bash
git init
git add .
git commit -m "Portfolio Streamlit pertama"
git branch -M main
git remote add origin https://github.com/USERNAME/my-portfolio.git
git push -u origin main
```

4. **Deploy.** Buka **share.streamlit.io** → **Create app** → pilih repo, branch `main`,
   Main file path `app.py`. Buka **Advanced settings** → Python **3.11** (default Cloud 3.12;
   versi Python tidak bisa diganti setelah deploy kecuali app dihapus dan di-deploy ulang).
   Klik **Deploy**, tunggu build, salin URL `https://<subdomain>.streamlit.app`.

✅ **Checkpoint:** URL terbuka di HP / mode incognito, tab ML Predictor bisa memprediksi.
Setiap `git push` berikutnya ke `main` meng-update app otomatis.

### Error deploy yang paling sering

| Gejala di log Cloud | Penyebab | Solusi |
|---|---|---|
| `ModuleNotFoundError: No module named 'plotly'` (atau `statsmodels`) | library tidak ada di `requirements.txt` | tambahkan dengan versi `==`, push lagi |
| `MediaFileStorageError: Error opening 'assets/foto.png'` | `assets/` tidak ter-commit, atau `app.py` tidak di root repo | commit `assets/`; taruh `app.py` di root |
| `FileNotFoundError` model/data | file tidak ter-push, atau path relatif terhadap folder kerja | commit file; pakai `Path(__file__).parent / "model" / ...` |
| Error saat `joblib.load` | versi scikit-learn di Cloud ≠ saat training | satu `requirements.txt` yang dipin |
| `StreamlitSecretNotFoundError` | secrets belum diisi di Cloud | *App settings → Secrets* |
| Build gagal saat install | versi library tidak tersedia untuk Python yang dipilih | pilih Python 3.11; buang library yang tidak dipakai |
| Halaman "gone to sleep" | ±12 jam tanpa pengunjung | buka link sebelum mengirim lamaran |

---

## Setelah deploy: README dan LinkedIn

- `README.md` di repo kalian: link live, 2 screenshot, ringkasan project, cara menjalankan.
- Pin repo di profil GitHub; pasang link app di bagian *Featured* LinkedIn dan di CV.
- Post LinkedIn (±150 kata): masalah → apa yang dibangun → satu insight dari data → link app.

## Lanjut ke assignment

Baca `assignment.md`: ganti isi contoh dengan milik kalian, tambah kartu project ketiga, ganti
rumus demo dengan model kalian (`model.predict`), dan ganti dataset Iris dengan data kalian.

---

## Kalau macet

| Masalah | Langkah cepat |
|---|---|
| `streamlit` tidak dikenali | venv belum aktif → aktifkan lagi (lihat "Sebelum kelas") |
| Ada app Streamlit lain yang masih jalan | Streamlit otomatis pindah ke port 8502 (lihat URL di terminal); atau hentikan app lama dengan `Ctrl + C` |
| Foto tidak tampil / `Error opening 'assets/foto.png'` | jalankan `streamlit run` dari dalam folder `my-portfolio`, dan pastikan `assets/foto.png` ada |
| Garis tren error / `No module named 'statsmodels'` | `pip install -r requirements.txt` (statsmodels ada di sana) |
| `pip install` lambat / gagal | pakai jaringan lain / hotspot; ikuti layar mentor dulu, install saat istirahat |
| Kode tertinggal | salin `portfolio_tabs/app.py`, lalu lanjut dari slide yang sedang dibahas |

## Referensi

- Dokumentasi Streamlit: https://docs.streamlit.io
- Deploy: https://docs.streamlit.io/deploy/streamlit-community-cloud
- Galeri inspirasi: https://streamlit.io/gallery
- Cheat sheet: https://github.com/daniellewisDL/streamlit-cheat-sheet
