# modules/basic_civil/rcc_beam.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def run():
    st.title("📐 RCC Beam Load Calculator")
    st.markdown("""
    This module helps civil engineers calculate the **bending moment** and **shear force** for a **simply supported beam** under uniformly distributed load (UDL).

    ### 🔍 Use Case:
    - RCC Slab Design
    - Beam Reinforcement
    - Structural Analysis

    ### 📘 Key Formulas:
    - **Maximum Bending Moment (M):** `wL² / 8`
    - **Maximum Shear Force (V):** `wL / 2`
    """)

    st.divider()
    st.subheader("📥 Input Parameters")

    col1, col2 = st.columns(2)
    with col1:
        L = st.number_input("Length of Beam (m)", min_value=1.0, step=0.1, value=5.0)
    with col2:
        w = st.number_input("Uniform Load (kN/m)", min_value=0.0, step=0.1, value=10.0)

    if L > 0 and w >= 0:
        M = (w * L ** 2) / 8  # Bending moment in kNm
        V = (w * L) / 2       # Shear force in kN

        st.success(f"🧮 Max Bending Moment: **{M:.2f} kNm**")
        st.info(f"🧮 Max Shear Force: **{V:.2f} kN**")

        st.divider()
        st.subheader("📊 Bending Moment & Shear Force Diagrams")

        # Bending Moment Diagram (parabolic)
        x = np.linspace(0, L, 100)
        Mx = (w * x * (L - x)) / 2  # Parabolic BMD
        Vx = (w * (L/2 - x))        # Linear SFD

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
        fig.tight_layout(pad=4.0)

        ax1.plot(x, Mx, color='blue', linewidth=2)
        ax1.set_title("Bending Moment Diagram")
        ax1.set_xlabel("Length along beam (m)")
        ax1.set_ylabel("Moment (kNm)")
        ax1.grid(True)

        ax2.plot(x, Vx, color='green', linewidth=2)
        ax2.set_title("Shear Force Diagram")
        ax2.set_xlabel("Length along beam (m)")
        ax2.set_ylabel("Shear Force (kN)")
        ax2.grid(True)

        st.pyplot(fig)
        st.video('https://www.youtube.com/watch?v=TBTCuZbEISE')
        st.info("ℹ️ Values based on basic assumptions of simply supported RCC beam with UDL.")
