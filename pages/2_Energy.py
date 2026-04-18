import streamlit as st
import pandas as pd

st.title("⚡ Energy Dashboard")

# Load data
df = pd.read_csv("data.csv")

energy = df["energy_pred"]

# Show summary
st.subheader("Energy Summary")
st.write(energy.describe())

# Show data
st.subheader("Energy Data")
st.dataframe(energy.head(20))

# Optional: Line chart
st.subheader("Energy Trend")
st.line_chart(energy)
