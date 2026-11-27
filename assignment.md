# Assignment Day 48 — Building a Streamlit-Based Portfolio

**Individu · dikumpulkan di LMS · maksimal H+7 kelas → Sabtu, 19 Desember 2026**
(jam batas mengikuti yang tertera di LMS).

> Catatan jadwal: tanggal deadline sama dengan **Final Test Teori (Day 49)**. Usahakan
> deploy selesai paling lambat Kamis, 17 Desember, supaya akhir pekan bisa fokus belajar.

## Brief

Kalian sudah membangun banyak hal: EDA, model klasik, deep learning, YOLO (Day 40), chatbot RAG
(Day 44), sistem rekomendasi (Day 45), API + Docker (Day 46), dan MLOps (Day 47). Sekarang
kumpulkan semuanya di **satu portfolio interaktif berbasis Streamlit** yang **live di internet**:
link yang akan kalian pasang di CV dan LinkedIn, dan yang nanti menjadi "rumah" untuk final project.

**Titik awal:** `lab/portfolio_tabs/app.py` yang kita bangun di kelas (tab Home, ML Predictor,
EDA Dashboard). Salin ke folder `my-portfolio/`, lalu ganti isinya dengan profil, project, model,
dan data kalian sendiri. Boleh juga membangun dari nol selama memenuhi rubric.

## Yang harus ada (deliverables)

1. **App Streamlit yang sudah di-deploy** (Streamlit Community Cloud, atau alternatif seperti
   Hugging Face Spaces) dan bisa dibuka siapa pun. Minimal tiga bagian seperti di kelas:
   **Home**, **ML Predictor**, **EDA Dashboard** (boleh ditambah tab lain).
2. **Repo GitHub public** berisi `app.py`, `assets/`, `requirements.txt` (versi dipin `==`),
   file model/data yang dibutuhkan app, dan **README.md** dengan link live, minimal 2 screenshot,
   dan cara menjalankan.
3. **Tab Home berisi kalian sendiri:** nama, foto, headline, skill, angka singkat (`st.metric`),
   link kontak (LinkedIn, GitHub, email; link CV disarankan), dan minimal **3 kartu project**
   dengan pola *Problem → Approach → Impact → Link*. App kelas punya 2 kartu: tambahkan minimal satu.
4. **Tab ML Predictor memakai model kalian sendiri.** Rumus demo di kelas diganti dengan
   `model.predict()` (lihat contoh di bawah). Tambahkan penjelasan singkat cara kerja model dan
   **batasannya**. Model Harga Rumah dari Day 46/47 boleh dipakai.
5. **Tab EDA Dashboard memakai dataset kalian** (bukan Iris): **≥ 3 grafik** dan **≥ 1 filter**
   (widget yang mengubah grafik), data dimuat dengan `@st.cache_data`.

### Dari rumus demo ke model kalian

Di `app.py` kelas, blok `if predict_btn:` (baris 108–117) menghitung harga dengan rumus. Ganti
dengan model yang sudah kalian latih dan simpan dengan `joblib.dump(model, "model/model.joblib")`.
Kerjakan **langkah 1 dulu**, selagi nomor baris masih sama dengan `app.py` kelas.

**Langkah 1.** Ganti baris 108–117 (dari `if predict_btn:` sampai `price_juta = price / 1_000_000`)
dengan blok ini. `st.metric(...)` dan `else:` di bawahnya tetap:

```python
        if predict_btn:
            model = load_model()
            X = pd.DataFrame([{            # nama kolom = nama kolom saat training
                "luas_tanah": luas_tanah,
                "luas_bangunan": luas_bangunan,
                "kamar_tidur": kamar_tidur,
                "kamar_mandi": kamar_mandi,
                "is_shm": is_shm,
            }])
            price = model.predict(X)[0]
            price_miliar = price / 1_000_000_000
            price_juta = price / 1_000_000
```

**Langkah 2.** Tambahkan import dan fungsi ini tepat di bawah baris 4 (`from sklearn.datasets import
load_iris`), sebelum `st.set_page_config`:

```python
import joblib

@st.cache_resource                 # model dimuat sekali, dipakai ulang di setiap rerun
def load_model():
    return joblib.load("model/model.joblib")
```

- Nama dan urutan kolom harus **sama persis** dengan saat training. Model Harga Rumah Day 46
  memakai `luas_tanah_m2, luas_bangunan_m2, kamar_tidur, kamar_mandi, jarak_ke_pusat_km,
  umur_bangunan_tahun, kota`; sesuaikan input form-nya.
- Commit folder `model/` (model kecil, beberapa MB). Tambahkan `joblib==1.6.0` ke
  `requirements.txt`, dan pastikan versi `scikit-learn` sama dengan saat training.
- `@st.cache_resource` disarankan supaya model tidak dimuat ulang di setiap klik. Tidak wajib
  untuk nilai penuh, tapi app tanpa cache akan terasa lambat.

## Rubric (total 100)

| # | Aspek | Poin | Kriteria nilai penuh |
|---|---|---|---|
| 1 | **Live & repo rapi** | 20 | Link `*.streamlit.app` (atau setara) terbuka tanpa error di incognito/HP; repo public; README berisi link live, ≥ 2 screenshot, cara menjalankan; `.gitignore` benar (tanpa `venv/`, tanpa `.streamlit/secrets.toml`) |
| 2 | **Personal branding** | 15 | Tab Home: foto, headline yang spesifik (bukan "passionate in data"), skill, angka singkat dengan `st.metric` yang memang milik kalian, link kontak yang bisa diklik (LinkedIn, GitHub, email) |
| 3 | **Project showcase** | 20 | ≥ 3 kartu project milik sendiri dengan Problem → Approach → Impact (ada angka/hasil terukur) → link (repo/demo); tidak ada isi contoh kelas yang tertinggal |
| 4 | **Deep-dive interaktif** | 25 | ML Predictor memakai model kalian (bukan rumus demo) dan hasilnya masuk akal; EDA memakai dataset kalian: ≥ 3 grafik + ≥ 1 filter yang berfungsi; ada penjelasan model + batasannya |
| 5 | **Kode & praktik Streamlit** | 15 | `requirements.txt` dipin `==` dan lengkap (termasuk `statsmodels` bila memakai `trendline="ols"`); data dimuat dengan `@st.cache_data`; app jalan di venv baru tanpa error; tidak ada secret/API key di repo; kode rapi (bagian per tab diberi komentar seperti `app.py` kelas) |
| 6 | **Desain & UX** | 5 | Layout rapi (`st.columns`, kartu, `st.divider`); `st.set_page_config` dengan judul dan ikon kalian; tidak ada error merah; terbaca di layar HP |
| | **Total** | **100** | |

### Pengurangan nilai yang sering terjadi

- Link mati / app error saat dinilai → aspek 1 maksimal 5 poin. *(App Community Cloud yang "tidur"
  bukan error: penilai akan membangunkannya. Pastikan app bisa bangun tanpa error.)*
- Isi contoh kelas tidak diganti (nama "Budi", angka di `st.metric`, kartu project contoh) → aspek 2 dan 3 tidak penuh.
- Rumus demo atau dataset Iris masih dipakai → aspek 4 maksimal 10 poin.
- API key / password ter-commit di repo → aspek 5 = 0 (dan segera *rotate* key-nya).
- Angka impact yang tidak bisa dijelaskan → mentor boleh menanyakannya saat review.

> Boleh memakai AI assistant (ChatGPT, Copilot, Claude, dll.) sebagai alat bantu, **tetapi kalian harus
> bisa menjelaskan setiap baris kode dan setiap angka** di portfolio. Itu juga yang akan ditanyakan saat interview.

## Cara mengumpulkan (LMS)

Kirim di LMS dalam satu submission:

1. **Link app live** (mis. `https://nama-kamu-portfolio.streamlit.app`)
2. **Link repo GitHub** (public)
3. **1 screenshot** tab Home
4. *(Opsional, untuk feedback; tidak menambah skor di atas 100)* link post LinkedIn tentang portfolio kalian

## Checklist sebelum submit

- [ ] Di venv baru: `pip install -r requirements.txt` lalu `streamlit run app.py` jalan tanpa error
- [ ] App dibuka di mode incognito **dan** di HP: ketiga tab tanpa error merah
- [ ] Prediksi di tab ML Predictor memberi angka yang masuk akal (dari model, bukan rumus)
- [ ] Tab EDA memakai data kalian; filter benar-benar mengubah grafik
- [ ] Tidak ada lagi "Budi", angka contoh, atau dataset Iris
- [ ] README: link live, screenshot, cara menjalankan
- [ ] Tidak ada `venv/`, `.streamlit/secrets.toml`, atau API key di repo
- [ ] Sudah minta satu teman melakukan "review 30 detik"

## Tips

- Python di Community Cloud dipilih di **Advanced settings** saat deploy (default 3.12). Pilih
  **3.11** agar sama dengan laptop/lab; versi Python tidak bisa diganti setelah deploy kecuali app
  dihapus dan di-deploy ulang.
- Setiap `git push` ke branch yang di-deploy → app ter-update otomatis.
- `st.image("assets/foto.png")` membaca path relatif terhadap folder tempat `streamlit run`
  dijalankan. Jalankan dari dalam folder `my-portfolio/`; di Cloud, `app.py` harus di root repo.
- Model besar (> 100 MB) tidak bisa di-push ke GitHub biasa: simpan di Hugging Face Hub / GitHub
  Release, lalu unduh saat app start di dalam fungsi `@st.cache_resource`.
- Final project (Day 51) nantinya tinggal ditambahkan sebagai kartu project + tab baru.
