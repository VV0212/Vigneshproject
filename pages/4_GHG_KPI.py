import streamlit as st
import pandas as pd

st.title("🌍 GHG & KPI Dashboard")

# Load data
df = pd.read_csv("data.csv")

energy = df["energy_pred"]
ghg = df["ghg_pred"]

# KPIs
st.subheader("Key Metrics")

col1, col2 = st.columns(2)

col1.metric("Total Energy (kWh)", round(energy.sum(), 2))
col2.metric("Total GHG (kg CO2)", round(ghg.sum(), 2))

# Summary
st.subheader("GHG Summary")
st.write(ghg.describe())

# Data preview
st.subheader("GHG Data")
st.dataframe(ghg.head(20))

# Trend chart
st.subheader("GHG Trend")
st.line_chart(ghg)
