import streamlit as st
import pandas as pd

df = pd.DataFrame({"Name": ["Alice", "Bob"],
                   "Score": [92, 85]})

st.dataframe(df)    # interaktif: sort & scroll
st.table(df)        # statis: tampil penuh
st.metric("Accuracy", "92%", "+2%")    # KPI + delta
st.json({"model": "XGBoost", "accuracy": 0.92})
