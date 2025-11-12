import streamlit as st
import importlib

def run():
    st.title("🛠 Problem Solving Lab Suite")
    st.markdown("💡 Explore **10 powerful tools** for real-world productivity, learning, and simulation.")
    st.markdown("---")

    # List of module names (without .py extension)
    modules_list = [
        "smart_billing",
        "student_grade_analyzer",
        "library_tracker",
        "hospital_scheduler",
        "railway_reservation",
        "atm_simulator",
        "weather_data_analyzer",
        "inventory_manager",
        "quiz_game",
        "file_crypto",
    ]

    # Sidebar selection
    selected_module = st.sidebar.selectbox("Select a Lab Module to Run", modules_list)

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"programming_lab.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_module}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_module}': {e}")