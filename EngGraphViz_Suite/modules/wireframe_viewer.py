import streamlit as st
import numpy as np
import plotly.graph_objects as go

def draw_cube():
    x = [0, 1, 1, 0, 0, 0, 1, 1, 0]
    y = [0, 0, 1, 1, 0, 0, 0, 1, 1]
    z = [0, 0, 0, 0, 0, 1, 1, 1, 1]
    lines = [
        [0, 1], [1, 2], [2, 3], [3, 0],  # bottom face
        [4, 5], [5, 6], [6, 7], [7, 4],  # top face
        [0, 4], [1, 5], [2, 6], [3, 7]   # vertical edges
    ]
    return x, y, z, lines

def draw_cylinder(resolution=30):
    h = 1
    r = 0.5
    theta = np.linspace(0, 2 * np.pi, resolution)
    x_bottom = r * np.cos(theta)
    y_bottom = r * np.sin(theta)
    z_bottom = np.zeros_like(theta)
    z_top = np.ones_like(theta)

    lines = []
    for i in range(len(theta)):
        lines.append([i, i + len(theta)])  # vertical lines

    return list(x_bottom) + list(x_bottom), list(y_bottom) + list(y_bottom), list(z_bottom) + list(z_top), lines

def draw_cone(resolution=30):
    h = 1
    r = 0.5
    theta = np.linspace(0, 2 * np.pi, resolution)
    x_base = r * np.cos(theta)
    y_base = r * np.sin(theta)
    z_base = np.zeros_like(theta)

    x = list(x_base) + [0]
    y = list(y_base) + [0]
    z = list(z_base) + [1]

    lines = []
    for i in range(resolution):
        lines.append([i, resolution])  # lines from base to apex

    return x, y, z, lines

def plot_wireframe(x, y, z, lines, title):
    fig = go.Figure()
    for line in lines:
        fig.add_trace(go.Scatter3d(
            x=[x[line[0]], x[line[1]]],
            y=[y[line[0]], y[line[1]]],
            z=[z[line[0]], z[line[1]]],
            mode='lines',
            line=dict(color='blue', width=4)
        ))
    fig.update_layout(
        scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
        title=title,
        width=700,
        height=500,
        margin=dict(r=10, l=10, b=10, t=40)
    )
    st.plotly_chart(fig)

def run():
    st.title("📐 Module 9: 3D Wireframe Viewer")
    st.markdown("Interactively explore **3D wireframe models** of basic engineering solids.")

    shape = st.selectbox("🧱 Choose 3D Solid", ["Cube", "Cylinder", "Cone"])

    if st.button("🎲 Generate Wireframe"):
        if shape == "Cube":
            x, y, z, lines = draw_cube()
        elif shape == "Cylinder":
            x, y, z, lines = draw_cylinder()
        elif shape == "Cone":
            x, y, z, lines = draw_cone()
        plot_wireframe(x, y, z, lines, title=f"3D Wireframe of {shape}")
