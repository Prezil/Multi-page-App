import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    layout="wide"
)

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Home", "About", "Projects", "Contact"]
)

# Homepage Content
st.title("Welcome to My Portfolio Website")

st.write("""
Hello! I am a student learning Streamlit and Python.
""")

# Dynamic Content
if page == "Home":
    st.header("Home Page")
    st.write("This is the homepage.")

elif page == "About":
    st.header("About Me")
    st.write("I love coding and building projects.")

elif page == "Projects":
    st.header("My Projects")
    st.write("Here are some of my projects.")

elif page == "Contact":
    st.header("Contact")
    st.write("You can contact me here.")
