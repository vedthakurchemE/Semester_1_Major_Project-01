import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header("🌡️ Module 8: Heat Transfer in Concrete (Newton's Law of Cooling)")

    st.markdown(r"""
    This module models how **concrete cools** after exothermic hydration using:

    \[
    T(t) = T_{\text{env}} + (T_0 - T_{\text{env}}) \cdot e^{-kt}
    \]

    Where:
    - \( T(t) \): temperature of concrete at time \( t \)
    - \( T_0 \): initial temperature (e.g., after curing, ~70–80°C)
    - \( T_{\text{env}} \): ambient temperature
    - \( k \): cooling constant (depends on concrete mass, insulation, etc.)

    Used in Civil Engineering for:
    - Curing simulation
    - Avoiding thermal cracks
    - Monitoring large pours (e.g. dams, bridges)
    """)

    # Inputs
    T0 = st.slider("Initial Concrete Temperature (°C)", 40, 100, 70)
    T_env = st.slider("Ambient Temperature (°C)", 10, 50, 30)
    k = st.slider("Cooling Constant k (1/hr)", 0.01, 1.0, 0.1, step=0.01)
    t_hours = st.slider("Total Time (hours)", 1, 72, 24)

    t = np.linspace(0, t_hours, 500)
    T = T_env + (T0 - T_env) * np.exp(-k * t)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(t, T, color='brown', label="Concrete Temp T(t)")
    ax.axhline(T_env, linestyle='--', color='gray', label="Ambient Temp")
    ax.set_xlabel("Time (hours)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Concrete Cooling Curve")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    st.success(f"📉 Final Temperature after {t_hours} hrs: {T[-1]:.2f} °C")

    st.markdown("""
    **Interpretation**:
    - Monitor early-age concrete temperature to prevent cracking.
    - Adjust insulation or mix design to control peak temperatures.
    - Helps in mass concrete thermal design (IS 10262, ACI 207).
    """)
