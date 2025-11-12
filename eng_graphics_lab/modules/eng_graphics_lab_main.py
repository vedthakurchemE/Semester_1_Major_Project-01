import streamlit as st
import importlib

def run():
    st.set_page_config(page_title="📐 Engineering Graphics Lab Suite", layout="centered")
    st.title("📐 Engineering Graphics Lab - Interactive Simulator Suite")
    st.caption("🚀 Explore **10 Real-World Visualization Modules** built for Engineering Graphics Lab using Python + Streamlit.")

    # List of module names (without .py extension)
    modules_list = [
        "orthographic_view_generator",
        "isometric_drawing_tool",
        "sectional_view_simulator",
        "thread_profile_visualizer",
        "fastener_identifier",
        "gear_tooth_visualizer",
        "auxiliary_view_builder",
        "wireframe_cube_viewer",
        "cad_exporter",
        "cam_displacement_diagram",
    ]

    # Sidebar selection
    selected_module = st.sidebar.selectbox("Select a Lab Module to Run", modules_list)

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"eng_graphics_lab.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_module}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_module}': {e}")