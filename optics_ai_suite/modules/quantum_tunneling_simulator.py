# quantum_tunneling_simulator.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def wave_function(E, V0, a, x):
    """Return the wave function across regions for 1D potential barrier."""
    m = 9.11e-31  # mass of electron (kg)
    hbar = 1.055e-34  # reduced Planck constant (J.s)
    eV = 1.602e-19  # J per eV

    k1 = np.sqrt(2 * m * E * eV) / hbar
    k2 = np.sqrt(2 * m * (V0 - E) * eV) / hbar if V0 > E else np.sqrt(2 * m * abs(E - V0) * eV) / hbar

    psi = np.zeros_like(x, dtype=np.complex128)

    for i, xi in enumerate(x):
        if xi < 0:
            psi[i] = np.exp(1j * k1 * xi)
        elif xi >= 0 and xi <= a:
            if E < V0:
                psi[i] = np.exp(-k2 * xi)
            else:
                psi[i] = np.exp(1j * k2 * xi)
        else:
            psi[i] = np.exp(1j * k1 * xi)

    return psi


def transmission_probability(E, V0, a):
    """Compute transmission probability T."""
    m = 9.11e-31
    hbar = 1.055e-34
    eV = 1.602e-19

    if E >= V0:
        return 1.0
    else:
        kappa = np.sqrt(2 * m * (V0 - E) * eV) / hbar
        T = np.exp(-2 * kappa * a)
        return T


def run():
    st.markdown("<h1 style='text-align: center;'>🔭 Quantum Tunneling Simulator</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>🚀 Visualize Wave Functions and Barrier Penetration</h4>",
                unsafe_allow_html=True)
    st.markdown("---")

    # Sidebar controls
    st.sidebar.header("⚙️ Parameters")
    E = st.sidebar.slider("Particle Energy E (eV)", 0.1, 10.0, 2.0, step=0.1)
    V0 = st.sidebar.slider("Barrier Height V₀ (eV)", 0.1, 10.0, 5.0, step=0.1)
    a = st.sidebar.slider("Barrier Width a (nm)", 0.1, 5.0, 1.0, step=0.1) * 1e-9  # in meters

    x = np.linspace(-2e-9, 5e-9, 1000)
    psi = wave_function(E, V0, a, x)
    prob_density = np.abs(psi) ** 2

    # Transmission probability
    T = transmission_probability(E, V0, a) * 100

    # Layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📉 Wave Function Amplitude")
        fig1, ax1 = plt.subplots()
        ax1.plot(x * 1e9, np.real(psi), label="Re[Ψ]", color='blue')
        ax1.plot(x * 1e9, np.imag(psi), label="Im[Ψ]", color='red')
        ax1.axvspan(0, a * 1e9, color='orange', alpha=0.3, label="Barrier")
        ax1.set_xlabel("x (nm)")
        ax1.set_ylabel("Amplitude")
        ax1.set_title("Wave Function (Real & Imag)")
        ax1.legend()
        st.pyplot(fig1)

    with col2:
        st.subheader("📊 Probability Density |Ψ|²")
        fig2, ax2 = plt.subplots()
        ax2.plot(x * 1e9, prob_density, color='purple')
        ax2.axvspan(0, a * 1e9, color='orange', alpha=0.3, label="Barrier")
        ax2.set_xlabel("x (nm)")
        ax2.set_ylabel("|Ψ(x)|²")
        ax2.set_title("Probability Density")
        ax2.legend()
        st.pyplot(fig2)

    st.markdown("### 📈 Transmission Estimate")
    st.metric(label="Transmission Probability", value=f"{T:.2f} %")
    st.markdown(f"""
    - Particle Energy: **{E:.2f} eV**
    - Barrier Height: **{V0:.2f} eV**
    - Barrier Width: **{a * 1e9:.2f} nm**
    - Tunneling is significant when **E < V₀**, otherwise near total transmission.
    """)
    st.info("🧬 This simulation models a quantum particle encountering a rectangular potential barrier.")
