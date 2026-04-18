import streamlit as st
import pandas as pd

st.title("💧 Water Dashboard")

# Load data
df = pd.read_csv("data.csv")

water = df["water_pred"]

# Summary
st.subheader("Water Summary")
st.write(water.describe())

# Data preview
st.subheader("Water Data")
st.dataframe(water.head(20))

# Trend chart
st.subheader("Water Trend")
st.line_chart(water)
