import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import ifft2

def generate_object_field(size=256, radius=0.4):
    """Simulate a circular object as a 2D amplitude field."""
    x = np.linspace(-1, 1, size)
    y = np.linspace(-1, 1, size)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    field = np.where(R < radius, 1.0, 0.0)
    return field

def generate_reference_wave(shape, wavelength, angle_deg):
    """Create reference wave at a given angle."""
    rows, cols = shape
    x = np.linspace(-1, 1, cols)
    angle_rad = np.deg2rad(angle_deg)
    phase = 2 * np.pi / wavelength * x * np.sin(angle_rad)
    ref_wave = np.exp(1j * phase)
    return np.tile(ref_wave, (rows, 1))

def create_hologram(object_wave, reference_wave):
    """Create the interference pattern (hologram)."""
    interference = object_wave + reference_wave
    hologram = np.abs(interference) ** 2
    return hologram / np.max(hologram)

def reconstruct_hologram(hologram):
    """Fourier-based hologram reconstruction."""
    field = ifft2(hologram)
    image = np.abs(field) ** 2
    return image / np.max(image)

def run():
    st.markdown("<h1 style='text-align: center;'>🧿 Hologram Visualizer</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>📸 Simulate Digital Holography using Interference</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # Sidebar parameters
    st.sidebar.header("🎚️ Hologram Parameters")
    wavelength_nm = st.sidebar.slider("Wavelength λ (nm)", 400, 700, 532, step=10)
    wavelength = wavelength_nm / 1e9  # nm → m
    angle = st.sidebar.slider("Reference Beam Angle (°)", -60, 60, 30)
    resolution = st.sidebar.selectbox("Resolution (pixels)", [256, 512, 1024], index=0)
    obj_radius = st.sidebar.slider("Object Radius", 0.2, 0.9, 0.4, step=0.01)
    z_distance_cm = st.sidebar.slider("Object Distance z (cm)", 0.1, 5.0, 1.0, step=0.01)
    z_distance = z_distance_cm / 100  # in meters

    # Simulation
    object_field = generate_object_field(resolution, obj_radius)
    reference_wave = generate_reference_wave(object_field.shape, wavelength, angle)
    phase_shift = np.exp(1j * 2 * np.pi / wavelength * z_distance)
    object_wave = object_field * phase_shift

    hologram = create_hologram(object_wave, reference_wave)
    reconstructed = reconstruct_hologram(hologram)

    # Layout and plots
    fig1, ax1 = plt.subplots()
    ax1.imshow(object_field, cmap='gray')
    ax1.set_title(f"Object Field (radius={obj_radius})")
    ax1.axis('off')

    fig2, ax2 = plt.subplots()
    ax2.imshow(hologram, cmap='inferno')
    ax2.set_title("Generated Hologram")
    ax2.axis('off')

    fig3, ax3 = plt.subplots()
    ax3.imshow(reconstructed, cmap='gray')
    ax3.set_title("Reconstructed Image")
    ax3.axis('off')

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🌀 Simulated Object Field")
        st.pyplot(fig1)
        plt.close(fig1)

        st.subheader("📷 Generated Hologram")
        st.pyplot(fig2)
        plt.close(fig2)

    with col2:
        st.subheader("🔁 Reconstructed Image")
        st.pyplot(fig3)
        plt.close(fig3)

        st.markdown("---")
        st.subheader("📊 Analysis")
        st.markdown(f"- **Wavelength (λ):** {wavelength_nm} nm")
        st.markdown(f"- **Reference Angle:** {angle}°")
        st.markdown(f"- **Object Radius:** {obj_radius:.2f}")
        st.markdown(f"- **Object Distance:** {z_distance_cm:.2f} cm")
        st.markdown(f"- **Resolution:** {resolution} px")
        st.success("✅ Hologram simulation complete!")

if __name__ == "__main__":
    run()
