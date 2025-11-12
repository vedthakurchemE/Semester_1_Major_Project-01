import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from numpy import trapz

def run():
    st.header("🚰 Module 10: Water Tank Filling Simulation")

    st.markdown(r"""
    This module models how a **water level rises** in a tank over time with variable inflow rate.

    ### Volume Balance:
    \[
    V(t) = \int_0^t Q(t)\, dt \quad \text{and} \quad h(t) = \frac{V(t)}{A}
    \]

    Where:
    - \( Q(t) \): inflow rate (m³/hr)
    - \( A \): tank area (m²)
    - \( V(t) \): volume (m³)
    - \( h(t) \): height (m)
    """)

    area = st.slider("Tank Area A (m²)", 1, 200, 50)
    T = st.slider("Simulation Duration (hours)", 1, 48, 12)
    scenario = st.selectbox("Inflow Pattern", ["Constant", "Increasing", "Fluctuating", "Custom Sinusoidal"])

    t = np.linspace(0, T, 500)

    if scenario == "Constant":
        Q = np.full_like(t, 10)
    elif scenario == "Increasing":
        Q = 2 + 0.8 * t
    elif scenario == "Fluctuating":
        Q = 10 + 3 * np.sin(2 * np.pi * t / 6)
    elif scenario == "Custom Sinusoidal":
        amp = st.slider("Amplitude (m³/hr)", 0, 20, 5)
        base = st.slider("Base Rate (m³/hr)", 0, 50, 15)
        freq = st.slider("Frequency (per hour)", 1, 10, 2)
        Q = base + amp * np.sin(2 * np.pi * freq * t / T)

    # Replace cumtrapz with cumulative trapz approximation
    V = np.zeros_like(t)
    for i in range(1, len(t)):
        V[i] = trapz(Q[:i+1], t[:i+1])

    h = V / area

    # Plotting
    fig, ax = plt.subplots(2, 1, figsize=(8, 7), sharex=True)
    ax[0].plot(t, Q, label="Inflow Rate Q(t)", color="royalblue")
    ax[0].set_ylabel("Flow Rate (m³/hr)")
    ax[0].grid(True)
    ax[0].legend()

    ax[1].plot(t, h, label="Water Height h(t)", color="seagreen")
    ax[1].set_ylabel("Water Height (m)")
    ax[1].set_xlabel("Time (hr)")
    ax[1].grid(True)
    ax[1].legend()

    st.pyplot(fig)

    st.success(f"💧 Final Water Level after {T} hrs: {h[-1]:.2f} meters")
    st.info(f"🧮 Total Volume Accumulated: {V[-1]:.2f} m³")

    st.markdown("""
    **Use Cases**:
    - Design tank size
    - Predict overflow time
    - Schedule pumping systems
    """)
