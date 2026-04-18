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

df["date"] = df["datetime"].dt.date

min_date = df["date"].min()
max_date = df["date"].max()

# Session state init
if "start_date" not in st.session_state:
    st.session_state.start_date = min_date

if "end_date" not in st.session_state:
    st.session_state.end_date = max_date

# Form
with st.sidebar.form("filter_form"):
    start_date = st.date_input("Start Date", st.session_state.start_date)
    end_date = st.date_input("End Date", st.session_state.end_date)

    submit = st.form_submit_button("Apply Filter")

# Update session state
if submit:
    st.session_state.start_date = start_date
    st.session_state.end_date = end_date

# Apply filter ALWAYS
filtered_df = df[
    (df["date"] >= st.session_state.start_date) &
    (df["date"] <= st.session_state.end_date)
].copy()

filtered_df = filtered_df.sort_values(by="datetime")

# Always sort
filtered_df = filtered_df.sort_values(by="datetime")

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
