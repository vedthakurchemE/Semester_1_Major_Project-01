# modules/sand_bulking_analyzer.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def bulking_curve(moisture):
    # Empirical curve (parabolic rise and fall of bulking)
    return 1 + 0.2 * moisture * np.exp(-0.3 * moisture)

def run():
    st.title("🏖️ Sand Bulking Analyzer")
    st.markdown("""
    Visualize the **bulking of sand** with respect to **moisture content**.

    🧪 **Bulking** is the increase in sand volume due to moisture film on particles. It can lead to under-sanding if not accounted for.

    ---
    ### 💡 Tip:
    Max bulking usually occurs between **4–6% moisture**.
    """)

    st.subheader("📊 Moisture Control")
    moisture = st.slider("Moisture Content (%)", 0, 20, 5)

    bulking_factor = bulking_curve(moisture)
    st.success(f"📈 Bulking Factor: **{bulking_factor:.3f}× Original Volume**")

    # Plotting bulking curve
    st.subheader("📈 Bulking Curve")
    m_values = np.linspace(0, 20, 100)
    b_values = bulking_curve(m_values)

    fig, ax = plt.subplots()
    ax.plot(m_values, b_values, color='darkgreen', linewidth=2)
    ax.axvline(moisture, color='red', linestyle='--', label=f"Current Moisture: {moisture}%")
    ax.set_title("Bulking of Sand vs Moisture Content")
    ax.set_xlabel("Moisture Content (%)")
    ax.set_ylabel("Bulking Factor")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
    st.video('https://www.youtube.com/watch?v=wzquEA2muTk')
    st.video('https://www.youtube.com/watch?v=RHmIItCSSM8')
    st.info("🧾 Engineers adjust sand volume in concrete mix when bulking exceeds 15%.")
