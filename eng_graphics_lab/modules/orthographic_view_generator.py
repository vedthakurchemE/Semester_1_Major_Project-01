# modules/orthographic_view_generator.py

import streamlit as st
import matplotlib.pyplot as plt


def draw_view(ax, view, l, b, h):
    if view == "Front":
        ax.plot([0, l, l, 0, 0], [0, 0, h, h, 0], color="blue")
        ax.set_title("Front View")
        ax.set_xlabel("Length")
        ax.set_ylabel("Height")
    elif view == "Top":
        ax.plot([0, l, l, 0, 0], [0, 0, b, b, 0], color="green")
        ax.set_title("Top View")
        ax.set_xlabel("Length")
        ax.set_ylabel("Breadth")
    elif view == "Side":
        ax.plot([0, b, b, 0, 0], [0, 0, h, h, 0], color="red")
        ax.set_title("Side View")
        ax.set_xlabel("Breadth")
        ax.set_ylabel("Height")

    ax.set_aspect('equal')
    ax.grid(True)


def run():
    st.title("📐 Orthographic View Generator")
    st.markdown("""
    Generate **2D Orthographic Projections** (Front, Top, Side) of a 3D rectangular object.

    Adjust the block dimensions and view type below.
    """)

    with st.sidebar:
        st.subheader("📏 Dimensions (in mm)")
        l = st.slider("Length (L)", 50, 300, 150)
        b = st.slider("Breadth (B)", 30, 200, 100)
        h = st.slider("Height (H)", 30, 200, 75)
        view = st.radio("📸 Select View", ["Front", "Top", "Side"])

    fig, ax = plt.subplots(figsize=(5, 5))
    draw_view(ax, view, l, b, h)
    st.pyplot(fig)

    st.info("✅ Use this tool to practice visualizing 2D views from 3D objects — essential for technical drawing.")
