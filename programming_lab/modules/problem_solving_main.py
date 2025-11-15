import streamlit as st
import importlib

def run():
    st.title("🛠 Problem Solving Lab Suite")
    st.markdown("💡 Explore **10 powerful tools** for real-world productivity, learning, and simulation.")
    st.markdown("---")

    # Technical name -> User-friendly label mapping
    modules_dict = {
        "smart_billing": "Smart Billing System",
        "student_grade_analyzer": "Student Grade Analyzer",
        "library_tracker": "Library Usage Tracker",
        "hospital_scheduler": "Hospital Appointment Scheduler",
        "railway_reservation": "Railway Reservation System",
        "atm_simulator": "ATM Simulator",
        "weather_data_analyzer": "Weather Data Analyzer",
        "inventory_manager": "Inventory Manager",
        "quiz_game": "Quiz Game (Knowledge Challenge)",
        "file_crypto": "File Encryptor/Decryptor"
    }

    # Sidebar only shows user-friendly tool names!
    selected_friendly = st.sidebar.selectbox("Select a Productivity Tool", list(modules_dict.values()))
    selected_module = [k for k, v in modules_dict.items() if v == selected_friendly][0]

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"programming_lab.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_friendly}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_friendly}': {e}")
