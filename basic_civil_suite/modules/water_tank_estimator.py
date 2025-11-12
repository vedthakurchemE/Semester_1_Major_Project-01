# modules/basic_civil/water_tank_estimator.py

import streamlit as st
import numpy as np

def run():
    st.title("🚰 Water Tank Volume Estimator")
    st.markdown("""
    Estimate the **capacity of water tanks** based on shape and size.

    ### 🔷 Applications:
    - Domestic and industrial water tank sizing
    - RCC/Plastic tank design validation
    - Estimating water storage for apartments, hostels, factories

    🔢 Outputs in Litres and Cubic Meters.
    """)

    st.divider()
    tank_type = st.selectbox("Select Tank Shape", ["Rectangular", "Cylindrical (Vertical)", "Cylindrical (Horizontal)", "Spherical"])

    st.subheader("📐 Enter Tank Dimensions")
    if tank_type == "Rectangular":
        l = st.number_input("Length (m)", min_value=0.1, value=2.0)
        b = st.number_input("Breadth (m)", min_value=0.1, value=1.5)
        h = st.number_input("Height (m)", min_value=0.1, value=1.0)
        volume_m3 = l * b * h

    elif tank_type == "Cylindrical (Vertical)" or tank_type == "Cylindrical (Horizontal)":
        d = st.number_input("Diameter (m)", min_value=0.1, value=1.2)
        h = st.number_input("Height/Length (m)", min_value=0.1, value=2.0)
        radius = d / 2
        volume_m3 = np.pi * radius ** 2 * h

    elif tank_type == "Spherical":
        d = st.number_input("Diameter (m)", min_value=0.1, value=1.0)
        radius = d / 2
        volume_m3 = (4/3) * np.pi * radius ** 3

    volume_litres = volume_m3 * 1000

    st.divider()
    st.success(f"🧮 Estimated Capacity: **{volume_m3:.2f} m³**  or  **{volume_litres:.0f} litres**")

    st.markdown(f"""
    ### ℹ️ Tank Type: {tank_type}
    - For RCC tanks: Add 10% extra volume for freeboard
    - For domestic usage: 135–150 litres/person/day
    """)
