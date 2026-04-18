import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Sustainability Dashboard", layout="wide")

st.title("🌍 Sustainability Dashboard")

# -------------------- LOAD DATA --------------------
url = "https://raw.githubusercontent.com/VV0212/Vigneshproject/main/data.csv"
df = pd.read_csv(url)

# Convert datetime
df["datetime"] = pd.to_datetime(df["datetime"])

# -------------------- SIDEBAR FILTER --------------------
st.sidebar.header("📅 Filter")

start_date = st.sidebar.date_input("Start Date", df["datetime"].min())
end_date = st.sidebar.date_input("End Date", df["datetime"].max())

# Apply filter
filtered_df = df[
    (df["datetime"] >= pd.to_datetime(start_date)) &
    (df["datetime"] <= pd.to_datetime(end_date))
].copy()

# SORT (IMPORTANT FIX)
filtered_df = filtered_df.sort_values(by="datetime")

# -------------------- KPI METRICS --------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Energy (kWh)", round(filtered_df["energy_pred"].sum(), 2))
col2.metric("Total Water (m³)", round(filtered_df["water_pred"].sum(), 2))
col3.metric("Total GHG (kg CO2)", round(filtered_df["ghg_pred"].sum(), 2))

# -------------------- ENERGY GRAPH --------------------
st.subheader("⚡ Energy: Actual vs Predicted")

fig_energy = px.line(
    filtered_df,
    x="datetime",
    y=["energy_actual", "energy_pred"],
    labels={"value": "Energy (kWh)", "variable": "Legend"},
)

fig_energy.update_layout(
    xaxis_title="Date",
    yaxis_title="Energy (kWh)",
    legend_title=""
)

st.plotly_chart(fig_energy, use_container_width=True)

# -------------------- WATER GRAPH --------------------
st.subheader("💧 Water: Actual vs Predicted")

fig_water = px.line(
    filtered_df,
    x="datetime",
    y=["water_actual", "water_pred"],
    labels={"value": "Water (m³)", "variable": "Legend"},
)

fig_water.update_layout(
    xaxis_title="Date",
    yaxis_title="Water (m³)",
    legend_title=""
)

st.plotly_chart(fig_water, use_container_width=True)

# -------------------- GHG GRAPH --------------------
st.subheader("🌍 GHG: Actual vs Predicted")

fig_ghg = px.line(
    filtered_df,
    x="datetime",
    y=["ghg_actual", "ghg_pred"],
    labels={"value": "GHG (kg CO2)", "variable": "Legend"},
)

fig_ghg.update_layout(
    xaxis_title="Date",
    yaxis_title="GHG (kg CO2)",
    legend_title=""
)

st.plotly_chart(fig_ghg, use_container_width=True)
