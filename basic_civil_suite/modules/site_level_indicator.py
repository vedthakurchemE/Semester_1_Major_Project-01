# modules/basic_civil/site_level_indicator.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def run():
    st.title("🧭 Site Level Indicator Tool")
    st.markdown("""
    Simulates **site level checking** like a spirit level to ensure horizontal or sloped surface accuracy.

    ### 📘 Used in:
    - Floor leveling  
    - Beam alignment  
    - Pavement slope checks  
    - Drainage slopes

    📏 Inputs can be:
    - Elevation difference (rise)
    - Surface length (run)
    """)

    st.subheader("📐 Enter Site Data")
    col1, col2 = st.columns(2)
    with col1:
        rise = st.number_input("Elevation Difference (cm)", min_value=0.0, value=0.0, step=0.1)
    with col2:
        run = st.number_input("Horizontal Length (m)", min_value=0.1, value=2.0)

    rise_m = rise / 100  # convert to meters
    slope_percent = (rise_m / run) * 100
    slope_deg = np.degrees(np.arctan(rise_m / run))

    # Output
    st.success(f"🧮 Slope: **{slope_percent:.2f}%**  or  **{slope_deg:.2f}°**")

    if rise == 0:
        st.info("✅ Surface is perfectly level.")
    elif slope_percent < 2:
        st.warning("⚠️ Surface is slightly tilted.")
    else:
        st.error("❌ Surface is not level. Adjust required.")

    # Visual Simulation
    st.subheader("📊 Level Simulation")
    fig, ax = plt.subplots(figsize=(5, 2))
    x = [0, run]
    y = [0, rise_m]
    ax.plot(x, y, 'orange', lw=4, label="Surface")
    ax.plot(x, [0, 0], 'k--', lw=1, label="Level")
    ax.set_xlim(0, run)
    ax.set_ylim(-0.1, max(0.1, rise_m + 0.05))
    ax.set_title("Level Check View")
    ax.set_xlabel("Length (m)")
    ax.set_ylabel("Height (m)")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    st.caption("ℹ️ Used as digital alternative to spirit/bubble level tools.")
