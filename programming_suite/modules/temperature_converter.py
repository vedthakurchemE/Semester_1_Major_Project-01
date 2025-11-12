# modules/temperature_converter.py

import streamlit as st

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert from from_unit to Celsius
    if from_unit == "Fahrenheit":
        value = (value - 32) * 5 / 9
    elif from_unit == "Kelvin":
        value = value - 273.15

    # Convert from Celsius to to_unit
    if to_unit == "Fahrenheit":
        return value * 9 / 5 + 32
    elif to_unit == "Kelvin":
        return value + 273.15
    else:
        return value

def run():
    st.title("🌡️ Temperature Unit Converter")
    st.markdown("""
    Convert between **Celsius, Fahrenheit, and Kelvin** units in real time.

    ---
    💡 **Formulae**:
    - °F = (°C × 9/5) + 32  
    - °C = (°F − 32) × 5/9  
    - K = °C + 273.15
    """)

    units = ["Celsius", "Fahrenheit", "Kelvin"]
    col1, col2, col3 = st.columns(3)

    with col1:
        value = st.number_input("🌡️ Enter Temperature", value=25.0)

    with col2:
        from_unit = st.selectbox("From Unit", units)

    with col3:
        to_unit = st.selectbox("To Unit", units, index=1)

    if st.button("🔁 Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"✅ {value}° {from_unit} = **{round(result, 2)}° {to_unit}**")
