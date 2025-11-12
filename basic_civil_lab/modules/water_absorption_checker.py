# modules/water_absorption_checker.py

import streamlit as st
import matplotlib.pyplot as plt

def run():
    st.title("💧 Water Absorption Test Simulator")
    st.markdown("""
    Simulate the **Water Absorption Test** for construction materials (bricks, aggregates) to determine how much water a dry specimen absorbs.

    ---
    ### 🧮 Formula:
    **Water Absorption (%) = ((Wet Weight - Dry Weight) / Dry Weight) × 100**

    📌 As per IS: 3495 (Part 2) for bricks and IS: 2386 (Part 3) for aggregates.
    """)

    st.subheader("📥 Enter Experimental Readings")
    dry_weight = st.number_input("Dry Weight (W₁) of Sample (g)", min_value=100.0, value=1500.0, step=10.0)
    wet_weight = st.number_input("Wet Weight (W₂) After 24h Immersion (g)", min_value=100.0, value=1620.0, step=10.0)

    if wet_weight <= dry_weight:
        st.error("❌ Wet weight must be greater than dry weight.")
        return

    if st.button("🧪 Calculate Absorption"):
        absorption = ((wet_weight - dry_weight) / dry_weight) * 100
        st.success(f"💧 Water Absorption: **{absorption:.2f}%**")

        if absorption <= 20:
            st.success("🟢 Within acceptable limits for bricks and aggregates.")
        else:
            st.warning("🔴 Excessive absorption! Material not suitable for quality construction.")

    st.divider()
    st.subheader("📊 Absorption Visualization")

    fig, ax = plt.subplots()
    ax.bar(["Dry Weight", "Wet Weight"], [dry_weight, wet_weight], color=["#8B4513", "#1E90FF"])
    ax.set_ylabel("Weight (g)")
    ax.set_title("Material Weight Before and After Immersion")
    st.pyplot(fig)

    st.caption("🧱 Applies to bricks, coarse aggregates, lightweight blocks, and other absorbent materials.")
