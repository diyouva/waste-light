import streamlit as st
import pandas as pd
from src.data_loader import load_data
from src.charts import plot_ph, plot_gas, plot_temperature
from src.utils import filter_data

st.set_page_config(page_title="Waste-to-Energy IoT Dashboard", layout="wide")

# ===== THEME =====
st.markdown("""
    <style>
    body { background-color: white; }
    h1, h2, h3, h4 { color: #004B87; }
    </style>
""", unsafe_allow_html=True)

# ===== LANDING PAGE =====
st.title("🌱 Waste Food to Energy – IoT Automation")
st.image("data/img1.png")

st.markdown("""
## Latar Belakang
Limbah makanan adalah salah satu penyumbang emisi karbon terbesar. Dalam pitch ini, ide yang diusulkan adalah **mengubah waste food menjadi energi** melalui proses biogas digester.  

## Masalah
- Volume limbah makanan tinggi.
- Ketidakstabilan pH pada reaktor biogas menyebabkan kegagalan produksi energi.
- Kurangnya sistem monitoring otomatis membuat operator kesulitan mengontrol.
""")

st.image("data/img2.png", caption="Masalah utama yang diidentifikasi")

st.markdown("""
## Solusi
Menggunakan **IoT system** untuk:
- Monitoring pH secara real-time.
- Mengontrol pompa feeding & buffering secara otomatis.
- Menyediakan dashboard terintegrasi yang user-friendly.
""")

st.image("data/img3.png", caption="Solusi IoT dengan kontrol otomatis pH")

# ===== LOAD DATA =====
df = load_data()

st.markdown("## Monitoring Data (Dummy Simulation)")

# Sidebar Filters
st.sidebar.header("Filters")
start_date = st.sidebar.date_input("Start date", df["timestamp"].min().date())
end_date = st.sidebar.date_input("End date", df["timestamp"].max().date())
state_filter = st.sidebar.selectbox("State", ["All"] + sorted(df["state"].unique()))

filtered_df = filter_data(df, pd.to_datetime(start_date), pd.to_datetime(end_date), state_filter)

# ===== Charts =====
st.subheader("pH Monitoring")
plot_ph(filtered_df)

st.subheader("Gas Production")
plot_gas(filtered_df)

st.subheader("Temperature")
plot_temperature(filtered_df)

# ===== Pump Activity =====
st.subheader("Pump Activity Log")
st.dataframe(filtered_df[["timestamp", "state", "feed_pump_ml", "buffer_pump_ml"]])

st.markdown("""
## Dampak
- Mengurangi limbah makanan.
- Menghasilkan energi terbarukan.
- Menurunkan biaya operasional reaktor.

## Next Step
- Pilot project skala UMKM/komunitas.
- Integrasi sensor tambahan (ORP, gas metana).
- Pengembangan AI untuk prediksi feeding.
""")

st.image("data/img4.png", caption="Roadmap implementasi")

st.markdown("""
---
📌 Dashboard ini dirancang agar **narasi dari awal sampai akhir jelas**: mulai dari masalah, solusi, implementasi IoT, hingga data simulasi dan dampak.  
Semua visual & konten diambil dari pitch PDF.
""")
