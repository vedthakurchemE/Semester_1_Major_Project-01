# modules/fineness_modulus_calculator.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run():
    st.title("🔍 Fineness Modulus Calculator")
    st.markdown("""
    This tool simulates **sieve analysis** and calculates the **Fineness Modulus (FM)** of aggregates.

    📏 **Fineness Modulus** is the weighted average of sieve sizes based on cumulative retained percentage.

    ---
    ### 🧮 Formula:
    `FM = (Cumulative % retained on standard sieves) / 100`

    Standard sieves:
    - 4.75 mm, 2.36 mm, 1.18 mm, 600 µm, 300 µm, 150 µm, Pan
    """)

    st.subheader("📊 Enter Weight Retained (in grams) for Each Sieve")

    sieves = ['4.75 mm', '2.36 mm', '1.18 mm', '600 µm', '300 µm', '150 µm', 'Pan']
    weights = []
    for sieve in sieves:
        w = st.number_input(f"Weight Retained on {sieve}", min_value=0.0, value=0.0, step=10.0)
        weights.append(w)

    total_sample = sum(weights)
    if total_sample == 0:
        st.warning("⚠️ Please enter non-zero weights to compute FM.")
        return

    df = pd.DataFrame({
        "Sieve Size": sieves,
        "Weight Retained (g)": weights
    })

    df["% Retained"] = df["Weight Retained (g)"] / total_sample * 100
    df["Cumulative % Retained"] = df["% Retained"].cumsum()

    fm = df["Cumulative % Retained"].iloc[:-1].sum() / 100

    st.subheader("📈 Sieve Analysis Data")
    st.dataframe(df.style.format({"% Retained": "{:.2f}", "Cumulative % Retained": "{:.2f}"}))

    st.success(f"🧮 Fineness Modulus (FM) = **{fm:.2f}**")

    if fm < 2.3:
        st.info("🟢 Fine Aggregate")
    elif 2.3 <= fm <= 3.1:
        st.info("🟡 Moderately Coarse")
    else:
        st.warning("🔴 Coarse Aggregate")

    st.subheader("📊 Cumulative % Retained Chart")
    fig, ax = plt.subplots()
    ax.plot(df["Sieve Size"], df["Cumulative % Retained"], marker='o', color='blue', linewidth=2)
    ax.set_xlabel("Sieve Size")
    ax.set_ylabel("Cumulative % Retained")
    ax.set_title("Cumulative Retained vs Sieve Size")
    ax.grid(True)
    st.pyplot(fig)

    st.video('https://www.youtube.com/watch?v=FT2MS4kyOcY')

    st.caption("📌 Fineness Modulus is crucial in concrete mix design and aggregate grading control.")
