import streamlit as st
import pandas as pd
from src.data_loader import load_data
from src.charts import plot_ph, plot_gas, plot_temperature
from src.utils import filter_data
import base64

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

st.markdown("## Monitoring Dashboard")

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

# ===== Grand Design Section =====
st.markdown("## 📘 IoT Grand Design")

st.markdown("""
### Key Points
- **Objectives:** Maintain digester pH at 6.8–7.2 with automatic actions if thresholds are crossed.  
- **Architecture:** Sensors → Controller → MQTT → Database → Dashboard → Alerts.  
- **Control Logic:**  
  • Recovery (pH < 6.6): Stop feeding, buffer dosing.  
  • Steady (6.8–7.2): Micro-feeding + cyclic agitation.  
  • Underfed (pH > 7.5): Incremental feeding.  
- **Roadmap:** MVP with ESP32 → Pilot scale with Node-RED/InfluxDB → Industrial with PLC & AI.
""")

# Show block diagram image
st.image("data/block_diagram.png", caption="IoT System Block Diagram")

# Button to display PDF in popup (iframe)
with open("data/IoT_Grand_Design.pdf", "rb") as f:
    pdf_bytes = f.read()
    b64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

if st.button("📄 View Full Grand Design PDF"):
    pdf_display = f'<iframe src="data:application/pdf;base64,{b64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
