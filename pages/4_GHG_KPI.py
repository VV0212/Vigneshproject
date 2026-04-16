import streamlit as st
import numpy as np

st.title("🌍 GHG & KPI Dashboard")

energy = np.load("energy_mlp_predictions.npy")
water = np.load("water_rf_predictions.npy")

ghg = energy * 0.48

water_intensity = water / energy
energy_intensity = energy / water
ghg_intensity = ghg / energy

st.subheader("KPIs")

col1, col2, col3 = st.columns(3)

col1.metric("Water Intensity", f"{water_intensity[0]:.4f}")
col2.metric("Energy Intensity", f"{energy_intensity[0]:.4f}")
col3.metric("GHG Intensity", f"{ghg_intensity[0]:.4f}")
