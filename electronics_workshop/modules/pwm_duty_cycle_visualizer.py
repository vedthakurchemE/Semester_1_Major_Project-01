# modules/pwm_duty_cycle_visualizer.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def generate_pwm(frequency, duty_cycle, duration=0.02, sampling_rate=10000):
    t = np.linspace(0, duration, int(duration * sampling_rate))
    period = 1 / frequency
    pwm_signal = ((t % period) < (duty_cycle / 100) * period).astype(int)
    return t, pwm_signal

def run():
    st.title("🎛️ PWM Duty Cycle Visualizer")
    st.markdown("""
    Visualize the **PWM waveform** with adjustable **frequency** and **duty cycle**.

    🧠 Useful for:
    - LED brightness control
    - Motor speed modulation
    - Signal simulation
    """)

    st.subheader("⚙️ PWM Configuration")
    freq = st.slider("🧭 Frequency (Hz)", 10, 2000, 100)
    duty = st.slider("📉 Duty Cycle (%)", 0, 100, 50)
    duration = st.slider("🕒 Signal Duration (sec)", 0.005, 0.05, 0.02, step=0.005)

    t, pwm = generate_pwm(freq, duty, duration)

    st.divider()
    st.subheader("📊 PWM Waveform")
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.plot(t, pwm, color='purple', drawstyle='steps-pre')
    ax.set_ylim(-0.2, 1.2)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Voltage (V)")
    ax.set_title(f"PWM Signal @ {freq} Hz, {duty}% Duty Cycle")
    ax.grid(True)
    st.pyplot(fig)

    st.info(f"✅ One PWM cycle = {1/freq:.4f} sec | ON Time ≈ {(duty/100)*(1/freq):.4f} sec | OFF Time ≈ {(1-duty/100)*(1/freq):.4f} sec")
    st.caption("📘 PWM is widely used in microcontrollers like Arduino, ESP32, STM32 for controlling outputs.")
