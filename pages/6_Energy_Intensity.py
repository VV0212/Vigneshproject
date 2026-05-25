import streamlit as st
import pandas as pd

# Read CSV
df = pd.read_csv("data.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Title
st.title("⚡ Energy Intensity")

# Line chart
st.line_chart(df["energy_intensity_kwh_per_unit"])

# Statistics
st.subheader("Statistics")
st.write(df["energy_intensity_kwh_per_unit"].describe())
