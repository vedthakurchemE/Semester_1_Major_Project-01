# modules/polarization_visualizer.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def malus_law(intensity_0, angle_deg):
    theta_rad = np.radians(angle_deg)
    return intensity_0 * (np.cos(theta_rad) ** 2)

def run():
    st.title("🕶️ Polarization Visualizer (Malus's Law)")
    st.markdown("""
    Simulate how **light intensity** varies through a polarizer-analyzer setup.

    **Malus's Law**  
    `I = I₀ × cos²(θ)`  
    where:
    - `I₀` is the initial intensity  
    - `θ` is the angle between polarization axes
    """)

    col1, col2 = st.columns(2)
    with col1:
        I0 = st.slider("🔆 Initial Intensity (I₀)", 10, 100, 50)
    with col2:
        angle = st.slider("🔄 Analyzer Angle (°)", 0, 180, 90)

    I = malus_law(I0, angle)

    st.success(f"📉 Transmitted Intensity: **{I:.2f} units**")

    st.subheader("📊 Intensity vs Analyzer Angle")
    angles = np.linspace(0, 180, 360)
    intensities = malus_law(I0, angles)

    fig, ax = plt.subplots()
    ax.plot(angles, intensities, color="blue", linewidth=2)
    ax.axvline(angle, color='red', linestyle='--', label=f"θ = {angle}°")
    ax.set_xlabel("Angle (θ in degrees)")
    ax.set_ylabel("Transmitted Intensity (I)")
    ax.set_title("Malus's Law Curve")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    st.caption("🔍 Used in sunglasses, optical sensors, and laser physics.")
