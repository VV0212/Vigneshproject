import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("💧 Water Prediction (Random Forest)")

water = np.load("water_rf_predictions.npy")

st.metric("Latest Water", f"{water[0]:.2f} m³")

fig, ax = plt.subplots()
ax.plot(water)
st.pyplot(fig)
