import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Sustainability Dashboard", layout="wide")

st.title("🌍 Sustainability Prediction Dashboard")

# ---------------- LOAD DATA ----------------
url = "https://raw.githubusercontent.com/VV0212/Vigneshproject/main/data.csv"
df = pd.read_csv(url)

# ---------------- CHECK REQUIRED COLUMNS ----------------
required_cols = ["datetime", "energy_pred", "water_pred", "ghg_pred"]

missing = [col for col in required_cols if col not in df.columns]

if missing:
    st.error(f"Missing columns: {missing}")
    st.stop()

# ---------------- CLEAN DATA ----------------
df["datetime"] = pd.to_datetime(df["datetime"])
df = df.sort_values("datetime")

# ---------------- SIDEBAR FILTER ----------------
st.sidebar.header("Filter")

start_date = st.sidebar.date_input("Start Date", df["datetime"].min())
end_date = st.sidebar.date_input("End Date", df["datetime"].max())

df = df[
    (df["datetime"].dt.date >= start_date) &
    (df["datetime"].dt.date <= end_date)
]

# ---------------- KPIs ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Energy (kWh)", f"{df['energy_pred'].mean():.2f}")
col2.metric("Water (m³)", f"{df['water_pred'].mean():.2f}")
col3.metric("GHG (kg CO2)", f"{df['ghg_pred'].mean():.2f}")
col4.metric("GHG Intensity", "0.480")

st.markdown("---")

# ---------------- SMOOTH DATA ----------------
df["energy_smooth"] = df["energy_pred"].rolling(10).mean()
df["water_smooth"] = df["water_pred"].rolling(10).mean()
df["ghg_smooth"] = df["ghg_pred"].rolling(10).mean()

# ---------------- GRAPHS ----------------
st.subheader("📈 Trends")

# ENERGY
fig1 = px.line(df, x="datetime", y=["energy_pred", "energy_smooth"],
               title="Energy Trend")
st.plotly_chart(fig1, use_container_width=True)

# WATER
fig2 = px.line(df, x="datetime", y=["water_pred", "water_smooth"],
               title="Water Trend")
st.plotly_chart(fig2, use_container_width=True)

# GHG
fig3 = px.line(df, x="datetime", y=["ghg_pred", "ghg_smooth"],
               title="GHG Trend")
st.plotly_chart(fig3, use_container_width=True)

# ---------------- TABLE ----------------
st.subheader("📊 Data Preview")
st.dataframe(df.tail(20))
