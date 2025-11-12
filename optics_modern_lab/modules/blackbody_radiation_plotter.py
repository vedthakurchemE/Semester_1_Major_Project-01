# modules/blackbody_radiation_plotter.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.626e-34  # Planck's constant (J·s)
c = 3e8  # Speed of light (m/s)
k = 1.38e-23  # Boltzmann constant (J/K)


def plancks_law(wavelength, T):
    """Calculate spectral radiance using Planck's law"""
    a = 2 * h * c ** 2
    b = (h * c) / (wavelength * k * T)
    intensity = a / (wavelength ** 5 * (np.exp(b) - 1))
    return intensity


def run():
    st.title("🌡️ Blackbody Radiation Plotter")
    st.markdown("""
    Visualize **Planck's Radiation Law** for blackbody emitters.

    - Shows how **wavelength** and **temperature** affect intensity.
    - Highlights **Wien’s Displacement Law**.

    **Planck's Law:**  
    `I(λ, T) = (2hc² / λ⁵) / (e^(hc / λkT) - 1)`
    """)

    T = st.slider("🌡️ Temperature (K)", min_value=1000, max_value=10000, value=5000, step=100)

    wavelengths = np.linspace(1e-9, 3e-6, 1000)  # 1 nm to 3000 nm
    intensity = plancks_law(wavelengths, T)

    peak_wavelength = 2.897e-3 / T * 1e9  # Wien's Law in nm

    st.success(f"📍 Peak Wavelength: {peak_wavelength:.1f} nm (Wien’s Law)")

    fig, ax = plt.subplots()
    ax.plot(wavelengths * 1e9, intensity, color='darkorange')
    ax.axvline(peak_wavelength, color='blue', linestyle='--', label="Wien’s Peak")
    ax.set_title("Blackbody Radiation Curve")
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Spectral Radiance (arb. units)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    st.caption("☀️ Explains stellar spectra, thermal imaging, and infrared tech.")
