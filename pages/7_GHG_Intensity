import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")

st.title("🌍 GHG Intensity")

st.line_chart(df["ghg_intensity_kg_co2e_per_unit"])

st.subheader("Statistics")
st.write(df["ghg_intensity_kg_co2e_per_unit"].describe())
