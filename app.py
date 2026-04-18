import streamlit as st
import pandas as pd

# -------------------------
# LOAD DATA
# -------------------------
df = pd.read_csv("https://raw.githubusercontent.com/VV0212/Vigneshproject/main/data.csv")

# FIX COLUMN NAMES (VERY IMPORTANT)
df.columns = df.columns.str.strip().str.lower()

# Convert datetime
df["datetime"] = pd.to_datetime(df["datetime"])

# -------------------------
# SIDEBAR FILTERS
# -------------------------
st.sidebar.header("🔍 Filters")

start_date = st.sidebar.date_input("Start Date", df["datetime"].min().date())
end_date = st.sidebar.date_input("End Date", df["datetime"].max().date())

# Apply filter
filtered_df = df[
    (df["datetime"].dt.date >= start_date) &
    (df["datetime"].dt.date <= end_date)
]

# -------------------------
# TITLE
# -------------------------
st.title("🏭 Sustainability Dashboard")
st.markdown("### ⚡ Energy | 💧 Water | 🌍 GHG Emission")

# -------------------------
# KPI - PREDICTIONS
# -------------------------
st.subheader("📊 Predictions Overview")

col1, col2, col3 = st.columns(3)

col1.metric("⚡ Energy (kWh)", round(filtered_df["energy_pred_kwh"].mean(), 2))
col2.metric("💧 Water (m³)", round(filtered_df["water_pred_volume"].mean(), 2))
col3.metric("🌍 GHG (kg CO₂)", round(filtered_df["ghg_pred_kg_co2e"].mean(), 2))

# -------------------------
# KPI - INTENSITY
# -------------------------
st.subheader("📊 Intensity Metrics")

col4, col5, col6 = st.columns(3)

col4.metric("⚡ Energy Intensity", round(filtered_df["energy_intensity_kwh_per_unit"].mean(), 2))
col5.metric("💧 Water Intensity", round(filtered_df["water_intensity_volume_per_unit"].mean(), 2))
col6.metric("🌍 GHG Intensity", round(filtered_df["ghg_intensity_kg_co2e_per_unit"].mean(), 2))

st.divider()

# -------------------------
# PREDICTION GRAPHS
# -------------------------
st.subheader("📈 Prediction Trends")

st.markdown("### ⚡ Energy Prediction")
st.line_chart(filtered_df.set_index("datetime")["energy_pred_kwh"])

st.markdown("### 💧 Water Prediction")
st.line_chart(filtered_df.set_index("datetime")["water_pred_volume"])

st.markdown("### 🌍 GHG Prediction")
st.line_chart(filtered_df.set_index("datetime")["ghg_pred_kg_co2e"])

st.divider()

# -------------------------
# INTENSITY GRAPHS
# -------------------------
st.subheader("📉 Intensity Trends")

st.markdown("### ⚡ Energy Intensity")
st.line_chart(filtered_df.set_index("datetime")["energy_intensity_kwh_per_unit"])

st.markdown("### 💧 Water Intensity")
st.line_chart(filtered_df.set_index("datetime")["water_intensity_volume_per_unit"])

st.markdown("### 🌍 GHG Intensity")
st.line_chart(filtered_df.set_index("datetime")["ghg_intensity_kg_co2e_per_unit"])

# -------------------------
# DATA TABLE
# -------------------------
st.subheader("📂 Filtered Data")
st.dataframe(filtered_df.head(50))
