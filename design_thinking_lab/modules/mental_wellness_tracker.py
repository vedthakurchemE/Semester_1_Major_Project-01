# modules/mental_wellness_tracker.py

import streamlit as st
import datetime
import matplotlib.pyplot as plt

def calculate_wellness_score(mood, stress, sleep):
    mood_score = mood * 2
    stress_score = (6 - stress) * 2  # Lower stress = higher score
    sleep_score = sleep * 1.5
    total_score = mood_score + stress_score + sleep_score
    return round(total_score, 1)

def run():
    st.title("🧠 Mental Wellness Tracker")
    st.markdown("""
    Track your **mental well-being** by entering how you feel daily.

    📈 Helps reflect and recognize mood patterns and stress over time.
    """)

    st.subheader("🗓️ Today's Entry")
    today = datetime.date.today()

    mood = st.slider("😊 Mood (1 = Bad, 5 = Excellent)", 1, 5, 3)
    stress = st.slider("😫 Stress Level (1 = Very Low, 5 = Very High)", 1, 5, 3)
    sleep = st.slider("😴 Sleep Quality (1 = Poor, 5 = Excellent)", 1, 5, 3)

    score = calculate_wellness_score(mood, stress, sleep)

    st.success(f"🧮 Your Wellness Score for {today}: **{score} / 25**")

    st.subheader("📊 Quick Wellness Summary")
    fig, ax = plt.subplots()
    labels = ["Mood", "Stress (Inverted)", "Sleep"]
    values = [mood * 2, (6 - stress) * 2, sleep * 1.5]

    ax.bar(labels, values, color=['skyblue', 'lightgreen', 'salmon'])
    ax.set_ylim(0, 10)
    ax.set_ylabel("Score")
    ax.set_title("Wellness Components Breakdown")

    st.pyplot(fig)

    st.info("💡 A score >18 suggests you're mentally in a good state. Reflect and revisit often.")

    with st.expander("🧘‍♀️ Tips to Improve Wellness"):
        st.markdown("""
        - Practice **mindfulness** or meditation for 10 mins.
        - Talk to someone you trust.
        - Get regular **physical activity**.
        - Sleep consistently and eat healthy.
        """)

    st.caption("💖 Built with empathy in Python + Streamlit")

