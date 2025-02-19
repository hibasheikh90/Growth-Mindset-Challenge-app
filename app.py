

import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🚀", layout="wide")

# Custom Styles
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
    }
    .stTextInput>div>div>input {
        font-size: 16px;
        padding: 10px;
        border-radius: 6px;
    }
    .stTable {
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize Session State
if "streak" not in st.session_state:
    st.session_state["streak"] = 0
if "leaderboard" not in st.session_state:
    st.session_state["leaderboard"] = {}
if "progress" not in st.session_state:
    st.session_state["progress"] = []
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Title & Introduction
st.title("🚀 Growth Mindset Challenge")
st.write("""
### Welcome to the Growth Mindset Challenge!  
A **growth mindset** means believing that intelligence and skills improve with effort and learning. Let's practice it together! 💡
""")

# 📝 Self-Assessment Quiz
st.header("📝 Quick Mindset Quiz")
questions = [
    "Do you see challenges as opportunities to grow?",
    "Do you believe hard work improves intelligence?",
    "Are you open to learning from mistakes?",
    "Do you appreciate constructive feedback?"
]

responses = []
for q in questions:
    responses.append(st.radio(q, ["Yes", "No"], index=None))  # No pre-selected answers

if st.button("Submit Quiz"):
    if None in responses:
        st.warning("Please answer all questions before submitting.")
    else:
        score = responses.count("Yes")
        if score >= 3:
            st.success("Great! You already have a strong growth mindset. Keep going! 🚀")
        else:
            st.warning("You can improve! Start by embracing challenges and learning from mistakes. 💡")

# 🎯 Goal Setting
st.header("🎯 Set Your Learning Goal")
goal = st.text_input("What is one skill or subject you want to improve?")
if goal:
    st.write(f"Awesome! Stay committed to learning **{goal}** and track your progress daily.")

# 📅 Track Your Daily Progress
st.header("📅 Track Your Daily Progress")
new_entry = st.text_area("What did you learn today?")
if st.button("Add Progress"):
    if new_entry:
        st.session_state["progress"].append(new_entry)
        st.success("Progress recorded!")
    else:
        st.warning("Please enter something before adding.")

if st.session_state["progress"]:
    st.subheader("Your Learning Journey 📖")
    for entry in st.session_state["progress"]:
        st.write(f"✅ {entry}")

# 🏆 Growth Mindset Leaderboard
st.header("🏆 Growth Mindset Leaderboard")

user_name = st.text_input("Enter your name to join the leaderboard:")
if user_name:
    if user_name not in st.session_state["leaderboard"]:
        st.session_state["leaderboard"][user_name] = st.session_state["streak"]

if st.button("Complete Today's Challenge ✅"):
    if user_name:
        st.session_state["streak"] += 1
        st.session_state["leaderboard"][user_name] = st.session_state["streak"]
        st.success(f"Awesome! Your streak is now {st.session_state['streak']} days! 🚀")
    else:
        st.warning("Please enter your name to track progress.")

# Sort Leaderboard by Streak Count
sorted_leaderboard = dict(sorted(st.session_state["leaderboard"].items(), key=lambda x: x[1], reverse=True))

# Display Leaderboard Table
if sorted_leaderboard:
    st.subheader("🔥 Top Learners")
    leaderboard_df = pd.DataFrame(sorted_leaderboard.items(), columns=["Participant", "Streak Days"])
    st.table(leaderboard_df)
else:
    st.info("Leaderboard is empty. Join the challenge by entering your name above!")

# 💬 Encouragement Messages
st.header("💬 Share Encouragement")
message = st.text_area("Motivate others by writing a positive message:")
if st.button("Post Message"):
    if message:
        st.session_state["messages"].append(message)
        st.success("Thank you for spreading positivity! 🌟")
    else:
        st.warning("Please write a message before posting.")

if st.session_state["messages"]:
    st.subheader("🌟 Community Motivation")
    for msg in st.session_state["messages"]:
        st.write(f"💬 {msg}")

# End Message
st.write("**Keep learning and growing! 🌱**")
