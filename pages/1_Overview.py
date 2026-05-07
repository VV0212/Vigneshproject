import streamlit as st
import pandas as pd

st.title("📊 Overview Dashboard")

# Load CSV
df = pd.read_csv("data.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# KPI columns
energy = df["energy_pred_kwh"]
water = df["water_pred_volume"]
ghg = df["ghg_pred_kg_co2e"]

# KPI cards
col1, col2, col3 = st.columns(3)

col1.metric(
    "⚡ Energy (kWh)",
    f"{energy.iloc[-1]:.2f}"
)

col2.metric(
    "💧 Water (m³)",
    f"{water.iloc[-1]:.2f}"
)

col3.metric(
    "🌍 GHG (kg CO2e)",
    f"{ghg.iloc[-1]:.2f}"
)

# Trend chart
st.subheader("Prediction Trends")

chart_df = pd.DataFrame({
    "Energy": energy,
    "Water": water,
    "GHG": ghg
})

st.line_chart(chart_df)
