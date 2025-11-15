import streamlit as st
import importlib
import traceback

def run():
    st.set_page_config(page_title="🧱 Civil Engineering Suite", layout="centered")
    st.title("🧱 Civil Engineering Suite")
    st.write("🔁 Built using Streamlit for Basic Civil Engineering")

    # Technical name: User-friendly label mapping
    modules_dict = {
        "soil_moisture_calculator": "Soil Moisture Calculator",
        "brick_estimator": "Brick Quantity Estimator",
        "cement_bag_estimator": "Cement Bag Estimator",
        "rcc_beam": "RCC Beam Designer (Reinforced Concrete)",
        "bbs_visualizer": "Bar Bending Schedule (BBS) Visualizer",
        "concrete_mix_tool": "Concrete Mix Design Tool",
        "water_tank_estimator": "Water Tank Volume Estimator",
        "slump_test": "Concrete Slump Test Simulator",
        "site_level_indicator": "Site Level Indicator (Level Tool)",
        "road_gradient_calculator": "Road Gradient Calculator"
    }

    # Show only user-friendly names in UI
    selected_friendly = st.sidebar.selectbox("Select Civil Tool", list(modules_dict.values()))
    selected_module = [k for k, v in modules_dict.items() if v == selected_friendly][0]

    # Safe module runner
    try:
        module = importlib.import_module(f"basic_civil_suite.modules.{selected_module}")
        if hasattr(module, "run") and callable(module.run):
            with st.spinner(f"🔄 Loading {selected_friendly}..."):
                module.run()
        else:
            st.warning(f"⚠ Module '{selected_friendly}' does not define a run() function.")
    except ModuleNotFoundError:
        st.error(f"❌ Module '{selected_module}' not found inside modules/.")
    except Exception:
        st.error(f"⚠️ Unexpected error running '{selected_friendly}'")
        with st.expander("Show Error Details"):
            st.code(traceback.format_exc(), language="python")
