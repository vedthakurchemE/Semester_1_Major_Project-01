# modules/basic_civil/brick_estimator.py

import streamlit as st
import matplotlib.pyplot as plt

def run():
    st.title("🧱 Brick Quantity Estimator")
    st.markdown("""
    This tool calculates the **approximate number of bricks** needed to build a wall.

    #### 🧮 Formula:
    `No. of Bricks = Volume of Wall / Volume of 1 Brick`

    ✅ Mortar gap and wastage options are also included.
    """)

    st.divider()
    st.subheader("📐 Wall Dimensions")
    col1, col2, col3 = st.columns(3)
    with col1:
        length = st.number_input("Length of Wall (m)", min_value=0.1, step=0.1)
    with col2:
        height = st.number_input("Height of Wall (m)", min_value=0.1, step=0.1)
    with col3:
        thickness = st.number_input("Thickness of Wall (m)", min_value=0.05, value=0.2)

    st.subheader("🧱 Brick Size (Standard: 190×90×90 mm)")

    custom_size = st.checkbox("🔧 Customize Brick Size")
    if custom_size:
        l_brick = st.number_input("Length (mm)", min_value=100, value=190)
        w_brick = st.number_input("Width (mm)", min_value=50, value=90)
        h_brick = st.number_input("Height (mm)", min_value=50, value=90)
    else:
        l_brick, w_brick, h_brick = 190, 90, 90

    mortar = st.checkbox("Include Mortar Gap (10mm)", value=True)
    wastage = st.slider("Wastage Allowance (%)", 0, 15, 5)

    # Convert mm to meters and include mortar gap
    mortar_gap = 10 if mortar else 0
    l = (l_brick + mortar_gap) / 1000
    w = (w_brick + mortar_gap) / 1000
    h = (h_brick + mortar_gap) / 1000
    brick_volume = l * w * h

    wall_volume = length * height * thickness
    num_bricks = wall_volume / brick_volume
    num_bricks_final = int(num_bricks * (1 + wastage / 100))

    st.divider()
    st.success(f"🧮 Approximate Bricks Required: **{num_bricks_final:,} bricks**")

    fig, ax = plt.subplots(figsize=(5, 2))
    ax.bar(["Wall Volume", "1 Brick Volume"], [wall_volume, brick_volume], color=["#8B4513", "#D2691E"])
    ax.set_ylabel("Volume (m³)")
    ax.set_title("Wall vs Brick Volume")
    st.pyplot(fig)

    st.info("ℹ️ Includes allowance for mortar and wastage. Always order slightly extra bricks on-site.")
