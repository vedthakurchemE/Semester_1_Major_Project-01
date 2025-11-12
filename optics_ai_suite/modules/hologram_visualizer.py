# hologram_visualizer.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, ifft2, fftshift

def generate_object_field(size=256):
    """Simulates a circular object as a 2D amplitude field."""
    x = np.linspace(-1, 1, size)
    y = np.linspace(-1, 1, size)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    field = np.where(R < 0.4, 1.0, 0.0)  # circular object
    return field

def generate_reference_wave(shape, wavelength, angle_deg):
    """Creates a plane reference wave at a given angle."""
    rows, cols = shape
    x = np.linspace(-1, 1, cols)
    angle_rad = np.deg2rad(angle_deg)
    phase = 2 * np.pi / wavelength * x * np.sin(angle_rad)
    ref_wave = np.exp(1j * phase)
    return np.tile(ref_wave, (rows, 1))

def create_hologram(object_wave, reference_wave):
    """Creates the interference pattern (hologram)."""
    interference = object_wave + reference_wave
    hologram = np.abs(interference) ** 2
    return hologram / np.max(hologram)

def reconstruct_hologram(hologram):
    """Performs a simple Fourier-based reconstruction."""
    field = ifft2(hologram)
    image = np.abs(field) ** 2
    return image / np.max(image)

def run():
    st.markdown("<h1 style='text-align: center;'>🧿 Hologram Visualizer</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>📸 Digital Holography using Interference Simulation</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # Sidebar inputs
    st.sidebar.header("🎚️ Simulation Parameters")
    wavelength = st.sidebar.slider("Wavelength λ (nm)", 400, 700, 532, step=10) / 1e9  # in meters
    angle = st.sidebar.slider("Reference Beam Angle (°)", -60, 60, 30)
    resolution = st.sidebar.selectbox("Resolution", [256, 512, 1024], index=0)

    # Generate object field
    object_field = generate_object_field(resolution)

    # Generate reference wave
    reference_wave = generate_reference_wave(object_field.shape, wavelength, angle)

    # Object wave with phase
    z_distance = 0.01  # 1 cm fixed
    phase_shift = np.exp(1j * 2 * np.pi / wavelength * z_distance)
    object_wave = object_field * phase_shift

    # Hologram generation
    hologram = create_hologram(object_wave, reference_wave)

    # Reconstructed image
    reconstructed = reconstruct_hologram(hologram)

    # Layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌀 Simulated Object Field")
        fig1, ax1 = plt.subplots()
        ax1.imshow(object_field, cmap='gray')
        ax1.set_title("Object Amplitude")
        ax1.axis('off')
        st.pyplot(fig1)

        st.subheader("📷 Generated Hologram")
        fig2, ax2 = plt.subplots()
        ax2.imshow(hologram, cmap='inferno')
        ax2.set_title("Interference Pattern (Hologram)")
        ax2.axis('off')
        st.pyplot(fig2)

    with col2:
        st.subheader("🔁 Reconstructed Image")
        fig3, ax3 = plt.subplots()
        ax3.imshow(reconstructed, cmap='gray')
        ax3.set_title("Reconstructed Output")
        ax3.axis('off')
        st.pyplot(fig3)

        st.markdown("---")
        st.info(f"🧬 Hologram generated using λ = {wavelength * 1e9:.0f} nm and reference angle {angle}°.")

