# modules/wave_particle_duality_explorer.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

h = 6.626e-34  # Planck's constant in J·s


def de_broglie_wavelength(mass, velocity):
    return h / (mass * velocity)


def run():
    st.title("🌊⚛️ Wave-Particle Duality Explorer")
    st.markdown("""
    Explore the dual nature of matter — both **waves and particles** — using quantum physics principles.

    **de Broglie Wavelength:**  
    `λ = h / (mv)`

    - Lower mass & velocity → longer wavelength
    - Visualize patterns like in **Young’s Double Slit**
    """)

    particle_type = st.selectbox("🧪 Choose Particle", ["Electron", "Proton", "Neutron", "Custom"])

    if particle_type == "Electron":
        mass = 9.11e-31
        velocity = st.slider("⚡ Velocity (m/s)", 1e5, 1e8, 2e6)
    elif particle_type == "Proton":
        mass = 1.67e-27
        velocity = st.slider("⚡ Velocity (m/s)", 1e4, 1e7, 1e6)
    elif particle_type == "Neutron":
        mass = 1.675e-27
        velocity = st.slider("⚡ Velocity (m/s)", 1e4, 1e6, 5e5)
    else:
        mass = st.number_input("Mass (kg)", min_value=1e-35, value=9.11e-31)
        velocity = st.number_input("Velocity (m/s)", min_value=1e3, value=1e6)

    λ = de_broglie_wavelength(mass, velocity)
    st.success(f"📏 de Broglie Wavelength: **{λ * 1e9:.3e} nm**")

    st.subheader("🌀 Simulated Interference Pattern (Young’s Setup)")

    slit_distance = 1e-6  # meters
    screen_distance = 1  # meter
    screen_range = np.linspace(-0.01, 0.01, 1000)  # 2 cm wide screen

    # Intensity pattern formula: I = cos²(π d x / λ L)
    beta = (np.pi * slit_distance * screen_range) / (λ * screen_distance)
    intensity = np.cos(beta) ** 2

    fig, ax = plt.subplots()
    ax.plot(screen_range * 1000, intensity, color='purple')
    ax.set_xlabel("Position on Screen (mm)")
    ax.set_ylabel("Relative Intensity")
    ax.set_title("Double-Slit Interference Pattern")
    ax.grid(True)
    st.pyplot(fig)

    st.caption("🎯 As particle mass increases → wavelength decreases → pattern disappears.")
