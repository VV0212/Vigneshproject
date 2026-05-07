import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")

st.title("⚡ Energy Intensity")

st.line_chart(df["energy_intensity_kwh_per_unit"])

st.subheader("Statistics")
st.write(df["energy_intensity_kwh_per_unit"].describe())
