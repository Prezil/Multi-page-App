import streamlit as st

st.title("About Me")

st.write("""
I am a CS student passionate about programming,
web development, and technology.
""")

age = st.slider("Select my age", 15, 30, 20)

st.write(f"My sample age is {age} years old.")

st.subheader("My Hobbies")

hobbies = ["Coding", "Gaming", "Watching Tech Videos", "Learning Python"]

for hobby in hobbies:
    st.write("•", hobby)