import streamlit as st

# Sidebar
with st.sidebar:
    page = st.radio("Go to",
                    ["Home", "Projects", "Contact"])

# Columns
col1, col2, col3 = st.columns(3)
col1.metric("Accuracy", "92%")

# Tabs
tab1, tab2 = st.tabs(["EDA", "Model"])
with tab1:
    st.write("EDA content...")

# Expander (bisa dilipat)
with st.expander("Show code"):
    st.code("model.fit(X, y)")
