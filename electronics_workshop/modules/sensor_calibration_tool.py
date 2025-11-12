# modules/sensor_calibration_tool.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def map_voltage_to_unit(voltage, v_min, v_max, u_min, u_max):
    return u_min + (voltage - v_min) * (u_max - u_min) / (v_max - v_min)

def run():
    st.title("🧪 Sensor Calibration Tool")
    st.markdown("""
    Convert **raw voltage readings (0–5V)** from analog sensors to calibrated real-world units (like °C, ppm, Lux, etc.).

    Formula (Linear Mapping):

    \n\n`Calibrated Value = Umin + (V - Vmin) × (Umax - Umin) / (Vmax - Vmin)`
    """)

    st.subheader("📟 Sensor Voltage Range")
    v_min = st.number_input("🔻 Minimum Sensor Voltage (V)", 0.0, 5.0, 0.5, step=0.1)
    v_max = st.number_input("🔺 Maximum Sensor Voltage (V)", 0.1, 5.0, 4.5, step=0.1)

    st.subheader("📏 Calibrated Unit Range")
    u_min = st.number_input("📉 Minimum Calibrated Value (e.g., 0°C)", -100.0, 1000.0, 0.0, step=1.0)
    u_max = st.number_input("📈 Maximum Calibrated Value (e.g., 100°C)", -100.0, 1000.0, 100.0, step=1.0)

    st.subheader("📥 Enter Sensor Voltage Reading (V)")
    voltage = st.slider("Sensor Output Voltage", v_min, v_max, (v_min + v_max) / 2)

    calibrated = map_voltage_to_unit(voltage, v_min, v_max, u_min, u_max)

    st.success(f"📊 Calibrated Value = **{calibrated:.2f} units**")

    st.divider()
    st.subheader("📈 Voltage to Calibrated Value Curve")
    voltages = np.linspace(v_min, v_max, 100)
    values = map_voltage_to_unit(voltages, v_min, v_max, u_min, u_max)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(voltages, values, color='darkgreen')
    ax.set_xlabel("Voltage (V)")
    ax.set_ylabel("Calibrated Unit")
    ax.set_title("Sensor Calibration Mapping")
    ax.grid(True)
    st.pyplot(fig)

    st.caption("📘 Example: TMP36 sensor outputs 0.5V to 1.5V for 0°C to 100°C.")
