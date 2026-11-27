import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# data yang sama dengan 03_charts.py
rng = np.random.default_rng(42)
dates = pd.date_range("2024-01-01", periods=60)
data = pd.DataFrame({
    "product_A": rng.integers(50, 200, 60).cumsum(),
    "product_B": rng.integers(30, 150, 60).cumsum(),
    "product_C": rng.integers(20, 100, 60).cumsum(),
}, index=dates)
total_sales = data.sum()

st.title("Sales Share by Product")
fig_pie = px.pie(
    values=total_sales.values,
    names=total_sales.index,
    title="Total Sales Distribution",
)
st.plotly_chart(fig_pie)

st.title("Sales Trends Over Time (Plotly)")
fig_line = px.line(
    data,
    y=["product_A", "product_B", "product_C"],
    title="Sales Trends (Plotly)",
)
st.plotly_chart(fig_line)
