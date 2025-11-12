# modules/isometric_drawing_tool.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def draw_isometric(ax, L, B, H):
    # Isometric angles
    angle_x = np.radians(30)
    angle_y = np.radians(150)

    # Base vectors
    x_axis = np.array([np.cos(angle_x), np.sin(angle_x)])
    y_axis = np.array([np.cos(angle_y), np.sin(angle_y)])
    z_axis = np.array([0, 1])

    # Corner points
    origin = np.array([0, 0])
    A = origin
    B_ = A + L * x_axis
    C = B_ + B * y_axis
    D = A + B * y_axis

    A_top = A + H * z_axis
    B_top = B_ + H * z_axis
    C_top = C + H * z_axis
    D_top = D + H * z_axis

    # Draw base
    ax.plot(*zip(A, B_, C, D, A), color='black')
    # Draw verticals
    ax.plot(*zip(A, A_top), color='gray')
    ax.plot(*zip(B_, B_top), color='gray')
    ax.plot(*zip(C, C_top), color='gray')
    ax.plot(*zip(D, D_top), color='gray')
    # Draw top
    ax.plot(*zip(A_top, B_top, C_top, D_top, A_top), color='blue')

    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Isometric View")

def run():
    st.title("📐 Isometric Drawing Tool")
    st.markdown("""
    Visualize the **isometric view** of a 3D block using standard 30° projection.

    Adjust the block’s dimensions using the sidebar.
    """)

    with st.sidebar:
        st.subheader("📏 Block Dimensions (mm)")
        L = st.slider("Length (L)", 50, 300, 150)
        B = st.slider("Breadth (B)", 50, 300, 100)
        H = st.slider("Height (H)", 50, 300, 75)

    fig, ax = plt.subplots(figsize=(6, 6))
    draw_isometric(ax, L, B, H)
    st.pyplot(fig)

    st.info("📘 Use this tool to understand how 3D objects are converted to 2D isometric views.")
