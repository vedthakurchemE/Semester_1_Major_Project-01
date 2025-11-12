# modules/basic_civil/road_gradient_calculator.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def run():
    st.title("🛣️ Road Gradient Calculator")
    st.markdown("""
    This tool calculates the **road gradient** based on elevation rise and horizontal distance.

    ### 📘 Definitions:
    - **Gradient (%)** = (Rise / Run) × 100
    - **Gradient (Degrees)** = arctan(Rise / Run)

    📌 Used in:
    - Hill road design  
    - Ramp & approach road analysis  
    - Drainage and slope safety
    """)

    st.divider()
    st.subheader("📏 Enter Slope Dimensions")

    col1, col2 = st.columns(2)
    with col1:
        rise = st.number_input("Elevation Rise (m)", min_value=0.1, step=0.1, value=2.0)
    with col2:
        run = st.number_input("Horizontal Run (m)", min_value=1.0, step=0.1, value=20.0)

    if run <= 0:
        st.error("Horizontal distance must be > 0")
        return

    # Calculations
    gradient_percent = (rise / run) * 100
    gradient_angle = np.degrees(np.arctan(rise / run))

    st.success(f"🧮 Gradient: **{gradient_percent:.2f}%** ({gradient_angle:.2f}°)")

    st.markdown("""
    - 🔺 **Gradient (%)** is used in road design.
    - 🔺 **Degrees** are used in plotting or angle-based specs.
    """)

    # Plot the slope triangle
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot([0, run], [0, 0], 'k-', lw=2)       # horizontal base
    ax.plot([0, 0], [0, rise], 'k--', lw=1)      # vertical rise
    ax.plot([0, run], [0, rise], 'r-', lw=3)     # hypotenuse (slope)

    ax.text(run/2, -0.5, f"Run = {run} m", ha='center')
    ax.text(-0.5, rise/2, f"Rise = {rise} m", va='center', rotation='vertical')
    ax.text(run/2, rise/2 + 0.5, f"Gradient = {gradient_percent:.2f}%", color='red', fontsize=12)

    ax.set_xlim(-2, run + 2)
    ax.set_ylim(-1, rise + 2)
    ax.set_aspect('equal')
    ax.axis('off')

    st.pyplot(fig)

    st.info("ℹ️ For highways, gradients are usually kept between **3% and 10%** depending on terrain.")
