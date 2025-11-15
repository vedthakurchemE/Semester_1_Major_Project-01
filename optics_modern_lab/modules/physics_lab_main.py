import streamlit as st
import importlib

def run():
    st.title("🔬 Optics & Modern Physics - Virtual Lab Suite")
    st.markdown("🚀 Explore **10 interactive experiments** in Optics & Modern Physics, built with Python + Streamlit.")
    st.markdown("---")

    # Technical name -> User-friendly label mapping
    modules_dict = {
        "newtons_rings_simulator": "Newton's Rings Simulator",
        "youngs_double_slit": "Young's Double Slit Experiment",
        "diffraction_grating_tool": "Diffraction Grating Tool",
        "laser_wavelength_measure": "Laser Wavelength Measurement",
        "photoelectric_effect_explorer": "Photoelectric Effect Explorer",
        "polarization_visualizer": "Polarization Visualizer",
        "blackbody_radiation_plotter": "Blackbody Radiation Plotter",
        "bohr_model_visualizer": "Bohr Model Visualizer",
        "xray_tube_simulator": "X-ray Tube Simulator",
        "wave_particle_duality_explorer": "Wave-Particle Duality Explorer"
    }

    # Sidebar only shows user-friendly names!
    selected_friendly = st.sidebar.selectbox("Select a Lab Experiment", list(modules_dict.values()))
    selected_module = [k for k, v in modules_dict.items() if v == selected_friendly][0]

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"optics_modern_lab.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_friendly}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_friendly}': {e}")
