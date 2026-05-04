import streamlit as st
import pandas as pd

st.title("⚡ Energy Dashboard")

df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip().str.lower()
df["datetime"] = pd.to_datetime(df["datetime"])

# Filters (same as main)
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

filtered_df = df[
    (df["datetime"] >= pd.to_datetime(start_date)) &
    (df["datetime"] <= pd.to_datetime(end_date))
]

energy = filtered_df["energy_intensity_kwh_per_unit"]

# Summary
st.subheader("Energy Summary")
st.write(energy.describe())

# Data
st.subheader("Energy Data")
st.dataframe(energy.head(20))

# Chart
st.subheader("Energy Trend")
st.line_chart(filtered_df.set_index("datetime")["energy_intensity_kwh_per_unit"])
