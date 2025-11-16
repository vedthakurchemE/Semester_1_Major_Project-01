# modules/voltage_divider_estimator.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def run():
    st.title("🔻 Voltage Divider Estimator")
    st.markdown("""
    This tool calculates the **output voltage (Vout)** for a resistive voltage divider.

    **Formula:**  
    Vout = Vin × R2 / (R1 + R2)

    📘 Used to generate reference voltages, sensor biasing, etc.
    """)

    st.subheader("⚙️ Input Parameters")
    col1, col2 = st.columns(2)

    with col1:
        vin = st.number_input("🔋 Input Voltage Vin (V)", min_value=0.1, value=12.0, step=0.1)
        r1 = st.number_input("🧱 Resistor R1 (Ω)", min_value=1.0, value=1000.0, step=10.0)
    with col2:
        r2 = st.number_input("🧱 Resistor R2 (Ω)", min_value=1.0, value=1000.0, step=10.0)
        show_plot = st.checkbox("📉 Show Vout vs R2 Plot", value=False)

    # Calculate output voltage
    vout = vin * r2 / (r1 + r2)
    st.success(f"📤 Output Voltage Vout = **{vout:.2f} V**")

    st.info("🔎 You can change R1 and R2 to design the desired output voltage.")

    if show_plot:
        st.divider()
        st.subheader("📊 Vout vs R2 (R1 fixed)")
        r2_vals = np.linspace(100, 10000, 1000)
        vout_vals = vin * r2_vals / (r1 + r2_vals)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(r2_vals, vout_vals, color="blue")
        ax.set_title("Voltage Divider Output vs R2")
        ax.set_xlabel("R2 (Ω)")
        ax.set_ylabel("Vout (V)")
        ax.grid(True)
        st.pyplot(fig)
        st.video('https://www.youtube.com/watch?v=lLcHgBQ-_l8')
    st.caption("💡 TIP: Choose standard E12 resistor values when designing real circuits.")
