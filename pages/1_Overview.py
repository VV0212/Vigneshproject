import streamlit as st
import numpy as np
import pandas as pd

st.title("📊 Overview Dashboard")

energy = np.load("energy_mlp_predictions.npy")
water = np.load("water_rf_predictions.npy")

ghg = energy * 0.48

df = pd.DataFrame({
    "Energy (kWh)": energy,
    "Water (m³)": water,
    "GHG (kg CO₂)": ghg
})

st.subheader("Summary")
st.write(df.describe())

st.dataframe(df.head(20))
