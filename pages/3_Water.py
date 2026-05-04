import streamlit as st
import pandas as pd

st.title("💧 Water Dashboard")

df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip().str.lower()
df["datetime"] = pd.to_datetime(df["datetime"])

start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

filtered_df = df[
    (df["datetime"] >= pd.to_datetime(start_date)) &
    (df["datetime"] <= pd.to_datetime(end_date))
]

water = filtered_df["water_intensity_volume_per_unit"]

st.subheader("Water Summary")
st.write(water.describe())

st.subheader("Water Data")
st.dataframe(water.head(20))

st.subheader("Water Trend")
st.line_chart(filtered_df.set_index("datetime")["water_intensity_volume_per_unit"])
