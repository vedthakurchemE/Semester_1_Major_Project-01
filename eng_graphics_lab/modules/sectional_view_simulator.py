# modules/sectional_view_simulator.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def draw_section(ax, length, breadth, height, section_type, section_depth):
    ax.set_aspect("equal")
    ax.set_title(f"{section_type} Section View")
    ax.set_xlabel("Width (mm)")
    ax.set_ylabel("Height (mm)")
    ax.grid(True)

    if section_type == "Vertical":
        # Show vertical cut at section_depth from left face
        ax.plot([0, 0, height, height, 0], [0, breadth, breadth, 0, 0], color="blue", label="Cut Surface")
        ax.fill_between([0, height], 0, section_depth, color='lightblue', alpha=0.5)
    elif section_type == "Horizontal":
        # Show horizontal section at height section_depth
        ax.plot([0, 0, length, length, 0], [0, height, height, 0, 0], color="red", label="Cut Surface")
        ax.fill_between([0, length], 0, section_depth, color='salmon', alpha=0.5)

def run():
    st.title("🧱 Sectional View Simulator")
    st.markdown("""
    Simulate how **vertical or horizontal sectioning** of a 3D block looks like in 2D.

    Useful for understanding internal component exposure in drawings.
    """)

    with st.sidebar:
        st.subheader("📏 Block Dimensions")
        length = st.slider("Length (L)", 50, 300, 150)
        breadth = st.slider("Breadth (B)", 50, 300, 100)
        height = st.slider("Height (H)", 50, 300, 80)

        st.subheader("✂️ Section Settings")
        section_type = st.radio("Section Type", ["Vertical", "Horizontal"])
        section_depth = st.slider("Section Depth (mm)", 10, height if section_type == "Horizontal" else breadth, 30)

    fig, ax = plt.subplots(figsize=(6, 5))
    draw_section(ax, length, breadth, height, section_type, section_depth)
    st.pyplot(fig)

    st.info("🔍 This tool helps you **visualize cuts through a block** — a key concept in engineering drawing.")
