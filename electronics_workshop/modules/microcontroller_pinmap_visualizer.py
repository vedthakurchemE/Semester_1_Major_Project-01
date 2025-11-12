# modules/microcontroller_pinmap_visualizer.py

import streamlit as st
import pandas as pd

# Example: ATmega328P pinout
pin_data = [
    {"Pin": "D0",  "Function": "RX (UART)",     "Type": "Digital"},
    {"Pin": "D1",  "Function": "TX (UART)",     "Type": "Digital"},
    {"Pin": "D2",  "Function": "INT0",          "Type": "Digital"},
    {"Pin": "D3",  "Function": "PWM / INT1",    "Type": "Digital / PWM"},
    {"Pin": "D4",  "Function": "Digital I/O",   "Type": "Digital"},
    {"Pin": "D5",  "Function": "PWM",           "Type": "Digital / PWM"},
    {"Pin": "D6",  "Function": "PWM",           "Type": "Digital / PWM"},
    {"Pin": "D7",  "Function": "Digital I/O",   "Type": "Digital"},
    {"Pin": "D8",  "Function": "Digital I/O",   "Type": "Digital"},
    {"Pin": "D9",  "Function": "PWM",           "Type": "Digital / PWM"},
    {"Pin": "D10", "Function": "PWM / SS (SPI)", "Type": "Digital / SPI"},
    {"Pin": "D11", "Function": "PWM / MOSI",    "Type": "Digital / SPI"},
    {"Pin": "D12", "Function": "MISO",          "Type": "Digital / SPI"},
    {"Pin": "D13", "Function": "SCK / LED",     "Type": "Digital / SPI"},
    {"Pin": "A0",  "Function": "ADC0",          "Type": "Analog"},
    {"Pin": "A1",  "Function": "ADC1",          "Type": "Analog"},
    {"Pin": "A2",  "Function": "ADC2",          "Type": "Analog"},
    {"Pin": "A3",  "Function": "ADC3",          "Type": "Analog"},
    {"Pin": "A4",  "Function": "SDA",           "Type": "Analog / I2C"},
    {"Pin": "A5",  "Function": "SCL",           "Type": "Analog / I2C"}
]

def run():
    st.title("📍 Microcontroller Pin Mapping Visualizer")
    st.markdown("""
    View and explore the **pin configuration** of a typical microcontroller (e.g., ATmega328P).

    🧭 Great for beginners to understand:
    - Digital & analog pins
    - PWM functionality
    - UART, SPI, and I2C communication pins
    """)

    pin_df = pd.DataFrame(pin_data)

    st.dataframe(pin_df, use_container_width=True)

    st.subheader("🔎 Filter by Pin Type")
    pin_type = st.selectbox("Choose Type", ["All", "Digital", "Analog", "PWM", "SPI", "I2C", "UART"])

    if pin_type != "All":
        filtered = pin_df[pin_df["Type"].str.contains(pin_type)]
        st.dataframe(filtered, use_container_width=True)
    else:
        st.info("Showing all pins and their functions.")

    st.caption("📘 Based on standard ATmega328P (Arduino UNO) layout. You can extend to ESP32, STM32, etc.")
