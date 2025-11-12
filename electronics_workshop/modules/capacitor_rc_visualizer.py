# modules/capacitor_rc_visualizer.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def capacitor_curve(R, C, V, mode='charging', t_max=5, steps=1000):
    t = np.linspace(0, t_max, steps)
    if mode == 'charging':
        v = V * (1 - np.exp(-t / (R * C)))
    else:
        v = V * np.exp(-t / (R * C))
    return t, v

def run():
    st.title("🧪 Capacitor Charging/Discharging Visualizer")
    st.markdown("""
    Explore how a **capacitor** charges and discharges in an **RC circuit**.

    📘 **Key Formulae**:
    - Charging: `V(t) = Vmax × (1 - e^(-t/RC))`
    - Discharging: `V(t) = Vmax × e^(-t/RC)`
    """)

    st.subheader("⚙️ Input Parameters")
    col1, col2, col3 = st.columns(3)
    with col1:
        R = st.number_input("Resistance R (Ohms)", min_value=1.0, value=1000.0)
    with col2:
        C = st.number_input("Capacitance C (Farads)", min_value=0.000001, value=0.00047, format="%.6f")
    with col3:
        V = st.number_input("Supply Voltage V (Volts)", min_value=0.0, value=5.0)

    mode = st.radio("🔄 Choose Mode", ["Charging", "Discharging"], horizontal=True)
    t, v = capacitor_curve(R, C, V, mode=mode.lower())

    st.divider()
    st.subheader("📈 Voltage vs Time")
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.plot(t, v, color="crimson", linewidth=2)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Voltage (V)")
    ax.set_title(f"Capacitor {mode} Curve (RC = {R*C:.3f} s)")
    ax.grid(True)
    st.pyplot(fig)

    st.success(f"⏱️ RC Time Constant: {R*C:.3f} seconds")
    st.caption("💡 RC circuits are used in filters, timers, and analog smoothing circuits.")
