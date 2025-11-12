# modules/basic_electronics/ohms_law_calculator.py

import streamlit as st

def run():
    st.title("⚡ Ohm's Law Calculator")
    st.markdown("""
    Use this tool to calculate **Voltage (V)**, **Current (I)**, or **Resistance (R)** using Ohm’s Law:

    \[
    V = I \\times R
    \]

    Select the variable you want to calculate, and provide the other two.
    """)

    # Select variable to calculate
    choice = st.radio("🔍 What do you want to calculate?", ["Voltage (V)", "Current (I)", "Resistance (R)"])

    if choice == "Voltage (V)":
        current = st.number_input("Enter Current (I) in Amperes", min_value=0.0, step=0.1)
        resistance = st.number_input("Enter Resistance (R) in Ohms", min_value=0.0, step=0.1)
        if st.button("Calculate Voltage"):
            voltage = current * resistance
            st.success(f"🔋 Voltage = {voltage:.2f} V")

    elif choice == "Current (I)":
        voltage = st.number_input("Enter Voltage (V) in Volts", min_value=0.0, step=0.1)
        resistance = st.number_input("Enter Resistance (R) in Ohms", min_value=0.1, step=0.1)
        if st.button("Calculate Current"):
            current = voltage / resistance
            st.success(f"🔌 Current = {current:.2f} A")

    elif choice == "Resistance (R)":
        voltage = st.number_input("Enter Voltage (V) in Volts", min_value=0.0, step=0.1)
        current = st.number_input("Enter Current (I) in Amperes", min_value=0.1, step=0.1)
        if st.button("Calculate Resistance"):
            resistance = voltage / current
            st.success(f"🧱 Resistance = {resistance:.2f} Ω")

    st.info("💡 Ohm’s Law is fundamental for every electronics engineer — used in circuit design, diagnostics, and testing.")
