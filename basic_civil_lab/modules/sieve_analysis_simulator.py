# modules/sieve_analysis_simulator.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run():
    st.title("🧪 Sieve Analysis Simulator")
    st.markdown("""
    Simulate the **sieve analysis test** to determine the **particle size distribution** of coarse/fine aggregates.

    ---
    ### 🧮 Formula:
    - **% Passing = Cumulative weight retained / Total sample weight × 100**
    - Used for **gradation analysis** and confirming aggregate size as per IS: 383

    """)

    st.subheader("📥 Enter Sieve Data")

    sieves = ["40 mm", "20 mm", "10 mm", "4.75 mm", "2.36 mm", "1.18 mm", "600 µm", "300 µm", "150 µm", "Pan"]
    retained_weights = []

    col1, col2 = st.columns([2, 3])
    with col1:
        total_weight = st.number_input("🔢 Total Sample Weight (g)", min_value=100.0, value=1000.0, step=10.0)

    with col2:
        st.markdown("📊 **Weight Retained on Each Sieve (g)**")
        for sieve in sieves:
            val = st.number_input(f"{sieve}", min_value=0.0, value=0.0, step=5.0, key=sieve)
            retained_weights.append(val)

    if sum(retained_weights) > total_weight:
        st.error("❌ Total retained weight cannot exceed total sample weight.")
        return

    if st.button("📉 Generate Gradation Curve"):
        df = pd.DataFrame({
            "Sieve Size": sieves,
            "Weight Retained (g)": retained_weights
        })

        df["Cumulative Retained (g)"] = df["Weight Retained (g)"].cumsum()
        df["% Passing"] = 100 - (df["Cumulative Retained (g)"] / total_weight * 100)

        st.subheader("📋 Tabulated Data")
        st.dataframe(df)

        st.subheader("📈 Particle Size Distribution Curve")
        fig, ax = plt.subplots()
        ax.plot(df["Sieve Size"], df["% Passing"], marker='o', linestyle='-', color='green')
        ax.set_xlabel("Sieve Size")
        ax.set_ylabel("% Passing")
        ax.set_title("Gradation Curve")
        ax.set_ylim(0, 100)
        ax.invert_xaxis()
        ax.grid(True)
        st.pyplot(fig)

        st.success("✅ Gradation Curve Generated. Compare with IS:383 zones to determine if aggregate is well-graded.")

    st.caption("🔬 Applies to fine & coarse aggregates. Used in pavement, concrete, and RCC mix design.")
