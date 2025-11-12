# modules/design_feedback_wall.py

import streamlit as st
import pandas as pd
from datetime import datetime

# Session state to store feedbacks
if "feedback_data" not in st.session_state:
    st.session_state.feedback_data = []

def run():
    st.title("🧠 Design Feedback Wall")
    st.markdown("""
    A collaborative wall to **collect feedback, ideas, issues, and emotions** from users or team members during prototyping.

    Perfect for **Design Thinking workshops**, **product feedback**, and **ideation sessions**.
    """)

    st.subheader("📝 Submit Your Feedback")

    name = st.text_input("Your Name (Optional)", max_chars=50)
    feedback_type = st.selectbox("Feedback Type", ["💡 Idea", "❗ Issue", "🤔 Suggestion", "😠 Frustration", "❤️ Appreciation"])
    message = st.text_area("Your Message", max_chars=300)

    if st.button("📬 Post Feedback"):
        if message.strip():
            st.session_state.feedback_data.append({
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Name": name if name else "Anonymous",
                "Type": feedback_type,
                "Message": message.strip()
            })
            st.success("✅ Feedback posted!")
        else:
            st.warning("⚠️ Please enter a message before submitting.")

    if st.session_state.feedback_data:
        st.subheader("🧾 Live Feedback Wall")
        df = pd.DataFrame(st.session_state.feedback_data)
        df = df[["Timestamp", "Name", "Type", "Message"]]
        st.dataframe(df[::-1], use_container_width=True)

    st.caption("🧪 Great tool for agile design feedback loops, empathy building, and reflection.")
