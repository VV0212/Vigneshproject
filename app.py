import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Water & Energy Dashboard")

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("data.csv")

# Convert datetime
df["datetime"] = pd.to_datetime(df["datetime"])
df = df.set_index("datetime")

# =========================
# SIDEBAR FILTER
# =========================

st.sidebar.header("Filters")

start_date = st.sidebar.date_input("Start Date", df.index.min())
end_date = st.sidebar.date_input("End Date", df.index.max())

filtered_df = df.loc[start_date:end_date]

# =========================
# VISUALIZATIONS
# =========================

st.subheader("Water Volume Over Time")
fig1 = px.line(filtered_df, x=filtered_df.index, y="volume")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Energy Consumption Over Time")
fig2 = px.line(filtered_df, x=filtered_df.index, y="total_energy_kwh")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Temperature Trend")
fig3 = px.line(filtered_df, x=filtered_df.index, y="temperature_c")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Humidity Trend")
fig4 = px.line(filtered_df, x=filtered_df.index, y="humidity_percent")
st.plotly_chart(fig4, use_container_width=True)

# =========================
# DATA VIEW
# =========================

with st.expander("View Raw Data"):
    st.dataframe(filtered_df)
