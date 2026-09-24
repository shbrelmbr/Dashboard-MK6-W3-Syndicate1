import streamlit as st
import streamlit.components.v1 as components

# Membuat tampilan layar menjadi lebar
st.set_page_config(layout="wide")
st.title("Dashboard MK 6 - Week 3 - Syndicate 1")

# Pastikan nama "dashboard.html" sesuai dengan nama file HTML Anda
with open("dashboard.html", "r", encoding="utf-8") as f:
    html_dashboard = f.read()

components.html(html_dashboard, height=800, scrolling=True)