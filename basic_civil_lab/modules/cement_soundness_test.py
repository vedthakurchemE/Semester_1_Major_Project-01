# modules/cement_soundness_test.py

import streamlit as st
import matplotlib.pyplot as plt

def run():
    st.title("🧪 Cement Soundness Test Simulator")
    st.markdown("""
    Simulate the **Le Chatelier test** for determining the **soundness of cement**.

    🚧 Soundness refers to the **volumetric stability** of hardened cement.  
    This test ensures cement doesn't expand excessively after setting, which can cause cracking.

    ---
    ### 🧪 Standard:
    - IS: 4031 (Part 3) – Le Chatelier Apparatus
    """)

    st.subheader("📐 Test Inputs")
    initial_distance = st.number_input("Initial Distance Between Indicator Points (mm)", min_value=0.0, value=10.0)
    final_distance = st.number_input("Final Distance After Boiling (mm)", min_value=0.0, value=12.0)

    expansion = final_distance - initial_distance

    if expansion < 0:
        st.error("❌ Final distance cannot be less than initial.")
        return

    st.success(f"📏 Soundness = {expansion:.2f} mm")

    # Verdict
    if expansion <= 10:
        st.info("✅ Cement is **sound** (Expansion within acceptable limit).")
    else:
        st.warning("⚠️ Cement is **unsound** (Exceeds expansion limit).")

    # Visualizing
    st.subheader("📊 Visual Indicator")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    ax.barh(["Initial", "Final"], [initial_distance, final_distance], color=["#4CAF50", "#FF5722"])
    ax.set_xlim(0, max(final_distance + 5, 15))
    ax.set_xlabel("Distance (mm)")
    ax.set_title("Le Chatelier Apparatus Indicator Movement")
    st.pyplot(fig)
    st.video('https://www.youtube.com/watch?v=RoGhRsdUi1Q')
    st.video('https://www.youtube.com/watch?v=sBo6yz4dNrI')

    st.caption("ℹ️ Excess lime or magnesia causes expansion leading to unsoundness.")
