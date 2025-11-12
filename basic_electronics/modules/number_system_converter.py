# modules/basic_electronics/number_system_converter.py

import streamlit as st

def convert_number(input_value, input_base):
    try:
        decimal_value = int(input_value, input_base)
        return {
            "Decimal": str(decimal_value),
            "Binary": bin(decimal_value)[2:],
            "Octal": oct(decimal_value)[2:],
            "Hexadecimal": hex(decimal_value)[2:].upper()
        }
    except Exception:
        return None

def run():
    st.title("🔢 Number System Converter")
    st.markdown("""
    Convert numbers between **Binary**, **Decimal**, **Octal**, and **Hexadecimal** systems.

    Useful in:
    - Digital electronics
    - Embedded systems
    - Computer architecture
    """)

    base_map = {
        "Decimal": 10,
        "Binary": 2,
        "Octal": 8,
        "Hexadecimal": 16
    }

    input_format = st.selectbox("📥 Input Number Format", list(base_map.keys()))
    input_value = st.text_input(f"Enter {input_format} Number")

    if input_value:
        result = convert_number(input_value.strip(), base_map[input_format])
        if result:
            st.subheader("🔄 Converted Values")
            for k, v in result.items():
                if k != input_format:
                    st.success(f"{k}: {v}")
        else:
            st.error("❌ Invalid input for the selected format.")
