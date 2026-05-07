import streamlit as st
import pandas as pd

st.title("📊 Overview Dashboard")

df = pd.read_csv("data.csv")

df.columns = df.columns.str.strip().str.lower()

energy = df["energy_intensity_kwh_per_unit"]
water = df["water_intensity_volume_per_unit"]
ghg = df["ghg_intensity_kgco2_per_unit"]

st.subheader("Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "⚡ Energy",
    f"{energy.iloc[-1]:.2f}"
)

col2.metric(
    "💧 Water",
    f"{water.iloc[-1]:.2f}"
)

col3.metric(
    "🌍 GHG",
    f"{ghg.iloc[-1]:.2f}"
)

st.subheader("Trends")

st.line_chart(df[[
    "energy_intensity_kwh_per_unit",
    "water_intensity_volume_per_unit",
    "ghg_intensity_kgco2_per_unit"
]])
