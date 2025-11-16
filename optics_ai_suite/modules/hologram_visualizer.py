import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, ifft2, fftshift

def generate_object_field(size=256):
    x = np.linspace(-1, 1, size)
    y = np.linspace(-1, 1, size)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    field = np.where(R < 0.4, 1.0, 0.0)
    return field

def generate_reference_wave(shape, wavelength, angle_deg):
    rows, cols = shape
    x = np.linspace(-1, 1, cols)
    angle_rad = np.deg2rad(angle_deg)
    phase = 2 * np.pi / wavelength * x * np.sin(angle_rad)
    ref_wave = np.exp(1j * phase)
    return np.tile(ref_wave, (rows, 1))

def create_hologram(object_wave, reference_wave):
    interference = object_wave + reference_wave
    hologram = np.abs(interference) ** 2
    return hologram / np.max(hologram)

def reconstruct_hologram(hologram):
    field = ifft2(hologram)
    image = np.abs(field) ** 2
    return image / np.max(image)

def run():
    st.markdown("<h1 style='text-align: center;'>🧿 Hologram Visualizer</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>📸 Digital Holography using Interference Simulation</h4>", unsafe_allow_html=True)
    st.markdown("---")

    st.sidebar.header("🎚️ Simulation Parameters")
    wavelength_nm = st.sidebar.slider("Wavelength λ (nm)", 400, 700, 532, step=10)
    wavelength = wavelength_nm / 1e9  # convert nm to meters
    angle = st.sidebar.slider("Reference Beam Angle (°)", -60, 60, 30)
    resolution = st.sidebar.selectbox("Resolution", [256, 512, 1024], index=0)

    object_field = generate_object_field(resolution)
    reference_wave = generate_reference_wave(object_field.shape, wavelength, angle)

    z_distance = 0.01  # 1 cm fixed
    phase_shift = np.exp(1j * 2 * np.pi / wavelength * z_distance)
    object_wave = object_field * phase_shift

    hologram = create_hologram(object_wave, reference_wave)
    reconstructed = reconstruct_hologram(hologram)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌀 Simulated Object Field")
        fig1, ax1 = plt.subplots()
        ax1.imshow(object_field, cmap='gray')
        ax1.set_title("Object Amplitude")
        ax1.axis('off')
        st.pyplot(fig1)
        plt.close(fig1)

        st.subheader("📷 Generated Hologram")
        fig2, ax2 = plt.subplots()
        ax2.imshow(hologram, cmap='inferno')
        ax2.set_title("Interference Pattern (Hologram)")
        ax2.axis('off')
        st.pyplot(fig2)
        plt.close(fig2)

    with col2:
        st.subheader("🔁 Reconstructed Image")
        fig3, ax3 = plt.subplots()
        ax3.imshow(reconstructed, cmap='gray')
        ax3.set_title("Reconstructed Output")
        ax3.axis('off')
        st.pyplot(fig3)
        plt.close(fig3)

        st.markdown("---")
        st.info(f"🧬 Hologram generated using λ = {wavelength_nm:.0f} nm and reference angle {angle}°.")

if __name__ == "__main__":
    run()
