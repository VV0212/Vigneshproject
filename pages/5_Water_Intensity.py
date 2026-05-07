import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")

st.title("💧 Water Intensity")

st.line_chart(df["water_intensity_volume_per_unit"])

st.subheader("Statistics")
st.write(df["water_intensity_volume_per_unit"].describe())
