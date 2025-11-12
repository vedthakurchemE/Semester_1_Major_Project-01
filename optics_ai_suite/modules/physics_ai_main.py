import streamlit as st
import importlib

def run():
    st.title("🔬 Optics & Modern Physics AI Suite")
    st.markdown("🚀 Explore **10 Interactive Modules** in Optics & Modern Physics using Python + Streamlit.")
    st.markdown("---")

    # List of module names (without .py extension)
    modules_list = [
        "smart_lens_designer",
        "hologram_visualizer",
        "solar_cell_analyzer",
        "quantum_tunneling_simulator",
        "optical_fiber_visualizer",
        "photoelectric_effect_simulator",
        "laser_divergence_simulator",
        "compton_effect_explorer",
        "atomic_spectra_visualizer",
        "wave_particle_duality_simulator",
    ]

    # Sidebar selection
    selected_module = st.sidebar.selectbox("Select a Lab Module to Run", modules_list)

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"optics_ai_suite.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_module}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_module}': {e}")
