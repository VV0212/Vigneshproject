import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("⚡ Energy Prediction (MLP)")

energy = np.load("energy_mlp_predictions.npy")

st.metric("Latest Energy", f"{energy[0]:.2f} kWh")

fig, ax = plt.subplots()
ax.plot(energy)
st.pyplot(fig)
