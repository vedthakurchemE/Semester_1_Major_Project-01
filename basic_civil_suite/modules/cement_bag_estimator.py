# modules/basic_civil/cement_bag_estimator.py

import streamlit as st

def run():
    st.title("🧱 Cement Bag Estimator")
    st.markdown("""
    This tool calculates the **number of 50 kg cement bags** required for your RCC concrete mix based on volume and mix ratio.

    #### 📘 Formula (by dry volume):
    > Cement = (Dry Volume × Cement Part) / Total Ratio × 1.54 (dry to wet conversion)

    🔹 **1.54** = bulking factor (wet to dry conversion)  
    🔹 **Volume of 1 cement bag** = 0.035 m³ (50 kg OPC)
    """)

    st.divider()
    st.subheader("📏 Input Parameters")

    col1, col2 = st.columns(2)
    with col1:
        concrete_volume = st.number_input("Concrete Volume Required (m³)", min_value=0.1, step=0.1, value=1.0)
    with col2:
        mix_grade = st.selectbox("Select RCC Mix Ratio", ["M5 (1:5:10)", "M10 (1:3:6)", "M15 (1:2:4)", "M20 (1:1.5:3)", "M25 (1:1:2)"])

    ratio_map = {
        "M5 (1:5:10)": (1, 5, 10),
        "M10 (1:3:6)": (1, 3, 6),
        "M15 (1:2:4)": (1, 2, 4),
        "M20 (1:1.5:3)": (1, 1.5, 3),
        "M25 (1:1:2)": (1, 1, 2)
    }

    cement, sand, agg = ratio_map[mix_grade]
    total_parts = cement + sand + agg
    dry_volume = concrete_volume * 1.54  # Wet to dry

    cement_volume = (dry_volume * cement) / total_parts
    bags = cement_volume / 0.035  # 1 bag = 0.035 m³

    st.divider()
    st.success(f"🧮 Cement Bags Required: **{bags:.1f} bags (50 kg each)**")

    st.markdown(f"""
    #### 📊 Mix Details:
    - **Concrete Volume**: {concrete_volume:.2f} m³  
    - **Dry Volume (wastage incl.)**: {dry_volume:.2f} m³  
    - **Mix Ratio**: {cement}:{sand}:{agg}  
    - **Cement Volume Needed**: {cement_volume:.2f} m³  
    """)

    st.info("ℹ️ Always round up & add extra ~5% on site to account for loss.")
