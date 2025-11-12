import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_hatched_rectangle(ax, x, y, width, height, angle=45, spacing=5, color='black'):
    # Draw base rectangle
    ax.add_patch(patches.Rectangle((x, y), width, height, edgecolor='black', facecolor='none', linewidth=2))

    # Add hatching lines
    x_end = x + width
    y_end = y + height
    for i in np.arange(-height, width + height, spacing):
        x0 = max(x, x + i)
        y0 = y
        x1 = x + i
        y1 = y + height
        if x1 < x:
            x1 = x
            y1 = y + i + height
        ax.plot([x0, min(x1, x_end)], [y0, y1], color=color, linewidth=1)

def draw_section(shape_type):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')

    if shape_type == "Full Section - Cylinder":
        st.markdown("✂️ Showing a full section of a cylinder (cut vertically)")
        # Outer circle
        circle = patches.Circle((5, 5), 3, edgecolor='black', facecolor='none', linewidth=2)
        ax.add_patch(circle)
        # Cut area - hatched
        draw_hatched_rectangle(ax, 2, 2, 3, 6)

    elif shape_type == "Half Section - Hollow Shaft":
        st.markdown("✂️ Showing half section of a hollow shaft")
        # Left half full
        ax.add_patch(patches.Circle((4.5, 5), 2, edgecolor='black', facecolor='lightblue', linewidth=2))
        ax.add_patch(patches.Circle((4.5, 5), 1, edgecolor='white', facecolor='white'))

        # Right half sectioned
        draw_hatched_rectangle(ax, 4.5, 3, 2, 4, spacing=4)

    elif shape_type == "Offset Section - L Block":
        st.markdown("✂️ Offset section to reveal steps in L-block")
        ax.add_patch(patches.Rectangle((2, 2), 6, 2, edgecolor='black', facecolor='none', linewidth=2))
        draw_hatched_rectangle(ax, 2, 4, 3, 2, spacing=4)
        ax.plot([5, 5], [4, 6], color='black', linewidth=2)  # right edge
        ax.plot([2, 2], [2, 4], color='black', linewidth=2)  # left edge

    st.pyplot(fig)

def run():
    st.title("📐 Module 4: Sectioning of Parts")
    st.markdown("Visualize sectional views of machine components to show **internal features** using hatching.")

    shape_type = st.selectbox("✏️ Choose Section Type", [
        "Full Section - Cylinder",
        "Half Section - Hollow Shaft",
        "Offset Section - L Block"
    ])

    if st.button("🔍 Show Sectional View"):
        draw_section(shape_type)
