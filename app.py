import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Sustainability Dashboard", layout="wide")

st.title("🌍 Sustainability Prediction Dashboard")

# ---------------- LOAD DATA ----------------
url = "https://raw.githubusercontent.com/VV0212/Vigneshproject/main/data.csv"

df = pd.read_csv(url)

# ---------------- CLEAN COLUMNS ----------------
df.columns = df.columns.str.strip().str.lower()

# ---------------- HANDLE DATETIME ----------------
if "datetime" in df.columns:
    df["date"] = pd.to_datetime(df["datetime"], errors="coerce")
elif "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
else:
    st.error(f"No datetime column found. Columns: {df.columns}")
    st.stop()

# ---------------- CHECK PREDICTIONS ----------------
required_cols = ["energy_pred", "water_pred"]

for col in required_cols:
    if col not in df.columns:
        st.error(f"Missing column: {col}")
        st.write("Available columns:", df.columns)
        st.stop()

# ---------------- PREPARE DATA ----------------
df["energy"] = df["energy_pred"]
df["water"] = df["water_pred"]

# ---------------- GHG ----------------
EMISSION_FACTOR = 0.48
df["ghg"] = df["energy"] * EMISSION_FACTOR

# ---------------- FILTER ----------------
st.sidebar.header("Filter")

start_date = st.sidebar.date_input("Start Date", df["date"].min())
end_date = st.sidebar.date_input("End Date", df["date"].max())

filtered_df = df[
    (df["date"] >= pd.to_datetime(start_date)) &
    (df["date"] <= pd.to_datetime(end_date))
]

if filtered_df.empty:
    st.warning("No data available")
    st.stop()

# ---------------- KPI ----------------
latest = filtered_df.iloc[-1]

energy_val = latest["energy"]
water_val = latest["water"]
ghg_val = latest["ghg"]

energy_intensity = energy_val / water_val if water_val != 0 else 0
ghg_intensity = ghg_val / energy_val if energy_val != 0 else 0

col1, col2, col3 = st.columns(3)

col1.metric("Energy (kWh)", f"{energy_val:.2f}")
col2.metric("Water (m³)", f"{water_val:.2f}")
col3.metric("GHG (kg CO2)", f"{ghg_val:.2f}")

col4, col5 = st.columns(2)

col4.metric("Energy Intensity (kWh/m³)", f"{energy_intensity:.3f}")
col5.metric("GHG Intensity (kg CO2/kWh)", f"{ghg_intensity:.3f}")

# ---------------- CHARTS ----------------
st.subheader("Trends")

fig1 = px.line(filtered_df, x="date", y="energy", title="Energy Trend")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.line(filtered_df, x="date", y="water", title="Water Trend")
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.line(filtered_df, x="date", y="ghg", title="GHG Trend")
st.plotly_chart(fig3, use_container_width=True)

# ---------------- TABLE ----------------
st.subheader("Data Preview")
st.dataframe(filtered_df.tail(20))
