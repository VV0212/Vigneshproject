import streamlit as st
import pandas as pd

st.title("📊 Overview Dashboard")

# Load data
df = pd.read_csv("data.csv")

energy = df["energy_pred"]
water = df["water_pred"]
ghg = df["ghg_pred"]

# Create dataframe
df_display = pd.DataFrame({
    "Energy (kWh)": energy,
    "Water (m³)": water,
    "GHG (kg CO2)": ghg
})

st.subheader("Summary")
st.write(df_display.describe())

st.dataframe(df_display.head(20))

st.dataframe(df.head(20))
