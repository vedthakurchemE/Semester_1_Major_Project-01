import streamlit as st
import importlib

def run():
    st.set_page_config(page_title="🔌 Electronics & Computer Workshop Suite", layout="centered")
    st.title("🔌 Electronics & Computer Workshop Suite")
    st.caption("🚀 Explore **10 Real-World Engineering Tools** developed for your Semester 1 major project.")

    # Technical name -> User-friendly label mapping
    modules_dict = {
        "led_current_limiter": "LED Current Limiter Designer",
        "bridge_rectifier_simulator": "Bridge Rectifier Simulator",
        "voltage_divider_estimator": "Voltage Divider Estimator",
        "logic_gate_circuit": "Logic Gate Circuit Simulator",
        "sensor_calibration_tool": "Sensor Calibration Tool",
        "raspberry_pi_gpio_tester": "Raspberry Pi GPIO Tester",
        "microcontroller_pinmap_visualizer": "Microcontroller Pinmap Visualizer",
        "power_supply_efficiency": "Power Supply Efficiency Analyzer",
        "pwm_duty_cycle_visualizer": "PWM Duty Cycle Visualizer",
        "capacitor_rc_visualizer": "Capacitor RC Circuit Visualizer"
    }

    # Sidebar shows only user-friendly names
    selected_friendly = st.sidebar.selectbox("Select a Lab Tool", list(modules_dict.values()))
    selected_module = [k for k, v in modules_dict.items() if v == selected_friendly][0]

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"electronics_workshop.modules.{selected_module}")

        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_friendly}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_friendly}': {e}")


        # Run the module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_module}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_module}': {e}")