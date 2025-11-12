# modules/gear_tooth_visualizer.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def generate_gear_outline(teeth, pitch_dia, pressure_angle_deg):
    angle = np.linspace(0, 2 * np.pi, 1000)
    radius = pitch_dia / 2
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)

    # Gear teeth positions
    tooth_angles = np.linspace(0, 2 * np.pi, teeth, endpoint=False)
    tooth_x = radius * np.cos(tooth_angles)
    tooth_y = radius * np.sin(tooth_angles)

    return x, y, tooth_x, tooth_y


def run():
    st.title("⚙️ Gear Tooth Visualizer")
    st.markdown("""
    Visualize a **spur gear profile** by adjusting number of teeth, pitch diameter, and pressure angle.

    Useful for sketching gears in engineering graphics and understanding tooth spacing.
    """)

    with st.sidebar:
        st.subheader("⚙️ Gear Parameters")
        teeth = st.slider("Number of Teeth", 6, 100, 24)
        pitch_dia = st.slider("Pitch Circle Diameter (mm)", 20, 200, 100)
        pressure_angle = st.slider("Pressure Angle (°)", 14, 25, 20)

    x, y, tooth_x, tooth_y = generate_gear_outline(teeth, pitch_dia, pressure_angle)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(x, y, label="Pitch Circle", color="black")
    ax.scatter(tooth_x, tooth_y, color="red", label="Teeth Centers")
    ax.set_title(f"Spur Gear: {teeth} Teeth, Pitch Ø = {pitch_dia} mm")
    ax.set_aspect("equal")
    ax.legend()
    ax.axis("off")
    st.pyplot(fig)

    st.info("📐 This tool helps visualize **gear design geometry** for hand sketching or CAD modeling.")
