import streamlit as st
import pandas as pd

st.title("🌍 GHG KPI Dashboard")

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

# Check if dataframe is empty
if filtered_df.empty:
    st.warning("No data available for selected date range.")
    st.stop()

# GHG data
ghg = filtered_df["ghg_pred_kg_co2e"]

# KPI
st.metric(
    "Latest GHG",
    f"{ghg.iloc[-1]:.2f} kg CO2e"
)

# Summary
st.subheader("GHG Summary")
st.write(ghg.describe())

# Data table
st.subheader("GHG Data")

st.dataframe(
    filtered_df[[
        "datetime",
        "ghg_pred_kg_co2e"
    ]]
)

# Trend chart
st.subheader("GHG Trend")

st.line_chart(
    filtered_df.set_index("datetime")[
        "ghg_pred_kg_co2e"
    ]
)
