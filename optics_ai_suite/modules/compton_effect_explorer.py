# compton_effect_explorer.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.markdown("<h1 style='text-align: center;'>🌀 Compton Effect Explorer</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>📡 Photon-Electron Scattering & Wavelength Shift</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # Constants
    h = 6.626e-34  # J·s
    c = 3e8        # m/s
    e = 1.602e-19  # C
    me = 9.11e-31  # kg
    λ_c = h / (me * c)  # Compton wavelength ≈ 2.426 x 10^-12 m

    # Sidebar inputs
    st.sidebar.header("⚙️ Input Parameters")
    λ0 = st.sidebar.slider("Initial Wavelength λ₀ (pm)", 1.0, 500.0, 70.0, step=1.0) * 1e-12  # Convert pm to meters
    angle_deg = st.sidebar.slider("Scattering Angle θ (°)", 0.0, 180.0, 60.0)

    # Computations
    theta_rad = np.radians(angle_deg)
    Δλ = λ_c * (1 - np.cos(theta_rad))  # Wavelength shift
    λ_prime = λ0 + Δλ  # Final wavelength
    E0 = h * c / λ0 / e  # Initial photon energy (in eV)
    E1 = h * c / λ_prime / e  # Final photon energy
    KE_electron = E0 - E1  # Recoil electron energy

    # Output
    st.subheader("📊 Results")
    st.markdown(f"- **Initial Wavelength λ₀:** {λ0*1e12:.2f} pm")
    st.markdown(f"- **Scattering Angle θ:** {angle_deg:.1f}°")
    st.markdown(f"- **Compton Shift Δλ:** {Δλ*1e12:.4f} pm")
    st.markdown(f"- **Scattered Wavelength λ′:** {λ_prime*1e12:.2f} pm")
    st.markdown(f"- **Scattered Photon Energy (E′):** {E1:.2f} eV")
    st.markdown(f"- **Recoil Electron Energy (KE):** {KE_electron:.2f} eV")

    st.info("🧬 Wavelength increases after scattering, and energy is transferred to the electron.")

    # Graph: Δλ vs θ
    st.subheader("📈 Compton Shift vs Angle")
    angles = np.linspace(0, 180, 500)
    delta_lambdas = λ_c * (1 - np.cos(np.radians(angles)))

    fig1, ax1 = plt.subplots()
    ax1.plot(angles, delta_lambdas * 1e12, color='purple')
    ax1.set_xlabel("Scattering Angle θ (degrees)")
    ax1.set_ylabel("Δλ (pm)")
    ax1.set_title("Wavelength Shift vs Angle")
    st.pyplot(fig1)

    # Graph: Energies vs θ
    st.subheader("⚡ Energies vs Angle")
    theta_vals = np.radians(np.linspace(0, 180, 500))
    delta_lambda_vals = λ_c * (1 - np.cos(theta_vals))
    lambda_primes = λ0 + delta_lambda_vals
    photon_energies = h * c / lambda_primes / e
    electron_energies = E0 - photon_energies

    fig2, ax2 = plt.subplots()
    ax2.plot(np.degrees(theta_vals), photon_energies, label="Scattered Photon Energy", color='blue')
    ax2.plot(np.degrees(theta_vals), electron_energies, label="Recoil Electron KE", color='green')
    ax2.set_xlabel("Scattering Angle θ (degrees)")
    ax2.set_ylabel("Energy (eV)")
    ax2.set_title("Photon & Electron Energy vs Scattering Angle")
    ax2.legend()
    st.pyplot(fig2)
