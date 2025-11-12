# modules/basic_electronics/rc_circuit_simulator.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def charging_curve(t, V, R, C):
    tau = R * C
    return V * (1 - np.exp(-t / tau))

def discharging_curve(t, V, R, C):
    tau = R * C
    return V * np.exp(-t / tau)

def run():
    st.title("⚙️ RC Circuit Simulator")
    st.markdown("""
    Simulates the **charging and discharging behavior** of a capacitor in an RC circuit.

    ---
    \[
    V(t) = V_0 (1 - e^{-t/RC}) \quad \text{(Charging)}
    \]
    \[
    V(t) = V_0 e^{-t/RC} \quad \text{(Discharging)}
    \]
    ---
    """)

    mode = st.radio("🔋 Mode", ["Charging", "Discharging"])
    V = st.slider("🔌 Supply Voltage V₀ (Volts)", 1, 50, 10)
    R = st.slider("🌀 Resistance R (kΩ)", 1, 100, 10) * 1e3  # in ohms
    C = st.slider("📦 Capacitance C (μF)", 1, 1000, 100) * 1e-6  # in farads

    duration = st.slider("⏱️ Simulation Duration (ms)", 10, 5000, 1000)
    t = np.linspace(0, duration / 1000, 500)

    if mode == "Charging":
        v_t = charging_curve(t, V, R, C)
    else:
        v_t = discharging_curve(t, V, R, C)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(t * 1000, v_t, color="purple", linewidth=2)
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Voltage (V)")
    ax.set_title(f"{mode} Curve - RC Circuit")
    ax.grid(True)

    st.pyplot(fig)

    st.info(f"🧮 Time Constant τ = RC = {R*C:.2f} seconds")
