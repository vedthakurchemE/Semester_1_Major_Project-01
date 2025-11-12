# photoelectric_effect_simulator.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.markdown("<h1 style='text-align: center;'>⚛️ Photoelectric Effect Simulator</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>🔬 Explore Photon Energy, Work Function, and Electron Emission</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # Constants
    h = 6.626e-34  # Planck’s constant (J·s)
    e = 1.602e-19  # Elementary charge (C)

    # Material database (work function in eV)
    materials = {
        "Sodium (Na)": 2.28,
        "Cesium (Cs)": 1.9,
        "Potassium (K)": 2.3,
        "Zinc (Zn)": 4.3,
        "Calcium (Ca)": 2.9,
        "Copper (Cu)": 4.7
    }

    # Sidebar Inputs
    st.sidebar.header("⚙️ Simulation Inputs")
    material = st.sidebar.selectbox("Select Metal Surface", list(materials.keys()))
    freq = st.sidebar.slider("Incident Light Frequency (×10¹⁴ Hz)", 1.0, 10.0, 5.0, step=0.1) * 1e14

    # Calculations
    work_fn_eV = materials[material]
    photon_energy_J = h * freq
    photon_energy_eV = photon_energy_J / e
    KE_eV = photon_energy_eV - work_fn_eV
    KE_eV = max(0, KE_eV)
    emission = photon_energy_eV >= work_fn_eV

    # Output Section
    st.subheader("📊 Results")
    st.markdown(f"- **Material:** `{material}`")
    st.markdown(f"- **Work Function (ϕ):** `{work_fn_eV} eV`")
    st.markdown(f"- **Photon Energy (E):** `{photon_energy_eV:.2f} eV`")
    st.markdown(f"- **Kinetic Energy (KE):** `{KE_eV:.2f} eV`")
    st.markdown(f"- **Electron Emitted?** {'✅ Yes' if emission else '❌ No'}")

    # Graph Plotting: KE vs Frequency
    freqs = np.linspace(1e14, 1e15, 500)
    photon_E = h * freqs / e
    KE = np.maximum(photon_E - work_fn_eV, 0)

    st.subheader("📈 Kinetic Energy vs Frequency")
    fig, ax = plt.subplots()
    ax.plot(freqs * 1e-14, KE, label="Kinetic Energy", color="darkgreen")
    ax.axhline(0, color="gray", linestyle="--")
    ax.axvline(freq * 1e-14, color="red", linestyle="--", label="Selected Frequency")
    ax.set_xlabel("Frequency (×10¹⁴ Hz)")
    ax.set_ylabel("Kinetic Energy (eV)")
    ax.set_title(f"KE vs Frequency for {material}")
    ax.legend()
    st.pyplot(fig)

    st.markdown("---")
    st.info("📌 Increase frequency to observe the threshold behavior and kinetic energy rise.")
