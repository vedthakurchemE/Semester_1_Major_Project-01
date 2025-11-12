# modules/led_current_limiter.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def run():
    st.title("🔦 LED Current Limiter Calculator")
    st.markdown("""
    Calculate the **resistor value** needed for an LED circuit to limit current.

    Formula:  
    R = (Vₛ – V_f) / I

    Where:  
    - Vₛ = Supply Voltage  
    - V_f = LED Forward Voltage  
    - I = Desired LED Current
    """)

    col1, col2 = st.columns(2)
    with col1:
        Vs = st.number_input("Supply Voltage Vₛ (V)", min_value=1.0, step=0.1, value=5.0)
        Vf = st.number_input("LED Forward Voltage V_f (V)", min_value=0.1, step=0.01, value=2.0)
    with col2:
        I_mA = st.number_input("Desired Current I (mA)", min_value=1.0, step=1.0, value=20.0)

    if st.button("Calculate Resistor"):
        I = I_mA / 1000  # to A
        R = (Vs - Vf) / I if I > 0 else float('inf')
        power = (I ** 2) * R

        st.success(f"🧮 Recommended Resistor: **{R:.1f} Ω**")
        st.info(f"💡 Estimated Power Dissipation: **{power:.3f} W**")

        fig, ax = plt.subplots()
        bars = ['Vs', 'Vf', 'Voltage Drop']
        vals = [Vs, Vf, Vs - Vf]
        ax.bar(bars, vals, color=['skyblue', 'orange', 'red'])
        ax.set_ylabel("Voltage (V)")
        ax.set_title("LED Voltage Diagram")
        st.pyplot(fig)

        st.caption("⚠️ Choose the nearest higher resistor component and power rating.")
