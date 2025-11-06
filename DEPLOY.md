# 🖼️ Aplikasi Pengolahan Citra Digital

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)

Aplikasi web interaktif untuk pengolahan citra digital dengan metode Filtering, Restorasi, dan Enhancement.

## 📋 Panduan Deploy ke Streamlit Cloud

### Langkah 1: Persiapan File
Pastikan semua file sudah ada di repository GitHub Anda:
- ✅ `app.py` (aplikasi utama)
- ✅ `requirements.txt` (dependencies)
- ✅ `.streamlit/config.toml` (konfigurasi tema)
- ✅ `.gitignore`

### Langkah 2: Push ke GitHub

```powershell
# Pastikan Anda di folder project
cd "d:\UNP\Tugas\Pengolahan Citra Digital\p"

# Add semua file
git add .

# Commit
git commit -m "Deploy: Aplikasi Pengolahan Citra Digital ready for Streamlit Cloud"

# Push ke GitHub
git push origin main
```

### Langkah 3: Deploy di Streamlit Cloud

1. **Buka** [share.streamlit.io](https://share.streamlit.io)
2. **Login** dengan akun GitHub Anda
3. **Klik** tombol "New app" (atau "Create app")
4. **Isi form deployment**:
   - Repository: `baktiihlasul/project-PCD`
   - Branch: `main`
   - Main file path: `app.py`
   - App URL (optional): pilih nama custom atau biarkan default
5. **Klik** "Deploy"!

⏱️ **Proses deployment biasanya memakan waktu 2-5 menit.**

### Langkah 4: Akses Aplikasi Online

Setelah selesai, Anda akan mendapat URL seperti:
```
https://baktiihlasul-project-pcd-app-xxxxx.streamlit.app
```

Bagikan URL tersebut kepada siapa saja untuk menggunakan aplikasi!

## 🎨 Fitur Aplikasi

- **Filtering**: Gaussian, Median, Sharpen
- **Restorasi**: NL-Means Denoising, Wiener Filter
- **Enhancement**: Histogram Equalization, CLAHE, Contrast Stretch
- Upload gambar PNG/JPG
- Download hasil processing

## 🔧 Troubleshooting

**Jika deployment gagal:**
1. Cek apakah semua file sudah ter-push ke GitHub
2. Pastikan `requirements.txt` menggunakan `opencv-python-headless` (bukan `opencv-python`)
3. Tunggu beberapa menit dan coba lagi
4. Cek logs di Streamlit Cloud dashboard

**Jika aplikasi lambat:**
- Streamlit Cloud versi gratis memiliki resource terbatas
- Untuk performa lebih baik, bisa upgrade ke Streamlit Cloud Pro

## 💻 Development Local (Optional)

Jika ingin test di localhost:

```powershell
# Install dependencies
pip install -r requirements.txt

# Run aplikasi
streamlit run app.py
```

Buka browser ke `http://localhost:8501`

---

**Dibuat dengan ❤️ menggunakan Streamlit**
