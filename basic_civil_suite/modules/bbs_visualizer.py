# modules/basic_civil/bbs_visualizer.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def calculate_bar_weight(length_m, diameter_mm):
    """Calculates steel bar weight using formula: (d² / 162) × L"""
    return (diameter_mm ** 2 / 162) * length_m

def run():
    st.title("🧮 Bar Bending Schedule (BBS) Visualizer")
    st.markdown("""
    Calculate and visualize **bar bending shapes, lengths, and total steel weight**.

    ### 📘 Used For:
    - RCC column, beam, and slab detailing
    - Cost estimation of steel reinforcement
    - Practical site-level documentation

    Formula:  
    > **Weight (kg)** = (d² / 162) × L  
    > Where `d = diameter (mm)`, `L = length (m)`
    """)

    st.subheader("📥 Bar Details Input")

    shape = st.selectbox("🔺 Bar Shape", ["Straight", "Cranked", "U-Shaped"])
    diameter = st.number_input("Bar Diameter (mm)", min_value=6, max_value=32, value=12)
    num_bars = st.number_input("Number of Bars", min_value=1, step=1, value=10)

    if shape == "Straight":
        length = st.number_input("Length (m)", min_value=0.1, value=6.0)
        total_length = length * num_bars

    elif shape == "Cranked":
        main_length = st.number_input("Main Bar Length (m)", min_value=0.1, value=4.5)
        crank_length = st.number_input("Crank Length (m)", min_value=0.1, value=0.6)
        crank_angle = st.slider("Crank Angle (°)", 30, 60, value=45)
        # Total crank offset = 2 * crank_length * cos(angle)
        crank_effective = 2 * crank_length * np.cos(np.radians(crank_angle))
        length = main_length + crank_effective
        total_length = length * num_bars

    elif shape == "U-Shaped":
        base = st.number_input("Base Length (m)", min_value=0.1, value=1.0)
        height = st.number_input("Vertical Height (m)", min_value=0.1, value=0.5)
        bend_radius = st.number_input("Bend Allowance (m)", min_value=0.01, value=0.05)
        length = base + 2 * height + 2 * bend_radius
        total_length = length * num_bars

    total_weight = calculate_bar_weight(total_length, diameter)

    st.success(f"📏 Total Bar Length: **{total_length:.2f} m**")
    st.info(f"⚖️ Estimated Total Weight: **{total_weight:.2f} kg**")

    # Visualization
    st.subheader("📊 Shape Visualization")
    fig, ax = plt.subplots(figsize=(6, 2))
    if shape == "Straight":
        ax.plot([0, length], [0, 0], 'b-', lw=4)
        ax.text(length/2, 0.1, f"{length:.2f} m", ha='center')
    elif shape == "Cranked":
        x = [0, main_length / 2, main_length / 2 + crank_length * np.cos(np.radians(crank_angle)), main_length]
        y = [0, 0, crank_length * np.sin(np.radians(crank_angle)), 0]
        ax.plot(x, y, 'orange', lw=4)
    elif shape == "U-Shaped":
        ax.plot([0, base, base, 0, 0], [0, 0, height, height, 0], 'green', lw=4)
        ax.text(base / 2, -0.1, f"{base:.2f} m", ha='center')
        ax.text(-0.1, height / 2, f"{height:.2f} m", va='center', rotation='vertical')

    ax.set_aspect('equal')
    ax.axis('off')
    st.pyplot(fig)

    st.caption("ℹ️ Always consider extra bar length for bends, hooks, anchorage, and overlaps.")
