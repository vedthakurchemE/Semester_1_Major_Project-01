# modules/basic_civil/slump_test.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def run():
    st.title("🧪 Slump Test Simulator")
    st.markdown("""
    This tool estimates the **slump value** of concrete based on its **Water/Cement (W/C) ratio** and **mix type**.

    #### 📘 Formula (Empirical):
    > Slump ≈ *k × (W/C - base)* × 100  
    *Where `k` depends on mix type.*

    ---
    **Used in construction** to:
    - Ensure proper workability
    - Prevent over/under-watering
    - Match required consistency for site conditions
    """)

    st.divider()
    mix_type = st.selectbox("🏗️ Select Concrete Mix Type", ["Dry Mix", "Plastic Mix", "Flowing Mix"])
    wc_ratio = st.slider("💧 Water/Cement Ratio", 0.3, 0.7, step=0.01, value=0.5)

    # Set base value and multiplier for each mix
    base_wc = 0.3
    k_values = {"Dry Mix": 2.5, "Plastic Mix": 4.2, "Flowing Mix": 6.5}
    k = k_values[mix_type]

    slump = max(0, k * (wc_ratio - base_wc) * 100)  # in mm
    slump = min(slump, 250)  # practical upper bound

    st.success(f"🧮 Estimated Slump: **{slump:.1f} mm**")

    # Visualize slump cone
    fig, ax = plt.subplots(figsize=(4, 4))
    cone_height = 300
    slump_display = cone_height - slump

    ax.plot([0.4, 0.6], [0, cone_height], color='gray', lw=4)
    ax.plot([1.4, 1.6], [0, cone_height], color='gray', lw=4)
    ax.plot([0.4, 1.4], [0, 0], color='gray', lw=4)
    ax.plot([0.6, 1.6], [cone_height, cone_height], color='gray', lw=4)
    ax.plot([0.6, 1.6], [slump_display, slump_display], color='blue', lw=4, linestyle='--')

    ax.text(0.7, slump_display + 10, f"{slump:.1f} mm", fontsize=12, color='blue')
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 320)
    ax.axis('off')
    st.pyplot(fig)

    # Slump category info
    if slump < 25:
        st.warning("🔴 Very Low Workability (Dry Mix) – Not suitable for standard concrete placement.")
    elif 25 <= slump <= 75:
        st.info("🟡 Low Workability – Suitable for lightly reinforced sections.")
    elif 75 < slump <= 150:
        st.success("🟢 Medium Workability – Commonly used in beams, slabs, columns.")
    else:
        st.warning("🔴 High Workability – Use caution to prevent segregation.")
