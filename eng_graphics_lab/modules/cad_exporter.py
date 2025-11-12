import streamlit as st
import ezdxf
import tempfile
import os
import matplotlib.pyplot as plt
import numpy as np

def create_dxf(shape, dimensions):
    doc = ezdxf.new()
    msp = doc.modelspace()

    if shape == "Rectangle":
        length, width = dimensions
        msp.add_lwpolyline([(0, 0), (length, 0), (length, width), (0, width), (0, 0)])
    elif shape == "Polygon":
        sides, radius = dimensions
        points = []
        for i in range(sides):
            angle = 2 * np.pi * i / sides
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            points.append((x, y))
        points.append(points[0])  # Close polygon
        msp.add_lwpolyline(points)

    return doc


def preview_shape(shape, dimensions):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.set_title(f"{shape} Preview (Not to Scale)", fontsize=14)

    try:
        if shape == "Rectangle":
            length, width = dimensions
            x = [0, length, length, 0, 0]
            y = [0, 0, width, width, 0]
            ax.plot(x, y, 'blue', linewidth=2)

        elif shape == "Polygon":
            sides, radius = dimensions
            angles = np.linspace(0, 2 * np.pi, sides + 1)
            x = radius * np.cos(angles)
            y = radius * np.sin(angles)
            ax.plot(x, y, 'purple', linewidth=2)

        ax.set_xlabel("X (mm)")
        ax.set_ylabel("Y (mm)")
        padding = 10
        ax.set_xlim(min(x) - padding, max(x) + padding)
        ax.set_ylim(min(y) - padding, max(y) + padding)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ Error in preview: {e}")


def run():
    st.title("📤 CAD DXF Exporter")
    st.markdown("""
    Create simple 2D shapes and **export them as `.dxf` CAD files** for use in AutoCAD or CNC tools.

    📂 Ideal for laser cutting, drafting practice, and prototyping.
    """)

    shape = st.selectbox("📐 Choose Shape to Export", ["Rectangle", "Polygon"])

    dimensions = ()
    if shape == "Rectangle":
        length = st.number_input("Length (mm)", min_value=10.0, value=100.0)
        width = st.number_input("Width (mm)", min_value=10.0, value=60.0)
        dimensions = (length, width)

    elif shape == "Polygon":
        sides = st.slider("Number of Sides", min_value=3, max_value=12, value=6)
        radius = st.number_input("Radius (mm)", min_value=5.0, value=50.0)
        dimensions = (sides, radius)

    st.subheader("🖼️ Shape Preview")
    preview_shape(shape, dimensions)

    if st.button("🚀 Export DXF"):
        doc = create_dxf(shape, dimensions)
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".dxf") as tmp:
                doc.saveas(tmp.name)
                with open(tmp.name, "rb") as f:
                    st.download_button("⬇️ Download DXF", f, file_name=f"{shape.lower()}.dxf")
            st.success(f"✅ {shape} DXF file created successfully!")
        except Exception as e:
            st.error(f"❌ Failed to export DXF: {e}")
        finally:
            try:
                os.unlink(tmp.name)
            except:
                pass

    st.caption("⚠️ DXF files are compatible with AutoCAD, Fusion360, SolidWorks, and most CNC software.")
