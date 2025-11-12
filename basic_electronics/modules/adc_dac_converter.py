# modules/basic_electronics/adc_dac_converter.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def adc_conversion(analog_voltage, v_ref, bits):
    max_digital = 2**bits - 1
    digital_output = int((analog_voltage / v_ref) * max_digital)
    return digital_output

def dac_conversion(digital_value, v_ref, bits):
    max_digital = 2**bits - 1
    analog_output = (digital_value / max_digital) * v_ref
    return analog_output

def run():
    st.title("🔄 ADC & DAC Converter Tool")
    st.markdown("""
    Simulate **Analog-to-Digital** and **Digital-to-Analog** conversions.

    ---
    **Formulas**:
    - ADC Output = \( \\left(\\frac{V_{in}}{V_{ref}}\\right) \\times (2^n - 1) \)
    - DAC Output = \( \\left(\\frac{Digital}{2^n - 1}\\right) \\times V_{ref} \)
    ---
    """)

    bits = st.slider("📊 Resolution (Bits)", 4, 16, 8)
    v_ref = st.slider("🔌 Reference Voltage (V)", 1.0, 10.0, 5.0)

    st.subheader("📥 Analog to Digital (ADC)")
    vin = st.number_input("Input Analog Voltage (V)", min_value=0.0, max_value=v_ref, step=0.1)
    digital = adc_conversion(vin, v_ref, bits)
    st.success(f"🔢 ADC Output: **{digital}** (out of {2**bits - 1})")

    st.subheader("📤 Digital to Analog (DAC)")
    dval = st.slider("Digital Input Value", 0, 2**bits - 1, digital)
    vout = dac_conversion(dval, v_ref, bits)
    st.success(f"🔁 DAC Output Voltage: **{vout:.2f} V**")

    st.markdown("### 📈 Resolution Effect on DAC Output")
    digital_range = np.arange(0, 2**bits)
    analog_range = dac_conversion(digital_range, v_ref, bits)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.step(digital_range, analog_range, where='mid', color='blue')
    ax.set_xlabel("Digital Value")
    ax.set_ylabel("Analog Voltage (V)")
    ax.set_title("DAC Output vs Digital Input")
    ax.grid(True)
    st.pyplot(fig)
