# modules/bohr_model_visualizer.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def energy_level(n):
    return -13.6 / n**2  # eV for hydrogen atom

def wavelength_from_levels(n1, n2):
    e1 = energy_level(n1)
    e2 = energy_level(n2)
    delta_E = abs(e2 - e1)  # eV
    h = 4.135667696e-15  # Planck's constant (eV·s)
    c = 3e8  # Speed of light (m/s)
    wavelength = (h * c) / (delta_E) * 1e9  # in nm
    return delta_E, wavelength

def run():
    st.title("🔭 Bohr Model Visualizer")
    st.markdown("""
    Visualize **energy level transitions** in the hydrogen atom using the **Bohr Model**.

    - Discrete energy states
    - Emission or absorption of photons
    - Estimate transition wavelength

    **Formula Used:**  
    `Eₙ = -13.6 / n² eV`
    """)

    col1, col2 = st.columns(2)
    with col1:
        n1 = st.selectbox("📥 Initial Orbit (n₁)", [1, 2, 3, 4, 5])
    with col2:
        n2 = st.selectbox("📤 Final Orbit (n₂)", [1, 2, 3, 4, 5], index=1)

    if n1 == n2:
        st.warning("⚠️ Initial and final orbit must be different.")
        return

    delta_E, λ_nm = wavelength_from_levels(n1, n2)

    st.success(f"🔺 Energy Difference: {delta_E:.2f} eV")
    st.success(f"📡 Emitted/Absorbed Wavelength: {λ_nm:.2f} nm")

    st.subheader("🔬 Energy Level Diagram")
    fig, ax = plt.subplots(figsize=(5, 6))

    levels = [energy_level(n) for n in range(1, 6)]
    for i, e in enumerate(levels, start=1):
        ax.hlines(e, 0, 1, label=f"n = {i}")
        ax.text(1.05, e, f"{e:.2f} eV", va='center')

    e1 = energy_level(n1)
    e2 = energy_level(n2)
    ax.annotate("", xy=(0.5, e2), xytext=(0.5, e1),
                arrowprops=dict(arrowstyle="<->", color='red', lw=2))
    ax.set_ylim(-14, 0)
    ax.axis("off")
    ax.legend()
    st.pyplot(fig)

    st.caption("📘 Based on Bohr’s postulates for the hydrogen atom.")
