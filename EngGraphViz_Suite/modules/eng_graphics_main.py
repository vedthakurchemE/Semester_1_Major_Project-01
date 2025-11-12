import streamlit as st
import importlib

def run():
    st.set_page_config(page_title="📘 Engineering Graphics Suite", layout="wide")
    st.title("📘 Engineering Graphics & Visualization Suite")
    st.markdown("🚀 Explore **10 Visualization Tools** designed for Engineering Graphics Lab using Python + Streamlit.")

    # List of module names (without .py extension)
    modules_list = [
        "projections_2d",
        "orthographic_view",
        "isometric_drawing",
        "sectioning_parts",
        "thread_visualizer",
        "fasteners_identification",
        "cam_profile_plotter",
        "gear_tooth_visualizer",
        "wireframe_viewer",
        "orthographic_projection",
    ]

    # Sidebar selection
    selected_module = st.sidebar.selectbox("Select a Lab Module to Run", modules_list)

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"EngGraphViz_Suite.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_module}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_module}': {e}")
