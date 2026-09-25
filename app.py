import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi Halaman Dasar
# Menambahkan judul di tab browser, ikon, dan layout lebar
st.set_page_config(
    page_title="Dashboard Syndicate 1", 
    page_icon="✨", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Injeksi CSS Kustom untuk Estetika
st.markdown("""
    <style>
    /* Mengurangi jarak putih (padding) yang terlalu lebar di bagian atas Streamlit */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 1rem;
    }
    /* Mengatur gaya teks untuk Judul Utama */
    .title-text {
        font-size: 2.5rem;
        font-weight: 800;
        color: #1E3A8A; /* Warna teks biru gelap */
        text-align: center;
        margin-bottom: 0px;
    }
    /* Mengatur gaya teks untuk Subjudul */
    .subtitle-text {
        font-size: 1.2rem;
        color: #6B7280; /* Warna abu-abu elegan */
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Menampilkan Judul yang Sudah Dipercantik
st.markdown('<div class="title-text">Dashboard MK 6 - Week 3</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">✨ Presented by Syndicate 1 ✨</div>', unsafe_allow_html=True)

# Menambahkan garis horizontal tipis sebagai pemisah
st.divider() 

# 4. Membaca dan Menampilkan Dashboard HTML
# Menggunakan blok try-except agar tampilannya tetap rapi jika file tidak sengaja terhapus
try:
    with open("dashboard.html", "r", encoding="utf-8") as f:
        html_dashboard = f.read()
    
    # Menampilkan HTML (tinggi disesuaikan sedikit agar lebih lega)
    components.html(html_dashboard, height=850, scrolling=True)

except FileNotFoundError:
    st.error("⚠️ File 'dashboard.html' tidak ditemukan di dalam folder. Pastikan nama dan lokasinya sudah benar.")