import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def gaussian_beam_radius(w0, wavelength, z):
    """Beam radius w(z) and Rayleigh range z_R as function of z."""
    z_R = np.pi * w0**2 / wavelength
    radius = w0 * np.sqrt(1 + (z / z_R) ** 2)
    return radius, z_R

def divergence_angle(w0, wavelength):
    """Laser beam divergence angle θ [radians]."""
    return wavelength / (np.pi * w0)

def single_slit_intensity(a, wavelength, theta):
    """Fraunhofer single-slit diffraction intensity pattern."""
    beta = (np.pi * a * np.sin(theta)) / wavelength
    # For sinc handling, prevent division by zero
    with np.errstate(divide='ignore', invalid='ignore'):
        intensity = (np.sinc(beta / np.pi)) ** 2
    return intensity

def main():
    st.set_page_config(page_title="🔴 Laser Divergence & Diffraction", layout="wide")

    st.markdown("<h1 style='text-align: center;'>🔴 Laser Beam Divergence & Diffraction</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>📡 Gaussian Spreading & Single-Slit Diffraction</h4>", unsafe_allow_html=True)
    st.markdown("""
        This simulation combines **Gaussian beam optics** and **Fraunhofer single-slit diffraction**.  
        Adjust parameters and explore the core optics principles interactively.  
        - **Download graphs** for further analysis.
    """, unsafe_allow_html=True)
    st.markdown("---")

    # --- Sidebar inputs ---
    st.sidebar.header("🔧 Beam Parameters")
    wavelength_nm = st.sidebar.slider("Wavelength λ (nm)", 400, 1000, 650, step=10)
    wavelength = wavelength_nm * 1e-9
    w0_um = st.sidebar.slider("Beam Waist w₀ (μm)", 1.0, 100.0, 20.0, step=1.0)
    w0 = w0_um * 1e-6
    max_z = st.sidebar.slider("Max Propagation Distance (m)", 0.01, 5.0, 1.0)

    st.sidebar.header("🌊 Diffraction Parameters")
    slit_width_um = st.sidebar.slider("Single Slit Width a (μm)", 1.0, 200.0, 100.0)
    slit_width = slit_width_um * 1e-6

    # --- Beam divergence calculation ---
    z_vals = np.linspace(0, max_z, 500)
    w_vals, z_R = gaussian_beam_radius(w0, wavelength, z_vals)
    theta_div = divergence_angle(w0, wavelength)

    # --- Beam divergence plot ---
    st.subheader("📈 Gaussian Beam Divergence")
    fig1, ax1 = plt.subplots()
    ax1.plot(z_vals, w_vals * 1e6, color="darkblue", lw=2, label="Beam Radius w(z)")
    ax1.axhline(y=w0_um, color='gray', linestyle='--', label="Beam Waist w₀")
    ax1.set_xlabel("Propagation Distance z (m)")
    ax1.set_ylabel("Beam Radius w(z) (μm)")
    ax1.set_title("Laser Beam Radius vs Distance")
    ax1.legend()
    st.pyplot(fig1)
    plt.close(fig1)
    st.download_button("Download Divergence Plot", data=fig1.canvas.tostring_rgb(), file_name="beam_divergence.png")

    st.markdown(f"""
    - **Beam Waist (w₀):** {w0_um:.2f} μm  
    - **Rayleigh Range (zᵣ):** {z_R:.3f} m  
    - **Divergence Angle (θ):** {np.degrees(theta_div):.2f}°  
    """)

    # --- Diffraction calculation and plot ---
    st.subheader("🌈 Single-Slit Diffraction Pattern")
    theta = np.linspace(-0.01, 0.01, 1000)
    intensity = single_slit_intensity(slit_width, wavelength, theta)

    fig2, ax2 = plt.subplots()
    ax2.plot(np.degrees(theta), intensity, color='darkred', label="Diffraction Intensity")
    ax2.set_xlabel("Angle θ (degrees)")
    ax2.set_ylabel("Relative Intensity")
    ax2.set_title("Fraunhofer Diffraction from Single Slit")
    ax2.legend()
    st.pyplot(fig2)
    plt.close(fig2)
    st.download_button("Download Diffraction Plot", data=fig2.canvas.tostring_rgb(), file_name="diffraction_pattern.png")

    central_max_width_deg = 2 * wavelength / slit_width * 180 / np.pi

    st.markdown(f"""
    - **Slit Width (a):** {slit_width_um:.2f} μm  
    - **Central Max Width ≈** {central_max_width_deg:.2f}°  
    """)

    st.info("📌 This simulator combines Gaussian beam optics and classical wave diffraction.<br>"
            "You can download the generated plots for your records or reports.",
            icon="ℹ️")

    st.sidebar.markdown("---")
    st.sidebar.markdown("**Tips:**\n- Increase slit width for sharper peaks\n- Try longer propagation to see far-field divergence")

if __name__ == "__main__":
    main()
