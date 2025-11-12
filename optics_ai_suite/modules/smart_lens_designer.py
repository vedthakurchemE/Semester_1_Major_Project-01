# smart_lens_designer.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    # Page title and description
    st.markdown("<h1 style='text-align: center;'>🔍 Smart Lens Designer</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>📐 Real-Time Ray Tracing and Focal Length Simulation</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # Sidebar input controls
    st.sidebar.header("🎛️ Lens Parameters")

    lens_type = st.sidebar.selectbox("Select Lens Type", ["Convex", "Concave"])
    n = st.sidebar.slider("Refractive Index (n)", 1.0, 2.0, 1.5, step=0.01)
    R1 = st.sidebar.slider("Radius of Curvature R1 (cm)", 5.0, 50.0, 20.0)
    R2 = st.sidebar.slider("Radius of Curvature R2 (cm)", 5.0, 50.0, 20.0)
    object_distance = st.sidebar.slider("Object Distance u (cm)", 10.0, 100.0, 30.0)
    object_height = st.sidebar.slider("Object Height (cm)", 2.0, 10.0, 5.0)

    # Adjust sign based on lens type
    if lens_type == "Convex":
        R1, R2 = R1, -R2
    else:
        R1, R2 = -R1, R2

    # Lens Maker's formula
    try:
        focal_length = 1 / ((n - 1) * ((1 / R1) - (1 / R2)))
    except ZeroDivisionError:
        focal_length = np.inf

    # Use lens formula: 1/f = 1/v - 1/u
    u = -object_distance
    try:
        v = 1 / ((1 / focal_length) + (1 / u))
    except ZeroDivisionError:
        v = np.inf

    magnification = -v / u
    image_height = magnification * object_height

    # Image analysis
    image_type = "Real" if v > 0 else "Virtual"
    orientation = "Upright" if magnification > 0 else "Inverted"

    # Layout results
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Simulation Results")
        st.markdown(f"- **Focal Length (f):** {round(focal_length, 2)} cm")
        st.markdown(f"- **Image Distance (v):** {round(v, 2)} cm")
        st.markdown(f"- **Magnification:** {round(magnification, 2)}")
        st.markdown(f"- **Image Height:** {round(image_height, 2)} cm")
        st.markdown(f"- **Image Type:** {image_type}")
        st.markdown(f"- **Orientation:** {orientation}")

    with col2:
        st.subheader("🔭 Ray Diagram")

        fig, ax = plt.subplots(figsize=(10, 4))
        lens_pos = 0
        obj_pos = lens_pos + u
        img_pos = lens_pos + v

        # Draw lens and axis
        ax.plot([lens_pos, lens_pos], [-10, 10], 'b', lw=3)
        ax.axhline(0, color='black', linestyle='--')

        # Draw object
        ax.plot([obj_pos, obj_pos], [0, object_height], 'r', lw=2)
        ax.plot(obj_pos, object_height, 'ro')
        ax.text(obj_pos, object_height + 0.5, 'Object', ha='center')

        # Draw image
        ax.plot([img_pos, img_pos], [0, image_height], 'k--', lw=2)
        ax.plot(img_pos, image_height, 'ko')
        ax.text(img_pos, image_height + 0.5, 'Image', ha='center')

        # Rays:
        # 1. Parallel to axis → through focus
        ax.plot([obj_pos, lens_pos], [object_height, object_height], 'orange')
        ax.plot([lens_pos, img_pos], [object_height, 0], 'orange', linestyle='--')

        # 2. Through optical center
        ax.plot([obj_pos, img_pos], [object_height, image_height], 'green')

        # 3. Through focal point → emerges parallel
        ax.plot([obj_pos, lens_pos], [object_height, 0], 'purple')
        ax.plot([lens_pos, img_pos], [0, image_height], 'purple', linestyle='--')

        # Focal points
        ax.plot([lens_pos + focal_length], [0], 'go')
        ax.plot([lens_pos - focal_length], [0], 'go')
        ax.text(lens_pos + focal_length, -1, 'F', ha='center')
        ax.text(lens_pos - focal_length, -1, "F'", ha='center')

        ax.set_xlim(-60, 60)
        ax.set_ylim(-15, 15)
        ax.set_xlabel("Axis (cm)")
        ax.set_ylabel("Height (cm)")
        ax.set_title("Ray Tracing Diagram")
        st.pyplot(fig)

    st.markdown("---")
    st.info("✅ This module simulates lens behavior for teaching, vision optimization, and scientific optics design.")
