import streamlit as st
import importlib

def run():
    st.title("🔬 Optics & Modern Physics AI Suite")
    st.markdown("🚀 Explore **10 Interactive Modules** in Optics & Modern Physics using Python + Streamlit.")
    st.markdown("---")

    # Technical name -> User-friendly label mapping
    modules_dict = {
        "smart_lens_designer": "Smart Lens Designer (Optical System Builder)",
        "solar_cell_analyzer": "Solar Cell Analyzer",
        "quantum_tunneling_simulator": "Quantum Tunneling Simulator",
        "optical_fiber_visualizer": "Optical Fiber Visualizer",
        "photoelectric_effect_simulator": "Photoelectric Effect Simulator",
        "compton_effect_explorer": "Compton Effect Explorer",
        "atomic_spectra_visualizer": "Atomic Spectra Visualizer",
        "wave_particle_duality_simulator": "Wave-Particle Duality Simulator"
    }

    # Sidebar shows only user-friendly names
    selected_friendly = st.sidebar.selectbox("Select a Physics Tool", list(modules_dict.values()))
    selected_module = [k for k, v in modules_dict.items() if v == selected_friendly][0]

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"optics_ai_suite.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_friendly}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_friendly}': {e}")
