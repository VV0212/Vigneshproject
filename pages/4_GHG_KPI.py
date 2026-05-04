import streamlit as st
import pandas as pd

st.title("🌍 GHG Dashboard")

df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip().str.lower()
df["datetime"] = pd.to_datetime(df["datetime"])

start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

filtered_df = df[
    (df["datetime"] >= pd.to_datetime(start_date)) &
    (df["datetime"] <= pd.to_datetime(end_date))
]

ghg = filtered_df["ghg_intensity_kg_co2e_per_unit"]

st.subheader("GHG Summary")
st.write(ghg.describe())

st.subheader("GHG Data")
st.dataframe(ghg.head(20))

st.subheader("GHG Trend")
st.line_chart(filtered_df.set_index("datetime")["ghg_intensity_kg_co2e_per_unit"])
