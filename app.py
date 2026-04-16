import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sustainability Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌍 Sustainability Prediction Dashboard")

# ---------------- LOAD DATA ----------------
energy = np.load("energy_mlp_predictions.npy")
water = np.load("water_rf_predictions.npy")

# GHG emission factor (you used this earlier)
EMISSION_FACTOR = 0.48  # kg CO2 per kWh

ghg = energy * EMISSION_FACTOR

# Create date column
dates = pd.date_range(start="2024-01-01", periods=len(energy))

df = pd.DataFrame({
    "Date": dates,
    "Energy (kWh)": energy,
    "Water (m³)": water,
    "GHG (kg CO2)": ghg
})

# ---------------- SIDEBAR FILTER ----------------
st.sidebar.header("📅 Filters")

start_date = st.sidebar.date_input("Start Date", df["Date"].min())
end_date = st.sidebar.date_input("End Date", df["Date"].max())

filtered_df = df[(df["Date"] >= pd.to_datetime(start_date)) & 
                 (df["Date"] <= pd.to_datetime(end_date))]

# ---------------- KPI CALCULATIONS ----------------
latest = filtered_df.iloc[-1]

energy_val = latest["Energy (kWh)"]
water_val = latest["Water (m³)"]
ghg_val = latest["GHG (kg CO2)"]

water_intensity = water_val / energy_val
energy_intensity = energy_val / water_val
ghg_intensity = ghg_val / energy_val

# ---------------- KPI CARDS ----------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("⚡ Energy (kWh)", f"{energy_val:.2f}")
col2.metric("💧 Water (m³)", f"{water_val:.2f}")
col3.metric("🌍 GHG (kg CO2)", f"{ghg_val:.2f}")

st.markdown("---")

col4, col5, col6 = st.columns(3)

col4.metric("💧 Water Intensity (m³/kWh)", f"{water_intensity:.4f}")
col5.metric("⚡ Energy Intensity (kWh/m³)", f"{energy_intensity:.4f}")
col6.metric("🌍 GHG Intensity (kg CO2/kWh)", f"{ghg_intensity:.4f}")

# ---------------- CHARTS ----------------

st.markdown("## 📈 Trends")

# Energy Chart
st.subheader("⚡ Energy Prediction (MLP)")
fig1 = px.line(filtered_df, x="Date", y="Energy (kWh)", title="Energy Trend")
st.plotly_chart(fig1, use_container_width=True)

# Water Chart
st.subheader("💧 Water Prediction (Random Forest)")
fig2 = px.line(filtered_df, x="Date", y="Water (m³)", title="Water Trend")
st.plotly_chart(fig2, use_container_width=True)

# GHG Chart
st.subheader("🌍 GHG Emissions (Derived)")
fig3 = px.line(filtered_df, x="Date", y="GHG (kg CO2)", title="GHG Trend")
st.plotly_chart(fig3, use_container_width=True)

# ---------------- DATA TABLE ----------------
st.markdown("## 📋 Data Table")
st
