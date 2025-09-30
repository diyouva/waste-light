import streamlit as st
import plotly.express as px

COLOR_MAP = {
    "Recovery": "#E74C3C",   # merah
    "Steady": "#27AE60",     # hijau
    "Underfed": "#F39C12"    # oranye
}

def plot_ph(df):
    fig = px.line(df, x="timestamp", y="pH", color="state",
                  color_discrete_map=COLOR_MAP,
                  title="pH over Time",
                  labels={"pH": "pH", "timestamp": "Time"})
    fig.add_hrect(y0=6.8, y1=7.2, fillcolor="#27AE60", opacity=0.2, line_width=0)
    st.plotly_chart(fig, use_container_width=True)

def plot_gas(df):
    fig = px.line(df, x="timestamp", y="gas_flow_Lh",
                  title="Gas Flow (L/h)",
                  labels={"gas_flow_Lh": "Gas Flow (L/h)", "timestamp": "Time"},
                  line_shape="spline", color_discrete_sequence=["#004B87"])
    st.plotly_chart(fig, use_container_width=True)

def plot_temperature(df):
    fig = px.line(df, x="timestamp", y="temperature_C",
                  title="Temperature (°C)",
                  labels={"temperature_C": "Temp (°C)", "timestamp": "Time"},
                  line_shape="spline", color_discrete_sequence=["#00A86B"])
    st.plotly_chart(fig, use_container_width=True)
