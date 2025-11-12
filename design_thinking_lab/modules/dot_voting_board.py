# modules/dot_voting_board.py

import streamlit as st

def run():
    st.title("🔘 Dot Voting Board")
    st.markdown("""
    Use **Dot Voting** to identify the best ideas from a brainstorming session.  
    🎯 Each participant is given a limited number of votes (dots) to cast on ideas they find most promising.

    Ideal for:
    - Narrowing down ideas from **Crazy 8s**
    - Group decision-making
    - Prioritizing features or solutions
    """)

    st.subheader("📝 Enter Your Ideas")
    idea_list = []
    for i in range(1, 9):
        idea = st.text_input(f"Idea {i}", key=f"idea_{i}")
        if idea:
            idea_list.append(idea)

    st.subheader("🗳️ Voting")
    total_votes = st.slider("How many dots per user?", 1, 10, 3)
    vote_data = {}

    if idea_list:
        st.markdown("### 🧠 Cast Your Votes")
        for idea in idea_list:
            votes = st.slider(f"🔘 Votes for: {idea}", 0, total_votes, 0, key=f"vote_{idea}")
            vote_data[idea] = votes

        if st.button("✅ Submit Votes"):
            st.success("✅ Voting Completed!")
            st.markdown("### 📊 Voting Results")
            sorted_votes = sorted(vote_data.items(), key=lambda x: x[1], reverse=True)
            for idea, vote in sorted_votes:
                st.markdown(f"**{idea}** — 🔵 {vote} votes")

            st.balloons()
            st.info("💡 Use the top-voted ideas in your prototyping phase.")

    else:
        st.warning("⚠️ Please enter at least one idea to enable voting.")
