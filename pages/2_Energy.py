import streamlit as st
import pandas as pd

st.title("⚡ Energy Dashboard")

# Load CSV
df = pd.read_csv("data.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Convert datetime
df["datetime"] = pd.to_datetime(df["datetime"])

# Sidebar date filters
start_date = st.sidebar.date_input(
    "Start Date",
    value=df["datetime"].min().date()
)

end_date = st.sidebar.date_input(
    "End Date",
    value=df["datetime"].max().date()
)

# Filter dataframe
filtered_df = df[
    (df["datetime"] >= pd.to_datetime(start_date)) &
    (df["datetime"] <= pd.to_datetime(end_date))
]

# Check if empty
if filtered_df.empty:
    st.warning("No data available for selected date range.")
    st.stop()

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

# Data table
st.subheader("Energy Data")

st.dataframe(
    filtered_df[[
        "datetime",
        "energy_pred_kwh"
    ]]
)

# Trend chart
st.subheader("Energy Trend")

st.line_chart(
    filtered_df.set_index("datetime")[
        "energy_pred_kwh"
    ]
)
