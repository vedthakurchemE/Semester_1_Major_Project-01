# modules/crazy_8s_brainstormer.py

import streamlit as st
from datetime import datetime

def run():
    st.title("🌀 Crazy 8s Brainstormer")
    st.markdown("""
    **Crazy 8s** is a fast-paced ideation exercise to generate **8 ideas in 8 minutes**.

    🚀 Helps break creative blocks and **expand solution possibilities** during the *Ideate* phase of Design Thinking.
    """)

    st.subheader("🎯 Problem Statement")
    problem = st.text_area("What problem are you brainstorming for?", value="How might we reduce student stress during exam preparation?")

    st.subheader("⏱️ Set Timer for Crazy 8s")
    minutes = st.slider("How many minutes?", 1, 8, 8)
    start_ideation = st.button("🧠 Start Brainstorming!")

    if start_ideation:
        st.success(f"💡 Start ideating now! You have {minutes} minute(s) to generate 8 ideas.")
        st.balloons()
        st.markdown("---")

        idea_inputs = []
        for i in range(1, 9):
            idea = st.text_input(f"💡 Idea {i}", key=f"idea_{i}")
            idea_inputs.append(idea)

        if st.button("✅ Submit Ideas"):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.success("✅ Crazy 8s submission complete!")
            st.markdown("### 📘 Your 8 Ideas")
            for idx, idea in enumerate(idea_inputs, 1):
                st.markdown(f"**{idx}.** {idea}")

            st.markdown(f"🕒 Time: *{timestamp}*")
            st.info("🔁 Use Crazy 8s multiple times to refine & remix your best ideas!")

    st.caption("💡 Tip: These ideas can be filtered using a voting matrix or dot voting in later stages.")
