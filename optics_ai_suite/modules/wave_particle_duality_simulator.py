import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.markdown("<h1 style='text-align: center;'>🌊 Wave-Particle Duality Simulator</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>🧠 Double-Slit Interference with Photons or Electrons</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # Sidebar Inputs
    st.sidebar.header("⚙️ Experiment Parameters")
    wave_type = st.sidebar.selectbox("🔬 Particle Type", ["Photon", "Electron"])

    if wave_type == "Photon":
        wavelength_nm = st.sidebar.slider("Wavelength λ (nm)", 100.0, 1000.0, 550.0)
    else:
        # For electrons, infer de Broglie wavelength from KE
        KE_eV = st.sidebar.slider("Electron Energy (eV)", 1.0, 1000.0, 100.0)
        h = 6.626e-34  # Planck's constant (J·s)
        m = 9.11e-31   # Electron mass (kg)
        e = 1.602e-19  # Charge (C)
        p = np.sqrt(2 * m * KE_eV * e)  # momentum
        λ = h / p
        wavelength_nm = λ * 1e9

    slit_distance = st.sidebar.slider("Slit Separation d (μm)", 1.0, 100.0, 20.0)
    slit_width = st.sidebar.slider("Slit Width a (μm)", 0.1, 20.0, 5.0)
    screen_distance = st.sidebar.slider("Screen Distance L (m)", 0.1, 5.0, 1.0)

    # Convert units
    λ = wavelength_nm * 1e-9
    d = slit_distance * 1e-6
    a = slit_width * 1e-6
    L = screen_distance

    # Screen setup
    y = np.linspace(-0.01, 0.01, 2000)  # ±1 cm on screen
    beta = (np.pi * a * y) / (λ * L)
    delta = (np.pi * d * y) / (λ * L)

    # Intensity pattern (Fraunhofer)
    single_slit = (np.sinc(beta / np.pi))**2
    double_slit = np.cos(delta)**2
    intensity = single_slit * double_slit
    intensity /= np.max(intensity)  # Normalize

    # Interference Plot
    st.subheader("📈 Interference Pattern")
    fig, ax = plt.subplots()
    ax.plot(y * 1e3, intensity, color='navy')
    ax.set_xlabel("Screen Position y (mm)")
    ax.set_ylabel("Normalized Intensity")
    ax.set_title(f"Double-Slit Interference ({wave_type})")
    st.pyplot(fig)

    # Output Summary
    st.markdown("---")
    st.subheader("📊 Summary")
    st.markdown(f"""
    - **Wave Type:** `{wave_type}`
    - **Wavelength (λ):** `{wavelength_nm:.2f} nm`
    - **Slit Separation (d):** `{slit_distance:.1f} μm`
    - **Slit Width (a):** `{slit_width:.1f} μm`
    - **Screen Distance (L):** `{screen_distance:.2f} m`
    """)

    if wave_type == "Electron":
        st.markdown(f"- **Electron KE:** `{KE_eV:.1f} eV`")

    # Quantum Explanation
    st.subheader("🧠 Quantum Interpretation")
    st.markdown(f"""
    - Each **{wave_type.lower()}** behaves like a wave and a particle.
    - Interference arises even when particles pass one at a time.
    - Bright and dark fringes are due to **constructive** and **destructive** interference.
    - For **photons**, wavelength is based on source color.
    - For **electrons**, wavelength comes from **de Broglie relation**:
      \n\\[ \\lambda = \\frac{{h}}{{p}} \\quad \\text{{where }} p = \\sqrt{{2mE}} \\]
    """)

    st.info("📌 You just simulated one of the most fundamental experiments in quantum physics!")
