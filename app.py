import streamlit as st
import numpy as np
import cv2
from PIL import Image
from skimage import restoration, exposure, img_as_ubyte
from skimage.restoration import denoise_nl_means, estimate_sigma

# ------------------ Konfigurasi Halaman ------------------
st.set_page_config(
    page_title="Aplikasi Pengolahan Citra Digital",
    layout="wide",
    page_icon="🖼️"
)

# ------------------ Custom CSS ------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #1e1e1e;
            color: white;
        }
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        h1, h2, h3 {
            color: #00adb5;
        }
        .css-1d391kg, .css-10trblm {
            color: white !important;
        }
        .stDownloadButton button {
            background-color: #00adb5;
            color: white;
            border-radius: 8px;
        }
        .stDownloadButton button:hover {
            background-color: #06c4cd;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------ Fungsi Utama ------------------
def load_image(uploaded_file):
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img

def to_rgb_for_display(img_bgr):
    return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

def apply_filter(img, method, ksize=3, sigma=1.0):
    if method == "Gaussian":
        k = int(ksize) if int(ksize) % 2 == 1 else int(ksize) + 1
        return cv2.GaussianBlur(img, (k, k), sigma)
    if method == "Median":
        k = int(ksize) if int(ksize) % 2 == 1 else int(ksize) + 1
        return cv2.medianBlur(img, k)
    if method == "Sharpen":
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
        return cv2.filter2D(img, -1, kernel)
    return img

def apply_restoration(img, method, param=3):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if method == "Denoise NL-Means":
        img_f = gray.astype(np.float32) / 255.0
        sigma_est = np.mean(estimate_sigma(img_f, channel_axis=None))
        patch_kw = dict(patch_size=5, patch_distance=6, fast_mode=True)
        den = denoise_nl_means(img_f, h=param * sigma_est, sigma=sigma_est, **patch_kw)
        den = img_as_ubyte(den)
        return cv2.cvtColor(den, cv2.COLOR_GRAY2BGR)
    if method == "Wiener (simple)":
        psf_size = max(3, int(param))
        psf = np.ones((psf_size, psf_size)) / (psf_size * psf_size)
        try:
            restored = restoration.wiener(gray.astype(np.float64), psf, balance=0.1)
            restored = np.clip(restored, 0, 255).astype(np.uint8)
            return cv2.cvtColor(restored, cv2.COLOR_GRAY2BGR)
        except Exception:
            return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    return img

def apply_enhancement(img, method, clip=2.0):
    if method == "Histogram Equalization":
        ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
        return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)
    if method == "CLAHE":
        ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=(8, 8))
        ycrcb[:, :, 0] = clahe.apply(ycrcb[:, :, 0])
        return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)
    if method == "Contrast Stretch":
        p2, p98 = np.percentile(img, (2, 98))
        stretched = exposure.rescale_intensity(img, in_range=(p2, p98))
        return stretched
    return img

# ------------------ UI ------------------
st.title("🖼️ Aplikasi Pengolahan Citra Digital")
st.markdown("### Filtering • Restorasi • Enhansi")
st.markdown("---")

with st.sidebar:
    st.header("⚙️ Kontrol Operasi")
    uploaded = st.file_uploader("Unggah gambar (PNG/JPG)", type=["png", "jpg", "jpeg"])
    mode = st.selectbox("Pilih operasi", ["Filtering", "Restoration", "Enhancement"])
    st.write("---")

if uploaded is None:
    st.info("⬅️ Silakan unggah gambar di sidebar untuk memulai.")
    st.stop()

img = load_image(uploaded)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📷 Gambar Asli")
    st.image(to_rgb_for_display(img), use_column_width=True)

with col2:
    st.subheader("✨ Hasil Proses")

    if mode == "Filtering":
        method = st.selectbox("Metode Filtering", ["Gaussian", "Median", "Sharpen"])
        ksize = st.slider("Kernel size (odd)", 1, 31, 3, step=2)
        sigma = st.slider("Sigma (Gaussian)", 0.0, 10.0, 1.0)
        res = apply_filter(img, method, ksize=ksize, sigma=sigma)

    elif mode == "Restoration":
        method = st.selectbox("Metode Restorasi", ["Denoise NL-Means", "Wiener (simple)"])
        param = st.slider("Parameter (h atau PSF size)", 1, 15, 3)
        res = apply_restoration(img, method, param=param)

    else:  # Enhancement
        method = st.selectbox("Metode Enhansi", ["Histogram Equalization", "CLAHE", "Contrast Stretch"])
        clip = st.slider("Clip limit (CLAHE)", 1.0, 10.0, 2.0)
        res = apply_enhancement(img, method, clip=clip)

    st.image(to_rgb_for_display(res), use_column_width=True)
    st.download_button("💾 Download Hasil (PNG)", cv2.imencode('.png', res)[1].tobytes(), file_name="result.png")
