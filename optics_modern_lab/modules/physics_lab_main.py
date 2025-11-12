import streamlit as st
import importlib

def run():
    st.title("🔬 Optics & Modern Physics - Virtual Lab Suite")
    st.markdown("🚀 Explore **10 interactive experiments** in Optics & Modern Physics, built with Python + Streamlit.")
    st.markdown("---")

    # List of module names (without .py extension)
    modules_list = [
        "newtons_rings_simulator",
        "youngs_double_slit",
        "diffraction_grating_tool",
        "laser_wavelength_measure",
        "photoelectric_effect_explorer",
        "polarization_visualizer",
        "blackbody_radiation_plotter",
        "bohr_model_visualizer",
        "xray_tube_simulator",
        "wave_particle_duality_explorer",
    ]

    # Sidebar selection
    selected_module = st.sidebar.selectbox("Select a Lab Module to Run", modules_list)

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"optics_modern_lab.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_module}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_module}': {e}")