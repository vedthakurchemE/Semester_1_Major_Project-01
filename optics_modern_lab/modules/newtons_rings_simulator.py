# modules/newtons_rings_simulator.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calculate_ring_radii(n, wavelength, R):
    # Returns list of radii (in mm) for n fringes
    m = np.arange(1, n + 1)
    radii = np.sqrt(m * wavelength * R) * 1000  # Convert to mm
    return m, radii

def run():
    st.title("🎯 Newton's Rings Simulator")
    st.markdown("""
    Simulate the **interference pattern of Newton’s Rings** for a plano-convex lens on a glass plate.

    **Fringe Radius Formula:**  
    `r_m = sqrt(m * λ * R)`  
    - *m*: Fringe number  
    - *λ*: Wavelength (in meters)  
    - *R*: Radius of curvature of the lens (in meters)
    """)

    st.subheader("⚙️ Experiment Settings")

    col1, col2, col3 = st.columns(3)
    with col1:
        wavelength_nm = st.number_input("Wavelength (nm)", min_value=300, max_value=800, value=600)
    with col2:
        radius_curvature_mm = st.number_input("Radius of Curvature (mm)", min_value=10.0, value=200.0)
    with col3:
        num_rings = st.slider("Number of Rings (m)", 1, 30, 10)

    wavelength = wavelength_nm * 1e-9      # convert nm to m
    R = radius_curvature_mm / 1000         # convert mm to m

    m, radii = calculate_ring_radii(num_rings, wavelength, R)

    st.subheader("📊 Fringe Radii Plot")
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(m, radii, 'bo-', label="Ring Radius")
    ax.set_xlabel("Fringe Order (m)")
    ax.set_ylabel("Radius (mm)")
    ax.set_title("Radius of Newton’s Rings vs Order")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
    st.video('https://www.youtube.com/watch?v=zAHiqx5mnnw')
    st.success(f"✅ Radius of {num_rings}th Ring: {radii[-1]:.2f} mm")
    st.caption("💡 Use different wavelengths to simulate colored light (e.g., red = 650 nm, green = 532 nm, blue = 450 nm).")
