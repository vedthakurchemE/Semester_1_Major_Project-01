# basic_electronics/basic_electronics_main.py
import streamlit as st
import importlib
import traceback

def run():
    st.set_page_config(page_title="🔌 Basic Electronics Suite", layout="centered")
    st.title("🔬 Basic Electronics Engineering Suite")

    modules_list = [
        "ohms_law_visualizer",
        "transistor_biasing_tool",
        "ac_waveform_analyzer",
        "rc_circuit_simulator",
        "rlc_resonance_visualizer",
        "digital_logic_gate_simulator",
        "diode_characteristics_plotter",
        "transistor_bias_calculator",
        "adc_dac_converter",
        "number_system_converter",
    ]

    selected_module = st.sidebar.selectbox("Select Electronics Tool", modules_list)

    # Safe module runner
    try:
        module = importlib.import_module(f"basic_electronics.modules.{selected_module}")
        if hasattr(module, "run") and callable(module.run):
            module.run()
        else:
            st.warning(f"⚠ Module '{selected_module}' does not define a run() function.")
    except ModuleNotFoundError:
        st.error(f"❌ Module '{selected_module}' not found inside modules/.")
    except Exception:
        st.error(f"⚠️ Unexpected error running '{selected_module}'")
        with st.expander("Show Error Details"):
            st.code(traceback.format_exc(), language="python")
