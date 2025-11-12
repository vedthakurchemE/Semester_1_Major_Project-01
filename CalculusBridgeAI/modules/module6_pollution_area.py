import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from numpy import trapz  # ✅ Replaced scipy.simps with numpy.trapz

def run():
    st.header("🌫 Module 6: Pollution Exposure Area Under Curve")

    st.markdown(r"""
    We calculate the **total exposure** to air pollution over time by integrating the pollution concentration curve.

    ### Mathematical Model:
    \[
    \text{Total Exposure} = \int_0^T C(t) \, dt
    \]
    Where:
    - \( C(t) \): Concentration of pollutant at time \( t \)
    - \( T \): Total time (in hours or days)

    This is used by environmental agencies to estimate the **cumulative harmful exposure** to pollutants like NO₂ or PM2.5.
    """)

    st.subheader("Pollution Scenario Selection")
    scenario = st.selectbox("Select Pollution Scenario", [
        "Urban Peak Hours",
        "Industrial Area Daytime",
        "Rural Clean Air",
        "Custom Sinusoidal"
    ])

    T = st.slider("Total Time Period (hours)", 1, 72, 24)
    time = np.linspace(0, T, 1000)

    if scenario == "Urban Peak Hours":
        C = 80 + 40 * np.sin(2 * np.pi * time / 24)
    elif scenario == "Industrial Area Daytime":
        C = 120 + 30 * np.sin(np.pi * time / 12)
    elif scenario == "Rural Clean Air":
        C = 20 + 5 * np.sin(2 * np.pi * time / 24)
    elif scenario == "Custom Sinusoidal":
        A = st.slider("Amplitude (A)", 0, 100, 40)
        base = st.slider("Base Pollution Level", 0, 200, 60)
        freq = st.slider("Frequency (per 24h)", 1, 10, 1)
        C = base + A * np.sin(2 * np.pi * freq * time / 24)

    # ✅ Numerical integration using trapz (stable)
    total_exposure = trapz(C, time)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(time, C, label="Pollution Concentration C(t)", color='darkorange')
    ax.fill_between(time, C, alpha=0.3, color='orange')
    ax.set_xlabel("Time (hours)")
    ax.set_ylabel("Concentration (µg/m³)")
    ax.set_title("Pollution Concentration Over Time")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    st.success(f"☣️ Total Pollution Exposure over {T} hours: {total_exposure:.2f} µg·hr/m³")

    st.markdown("""
    **Interpretation**:
    - This value helps determine health risk due to long-term exposure.
    - Integrating C(t) gives cumulative pollutant dose over time.
    - Try simulating multiple environments to compare.
    """)
