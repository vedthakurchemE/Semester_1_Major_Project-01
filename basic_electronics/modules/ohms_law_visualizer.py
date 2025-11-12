# modules/basic_electronics/ohms_law_visualizer.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def run():
    st.title("⚡ Ohm’s Law Visualizer")
    st.markdown("""
    Understand the relationship between:

    \[
    V = I \\times R
    \]

    - Change any two parameters to compute the third.
    - See how the values relate with real-time plotting.
    """)

    st.subheader("🔧 Input Parameters")
    option = st.radio("Select two known values", ["Voltage & Resistance", "Current & Resistance", "Voltage & Current"])

    if option == "Voltage & Resistance":
        voltage = st.slider("Voltage (V)", 0.0, 240.0, 12.0)
        resistance = st.slider("Resistance (Ω)", 1.0, 1000.0, 100.0)
        current = voltage / resistance
    elif option == "Current & Resistance":
        current = st.slider("Current (A)", 0.0, 10.0, 1.0)
        resistance = st.slider("Resistance (Ω)", 1.0, 1000.0, 100.0)
        voltage = current * resistance
    else:
        voltage = st.slider("Voltage (V)", 0.0, 240.0, 12.0)
        current = st.slider("Current (A)", 0.0, 10.0, 1.0)
        resistance = voltage / current if current != 0 else 0

    st.subheader("📊 Results")
    st.success(f"Voltage (V): {voltage:.2f} V")
    st.success(f"Current (I): {current:.2f} A")
    st.success(f"Resistance (R): {resistance:.2f} Ω")

    st.markdown("### 🔋 Visualization")
    fig, ax = plt.subplots()
    ax.plot(np.array([0, resistance]), np.array([0, voltage]), label="Ohm's Law Line", color='orange')
    ax.set_xlabel("Resistance (Ω)")
    ax.set_ylabel("Voltage (V)")
    ax.set_title("Ohm's Law Relationship")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    st.info("🔌 Core concept for all analog/digital circuits, embedded systems, and power design.")
