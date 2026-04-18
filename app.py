import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Sustainability Dashboard", layout="wide")

# ---------------- TITLE ----------------
st.title("🌍 Sustainability Dashboard")

# ---------------- LOAD DATA ----------------
url = "https://raw.githubusercontent.com/VV0212/Vigneshproject/main/data.csv"
df = pd.read_csv(url)

# Convert datetime
df["datetime"] = pd.to_datetime(df["datetime"])

# ---------------- SIDEBAR FILTER ----------------
st.sidebar.header("📅 Filter")

start_date = st.sidebar.date_input("Start Date", df["datetime"].min())
end_date = st.sidebar.date_input("End Date", df["datetime"].max())

# Apply filter
filtered_df = df[
    (df["datetime"] >= pd.to_datetime(start_date)) &
    (df["datetime"] <= pd.to_datetime(end_date))
]

# ---------------- SHOW SELECTED RANGE ----------------
st.write(f"Showing data from **{start_date}** to **{end_date}**")
st.write(f"Total records: {len(filtered_df)}")

# ---------------- KPI SECTION ----------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Energy (kWh)", round(filtered_df["energy_pred"].sum(), 2))
col2.metric("Total Water (m³)", round(filtered_df["water_pred"].sum(), 2))
col3.metric("Total GHG (kg CO2)", round(filtered_df["ghg_pred"].sum(), 2))

# ---------------- TRENDS ----------------
st.subheader("📈 Trends")

# Energy Trend
fig_energy = px.line(
    filtered_df,
    x="datetime",
    y="energy_pred",
    title="Energy Consumption Trend"
)
st.plotly_chart(fig_energy, use_container_width=True)

# Water Trend
fig_water = px.line(
    filtered_df,
    x="datetime",
    y="water_pred",
    title="Water Consumption Trend"
)
st.plotly_chart(fig_water, use_container_width=True)

# GHG Trend
fig_ghg = px.line(
    filtered_df,
    x="datetime",
    y="ghg_pred",
    title="GHG Emissions Trend"
)
st.plotly_chart(fig_ghg, use_container_width=True)

# ---------------- SUMMARY TABLE ----------------
st.subheader("📋 Summary Statistics")
st.write(filtered_df[["energy_pred", "water_pred", "ghg_pred"]].describe())

# ---------------- DATA PREVIEW ----------------
st.subheader("📄 Data Preview")
st.dataframe(filtered_df.head(20))
