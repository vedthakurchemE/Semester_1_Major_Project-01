import streamlit as st
import importlib

def run():
    st.set_page_config(page_title="📐 Engineering Graphics Lab Suite", layout="centered")
    st.title("📐 Engineering Graphics Lab - Interactive Simulator Suite")
    st.caption("🚀 Explore **10 Real-World Visualization Modules** built for Engineering Graphics Lab using Python + Streamlit.")

    # Technical name -> User-friendly label mapping
    modules_dict = {
        "orthographic_view_generator": "Orthographic View Generator",
        "isometric_drawing_tool": "Isometric Drawing Tool",
        "sectional_view_simulator": "Sectional View Simulator",
        "thread_profile_visualizer": "Thread Profile Visualizer",
        "fastener_identifier": "Fastener Identifier",
        "gear_tooth_visualizer": "Gear Tooth Visualizer",
        "auxiliary_view_builder": "Auxiliary View Builder",
        "wireframe_cube_viewer": "Wireframe Cube Viewer",
        "cam_displacement_diagram": "CAM Displacement Diagram Creator"
    }

    # Sidebar only shows user-friendly names!
    selected_friendly = st.sidebar.selectbox("Select a Graphics Tool", list(modules_dict.values()))
    selected_module = [k for k, v in modules_dict.items() if v == selected_friendly][0]

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"eng_graphics_lab.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_friendly}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_friendly}': {e}")
