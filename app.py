

import streamlit as st
import random
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
import time
import numpy as np
from PIL import Image

# Function to load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_w98qte06.json")
lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_3rwasyjy.json")

# Initialize session state
if "users" not in st.session_state:
    st.session_state.users = {}

st.title("🚀 Interactive Learning Hub: Code & Create")

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/programming.png")
    st.header("📚 Learning Center")
    name = st.text_input("Your Name")
    goal = st.text_input("Learning Goal")
    learning_path = st.selectbox("🛣️ Choose Your Path", ["Web Development", "Data Science", "AI/ML", "Blockchain"])
    experience_level = st.select_slider("⭐ Experience Level", ["Beginner", "Intermediate", "Advanced"])
    preferred_language = st.multiselect("💻 Preferred Languages", ["Python", "JavaScript", "Java", "C++"])
    study_time = st.slider("Daily Study Hours", 0, 12, 2)
    st_lottie(lottie_coding, height=150)

if name:
    if name not in st.session_state.users:
        st.session_state.users[name] = {
            "Skill Level": 1,
            "XP Points": 0,
            "Study Hours": study_time,
            "Languages": preferred_language
        }
        st_lottie(lottie_hello, height=150)

    st.subheader(f"Welcome, {name} 🎉")
    st.write(f"**Path:** {learning_path} | **Level:** {experience_level}")
    st.write(f"**Goal:** {goal} | **Daily Study:** {study_time} hours")

    # File Upload Feature
    st.subheader("📁 File Upload Center")
    uploaded_file = st.file_uploader("Upload your project files", type=['py', 'txt', 'jpg', 'png' ,'pdf' ,'csv' ,'xlsx' , 'excel'])
    if uploaded_file:
        if uploaded_file.type.startswith('image'):
            st.image(Image.open(uploaded_file), caption='Uploaded Image', use_column_width=True)
        else:
            st.write("File Contents:")
            st.code(uploaded_file.getvalue().decode("utf-8"), language="python")

    # Learning Progress Graph
    progress = np.random.randint(10, 100, size=30)
    fig = px.line(y=progress, x=list(range(1, 31)), title="📈 Learning Progress")
    st.plotly_chart(fig)

    # Pomodoro Timer
    st.subheader("⏱️ Pomodoro Timer")
    pomodoro_duration = st.slider("Work Duration (minutes)", 1, 60, 25)
    if st.button("Start Timer"):
        for sec in range(pomodoro_duration * 60, -1, -1):
            mins, secs = divmod(sec, 60)
            st.metric("Time Remaining", f"{mins:02d}:{secs:02d}")
            time.sleep(1)
        st.success("Time's up! Take a break! ☕")

    # Coding Challenge
    st.subheader("🎯 Today's Coding Challenge")
    challenges = ["Build a To-Do App", "Create an API", "Design a Database", "Build a Chatbot"]
    if st.button("Get New Challenge 🎲"):
        st.info(f"Challenge: {random.choice(challenges)}")
        st.session_state.users[name]["XP Points"] += 10

    # Code Editor
    st.subheader("💻 Code Playground")
    language = st.selectbox("Select Language", ["python", "javascript"])
    code = st.text_area("Write your code here:", height=200)
    if st.button("Run Code ▶️"):
        st.code(code, language=language)
        st.success("Code executed successfully!")

    # Learning Resources
    st.subheader("📚 Learning Resources")
    tabs = st.tabs(["Tutorials", "Docs", "Projects"])
    with tabs[0]:
        st.write("Interactive video tutorials")
        st.video("https://youtu.be/example")
    with tabs[1]:
        st.write("Comprehensive documentation")
        st.markdown("[View Documentation](https://docs.example.com)")
    with tabs[2]:
        st.write("Hands-on project templates")
        if st.button("Start a Project"):
            st.success("Project initialized!")

    # Leaderboard
    st.subheader("🏅 Global Leaderboard")
    df = pd.DataFrame.from_dict(st.session_state.users, orient="index")
    df["Total Score"] = df["Skill Level"] * 100 + df["XP Points"]
    df = df.sort_values(by=["Total Score"], ascending=False)
    st.table(df[["Skill Level", "XP Points", "Total Score"]])
