import streamlit as st
import pandas as pd

st.title("💧 Water Dashboard")

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

# Water data
water = filtered_df["water_pred_volume"]

# KPI
st.metric(
    "Latest Water",
    f"{water.iloc[-1]:.2f} m³"
)

# Summary
st.subheader("Water Summary")
st.write(water.describe())

# Data table
st.subheader("Water Data")

st.dataframe(
    filtered_df[[
        "datetime",
        "water_pred_volume"
    ]]
)

# Trend chart
st.subheader("Water Trend")

st.line_chart(
    filtered_df.set_index("datetime")[
        "water_pred_volume"
    ]
)
