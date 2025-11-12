# modules/youngs_double_slit.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calculate_intensity(x, d, D, λ):
    β = (np.pi * d * x) / (λ * D)
    return (np.cos(β))**2

def run():
    st.title("🌈 Young's Double Slit Experiment Simulator")
    st.markdown("""
    Simulate the **interference pattern** generated in the famous **Young's Double Slit Experiment**.

    **Fringe Formula:**  
    `β = (λ × D) / d` — Fringe Width  
    `I ∝ cos²(πdx / λD)` — Intensity Pattern
    """)

    st.subheader("🔧 Input Parameters")
    col1, col2, col3 = st.columns(3)
    with col1:
        wavelength_nm = st.slider("🟣 Wavelength λ (nm)", 400, 700, 550)
    with col2:
        slit_distance_mm = st.slider("🔸 Slit Separation d (mm)", 0.1, 5.0, 0.5)
    with col3:
        screen_distance_cm = st.slider("📏 Screen Distance D (cm)", 10, 100, 50)

    # Unit conversions
    λ = wavelength_nm * 1e-9
    d = slit_distance_mm * 1e-3
    D = screen_distance_cm / 100

    # X range on the screen
    x = np.linspace(-0.01, 0.01, 1000)
    I = calculate_intensity(x, d, D, λ)

    st.subheader("🎨 Interference Pattern")
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.plot(x * 1000, I, color="purple")
    ax.set_xlabel("Position on Screen (mm)")
    ax.set_ylabel("Relative Intensity")
    ax.set_title("Young's Double Slit Interference Pattern")
    ax.grid(True)
    st.pyplot(fig)

    fringe_width = (λ * D) / d * 1000  # mm
    st.success(f"📐 Fringe Width β ≈ **{fringe_width:.3f} mm**")
    st.caption("🧠 Used in wavelength estimation and wave property demonstrations.")
