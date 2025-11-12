# modules/photoelectric_effect_explorer.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def calculate_photoelectric_effect(frequency, intensity, threshold_freq):
    h = 6.626e-34  # Planck's constant (J·s)
    e = 1.602e-19  # Charge of electron (C)

    # Energy of photon = hf
    E = h * frequency

    # Work function = h * threshold frequency
    work_function = h * threshold_freq

    # Kinetic energy of emitted electron
    KE = max(E - work_function, 0)

    # Current proportional to intensity and KE > 0
    current = intensity if KE > 0 else 0

    return KE / e, current  # Return KE in eV, and current as relative value


def run():
    st.title("🧠 Photoelectric Effect Explorer")
    st.markdown("""
    Explore the **quantum nature of light** by simulating the **photoelectric effect**.

    **Einstein’s Equation:**  
    `E = hf = φ + KE`

    - `f` = frequency of incident light  
    - `φ = h*f₀` = work function (threshold energy)  
    - `KE` = kinetic energy of emitted electron
    """)

    st.subheader("📐 Input Parameters")
    col1, col2, col3 = st.columns(3)
    with col1:
        frequency = st.slider("🌈 Light Frequency (THz)", 300, 1200, 600)
    with col2:
        intensity = st.slider("💡 Light Intensity (arb. units)", 0, 100, 50)
    with col3:
        threshold_freq = st.slider("⚠️ Threshold Frequency (THz)", 200, 800, 500)

    f = frequency * 1e12  # Convert THz to Hz
    f0 = threshold_freq * 1e12  # Convert THz to Hz

    ke_eV, current = calculate_photoelectric_effect(f, intensity, f0)

    st.success(f"🔋 Electron Kinetic Energy: **{ke_eV:.3f} eV**")
    st.success(f"🔌 Photoelectric Current (relative): **{current:.1f} units**")

    st.subheader("📈 Emission Condition Visualization")
    fig, ax = plt.subplots()
    bar_colors = ["green" if ke_eV > 0 else "gray"]
    ax.bar(["Kinetic Energy"], [ke_eV], color=bar_colors)
    ax.set_ylabel("Energy (eV)")
    ax.set_title("Electron Emission Indicator")
    st.pyplot(fig)

    if ke_eV > 0:
        st.info("✅ Electron emission occurs. Photon energy exceeds work function.")
    else:
        st.warning("❌ No emission. Photon energy is below work function.")

    st.caption("🧪 This experiment verified quantum theory and led to Einstein’s Nobel Prize.")
