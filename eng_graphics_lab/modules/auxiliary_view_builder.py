# modules/auxiliary_view_builder.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def rotate_points(x, y, angle_deg):
    angle_rad = np.radians(angle_deg)
    x_new = x * np.cos(angle_rad) - y * np.sin(angle_rad)
    y_new = x * np.sin(angle_rad) + y * np.cos(angle_rad)
    return x_new, y_new

def run():
    st.title("📐 Auxiliary View Builder")
    st.markdown("""
    Visualize how to generate an **auxiliary view** from an inclined surface in engineering drawing.

    Rotate an inclined edge to project its **true length and shape** — useful in creating precise part drawings.
    """)

    st.subheader("🔧 Input Triangle Dimensions")
    base = st.slider("Base Length (mm)", 50, 200, 100)
    height = st.slider("Height (mm)", 50, 200, 80)
    angle = st.slider("Inclination Angle (°)", 0, 90, 30)

    # Original triangle points (Right-angle triangle)
    x = np.array([0, base, 0])
    y = np.array([0, 0, height])

    # Rotate to auxiliary view
    x_rot, y_rot = rotate_points(x, y, angle)

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    # Front View
    axs[0].plot(x, y, 'o-', color='blue')
    axs[0].set_title("📄 Front View")
    axs[0].set_aspect('equal')
    axs[0].grid(True)
    axs[0].set_xlim(min(x)-20, max(x)+20)
    axs[0].set_ylim(min(y)-20, max(y)+20)

    # Auxiliary View
    axs[1].plot(x_rot, y_rot, 'o-', color='green')
    axs[1].set_title("📄 Auxiliary View")
    axs[1].set_aspect('equal')
    axs[1].grid(True)
    axs[1].set_xlim(min(x_rot)-20, max(x_rot)+20)
    axs[1].set_ylim(min(y_rot)-20, max(y_rot)+20)

    st.pyplot(fig)

    st.info("✅ This demonstrates how auxiliary views reveal true shape of inclined features.")
