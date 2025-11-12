# quiz_game.py
# 🎯 Quiz Game with Leaderboard (Streamlit)

import streamlit as st

def run():
    st.title("🎯 Quiz Game with Leaderboard")

    # Initialize leaderboard
    if "leaderboard" not in st.session_state or not isinstance(st.session_state["leaderboard"], list):
        st.session_state["leaderboard"] = []

    # Quiz Questions
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Venus", "Jupiter"],
            "answer": "Mars"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["William Shakespeare", "Mark Twain", "Charles Dickens", "Jane Austen"],
            "answer": "William Shakespeare"
        }
    ]

    name = st.text_input("Enter your name to start the quiz:")

    if name:
        score = 0
        for i, q in enumerate(questions):
            st.subheader(f"Q{i+1}: {q['question']}")
            answer = st.radio("Select your answer:", q["options"], key=f"q{i}")
