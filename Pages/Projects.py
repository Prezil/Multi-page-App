import streamlit as st

st.title("My Projects")

project = st.selectbox(
    "Choose a project",
    [
        "Object Detection System",
        "Random Joke Generator",
        "Color Mood Picker"
    ]
)

if project == "Object Detection System":
    st.write("""
    A real-time object detection system using YOLO and Streamlit.
    """)

elif project == "Random Joke Generator":
    st.write("""
    A fun app that displays random silly jokes to make users laugh.
    """)

elif project == "Color Mood Picker":
    st.write("""
    An app that lets users pick a color and shows a matching mood or vibe.
    """)

rating = st.slider("Rate this page", 1, 5)

st.write(f"You rated this page {rating}/5")