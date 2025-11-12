# modules/basic_electronics/rlc_resonance_visualizer.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def impedance_series_rlc(R, L, C, freq):
    omega = 2 * np.pi * freq
    Z = np.sqrt(R**2 + (omega * L - 1 / (omega * C))**2)
    return Z

def run():
    st.title("📡 RLC Resonance Visualizer")
    st.markdown("""
    This module simulates a **Series RLC circuit** and visualizes **impedance vs frequency**.

    ---
    \[
    f_0 = \\frac{1}{2\\pi\\sqrt{LC}}
    \]
    \[
    Z = \\sqrt{R^2 + (\\omega L - \\frac{1}{\\omega C})^2}
    \]
    ---
    """)

    R = st.slider("🌀 Resistance R (Ω)", 1, 1000, 100)
    L = st.slider("🔁 Inductance L (mH)", 1, 1000, 100) * 1e-3  # in H
    C = st.slider("📦 Capacitance C (μF)", 1, 1000, 100) * 1e-6  # in F

    f_resonant = 1 / (2 * np.pi * np.sqrt(L * C))
    f = np.linspace(1, 2 * f_resonant, 1000)
    Z = impedance_series_rlc(R, L, C, f)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(f, Z, color="crimson", linewidth=2)
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Impedance (Ω)")
    ax.set_title("🔊 Impedance vs Frequency in RLC Series Circuit")
    ax.grid(True)

    st.pyplot(fig)

    st.success(f"📍 Resonant Frequency: **{f_resonant:.2f} Hz**")
    st.info("📘 At resonance, inductive reactance = capacitive reactance and impedance is minimum.")
