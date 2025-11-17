import streamlit as st
import matplotlib.pyplot as plt  # Remove if not used
import numpy as np  # Remove if not used


def run():
    st.title("🧱 Brick Compression Strength Tool")

    # Correct local path handling
    local_video_path = r"C:\Users\VED THAKUR\OneDrive\Videos\Captures\📘 Semester 1 – Engineering Project Suite · Streamlit - Comet 2025-11-17 17-47-30.mp4"
    try:
        video_file = open(local_video_path, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    except Exception as e:
        st.error(f"Could not load local video: {e}")

    # Or display a YouTube video
    st.video('https://youtu.be/VspSVg1tk_Q')

    st.markdown("""
    Simulate the **compressive strength test** for bricks based on **maximum load and contact area**.

    ---
    ### 🧮 Formula:
    \[
    \text{Compressive Strength (N/mm²)} = \frac{\text{Maximum Load (N)}}{\text{Loaded Area (mm²)}}
    \]
    """)

    st.subheader("📥 Enter Test Parameters")
    col1, col2 = st.columns(2)

    with col1:
        max_load = st.number_input("🔨 Maximum Load (kN)", min_value=1.0, value=100.0, step=1.0)
        max_load_n = max_load * 1000  # Convert to Newton

    with col2:
        length = st.number_input("📏 Brick Length (mm)", min_value=100.0, value=190.0, step=1.0)
        width = st.number_input("📏 Brick Width (mm)", min_value=50.0, value=90.0, step=1.0)

    area = length * width  # Loaded area in mm²

    if area == 0:
        st.warning("🧮 Enter valid dimensions.")
        return

    strength = round(max_load_n / area, 2)

    st.divider()
    st.success(f"🧱 Compressive Strength: **{strength} N/mm²**")

    # Grading check
    st.markdown("### 📊 IS Classification (IS 1077:1992)")
    if strength >= 35:
        st.info("🏗️ **Grade A (Very High Strength Brick)** - Suitable for heavy load-bearing structures.")
    elif 25 <= strength < 35:
        st.info("🏗️ **Grade B (High Strength Brick)** - Suitable for high-rise buildings.")
    elif 12 <= strength < 25:
        st.info("🏘️ **Grade C (Moderate Strength Brick)** - Used in general building works.")
    else:
        st.warning("⚠️ **Below standard. Not recommended for structural work.**")

    st.caption("🔍 Based on IS: 3495 and IS: 1077 guidelines. Values are for educational purposes.")


if __name__ == "__main__":
    run()
