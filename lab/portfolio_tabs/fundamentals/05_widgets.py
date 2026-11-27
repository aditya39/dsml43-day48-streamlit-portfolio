import streamlit as st
# Input teks
name = st.text_input("Your name")
bio = st.text_area("About you")
# Input angka
age = st.number_input("Age", 18, 100)
rating = st.slider("Rating", 1, 10, 7)
# Pilihan
model = st.selectbox("Model", ["RF", "XGBoost", "SVM"])
features = st.multiselect(
    "Features", ["Age", "Income", "Education"])
# Boolean & file
show = st.checkbox("Show raw data")
file = st.file_uploader("Upload CSV")
# Aksi
if st.button("Train Model"):
    st.write("Training...")
