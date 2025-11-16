# modules/flow_table_test.py

import streamlit as st
import matplotlib.pyplot as plt

def calculate_flow(initial_diameter, final_diameter):
    return ((final_diameter - initial_diameter) / initial_diameter) * 100

def run():
    st.title("🌀 Flow Table Test Simulator")
    st.markdown("""
    Simulate the **Flow Table Test** to determine the **workability and consistency** of mortar or cement paste.

    ---
    ### 🧪 Formula:
    `Flow % = ((Final Diameter - Initial Diameter) / Initial Diameter) × 100`
    """)

    st.subheader("📐 Input Measurements")

    col1, col2 = st.columns(2)
    with col1:
        initial_dia = st.number_input("Initial Diameter (cm)", min_value=5.0, value=10.0, step=0.1)
    with col2:
        final_dia = st.number_input("Final Diameter after 25 drops (cm)", min_value=5.0, value=14.0, step=0.1)

    if final_dia < initial_dia:
        st.warning("⚠️ Final diameter should be greater than initial diameter.")
        return

    flow_percent = calculate_flow(initial_dia, final_dia)
    st.success(f"🧮 Calculated Flow: **{flow_percent:.2f}%**")

    st.subheader("📊 Visualization")
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(["Initial Dia", "Final Dia"], [initial_dia, final_dia], color=["#4682B4", "#32CD32"])
    ax.set_ylabel("Diameter (cm)")
    ax.set_title("Flow Table Expansion")
    st.pyplot(fig)
    st.video('https://www.youtube.com/watch?v=xgwe2Rj42UQ')
    st.caption("📘 Based on IS 5512: Used in evaluating cement mortar workability.")
