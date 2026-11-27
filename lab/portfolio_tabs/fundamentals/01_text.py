import streamlit as st

# Judul dan header
st.title("Main Title")          # H1
st.header("Section Header")     # H2
st.subheader("Subsection")      # H3

# Teks biasa
st.write("Auto-formats anything!")
st.markdown("**Bold**, *italic*, `code`")
st.latex(r"E = mc^2")
st.code("print('hello')", language="python")
st.caption("Small grey caption")
