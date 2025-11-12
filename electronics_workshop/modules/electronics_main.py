import streamlit as st
import importlib

def run():
    st.set_page_config(page_title="🔌 Electronics & Computer Workshop Suite", layout="centered")
    st.title("🔌 Electronics & Computer Workshop Suite")
    st.caption("🚀 Explore **10 Real-World Engineering Tools** developed for your Semester 1 major project.")

    # List of module names (without .py extension)
    modules_list = [
        "led_current_limiter",
        "bridge_rectifier_simulator",
        "voltage_divider_estimator",
        "logic_gate_circuit",
        "sensor_calibration_tool",
        "raspberry_pi_gpio_tester",
        "microcontroller_pinmap_visualizer",
        "power_supply_efficiency",
        "pwm_duty_cycle_visualizer",
        "capacitor_rc_visualizer",
    ]

    # Sidebar selection
    selected_module = st.sidebar.selectbox("Select a Lab Module to Run", modules_list)

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"electronics_workshop.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_module}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_module}': {e}")