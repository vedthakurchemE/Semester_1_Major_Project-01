# basic_civil_suite/modules/civil_tools_main.py
import streamlit as st
import importlib
import traceback

def run():
    st.set_page_config(page_title="🧱 Civil Engineering Suite", layout="centered")
    st.title("🧱 Civil Engineering Suite")
    st.write("🔁 Built using Streamlit for Basic Civil Engineering")

    # List of Civil Tools
    modules_list = [
        "soil_moisture_calculator",
        "brick_estimator",
        "cement_bag_estimator",
        "rcc_beam",
        "bbs_visualizer",
        "concrete_mix_tool",
        "water_tank_estimator",
        "slump_test",
        "site_level_indicator",
        "road_gradient_calculator"
    ]

    selected_module = st.sidebar.selectbox("Select Civil Tool", modules_list)

    # Safe module runner
    try:
        module = importlib.import_module(f"basic_civil_suite.modules.{selected_module}")
        if hasattr(module, "run") and callable(module.run):
            with st.spinner(f"🔄 Loading {selected_module}..."):
                module.run()
        else:
            st.warning(f"⚠ Module '{selected_module}' does not define a run() function.")
    except ModuleNotFoundError:
        st.error(f"❌ Module '{selected_module}' not found inside modules/.")
    except Exception:
        st.error(f"⚠️ Unexpected error running '{selected_module}'")
        with st.expander("Show Error Details"):
            st.code(traceback.format_exc(), language="python")
