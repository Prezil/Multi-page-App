import streamlit as st

st.title("My Skills")

skills = {
    "Python": 85,
    "Streamlit": 80,
    "HTML/CSS": 70,
    "Networking": 75
}

for skill, value in skills.items():
    st.write(skill)
    st.progress(value)