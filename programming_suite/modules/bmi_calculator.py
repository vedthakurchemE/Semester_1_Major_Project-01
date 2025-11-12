# modules/bmi_calculator.py

import streamlit as st
import matplotlib.pyplot as plt

def run():
    st.title("⚖️ BMI Calculator")
    st.markdown("""
    This tool calculates your **Body Mass Index (BMI)** and classifies your health status.

    ---
    ### 📘 BMI Formula:
    \[
    \text{BMI} = \frac{\text{Weight (kg)}}{[\text{Height (m)}]^2}
    \]
    """)

    col1, col2 = st.columns(2)

    with col1:
        weight = st.number_input("Enter your weight (kg)", min_value=10.0, max_value=200.0, step=0.5)
    with col2:
        height_cm = st.number_input("Enter your height (cm)", min_value=50.0, max_value=250.0, step=0.5)

    if st.button("🧮 Calculate BMI"):
        height_m = height_cm / 100
        bmi = round(weight / (height_m ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif 18.5 <= bmi < 25:
            category = "Normal"
            color = "green"
        elif 25 <= bmi < 30:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"

        st.success(f"Your BMI is **{bmi}**, which is categorized as **{category}**.")

        # 📊 Visualization
        fig, ax = plt.subplots()
        ax.bar(["Your BMI"], [bmi], color=color)
        ax.axhline(y=18.5, color='gray', linestyle='--', label="Min Normal")
        ax.axhline(y=25, color='gray', linestyle='--', label="Max Normal")
        ax.set_ylabel("BMI")
        ax.set_title("Body Mass Index")
        ax.legend()
        st.pyplot(fig)

        st.info("💡 Tip: Ideal BMI is between **18.5 – 24.9** for a healthy body.")
