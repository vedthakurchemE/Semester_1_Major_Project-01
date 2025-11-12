# modules/basic_civil/concrete_mix_tool.py

import streamlit as st

def run():
    st.title("🧪 Concrete Mix Ratio Tool")
    st.markdown("""
    Generate **concrete mix quantities** for a given RCC grade and volume.

    ### 📘 Assumptions:
    - Dry volume = Wet volume × 1.54
    - 1 bag cement = 50 kg = 0.035 m³
    - Typical density of materials:
        - Cement = 1440 kg/m³  
        - Sand = 1450 kg/m³  
        - Aggregate = 1500 kg/m³  
        - Water = 1000 kg/m³
    """)

    st.subheader("📥 Input")
    volume = st.number_input("Concrete Volume (m³)", min_value=0.1, step=0.1, value=1.0)
    grade = st.selectbox("Select RCC Grade", [
        "M5 (1:5:10)", "M7.5 (1:4:8)", "M10 (1:3:6)", "M15 (1:2:4)",
        "M20 (1:1.5:3)", "M25 (1:1:2)", "M30 (1:0.75:1.5)"
    ])

    ratio_dict = {
        "M5 (1:5:10)": (1, 5, 10),
        "M7.5 (1:4:8)": (1, 4, 8),
        "M10 (1:3:6)": (1, 3, 6),
        "M15 (1:2:4)": (1, 2, 4),
        "M20 (1:1.5:3)": (1, 1.5, 3),
        "M25 (1:1:2)": (1, 1, 2),
        "M30 (1:0.75:1.5)": (1, 0.75, 1.5)
    }

    cement_p, sand_p, agg_p = ratio_dict[grade]
    total_parts = cement_p + sand_p + agg_p
    dry_volume = volume * 1.54

    cement_vol = (cement_p / total_parts) * dry_volume
    sand_vol = (sand_p / total_parts) * dry_volume
    agg_vol = (agg_p / total_parts) * dry_volume

    # Convert to kg
    cement_kg = cement_vol * 1440
    sand_kg = sand_vol * 1450
    agg_kg = agg_vol * 1500

    # Bag count
    cement_bags = cement_kg / 50

    st.subheader("📊 Mix Output:")
    st.success(f"Cement: **{cement_kg:.1f} kg**  (~{cement_bags:.1f} bags)")
    st.info(f"Sand: **{sand_kg:.1f} kg**")
    st.info(f"Aggregate: **{agg_kg:.1f} kg**")
    st.caption(f"Dry Volume Used: {dry_volume:.2f} m³")

    st.markdown(f"""
    ### ℹ️ Summary
    - Mix Ratio → {cement_p}:{sand_p}:{agg_p}  
    - Total Cement Bags → **{cement_bags:.1f}**  
    - Volume Input → {volume:.2f} m³ (Wet)  
    - Volume Output → {dry_volume:.2f} m³ (Dry)
    """)
