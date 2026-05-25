import streamlit as st
import pandas as pd

# Read CSV file
df = pd.read_csv("data.csv")

# Show all column names from CSV
st.write(df.columns)

# Page title
st.title("⚡ Energy Intensity")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Check if column exists
if "energy_intensity_kwh_per_unit" in df.columns:

    # Show line chart
    st.line_chart(df["energy_intensity_kwh_per_unit"])

    # Statistics section
    st.subheader("Statistics")
    st.write(df["energy_intensity_kwh_per_unit"].describe())

else:
    st.error("Column 'energy_intensity_kwh_per_unit' not found in data.csv")
