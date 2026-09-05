import streamlit as st
import random

st.set_page_config(page_title="QuizGenius AI", page_icon="⚡")

# Initialize Session State
if "score" not in st_state:
    st.session_state.score = 0
if "difficulty" not in st_state:
    st.session_state.difficulty = "Medium"
if "question_count" not in st_state:
    st.session_state.question_count = 0
if "weak_spots" not in st_state:
    st.session_state.weak_spots = []

# Mock Question Bank based on adaptive difficulty
questions_db = {
    "Easy": [
        {"q": "What does AI stand for?", "options": ["Artificial Intelligence", "Automated Input", "Array Integration"], "ans": "Artificial Intelligence", "topic": "AI Basics"},
    ],
    "Medium": [
        {"q": "Which algorithm is commonly used for classification?", "options": ["Linear Regression", "Decision Tree", "K-Means Clustering"], "ans": "Decision Tree", "topic": "ML Algorithms"},
    ],
    "Hard": [
        {"q": "What mechanism allows Transformers to weigh input tokens dynamically?", "options": ["Convolution", "Self-Attention", "Recurrent Backpropagation"], "ans": "Self-Attention", "topic": "Deep Learning Architecture"},
    ]
}

st.title("⚡ QuizGenius AI Prototype")
st.caption("Theme: Adaptive Intelligence System (AIS-02)")

st.sidebar.metric("Current Score", st.session_state.score)
st.sidebar.metric("Adaptive Difficulty", st.session_state.difficulty)

# Load Question
current_q = questions_db[st.session_state.difficulty][0]

st.subheader(f"Question ({st.session_state.difficulty} Level):")
st.write(current_q["q"])

user_choice = st.radio("Select your answer:", current_q["options"])

if st.button("Submit Answer"):
    st.session_state.question_count += 1
    if user_choice == current_q["ans"]:
        st.success("Correct! Adjusting difficulty upward...")
        st.session_state.score += 10
        st.session_state.difficulty = "Hard" if st.session_state.difficulty == "Medium" else "Hard"
    else:
        st.error(f"Incorrect. Correct answer was: {current_q['ans']}")
        st.session_state.weak_spots.append(current_q["topic"])
        st.session_state.difficulty = "Easy"

if st.session_state.weak_spots:
    st.warning("🎯 Identified Knowledge Gap:")
    st.write(f"Recommended Resource for: **{st.session_state.weak_spots[-1]}**")
  
