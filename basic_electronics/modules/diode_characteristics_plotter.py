# modules/basic_electronics/diode_characteristics_plotter.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def diode_current(V, Is, n, Vt):
    return Is * (np.exp(V / (n * Vt)) - 1)

def run():
    st.title("🔌 Diode Characteristics Plotter")
    st.markdown("""
    Visualizes **forward-biased I–V characteristics** of a diode using Shockley’s diode equation:

    ---
    \[
    I = I_s (e^{V / nV_t} - 1)
    \]
    Where:
    - \( I_s \) = Saturation current  
    - \( V_t \) = Thermal voltage (≈ 25.85 mV at room temp)  
    - \( n \) = Ideality factor (1–2)
    ---
    """)

    # Diode config
    diode_type = st.radio("📟 Diode Type", ["Silicon", "Germanium", "Custom"])
    if diode_type == "Silicon":
        Is = 1e-12
        n = 1.7
    elif diode_type == "Germanium":
        Is = 1e-6
        n = 1.2
    else:
        Is = st.number_input("Saturation Current (A)", min_value=1e-15, value=1e-12, format="%.1e")
        n = st.slider("Ideality Factor (n)", 1.0, 2.0, 1.5)

    Vt = 0.02585  # Thermal voltage at room temperature
    V = np.linspace(0, 0.8, 300)
    I = diode_current(V, Is, n, Vt)

    # Plot
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(V, I * 1000, color="darkgreen", linewidth=2)
    ax.set_xlabel("Voltage (V)")
    ax.set_ylabel("Current (mA)")
    ax.set_title("📈 Diode Forward I–V Characteristics")
    ax.grid(True)
    st.pyplot(fig)

    st.info("⚠️ Plot is for forward bias only. Reverse region excluded in this simulation.")
