# Aplikasi Pengolahan Citra Digital (sederhana)

Ini adalah aplikasi sederhana untuk eksperimen pengolahan citra digital: Filtering, Restorasi, dan Enhansi.

Fitur:
- Filtering: Gaussian, Median, Sharpen
- Restorasi: Denoise (NL-Means), Wiener (sederhana)
- Enhansi: Histogram Equalization, CLAHE, Contrast Stretch

Cara menjalankan (Windows):

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
