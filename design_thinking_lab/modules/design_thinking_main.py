import streamlit as st
import importlib

def run():
    st.set_page_config(page_title="🧠 Design Thinking Lab Suite", layout="centered")
    st.title("🧠 Design Thinking Lab Suite")
    st.caption("🚀 Explore **10 High-Impact Real-World Modules** for innovation, empathy, and sustainability.")

    # List of module names (without .py extension)
    modules_list = [
        "accessibility_barrier_mapper",
        "crazy_8s_brainstormer",
        "design_feedback_wall",
        "dot_voting_board",
        "eco_product_feedback_collector",
        "empathy_map_creator",
        "mental_wellness_tracker",
        "problem_solution_map",
        "smart_waste_segregator",
        "smart_water_usage_monitor",
    ]

    # Sidebar selection
    selected_module = st.sidebar.selectbox("Select a Lab Module to Run", modules_list)

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"design_thinking_lab.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_module}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_module}': {e}")

