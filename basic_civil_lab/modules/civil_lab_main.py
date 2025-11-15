import streamlit as st
import importlib

def run():
    st.set_page_config(page_title="Civil Engineering Lab Suite", layout="centered")
    st.title("🧱 Civil Engineering Lab Suite")
    st.caption("10 Interactive Modules for Basic Civil Engineering")

    # Mapping: technical -> user-friendly name
    modules_dict = {
        "brick_compression_tool": "Brick Compression Strength Tester",
        "cement_consistency_tester": "Cement Consistency Assessment",
        "cement_fineness_analyzer": "Cement Fineness Analyzer",
        "cement_soundness_test": "Cement Soundness Evaluation",
        "fineness_modulus_calculator": "Fineness Modulus Calculator (Aggregate Grading)",
        "flow_table_test": "Cement Flow Table Test (Workability)",
        "sand_bulking_analyzer": "Sand Bulking Analyzer",
        "sieve_analysis_simulator": "Aggregate Sieve Analysis Simulator",
        "specific_gravity_calculator": "Specific Gravity Calculator (Materials)",
        "water_absorption_checker": "Water Absorption Checker (Brick/Material)"
    }

    # Sidebar selection: Only show friendly names
    selected_friendly = st.sidebar.selectbox("Select a Lab Module to Run", list(modules_dict.values()))
    # Find the technical name for import
    selected_module = [key for key, value in modules_dict.items() if value == selected_friendly][0]

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
