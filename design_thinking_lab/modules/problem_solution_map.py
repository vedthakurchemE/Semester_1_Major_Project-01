# modules/problem_solution_map.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run():
    st.title("🗺️ Problem-Solution Mapper")
    st.markdown("""
    Map **user problems** to **creative solutions** visually.  
    Useful during the **Ideate** and **Define** phases of Design Thinking.

    💡 Helps in organizing ideas and building a clear path forward.
    """)

    num_entries = st.slider("🔢 How many problems to map?", min_value=1, max_value=10, value=3)

    problems = []
    solutions = []

    st.subheader("🧩 Enter Problems and Solutions")
    for i in range(num_entries):
        col1, col2 = st.columns(2)
        with col1:
            problem = st.text_input(f"Problem #{i+1}", key=f"p{i}")
        with col2:
            solution = st.text_input(f"Proposed Solution #{i+1}", key=f"s{i}")

        if problem and solution:
            problems.append(problem)
            solutions.append(solution)

    if problems and solutions:
        st.subheader("📊 Problem → Solution Map")
        df = pd.DataFrame({
            "Problem": problems,
            "Solution": solutions
        })

        st.table(df)

        fig, ax = plt.subplots(figsize=(8, len(problems) * 1.2))
        for i, (p, s) in enumerate(zip(problems, solutions)):
            ax.plot([0, 1], [i, i], 'k-', lw=1)
            ax.text(-0.05, i, f"🧱 {p}", va='center', ha='right', fontsize=10, wrap=True)
            ax.text(1.05, i, f"💡 {s}", va='center', ha='left', fontsize=10, wrap=True)

        ax.axis('off')
        st.pyplot(fig)

        st.success("✅ Use this map to select the most feasible and impactful ideas.")

    else:
        st.warning("⚠️ Enter at least one valid Problem-Solution pair to generate the map.")
