import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_orthographic_views(solid):
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    titles = ['Front View', 'Top View', 'Side View']

    for ax, title in zip(axs, titles):
        ax.set_title(title)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    if solid == "Cube":
        for ax in axs:
            ax.add_patch(patches.Rectangle((3, 3), 4, 4, edgecolor='black', facecolor='lightblue', linewidth=2))

    elif solid == "Cylinder":
        # Front View
        axs[0].add_patch(patches.Rectangle((3, 3), 4, 4, edgecolor='black', facecolor='lightgreen', linewidth=2))
        # Top View
        axs[1].add_patch(patches.Circle((5, 5), 2, edgecolor='black', facecolor='lightgreen', linewidth=2))
        # Side View
        axs[2].add_patch(patches.Rectangle((3, 3), 4, 4, edgecolor='black', facecolor='lightgreen', linewidth=2))

    elif solid == "L-block":
        # Front View
        axs[0].add_patch(patches.Rectangle((3, 3), 4, 2, edgecolor='black', facecolor='orange'))
        axs[0].add_patch(patches.Rectangle((3, 5), 2, 2, edgecolor='black', facecolor='orange'))
        # Top View
        axs[1].add_patch(patches.Rectangle((3, 3), 4, 2, edgecolor='black', facecolor='orange'))
        axs[1].add_patch(patches.Rectangle((3, 5), 2, 2, edgecolor='black', facecolor='orange'))
        # Side View
        axs[2].add_patch(patches.Rectangle((3, 3), 2, 4, edgecolor='black', facecolor='orange'))

    plt.tight_layout()
    st.pyplot(fig)

def run():
    st.title("📐 Module 10: Orthographic Projection Generator")
    st.markdown("Generate **2D orthographic projections** (front, top, side views) from 3D engineering models.")

    solid = st.selectbox("📦 Choose Solid", ["Cube", "Cylinder", "L-block"])

    if st.button("🧭 Generate Orthographic Views"):
        draw_orthographic_views(solid)
