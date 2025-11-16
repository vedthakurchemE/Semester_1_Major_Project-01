import streamlit as st
import importlib
import sys
import os

def run():
    st.title("🔬 Optics & Modern Physics AI Suite")
    st.markdown("🚀 Explore **10 Interactive Modules** in Optics & Modern Physics using Python + Streamlit.")
    st.markdown("---")

    modules_dict = {
        "smart_lens_designer": "Smart Lens Designer (Optical System Builder)",
        "solar_cell_analyzer": "Solar Cell Analyzer",
        "quantum_tunneling_simulator": "Quantum Tunneling Simulator",
        "optical_fiber_visualizer": "Optical Fiber Visualizer",
        "photoelectric_effect_simulator": "Photoelectric Effect Simulator",
        "hologram_visualizer": "Hologram Visualizer",
        "laser_divergence_simulator": "Laser Divergence Simulator",
        "compton_effect_explorer": "Compton Effect Explorer",
        "atomic_spectra_visualizer": "Atomic Spectra Visualizer",
        "wave_particle_duality_simulator": "Wave-Particle Duality Simulator"
    }

    selected_friendly = st.sidebar.selectbox("Select a Physics Tool", list(modules_dict.values()))
    selected_module = [k for k, v in modules_dict.items() if v == selected_friendly][0]

    # Try to import with both possible paths
    module_paths = [
        f"optics_ai_suite.modules.{selected_module}",
        f"modules.{selected_module}"  # fallback if running from inside optics_ai_suite
    ]

    imported = False
    for path in module_paths:
        try:
            module = importlib.import_module(path)
            imported = True
            break
        except ModuleNotFoundError:
            continue

    if imported:
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_friendly}' does not have a run() function.")
    else:
        st.error(
            f"Module '{selected_module}' could not be imported!\n\n"
            "Possible solutions:\n"
            "- Make sure you run Streamlit from your project root (not inside 'modules').\n"
            "- If running from inside 'optics_ai_suite', try 'streamlit run physics_ai_main.py'.\n"
            "- Double-check spelling/capitalization of filenames and imports."
        )

if __name__ == "__main__":
    run()
