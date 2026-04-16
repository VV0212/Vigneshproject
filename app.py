import streamlit as st

st.set_page_config(page_title="Sustainability Dashboard", layout="wide")

st.title("🌍 Sustainability Prediction Dashboard")

st.markdown("""
### Welcome!

Use the sidebar to navigate:

- 📊 Overview
- ⚡ Energy Prediction (MLP)
- 💧 Water Prediction (Random Forest)
- 🌍 GHG Emissions & KPIs
""")
