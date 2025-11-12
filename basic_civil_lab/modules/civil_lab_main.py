import streamlit as st
import importlib

def run():
    st.set_page_config(page_title="Civil Engineering Lab Suite", layout="centered")
    st.title("🧱 Civil Engineering Lab Suite")
    st.caption("10 Interactive Modules for Basic Civil Engineering")

    # List of module names (without .py extension)
    modules_list = [
        "brick_compression_tool",
        "cement_consistency_tester",
        "cement_fineness_analyzer",
        "cement_soundness_test",
        "fineness_modulus_calculator",
        "flow_table_test",
        "sand_bulking_analyzer",
        "sieve_analysis_simulator",
        "specific_gravity_calculator",
        "water_absorption_checker"
    ]

    # Sidebar selection
    selected_module = st.sidebar.selectbox("Select a Lab Module to Run", modules_list)

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"basic_civil_lab.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_module}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_module}': {e}")
