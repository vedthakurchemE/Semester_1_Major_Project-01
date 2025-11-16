# modules/diffraction_grating_tool.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def diffraction_angles(n, d, λ):
    # Return angle in degrees using the diffraction formula: nλ = d sinθ
    sin_theta = n * λ / d
    valid = np.abs(sin_theta) <= 1
    angles_deg = np.degrees(np.arcsin(sin_theta[valid]))
    return n[valid], angles_deg

def run():
    st.title("🧪 Diffraction Grating Simulator")
    st.markdown("""
    Simulate the **diffraction pattern** caused by a grating using multiple light wavelengths.

    **Equation Used:**  
    `nλ = d sinθ` — for constructive interference
    """)

    st.subheader("🔧 Input Parameters")
    col1, col2 = st.columns(2)
    with col1:
        wavelength_nm = st.slider("🔴 Wavelength (nm)", 400, 700, 550)
    with col2:
        lines_per_mm = st.slider("📏 Grating Lines per mm", 100, 1000, 500)

    λ = wavelength_nm * 1e-9  # Convert nm to m
    d = 1e-3 / lines_per_mm   # Convert lines/mm to slit spacing in meters

    # Orders of diffraction to consider
    n_vals = np.arange(1, 6)
    n, angles = diffraction_angles(n_vals, d, λ)

    st.subheader("📈 Diffraction Angles")
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.stem(n, angles, basefmt=" ", linefmt="blue", markerfmt="bo")
    ax.set_xlabel("Order of Diffraction (n)")
    ax.set_ylabel("Diffraction Angle (degrees)")
    ax.set_title("Diffraction Angle vs Order")
    ax.grid(True)
    st.pyplot(fig)
    st.video('https://www.youtube.com/watch?v=p8cyO76gxZI')
    if len(angles) > 0:
        st.success(f"✅ Max observable order: n = {n[-1]}, θ = {angles[-1]:.2f}°")
    else:
        st.error("⚠️ No valid diffraction angles found (maybe λ or grating too large).")

    st.caption("🌈 Used in spectrometers, lasers, and wavelength determination.")
