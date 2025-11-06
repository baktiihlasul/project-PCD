# Aplikasi Pengolahan Citra Digital

Aplikasi web interaktif untuk pengolahan citra digital dengan berbagai metode: Filtering, Restorasi, dan Enhancement.

## 🌟 Fitur

- **Filtering Image**: 
  - Gaussian Blur (dengan kontrol sigma dan kernel size)
  - Median Filter (untuk noise removal)
  - Sharpen Filter (untuk mempertajam gambar)
  
- **Restorasi Citra**:
  - Non-Local Means Denoising (NL-Means)
  - Wiener Filter (simple deconvolution)
  
- **Enhancement Citra**:
  - Histogram Equalization
  - CLAHE (Contrast Limited Adaptive Histogram Equalization)
  - Contrast Stretching

- Upload gambar format PNG/JPG
- Preview real-time
- Download hasil sebagai PNG

## 🚀 Deploy ke Streamlit Cloud

Untuk deploy aplikasi ini ke Streamlit Cloud (gratis):

1. Push semua file ke repository GitHub Anda
2. Buka [share.streamlit.io](https://share.streamlit.io)
3. Login dengan akun GitHub Anda
4. Klik "New app"
5. Pilih repository: `baktiihlasul/project-PCD`
6. Branch: `main`
7. Main file path: `app.py`
8. Klik "Deploy"!

Aplikasi Anda akan online dalam beberapa menit di URL seperti: `https://share.streamlit.io/baktiihlasul/project-pcd/main/app.py`

## 💻 Cara menjalankan (Windows - Local):

1. (Direkomendasikan) Buat virtual environment dan aktifkan:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Jalankan aplikasi:

```powershell
streamlit run app.py
```

Setelah aplikasi terbuka di browser, unggah gambar dan coba operasi di sidebar.
