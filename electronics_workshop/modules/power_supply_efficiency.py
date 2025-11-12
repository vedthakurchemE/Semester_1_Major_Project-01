# modules/power_supply_efficiency.py

import streamlit as st
import matplotlib.pyplot as plt

def run():
    st.title("🔋 Power Supply Efficiency Calculator")
    st.markdown("""
    Estimate **efficiency**, **power loss**, and **heat dissipation** of a power supply circuit.

    📘 **Formula Used**:
    - `Efficiency (%) = (Pout / Pin) × 100`
    - `Power Loss = Pin - Pout`
    """)

    st.subheader("⚙️ Input Parameters")

    input_voltage = st.number_input("🔌 Input Voltage (V)", min_value=0.0, value=12.0, step=0.1)
    output_voltage = st.number_input("🔋 Output Voltage (V)", min_value=0.0, value=5.0, step=0.1)
    output_current = st.number_input("📦 Output Load Current (A)", min_value=0.0, value=1.0, step=0.1)

    pin = input_voltage * output_current  # Assumes 100% current passes through
    pout = output_voltage * output_current
    power_loss = pin - pout
    efficiency = (pout / pin) * 100 if pin != 0 else 0

    st.divider()
    st.subheader("📊 Results")
    st.success(f"⚡ Efficiency: **{efficiency:.2f}%**")
    st.info(f"🔥 Power Loss: **{power_loss:.2f} W**")
    st.warning(f"📉 Output Power: **{pout:.2f} W** | Input Power: **{pin:.2f} W**")

    st.subheader("📈 Efficiency Visualization")
    labels = ['Output Power', 'Power Loss']
    values = [pout, power_loss]
    colors = ['#00b894', '#d63031']

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(labels, values, color=colors)
    ax.set_ylabel("Watts (W)")
    ax.set_title("Power Distribution")
    st.pyplot(fig)

    st.caption("🧠 Useful for switching regulators, battery circuits, and voltage regulators like LM317, 7805, buck/boost converters.")
