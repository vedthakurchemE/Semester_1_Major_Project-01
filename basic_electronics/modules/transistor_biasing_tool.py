# modules/basic_electronics/transistor_biasing_tool.py

import streamlit as st
import matplotlib.pyplot as plt

def run():
    st.title("⚙️ Transistor Biasing Tool")
    st.markdown("""
    Simulates **DC biasing** for a **Common Emitter NPN Transistor** configuration.

    Calculates the following:

    - Base current \( I_B \)
    - Collector current \( I_C \)
    - Emitter current \( I_E \)
    - Collector-Emitter voltage \( V_{CE} \)

    ---
    """)

    st.subheader("🔧 Circuit Parameters")

    Vcc = st.slider("Vcc (V)", 5, 20, 12)
    Rb = st.slider("Base Resistor Rb (kΩ)", 1, 500, 100) * 1e3
    Rc = st.slider("Collector Resistor Rc (Ω)", 100, 5000, 1000)
    Re = st.slider("Emitter Resistor Re (Ω)", 0, 2000, 500)
    beta = st.slider("Transistor β (Current Gain)", 50, 500, 100)
    Vbe = st.slider("Base-Emitter Voltage Vbe (V)", 0.5, 1.0, 0.7)

    Vb = Vcc * Re / (Rb + Re)
    Ib = (Vcc - Vbe) / Rb
    Ic = beta * Ib
    Ie = Ic + Ib
    Vce = Vcc - Ic * Rc - Ie * Re

    st.subheader("📊 Biasing Results")
    st.success(f"Base Current IB = {Ib * 1e3:.2f} mA")
    st.success(f"Collector Current IC = {Ic * 1e3:.2f} mA")
    st.success(f"Emitter Current IE = {Ie * 1e3:.2f} mA")
    st.success(f"Collector-Emitter Voltage VCE = {Vce:.2f} V")

    st.markdown("### 🔋 Output Load Line (VCE vs IC)")
    Vce_vals = [0, Vcc]
    Ic_vals = [(Vcc / (Rc + Re)), 0]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(Vce_vals, Ic_vals, 'r--', label="Load Line")
    ax.plot(Vce, Ic * 1e3, 'bo', label="Q-Point")
    ax.set_xlabel("VCE (V)")
    ax.set_ylabel("IC (mA)")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    st.info("✅ Helps you visualize operating point (Q-point) and ensures transistor stays in active region.")
