import streamlit as st
import importlib

def run():
    st.set_page_config(page_title="📘 Engineering Graphics Suite", layout="wide")
    st.title("📘 Engineering Graphics & Visualization Suite")
    st.markdown("🚀 Explore **10 Visualization Tools** designed for Engineering Graphics Lab using Python + Streamlit.")

    # Technical name -> User-friendly label mapping
    modules_dict = {
        "projections_2d": "2D Projections Generator",
        "orthographic_view": "Orthographic View Creator",
        "isometric_drawing": "Isometric Drawing Tool",
        "sectioning_parts": "Sectioning Parts Simulator",
        "thread_visualizer": "Thread Visualizer",
        "fasteners_identification": "Fasteners Identification Tool",
        "gear_tooth_visualizer": "Gear Tooth Visualizer",
        "orthographic_projection": "Orthographic Projection Simulator"
    }

    # Sidebar only shows user-friendly names
    selected_friendly = st.sidebar.selectbox("Select a Graphics Tool", list(modules_dict.values()))
    selected_module = [k for k, v in modules_dict.items() if v == selected_friendly][0]

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"EngGraphViz_Suite.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_friendly}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_friendly}': {e}")
