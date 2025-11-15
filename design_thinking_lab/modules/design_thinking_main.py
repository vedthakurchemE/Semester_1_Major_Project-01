import streamlit as st
import importlib

def run():
    st.set_page_config(page_title="🧠 Design Thinking Lab Suite", layout="centered")
    st.title("🧠 Design Thinking Lab Suite")
    st.caption("🚀 Explore **10 High-Impact Real-World Modules** for innovation, empathy, and sustainability.")

    # Technical name -> User-friendly label mapping
    modules_dict = {
        "accessibility_barrier_mapper": "Accessibility Barrier Mapper",
        "crazy_8s_brainstormer": "Crazy 8’s Brainstorming Tool",
        "design_feedback_wall": "Design Feedback Wall",
        "dot_voting_board": "Dot Voting Decision Board",
        "eco_product_feedback_collector": "Eco-friendly Product Feedback Collector",
        "empathy_map_creator": "Empathy Map Creator",
        "mental_wellness_tracker": "Mental Wellness Tracker",
        "problem_solution_map": "Problem/Solution Mapping Tool",
        "smart_waste_segregator": "Smart Waste Segregator Simulator",
        "smart_water_usage_monitor": "Smart Water Usage Monitor"
    }

    # Sidebar shows only user-friendly names
    selected_friendly = st.sidebar.selectbox("Select a Design Thinking Tool", list(modules_dict.values()))
    selected_module = [k for k, v in modules_dict.items() if v == selected_friendly][0]

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"design_thinking_lab.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_friendly}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_friendly}': {e}")
