import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def draw_isometric_block(block_type):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    ax.axis('off')

    # Axonometric basis vectors
    i = np.array([1, 0])
    j = np.array([np.cos(np.radians(120)), np.sin(np.radians(120))])
    k = np.array([np.cos(np.radians(240)), np.sin(np.radians(240))])

    def iso_point(x, y, z):
        return x * i + y * j + z * k

    def draw_box(origin, size=(1, 1, 1), color='skyblue'):
        ox, oy, oz = origin
        dx, dy, dz = size

        # Bottom corners
        A = iso_point(ox, oy, oz)
        B = iso_point(ox + dx, oy, oz)
        C = iso_point(ox + dx, oy + dy, oz)
        D = iso_point(ox, oy + dy, oz)

        # Top corners
        E = iso_point(ox, oy, oz + dz)
        F = iso_point(ox + dx, oy, oz + dz)
        G = iso_point(ox + dx, oy + dy, oz + dz)
        H = iso_point(ox, oy + dy, oz + dz)

        # Draw edges
        edges = [(A, B), (B, C), (C, D), (D, A),
                 (E, F), (F, G), (G, H), (H, E),
                 (A, E), (B, F), (C, G), (D, H)]

        for edge in edges:
            x_vals = [edge[0][0], edge[1][0]]
            y_vals = [edge[0][1], edge[1][1]]
            ax.plot(x_vals, y_vals, color='black', linewidth=2)

        # Fill top face
        ax.fill([E[0], F[0], G[0], H[0]], [E[1], F[1], G[1], H[1]], color=color, alpha=0.5)

    # Choose which object to draw
    if block_type == "Cube":
        draw_box((0, 0, 0), size=(2, 2, 2))
    elif block_type == "L-Block":
        draw_box((0, 0, 0), size=(2, 1, 1))
        draw_box((0, 1, 0), size=(1, 1, 1))
    elif block_type == "Step Block":
        draw_box((0, 0, 0), size=(2, 2, 1))
        draw_box((0, 0, 1), size=(1, 2, 1))

    st.pyplot(fig)

def run():
    st.title("📐 Module 3: Isometric Drawing Generator")
    st.markdown("Visualize **3D isometric views** of basic blocks using simulated 30° axonometric projection.")

    block_type = st.selectbox("📦 Choose Block Type", ["Cube", "L-Block", "Step Block"])

    if st.button("📊 Generate Isometric View"):
        draw_isometric_block(block_type)
