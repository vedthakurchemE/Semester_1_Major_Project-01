import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def involute_curve(base_radius, theta_max=np.pi/2, num_points=100):
    theta = np.linspace(0, theta_max, num_points)
    x = base_radius * (np.cos(theta) + theta * np.sin(theta))
    y = base_radius * (np.sin(theta) - theta * np.cos(theta))
    return x, y

def cycloidal_tooth_profile(rack_height, pitch, points=100):
    t = np.linspace(0, 2*np.pi, points)
    x = pitch * (t - np.sin(t)) / (2 * np.pi)
    y = rack_height * (1 - np.cos(t)) / 2
    return x, y

def draw_gear_teeth(profile, num_teeth, module, pressure_angle_deg):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    ax.axis('off')

    pitch_dia = num_teeth * module
    base_radius = pitch_dia / 2 * np.cos(np.radians(pressure_angle_deg))
    pitch_radius = pitch_dia / 2
    addendum = module
    dedendum = 1.25 * module

    if profile == "Involute":
        for i in range(num_teeth):
            angle = 2 * np.pi * i / num_teeth
            x_invo, y_invo = involute_curve(base_radius)
            x_tooth = x_invo + pitch_radius
            y_tooth = y_invo
            # Rotate tooth
            x_rot = x_tooth * np.cos(angle) - y_tooth * np.sin(angle)
            y_rot = x_tooth * np.sin(angle) + y_tooth * np.cos(angle)
            ax.plot(x_rot, y_rot, color='darkblue')

        # Draw pitch circle
        circle = plt.Circle((0, 0), pitch_radius, color='gray', linestyle='--', fill=False)
        ax.add_patch(circle)

    elif profile == "Cycloidal":
        x, y = cycloidal_tooth_profile(module * 2, module * np.pi)
        for i in range(num_teeth):
            angle = 2 * np.pi * i / num_teeth
            x_rot = x * np.cos(angle) - y * np.sin(angle)
            y_rot = x * np.sin(angle) + y * np.cos(angle)
            ax.plot(x_rot, y_rot, color='darkgreen')

    elif profile == "Rack & Pinion":
        ax.plot([0, module * num_teeth], [0, 0], 'black', linewidth=2)
        for i in range(num_teeth):
            ax.add_patch(plt.Rectangle((i * module, 0), module / 2, module, edgecolor='black', facecolor='lightgray'))

    st.pyplot(fig)

def run():
    st.title("⚙️ Module 8: Gear Tooth Profile Visualizer")
    st.markdown("Visualize different **gear tooth shapes** used in mechanical engineering.")

    profile = st.selectbox("🧩 Select Tooth Profile", ["Involute", "Cycloidal", "Rack & Pinion"])
    num_teeth = st.slider("🦷 Number of Teeth", 6, 40, 12)
    module = st.slider("📐 Module (mm)", 1, 5, 2)
    pressure_angle = st.slider("📏 Pressure Angle (°)", 14, 25, 20)

    if st.button("🔍 Generate Gear Profile"):
        draw_gear_teeth(profile, num_teeth, module, pressure_angle)
