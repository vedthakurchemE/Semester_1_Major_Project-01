# modules/basic_civil/soil_moisture_calculator.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def run():
    st.set_page_config(page_title="Soil Moisture Calculator", layout="centered")
    st.title("💧 Soil Moisture Content Calculator")
    st.markdown("""
    This tool estimates **moisture content** in a soil sample using standard geotechnical formulas.

    #### 📘 Formula:
    > Moisture (%) = ((Wet Weight - Dry Weight) / Dry Weight) × 100

    It's used in construction, agriculture, and geotechnical site testing to determine water content in soil.
    """)

    st.divider()
    st.subheader("🧪 Enter Soil Sample Measurements")

    col1, col2 = st.columns(2)
    with col1:
        w_dry = st.number_input("Dry Weight (grams)", min_value=0.01, step=0.01, format="%.2f", help="Dry soil weight after oven drying.")
    with col2:
        w_wet = st.number_input("Wet Weight (grams)", min_value=0.01, step=0.01, format="%.2f", help="Wet soil weight before drying.")

    st.divider()

    if w_dry and w_wet:
        if w_wet >= w_dry:
            moisture = ((w_wet - w_dry) / w_dry) * 100
            st.success(f"🌱 Moisture Content: **{moisture:.2f}%**")

            # Moisture graph
            fig, ax = plt.subplots(figsize=(6, 3))
            ax.bar(["Dry Weight", "Wet Weight"], [w_dry, w_wet], color=["sienna", "skyblue"])
            ax.set_title("Soil Sample Weights")
            ax.set_ylabel("Weight (grams)")
            st.pyplot(fig)

            st.video('https://www.youtube.com/watch?v=g5XLQaRi9JA')

            if moisture < 5:
                st.warning("⚠️ Soil is very dry — not ideal for agriculture or compaction.")
            elif moisture > 35:
                st.warning("⚠️ Soil is highly saturated — drainage may be needed.")
            else:
                st.info("✅ Moisture is within typical range for general soil use.")
        else:
            st.error("❌ Wet weight must be greater than or equal to dry weight.")
