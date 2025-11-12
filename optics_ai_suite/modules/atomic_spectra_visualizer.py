# atomic_spectra_visualizer.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def get_spectral_region(wavelength_nm):
    if wavelength_nm < 400:
        return "Ultraviolet (UV)", "#9400D3"
    elif 400 <= wavelength_nm <= 700:
        return "Visible", "rgb(0,255,0)"
    else:
        return "Infrared (IR)", "#FF5733"

def run():
    st.markdown("<h1 style='text-align: center;'>🌈 Atomic Spectra Visualizer</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>🔬 Bohr Model & Emission Spectra Transitions</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # Constants
    h = 6.626e-34  # J·s
    c = 3e8        # m/s
    e = 1.602e-19  # C
    R_H = 1.097e7  # Rydberg constant (1/m)

    # Sidebar inputs
    st.sidebar.header("⚙️ Transition Parameters")
    atom = st.sidebar.selectbox("Select Atom", ["Hydrogen (Z=1)", "He⁺ (Z=2)", "Li²⁺ (Z=3)"])
    Z = int(atom.split("=")[-1].replace(")", ""))

    n1 = st.sidebar.slider("Initial Energy Level (n₁)", 2, 10, 3)
    n2 = st.sidebar.slider("Final Energy Level (n₂)", 1, n1 - 1, 2)

    # Error handling: No transition when n1 == n2
    if n1 == n2:
        st.warning("⚠️ No transition possible: Initial and final energy levels are the same (n₁ = n₂).")
        st.markdown("""
        - 📌 Atomic spectra are produced **only when electrons transition** between different energy levels.
        - Since `n₁ = n₂`, the **energy difference (ΔE) = 0**, so:
            - ❌ No photon is emitted or absorbed
            - ❌ No spectral line is produced
            - ❌ This is not a valid atomic transition
        """)
        st.stop()

    # Energy and wavelength calculations
    delta_E = 13.6 * Z**2 * (1/n2**2 - 1/n1**2)  # in eV
    wavelength_m = h * c / (delta_E * e)
    wavelength_nm = wavelength_m * 1e9
    region, color = get_spectral_region(wavelength_nm)

    st.subheader("📊 Transition Results")
    st.markdown(f"- **Atom:** `{atom}`")
    st.markdown(f"- **Transition:** n₁ = {n1} → n₂ = {n2}")
    st.markdown(f"- **Energy Emitted (ΔE):** {delta_E:.2f} eV")
    st.markdown(f"- **Wavelength (λ):** {wavelength_nm:.2f} nm")
    st.markdown(f"- **Spectral Region:** `{region}`")

    st.subheader("🎨 Spectral Line Preview")
    st.markdown(f"<div style='width:100%;height:50px;background:{color};text-align:center;color:white;font-weight:bold;'>λ = {wavelength_nm:.2f} nm ({region})</div>", unsafe_allow_html=True)

    # Bohr orbit diagram
    st.subheader("🔭 Bohr Orbit Transitions")
    levels = list(range(1, n1+2))
    radii = [n**2 / Z for n in levels]

    fig, ax = plt.subplots(figsize=(5, 5))
    for i, r in enumerate(radii):
        circle = plt.Circle((0, 0), r, fill=False, linestyle='--' if i+1 == n2 else '-', edgecolor='gray')
        ax.add_artist(circle)
        ax.text(r + 0.1, 0, f"n={i+1}", fontsize=10)

    ax.plot([radii[n1-1], radii[n2-1]], [0, 0], 'r->', lw=2, label="Transition")
    ax.set_xlim(-radii[-1]-1, radii[-1]+1)
    ax.set_ylim(-radii[-1]-1, radii[-1]+1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title("Bohr Model: Electron Transition")
    st.pyplot(fig)

    st.info("📌 This simulation shows photon emission when electrons fall from higher to lower energy levels.")
