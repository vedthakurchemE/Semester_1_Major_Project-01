import streamlit as st
import importlib

def run():
    st.set_page_config(page_title="🧮 Calculus Suite", layout="centered")
    st.title("📊 Calculus Tools")
    st.caption("🔁 10-in-1 Real World Calculus Simulator")

    # Technical name -> User-friendly label mapping
    modules_dict = {
        "module1_population_growth": "Population Growth Modeling",
        "module2_economic_rate_change": "Economic Rate of Change Simulator",
        "module3_drug_dosage_optimizer": "Drug Dosage Optimizer",
        "module4_rocket_trajectory": "Rocket Trajectory Calculator",
        "module5_cost_minimizer": "Cost Minimizer (Optimization)",
        "module6_pollution_area": "Pollution Area Calculator",
        "module7_traffic_flow": "Traffic Flow Analyzer",
        "module8_concrete_cooling": "Concrete Cooling Simulation",
        "module9_beam_deflection": "Beam Deflection Calculator",
        "module10_tank_filling": "Tank Filling Rate Calculator"
    }

    # Sidebar: Only show friendly labels
    selected_friendly = st.sidebar.selectbox("Select a Calculus Tool", list(modules_dict.values()))
    selected_module = [k for k, v in modules_dict.items() if v == selected_friendly][0]

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"CalculusBridgeAI.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_friendly}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_friendly}': {e}")
