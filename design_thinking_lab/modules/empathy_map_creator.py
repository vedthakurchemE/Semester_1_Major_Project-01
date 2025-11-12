# modules/empathy_map_creator.py

import streamlit as st

def run():
    st.title("🧠 Empathy Map Creator")
    st.markdown("""
    Use this tool to **visually build an Empathy Map** for a target user.

    Helps in understanding:
    - What the user **says**
    - What they **think**
    - What they **do**
    - What they **feel**

    💡 Ideal for the **Empathize** phase in Design Thinking!
    """)

    st.subheader("👤 User Persona")
    user_name = st.text_input("User Name / Role", value="Student preparing for exams")
    context = st.text_area("Context / Scenario", value="Has 2 months left before final exams and feels overwhelmed by subjects.")

    st.subheader("🗣️ SAYS")
    says = st.text_area("What does the user SAY?", value="\"I don’t have enough time!\"")

    st.subheader("💭 THINKS")
    thinks = st.text_area("What does the user THINK?", value="I'm afraid I’ll fail. Others are doing better than me.")

    st.subheader("🤲 DOES")
    does = st.text_area("What does the user DO?", value="Makes timetables, watches YouTube lectures, procrastinates.")

    st.subheader("❤️ FEELS")
    feels = st.text_area("What does the user FEEL?", value="Anxious, confused, demotivated.")

    if st.button("🎯 Generate Empathy Map"):
        st.success("🧠 Empathy Map Generated Below")

        st.markdown("---")
        st.markdown(f"### 👤 User: **{user_name}**")
        st.markdown(f"**Context:** {context}")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🗣️ Says")
            st.info(says)

            st.markdown("#### 🤲 Does")
            st.warning(does)

        with col2:
            st.markdown("#### 💭 Thinks")
            st.info(thinks)

            st.markdown("#### ❤️ Feels")
            st.warning(feels)

    st.caption("🎨 Tip: Use this map as input for brainstorming solutions based on deep user empathy.")
