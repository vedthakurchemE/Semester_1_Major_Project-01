# modules/xray_tube_simulator.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.626e-34  # Planck's constant (J·s)
c = 3e8  # Speed of light (m/s)
e = 1.602e-19  # Electron charge (C)


def calculate_min_wavelength(voltage_kV):
    """Calculate λmin using λ = hc/eV"""
    V = voltage_kV * 1e3  # Convert kV to V
    return (h * c) / (e * V) * 1e10  # in Angstroms


def bremsstrahlung_spectrum(voltage_kV, resolution=1000):
    """Simulated Bremsstrahlung intensity curve"""
    λmin = calculate_min_wavelength(voltage_kV)
    λ = np.linspace(λmin, 10, resolution)  # From λmin to 10 Å
    intensity = (1 / λ) * np.exp(-λ / λmin)
    return λ, intensity


def run():
    st.title("📡 X-Ray Tube Simulator")
    st.markdown("""
    Simulate the **generation of X-rays** in a vacuum tube setup.

    - **Accelerated electrons** hit a metal target.
    - Produces **Bremsstrahlung** + **Characteristic X-rays**.

    **Key Relation:**  
    `λmin = hc / eV` (Short-wavelength limit)
    """)

    voltage = st.slider("⚡ Accelerating Voltage (kV)", min_value=10, max_value=150, value=60)
    λmin = calculate_min_wavelength(voltage)

    st.success(f"🔻 Minimum Wavelength (λmin): {λmin:.2f} Å")

    st.subheader("📊 Simulated X-ray Spectrum")

    λ, intensity = bremsstrahlung_spectrum(voltage)

    fig, ax = plt.subplots()
    ax.plot(λ, intensity, label="Bremsstrahlung", color="darkred")

    # Add sample characteristic lines (for Copper target)
    ax.axvline(x=1.54, color='blue', linestyle='--', label="Kα (Cu)")
    ax.axvline(x=1.49, color='green', linestyle='--', label="Kβ (Cu)")

    ax.set_xlim(λmin, 5)
    ax.set_xlabel("Wavelength (Å)")
    ax.set_ylabel("Relative Intensity")
    ax.set_title("X-ray Spectrum")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    st.caption("📌 Used in medical imaging, crystallography, and material science.")
