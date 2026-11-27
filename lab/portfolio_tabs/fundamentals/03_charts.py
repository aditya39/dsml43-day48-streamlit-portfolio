import streamlit as st
import pandas as pd
import numpy as np

rng = np.random.default_rng(42)
dates = pd.date_range("2024-01-01", periods=60)
data = pd.DataFrame({
    "product_A": rng.integers(50, 200, 60).cumsum(),
    "product_B": rng.integers(30, 150, 60).cumsum(),
    "product_C": rng.integers(20, 100, 60).cumsum(),
}, index=dates)

st.title("Sales Trends Over Time")
st.line_chart(data)

st.title("Total Sales by Product")
total_sales = data.sum()
st.bar_chart(total_sales)
