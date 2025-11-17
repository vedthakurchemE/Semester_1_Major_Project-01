# modules/cement_consistency_tester.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def run():
    st.title("🧪 Cement Consistency Tester (Vicat Apparatus Simulator)")
    st.markdown("""
    This simulator helps estimate the **standard consistency** of cement using the **Vicat Apparatus**.

    📘 According to IS:4031 (Part 4) – Standard consistency is defined as the % of water required for a 10 mm to 12 mm penetration of the Vicat plunger.

    #### 📐 Formula:
    `Standard Consistency = (Water Added / Weight of Cement) × 100`
    """)

    st.subheader("🔢 Input Parameters")

    weight_cement = st.number_input("Weight of Cement (g)", min_value=100, value=400)
    trial_no = st.number_input("Number of Trials", min_value=1, max_value=10, value=3)

    water_inputs = []
    penetration_outputs = []

    st.markdown("### 🧪 Trial Data Entry")
    for i in range(int(trial_no)):
        col1, col2 = st.columns(2)
        with col1:
            w = st.number_input(f"Trial {i+1} - Water Added (ml)", min_value=50.0, value=100.0 + i*10)
        with col2:
            p = st.slider(f"Trial {i+1} - Penetration Depth (mm)", 0, 50, 10 + i*2)
        water_inputs.append(w)
        penetration_outputs.append(p)

    st.divider()
    st.subheader("📈 Penetration vs Water Content Graph")

    fig, ax = plt.subplots()
    ax.plot(water_inputs, penetration_outputs, 'bo-', linewidth=2)
    ax.axhline(10, color='green', linestyle='--', label='10 mm Ideal')
    ax.axhline(12, color='orange', linestyle='--', label='12 mm Upper Limit')
    ax.set_xlabel("Water Added (ml)")
    ax.set_ylabel("Penetration Depth (mm)")
    ax.set_title("Penetration vs Water Content")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    st.divider()
    st.subheader("📊 Suggested Standard Consistency")

    # Interpolate best fit value (just a demonstration)
    if any(10 <= p <= 12 for p in penetration_outputs):
        idx = next(i for i, p in enumerate(penetration_outputs) if 10 <= p <= 12)
        w_required = water_inputs[idx]
        std_consistency = round((w_required / weight_cement) * 100, 2)
        st.success(f"✅ Standard Consistency is approximately **{std_consistency}%**")
    else:
        st.warning("⚠️ No trial has penetration between 10 mm and 12 mm. Try adjusting water content.")


    st.video('https://www.youtube.com/watch?v=Lq7Xx1yD4Mg')
    st.video('https://www.youtube.com/watch?v=qszlGazu4kU')

    st.caption("📘 Always perform minimum 3 trials to ensure valid estimation.")
