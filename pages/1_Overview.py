import streamlit as st
import pandas as pd

st.title("📊 Overview Dashboard")

# Load CSV
df = pd.read_csv("data.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# DEBUG: show all available columns
st.write("Available Columns:", df.columns.tolist())

# Assign columns
energy = df["energy_intensity_kwh_per_unit"]
water = df["water_intensity_volume_per_unit"]

# Try possible GHG column names
if "ghg_intensity_kgco2_per_unit" in df.columns:
    ghg = df["ghg_intensity_kgco2_per_unit"]

elif "ghg_emissions_kgco2_per_unit" in df.columns:
    ghg = df["ghg_emissions_kgco2_per_unit"]

elif "ghg_pred" in df.columns:
    ghg = df["ghg_pred"]

else:
    st.error("GHG column not found in data.csv")
    st.stop()

# KPI Cards
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

# Trends
st.subheader("Prediction Trends")

chart_df = pd.DataFrame({
    "Energy": energy,
    "Water": water,
    "GHG": ghg
})

st.line_chart(chart_df)
