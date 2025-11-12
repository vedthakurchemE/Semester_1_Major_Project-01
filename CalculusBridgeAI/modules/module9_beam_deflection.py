import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def run():
    st.header("📐 Module 9: Beam Deflection Visualizer")

    st.markdown(r"""
    This module simulates **vertical deflection of a simply supported beam** using:

    \[
    EI \frac{d^2y}{dx^2} = M(x)
    \]

    Using **double integration** of the bending moment equation:

    \[
    y(x) = \frac{1}{EI} \int \int M(x) \, dx^2
    \]

    You can simulate:
    - Point Load at center
    - Uniformly Distributed Load (UDL)
    """)

    # Input Parameters
    L = st.slider("Beam Length L (m)", 1, 20, 10)
    E = st.slider("Modulus of Elasticity E (GPa)", 1, 300, 200) * 1e9  # Convert to Pascals
    I = st.slider("Moment of Inertia I (cm⁴)", 100, 50000, 5000) * 1e-8  # Convert to m⁴

    load_type = st.selectbox("Loading Type", ["Point Load at Center", "Uniformly Distributed Load"])

    x = np.linspace(0, L, 1000)

    if load_type == "Point Load at Center":
        P = st.slider("Point Load P (kN)", 1, 100, 10) * 1e3  # Convert to N

        # Deflection formula for simply supported beam with center load
        y = (P * x * (L ** 3 - 2 * L * x ** 2 + x ** 3)) / (48 * E * I)
        y = np.where(x <= L / 2, y, (P * (L - x) * (L ** 3 - 2 * L * (L - x) ** 2 + (L - x) ** 3)) / (48 * E * I))

    else:
        w = st.slider("Uniform Load w (kN/m)", 1, 100, 10) * 1e3  # Convert to N/m

        # Deflection formula for UDL: y(x) = (w x (L^3 - 2Lx^2 + x^3)) / (24EI)
        y = (w * x * (L ** 3 - 2 * L * x ** 2 + x ** 3)) / (24 * E * I)

    max_deflection = np.min(y)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(x, -y * 1000, label="Deflection (mm)", color="blue")  # Convert to mm
    ax.axhline(0, color="gray", linestyle="--")
    ax.set_xlabel("Length along Beam (m)")
    ax.set_ylabel("Deflection (mm)")
    ax.set_title(f"Beam Deflection Curve ({load_type})")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    st.success(f"📉 Maximum Deflection: {-max_deflection * 1000:.2f} mm")

    st.markdown("""
    **Notes**:
    - Assumes linear elastic behavior (Euler–Bernoulli theory).
    - Results valid for small deflections.
    - Useful in structural design & serviceability checks.
    """)
