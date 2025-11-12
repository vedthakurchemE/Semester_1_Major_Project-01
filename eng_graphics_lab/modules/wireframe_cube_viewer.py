# modules/wireframe_cube_viewer.py

import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import numpy as np

def cube_edges():
    # Define cube vertices
    v = np.array([[0, 0, 0],
                  [1, 0, 0],
                  [1, 1, 0],
                  [0, 1, 0],
                  [0, 0, 1],
                  [1, 0, 1],
                  [1, 1, 1],
                  [0, 1, 1]])
    # Define edges by connecting vertex indices
    edges = [(v[i], v[j]) for i, j in [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]]
    return edges

def run():
    st.title("🧱 Wireframe Cube Viewer")
    st.markdown("""
    Rotate and explore a **3D wireframe cube** to understand visibility, projections, and hidden edges.

    Used for building intuition for **orthographic views** and spatial understanding.
    """)

    elev = st.slider("📐 Elevation Angle", 0, 90, 30)
    azim = st.slider("🧭 Azimuth Angle", 0, 360, 45)

    edges = cube_edges()

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(elev=elev, azim=azim)

    line_segments = Line3DCollection(edges, colors='black', linewidths=2)
    ax.add_collection3d(line_segments)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.set_axis_off()
    ax.set_title("3D Wireframe View of Cube")

    st.pyplot(fig)
    st.info("🔍 Use this view to understand how 3D objects are visualized in 2D drawings.")
