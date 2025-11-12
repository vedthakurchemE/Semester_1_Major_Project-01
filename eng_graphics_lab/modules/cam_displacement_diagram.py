# modules/cam_displacement_diagram.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def uniform_motion(theta, h):
    return h * theta / np.max(theta)


def shm_motion(theta, h):
    return h * (1 - np.cos(np.pi * theta / np.max(theta))) / 2


def cycloidal_motion(theta, h):
    return h * (theta / np.max(theta) - (1 / (2 * np.pi)) * np.sin(2 * np.pi * theta / np.max(theta)))


def run():
    st.title("📊 Cam Displacement Diagram Generator")
    st.markdown("""
    Simulate follower **displacement curves** for different cam motions:

    - 📈 Uniform Motion  
    - 🌊 Simple Harmonic Motion (SHM)  
    - 🔁 Cycloidal Motion

    Helps visualize how follower motion varies with cam rotation.
    """)

    motion_type = st.selectbox("🎯 Select Motion Type", ["Uniform", "SHM", "Cycloidal"])
    total_angle = st.slider("🔁 Cam Rotation Angle (°)", 90, 360, 180)
    h = st.slider("📏 Total Lift (mm)", 10, 100, 50)

    theta = np.linspace(0, total_angle, 500)

    if motion_type == "Uniform":
        y = uniform_motion(theta, h)
    elif motion_type == "SHM":
        y = shm_motion(theta, h)
    else:
        y = cycloidal_motion(theta, h)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(theta, y, color='darkblue', linewidth=2)
    ax.set_title(f"{motion_type} Displacement Diagram")
    ax.set_xlabel("Cam Angle (°)")
    ax.set_ylabel("Follower Displacement (mm)")
    ax.grid(True)

    st.pyplot(fig)
    st.success("✅ Diagram plotted successfully!")
    st.info("ℹ️ These curves are used to generate cam profiles in mechanical systems.")
