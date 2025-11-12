# modules/laser_wavelength_measure.py

import streamlit as st
import numpy as np

def calculate_wavelength(d, D, x):
    # d = distance between slits (m)
    # D = distance from slits to screen (m)
    # x = fringe spacing (m)
    λ = (x * d) / D
    return λ * 1e9  # Convert to nm

def run():
    st.title("🔦 Laser Wavelength Estimator")
    st.markdown("""
    Estimate the **wavelength of a laser** using diffraction principles and experimental inputs.

    **Formula Used:**  
    `λ = (x × d) / D`  
    where:
    - `λ` = Wavelength (m)  
    - `x` = Fringe spacing (m)  
    - `d` = Slit separation (m)  
    - `D` = Distance to screen (m)
    """)

    st.subheader("📐 Input Experimental Parameters")
    col1, col2, col3 = st.columns(3)
    with col1:
        d_mm = st.number_input("Slit Separation (mm)", min_value=0.1, max_value=10.0, value=0.25)
    with col2:
        D_cm = st.number_input("Distance to Screen (cm)", min_value=10.0, max_value=200.0, value=100.0)
    with col3:
        x_mm = st.number_input("Fringe Spacing (mm)", min_value=0.01, max_value=10.0, value=1.2)

    d = d_mm / 1000      # mm → m
    D = D_cm / 100       # cm → m
    x = x_mm / 1000      # mm → m

    wavelength_nm = calculate_wavelength(d, D, x)

    st.success(f"📏 Estimated Laser Wavelength: **{wavelength_nm:.2f} nm**")
    st.info("🔍 Typical lasers range from 532 nm (green) to 650 nm (red).")
    st.caption("🎯 Adjust setup for accurate fringe measurement.")
