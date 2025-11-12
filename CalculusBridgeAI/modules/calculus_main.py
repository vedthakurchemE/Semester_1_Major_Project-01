import streamlit as st
import importlib

def run():
    st.set_page_config(page_title="🧮 Calculus Suite", layout="centered")
    st.title("📊 Calculus Tools")
    st.caption("🔁 10-in-1 Real World Calculus Simulator")

    # List of module names (without .py extension)
    modules_list = [
        "module1_population_growth",
        "module2_economic_rate_change",
        "module3_drug_dosage_optimizer",
        "module4_rocket_trajectory",
        "module5_cost_minimizer",
        "module6_pollution_area",
        "module7_traffic_flow",
        "module8_concrete_cooling",
        "module9_beam_deflection",
        "module10_tank_filling",
    ]

    # Sidebar selection
    selected_module = st.sidebar.selectbox("Select a Lab Module to Run", modules_list)

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"CalculusBridgeAI.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_module}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_module}': {e}")
