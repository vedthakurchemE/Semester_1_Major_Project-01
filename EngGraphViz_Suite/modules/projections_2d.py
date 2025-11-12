import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_views(shape):
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))

    # FRONT VIEW
    axs[0].set_title("Front View")
    axs[0].set_xlim(0, 10)
    axs[0].set_ylim(0, 10)
    axs[0].set_aspect('equal')
    axs[0].grid(True)

    # TOP VIEW
    axs[1].set_title("Top View")
    axs[1].set_xlim(0, 10)
    axs[1].set_ylim(0, 10)
    axs[1].set_aspect('equal')
    axs[1].grid(True)

    # SIDE VIEW
    axs[2].set_title("Side View")
    axs[2].set_xlim(0, 10)
    axs[2].set_ylim(0, 10)
    axs[2].set_aspect('equal')
    axs[2].grid(True)

    if shape == "Cube":
        # Simple 10x10 block from all views
        for ax in axs:
            ax.add_patch(patches.Rectangle((2, 2), 6, 6, edgecolor='blue', facecolor='lightblue', linewidth=2))

    elif shape == "L-Shape":
        # FRONT
        axs[0].add_patch(patches.Rectangle((2, 2), 6, 4, edgecolor='blue', facecolor='lightblue', linewidth=2))
        axs[0].add_patch(patches.Rectangle((2, 6), 3, 2, edgecolor='blue', facecolor='lightblue', linewidth=2))

        # TOP
        axs[1].add_patch(patches.Rectangle((2, 2), 6, 4, edgecolor='blue', facecolor='lightblue', linewidth=2))
        axs[1].add_patch(patches.Rectangle((2, 6), 3, 2, edgecolor='blue', facecolor='lightblue', linewidth=2))

        # SIDE
        axs[2].add_patch(patches.Rectangle((2, 2), 6, 4, edgecolor='blue', facecolor='lightblue', linewidth=2))
        axs[2].add_patch(patches.Rectangle((5, 6), 3, 2, edgecolor='blue', facecolor='lightblue', linewidth=2))

    elif shape == "T-Shape":
        # FRONT
        axs[0].add_patch(patches.Rectangle((3, 2), 4, 4, edgecolor='blue', facecolor='lightblue', linewidth=2))
        axs[0].add_patch(patches.Rectangle((2, 6), 6, 2, edgecolor='blue', facecolor='lightblue', linewidth=2))

        # TOP
        axs[1].add_patch(patches.Rectangle((3, 2), 4, 4, edgecolor='blue', facecolor='lightblue', linewidth=2))
        axs[1].add_patch(patches.Rectangle((2, 6), 6, 2, edgecolor='blue', facecolor='lightblue', linewidth=2))

        # SIDE
        axs[2].add_patch(patches.Rectangle((3, 2), 4, 4, edgecolor='blue', facecolor='lightblue', linewidth=2))
        axs[2].add_patch(patches.Rectangle((3, 6), 4, 2, edgecolor='blue', facecolor='lightblue', linewidth=2))

    for ax in axs:
        ax.axis('off')

    st.pyplot(fig)

def run():
    st.title("📐 Module 1: 2D Projection Viewer")
    st.markdown("Visualize **Top, Front, and Side views** of 3D shapes using orthographic projection.")

    shape = st.selectbox("Choose Object Shape:", ["Cube", "L-Shape", "T-Shape"])

    if st.button("📊 Generate Projections"):
        draw_views(shape)
