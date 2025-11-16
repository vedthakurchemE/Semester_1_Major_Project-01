import streamlit as st
import importlib
import traceback

def run():
    st.set_page_config(page_title="🔌 Basic Electronics Suite", layout="centered")
    st.title("🔬 Basic Electronics Engineering Suite")

    # Map technical names to user-friendly descriptions
    modules_dict = {
        "ohms_law_visualizer": "Ohm's Law Visualizer",
        "transistor_biasing_tool": "Transistor Biasing Tool",
        "rc_circuit_simulator": "RC Circuit Simulator (Resistor-Capacitor)",
        "rlc_resonance_visualizer": "RLC Resonance Visualizer",
        "digital_logic_gate_simulator": "Digital Logic Gate Simulator",
        "diode_characteristics_plotter": "Diode Characteristics Plotter",
        "adc_dac_converter": "ADC/DAC Converter Simulator",
        "number_system_converter": "Number System Converter (Binary, Decimal, Hex)"
    }

    # Show user-friendly names in the sidebar
    selected_friendly = st.sidebar.selectbox("Select Electronics Tool", list(modules_dict.values()))
    selected_module = [k for k, v in modules_dict.items() if v == selected_friendly][0]

    # Safe module runner
    try:
        module = importlib.import_module(f"basic_electronics.modules.{selected_module}")
        if hasattr(module, "run") and callable(module.run):
            module.run()
        else:
            st.warning(f"⚠ Module '{selected_friendly}' does not define a run() function.")
    except ModuleNotFoundError:
        st.error(f"❌ Module '{selected_module}' not found inside modules/.")
    except Exception:
        st.error(f"⚠️ Unexpected error running '{selected_friendly}'")
        with st.expander("Show Error Details"):
            st.code(traceback.format_exc(), language="python")
