# laser_divergence_simulator.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import j1

def gaussian_beam_radius(w0, wavelength, z):
    """Beam radius w(z) as function of distance z"""
    z_R = np.pi * w0**2 / wavelength
    return w0 * np.sqrt(1 + (z / z_R)**2), z_R

def divergence_angle(w0, wavelength):
    """Beam divergence angle θ"""
    return wavelength / (np.pi * w0)

def single_slit_intensity(a, wavelength, theta):
    """Fraunhofer single-slit diffraction intensity"""
    beta = (np.pi * a * np.sin(theta)) / wavelength
    return (np.sinc(beta / np.pi))**2

def run():
    st.markdown("<h1 style='text-align: center;'>🔴 Laser Beam Divergence & Diffraction</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>📡 Gaussian Spreading & Single-Slit Diffraction</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # Sidebar inputs
    st.sidebar.header("🔧 Beam Parameters")
    wavelength = st.sidebar.slider("Wavelength λ (nm)", 400, 1000, 650, step=10) * 1e-9
    w0 = st.sidebar.slider("Beam Waist w₀ (μm)", 1.0, 100.0, 20.0, step=1.0) * 1e-6
    max_z = st.sidebar.slider("Max Propagation Distance (m)", 0.01, 5.0, 1.0)

    st.sidebar.header("🌊 Diffraction Parameters")
    slit_width = st.sidebar.slider("Single Slit Width a (μm)", 1.0, 200.0, 100.0) * 1e-6

    # Beam divergence visualization
    z_vals = np.linspace(0, max_z, 500)
    w_vals, z_R = gaussian_beam_radius(w0, wavelength, z_vals)
    theta_div = divergence_angle(w0, wavelength)

    st.subheader("📈 Gaussian Beam Divergence")
    fig1, ax1 = plt.subplots()
    ax1.plot(z_vals, w_vals * 1e6, color="darkblue", lw=2)
    ax1.axhline(y=w0 * 1e6, color='gray', linestyle='--', label="Beam Waist w₀")
    ax1.set_xlabel("Propagation Distance z (m)")
    ax1.set_ylabel("Beam Radius w(z) (μm)")
    ax1.set_title("Laser Beam Radius vs Distance")
    ax1.legend()
    st.pyplot(fig1)

    st.markdown(f"""
    - **Beam Waist (w₀):** {w0*1e6:.2f} μm  
    - **Rayleigh Range (zᵣ):** {z_R:.3f} m  
    - **Divergence Angle (θ):** {np.degrees(theta_div):.2f}°  
    """)

    st.subheader("🌈 Single-Slit Diffraction Pattern")
    theta = np.linspace(-0.01, 0.01, 1000)
    intensity = single_slit_intensity(slit_width, wavelength, theta)

    fig2, ax2 = plt.subplots()
    ax2.plot(np.degrees(theta), intensity, color='darkred')
    ax2.set_xlabel("Angle θ (degrees)")
    ax2.set_ylabel("Relative Intensity")
    ax2.set_title("Fraunhofer Diffraction from Single Slit")
    st.pyplot(fig2)

    st.markdown(f"""
    - **Slit Width (a):** {slit_width * 1e6:.2f} μm  
    - **Central Max Width ≈** {2 * wavelength / slit_width * 180 / np.pi:.2f}°  
    """)

    st.info("📌 This simulator combines Gaussian beam optics and classical wave diffraction.")
