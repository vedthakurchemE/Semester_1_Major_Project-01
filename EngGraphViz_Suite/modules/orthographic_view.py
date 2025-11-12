import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon


def draw_orthographic(shape):
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))

    titles = ["Front View", "Top View", "Side View"]
    for i, ax in enumerate(axs):
        ax.set_title(titles[i])
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.grid(False)

    if shape == "Step Block":
        # Front
        axs[0].add_patch(Rectangle((2, 2), 6, 2, facecolor='lightblue', edgecolor='blue', linewidth=2))
        axs[0].add_patch(Rectangle((2, 4), 4, 2, facecolor='lightblue', edgecolor='blue', linewidth=2))
        # Top
        axs[1].add_patch(Rectangle((2, 2), 6, 4, facecolor='lightgreen', edgecolor='green', linewidth=2))
        # Side
        axs[2].add_patch(Rectangle((2, 2), 6, 2, facecolor='lightcoral', edgecolor='red', linewidth=2))
        axs[2].add_patch(Rectangle((4, 4), 2, 2, facecolor='lightcoral', edgecolor='red', linewidth=2))

    elif shape == "Z Block":
        # Front
        axs[0].add_patch(Rectangle((2, 2), 4, 2, facecolor='lightblue', edgecolor='blue', linewidth=2))
        axs[0].add_patch(Rectangle((6, 4), 2, 2, facecolor='lightblue', edgecolor='blue', linewidth=2))
        # Top
        axs[1].add_patch(Rectangle((2, 2), 6, 2, facecolor='lightgreen', edgecolor='green', linewidth=2))
        axs[1].add_patch(Rectangle((6, 4), 2, 2, facecolor='lightgreen', edgecolor='green', linewidth=2))
        # Side
        axs[2].add_patch(Rectangle((2, 2), 2, 4, facecolor='lightcoral', edgecolor='red', linewidth=2))
        axs[2].add_patch(Rectangle((4, 4), 4, 2, facecolor='lightcoral', edgecolor='red', linewidth=2))

    elif shape == "U Block":
        # Front
        axs[0].add_patch(Rectangle((2, 2), 2, 6, facecolor='lightblue', edgecolor='blue', linewidth=2))
        axs[0].add_patch(Rectangle((4, 4), 2, 4, facecolor='white', edgecolor='white'))
        axs[0].add_patch(Rectangle((6, 2), 2, 6, facecolor='lightblue', edgecolor='blue', linewidth=2))
        # Top
        axs[1].add_patch(Rectangle((2, 2), 2, 6, facecolor='lightgreen', edgecolor='green', linewidth=2))
        axs[1].add_patch(Rectangle((6, 2), 2, 6, facecolor='lightgreen', edgecolor='green', linewidth=2))
        # Side
        axs[2].add_patch(Rectangle((2, 2), 6, 6, facecolor='lightcoral', edgecolor='red', linewidth=2))
        axs[2].add_patch(Rectangle((4, 4), 2, 4, facecolor='white', edgecolor='white'))

    st.pyplot(fig)


def run():
    st.title("📐 Module 2: Orthographic View Generator")
    st.markdown("Visualize **2D orthographic projections** from a 3D object block.")

    shape = st.selectbox("🔧 Select a 3D Object Shape", ["Step Block", "Z Block", "U Block"])

    if st.button("📊 Generate Views"):
        draw_orthographic(shape)
