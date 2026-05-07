import streamlit as st
import pandas as pd

st.title("⚡ Energy Dashboard")

# Load CSV
df = pd.read_csv("data.csv")

# Clean columns
df.columns = df.columns.str.strip().str.lower()

# Convert datetime
df["datetime"] = pd.to_datetime(df["datetime"])

# Sidebar filters
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

# Filter dataframe
filtered_df = df[
    (df["datetime"] >= pd.to_datetime(start_date)) &
    (df["datetime"] <= pd.to_datetime(end_date))
]

# Energy data
energy = filtered_df["energy_pred_kwh"]

# KPI
st.metric(
    "Latest Energy",
    f"{energy.iloc[-1]:.2f} kWh"
)

# Summary
st.subheader("Energy Summary")
st.write(energy.describe())

# Table
st.subheader("Energy Data")
st.dataframe(filtered_df[[
    "datetime",
    "energy_pred_kwh"
]].head(20))

# Chart
st.subheader("Energy Trend")

st.line_chart(
    filtered_df.set_index("datetime")[
        "energy_pred_kwh"
    ]
)
