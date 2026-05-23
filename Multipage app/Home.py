import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    page_icon="🌐",
    layout="wide"
)

st.title("Welcome to My Portfolio Website")

st.write("""
Hello! I am a student learning Streamlit and Python.

This website contains information about me, my projects,
skills, and contact details.
""")

col1, col2 = st.columns(2)

with col1:
    st.header("Features")
    st.write("""
    - Multipage navigation
    - Interactive inputs
    - Clean UI design
    - Personal portfolio
    """)

with col2:
    st.header("Quick Interaction")

    name = st.text_input("Enter your name")

    if st.button("Greet Me"):
        st.success(f"Welcome to my website, {name}!")