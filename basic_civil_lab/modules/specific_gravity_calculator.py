# modules/specific_gravity_calculator.py

import streamlit as st
import matplotlib.pyplot as plt

def run():
    st.title("⚖️ Specific Gravity of Cement Calculator")
    st.markdown("""
    Estimate the **specific gravity of cement** using **Le Chatelier Flask Method**.

    📘 **Formula:**
    \n`Specific Gravity (G) = (W2 - W1) / (W3 - W1 - W4 + W2)`

    - W1: Weight of empty flask
    - W2: Weight of flask + cement
    - W3: Weight of flask + cement + kerosene
    - W4: Weight of flask filled with kerosene only
    """)

    st.divider()
    st.subheader("📥 Enter Weights (grams)")

    W1 = st.number_input("W1: Empty Flask", min_value=0.0, value=50.0, step=0.1)
    W2 = st.number_input("W2: Flask + Cement", min_value=W1, value=100.0, step=0.1)
    W3 = st.number_input("W3: Flask + Cement + Kerosene", min_value=W2, value=160.0, step=0.1)
    W4 = st.number_input("W4: Flask + Kerosene Only", min_value=W1, value=130.0, step=0.1)

    if st.button("🧮 Calculate Specific Gravity"):
        try:
            numerator = W2 - W1
            denominator = (W3 - W1) - (W4 - W2)
            if denominator == 0:
                st.error("⚠️ Division by zero. Please check your inputs.")
            else:
                G = round(numerator / denominator, 3)
                st.success(f"✅ Specific Gravity of Cement: **{G}**")
                if G < 3.10:
                    st.info("🔎 May indicate older or less dense cement.")
                else:
                    st.info("✅ Cement quality likely acceptable.")
        except:
            st.error("❌ Invalid values. Please recheck input.")

    st.divider()
    st.subheader("📊 Visual Reference")

    labels = ['Empty Flask (W1)', 'Flask + Cement (W2)', 'Flask + Cement + Kerosene (W3)', 'Flask + Kerosene (W4)']
    weights = [W1, W2, W3, W4]

    fig, ax = plt.subplots()
    ax.barh(labels, weights, color='skyblue')
    ax.set_xlabel("Weight (grams)")
    ax.set_title("Weights for Specific Gravity Test")
    st.pyplot(fig)

    st.caption("📘 Use fresh, dry cement and kerosene for accurate results.")
