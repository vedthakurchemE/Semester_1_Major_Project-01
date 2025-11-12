# solar_cell_analyzer.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def solar_spectrum(wavelength_nm):
    """Approximate solar spectrum using Planck's law."""
    h = 6.626e-34  # J*s
    c = 3e8        # m/s
    k = 1.381e-23  # J/K
    T = 5778       # Sun's surface temp

    wavelength_m = wavelength_nm * 1e-9
    intensity = (2 * h * c**2) / (wavelength_m**5) / (np.exp(h * c / (wavelength_m * k * T)) - 1)
    return intensity / np.max(intensity)

def calculate_efficiency(Eg):
    """Estimate theoretical efficiency using basic photon absorption logic."""
    # Photon energy range from 0.3 eV to 4 eV
    E = np.linspace(0.3, 4, 1000)
    q = 1.602e-19

    absorbed = E >= Eg
    efficiency = np.trapz((Eg / E[absorbed]), E[absorbed]) / np.trapz(np.ones_like(E), E)
    return efficiency * 100

def run():
    st.markdown("<h1 style='text-align: center;'>🔆 Solar Cell Analyzer</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>🌡️ Band Gap vs Theoretical Efficiency Explorer</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # Sidebar controls
    st.sidebar.header("⚙️ Input Parameters")
    Eg = st.sidebar.slider("Band Gap Energy (eV)", 0.5, 3.5, 1.1, step=0.05)

    # Matching materials
    material_map = {
        1.1: "Silicon",
        1.42: "Gallium Arsenide (GaAs)",
        1.5: "Perovskite (CH3NH3PbI3)",
        1.0: "Germanium",
        1.5: "CdTe",
        2.4: "ZnO",
        3.4: "GaN"
    }

    nearest_material = min(material_map.keys(), key=lambda x: abs(x - Eg))
    material = material_map.get(nearest_material, "Unknown")

    # Efficiency Estimation
    efficiency = calculate_efficiency(Eg)

    # Solar spectrum plotting
    wavelength = np.linspace(300, 2500, 1000)
    spectrum = solar_spectrum(wavelength)
    photon_energy = 1240 / wavelength  # in eV

    # Layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Solar Spectrum vs Band Gap")
        fig, ax = plt.subplots()
        ax.plot(wavelength, spectrum, label="Normalized Solar Spectrum", color="goldenrod")
        ax.axvline(1240 / Eg, color='red', linestyle='--', label=f'Band Gap = {Eg} eV')
        ax.fill_between(wavelength, 0, spectrum, where=photon_energy >= Eg, color='skyblue', alpha=0.5, label="Absorbed Photons")
        ax.set_xlim(300, 2500)
        ax.set_xlabel("Wavelength (nm)")
        ax.set_ylabel("Relative Intensity")
        ax.set_title("Solar Spectrum and Absorption Cutoff")
        ax.legend()
        st.pyplot(fig)

    with col2:
        st.subheader("⚡ Efficiency Estimate")
        st.metric("Estimated Max Efficiency", f"{efficiency:.2f} %")
        st.metric("Closest Material Match", f"{material}")
        st.markdown(f"""
        - **Band Gap:** {Eg:.2f} eV  
        - **Material:** {material}  
        - **Photon Energy Threshold:** {1240 / Eg:.0f} nm  
        """)
        st.markdown("✅ This estimate is based on idealized assumptions (Shockley–Queisser Limit).")

    st.markdown("---")
    st.info("🧪 Use this module to explore how different band gap materials impact solar cell efficiency based on solar spectrum overlap.")
