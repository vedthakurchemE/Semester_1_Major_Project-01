# modules/raspberry_pi_gpio_tester.py

import streamlit as st

# Default GPIO pins (BCM mode) for simulation
GPIO_PINS = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26]

def run():
    st.title("🧪 Raspberry Pi GPIO Tester")
    st.markdown("""
    Simulate the **Raspberry Pi GPIO pin toggling** in BCM mode.

    - Toggle pins ON or OFF
    - View real-time pin status
    - Educational simulator (no hardware needed)
    """)

    st.info("📌 This simulation assumes BCM pin numbering for Raspberry Pi 3/4.")

    pin_states = {}
    col1, col2, col3, col4 = st.columns(4)

    cols = [col1, col2, col3, col4]
    for i, pin in enumerate(GPIO_PINS):
        with cols[i % 4]:
            state = st.toggle(f"GPIO {pin}", key=f"gpio_{pin}")
            pin_states[pin] = "HIGH" if state else "LOW"

    st.divider()
    st.subheader("📊 GPIO Status Table")

    st.table({
        "GPIO Pin": GPIO_PINS,
        "State": [pin_states[pin] for pin in GPIO_PINS]
    })
    st.video('https://www.youtube.com/watch?v=huaE9WPXyX4')
    st.caption("💡 Real Raspberry Pi GPIO pins can be controlled using `RPi.GPIO` or `gpiozero` in Python.")
