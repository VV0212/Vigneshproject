import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Sustainability Dashboard", layout="wide")

st.title("🌍 Sustainability Dashboard")

# -------------------- LOAD DATA --------------------
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/VV0212/Vigneshproject/main/data.csv"
    df = pd.read_csv(url)
    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.sort_values(by="datetime")

    # Create smooth columns
    df["energy_smooth"] = df["energy_pred"].rolling(window=5).mean()
    df["water_smooth"] = df["water_pred"].rolling(window=5).mean()
    df["ghg_smooth"] = df["ghg_pred"].rolling(window=5).mean()

    return df

df = load_data()

# -------------------- SIDEBAR FILTER --------------------
st.sidebar.header("📅 Filter")

# Convert to DATE (not datetime)
df["date"] = df["datetime"].dt.date

min_date = df["date"].min()
max_date = df["date"].max()

start_date = st.sidebar.date_input("Start Date", min_date)
end_date = st.sidebar.date_input("End Date", max_date)

# Apply filter using DATE (not datetime)
filtered_df = df[
    (df["date"] >= start_date) &
    (df["date"] <= end_date)
].copy()

# IMPORTANT: sort again
filtered_df = filtered_df.sort_values(by="datetime")

# -------------------- DEBUG (REMOVE LATER) --------------------
# st.write("Filtered rows:", len(filtered_df))

# -------------------- KPI METRICS --------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Energy (kWh)", round(filtered_df["energy_pred"].sum(), 2))
col2.metric("Total Water (m³)", round(filtered_df["water_pred"].sum(), 2))
col3.metric("Total GHG (kg CO2)", round(filtered_df["ghg_pred"].sum(), 2))

# -------------------- ENERGY GRAPH --------------------
st.subheader("⚡ Energy: Predicted vs Smooth Trend")

fig_energy = px.line(
    filtered_df,
    x="datetime",
    y=["energy_pred", "energy_smooth"],
)

st.plotly_chart(fig_energy, use_container_width=True)

# -------------------- WATER GRAPH --------------------
st.subheader("💧 Water: Predicted vs Smooth Trend")

fig_water = px.line(
    filtered_df,
    x="datetime",
    y=["water_pred", "water_smooth"],
)

st.plotly_chart(fig_water, use_container_width=True)

# -------------------- GHG GRAPH --------------------
st.subheader("🌍 GHG: Predicted vs Smooth Trend")

fig_ghg = px.line(
    filtered_df,
    x="datetime",
    y=["ghg_pred", "ghg_smooth"],
)

st.plotly_chart(fig_ghg, use_container_width=True)
