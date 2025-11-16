# modules/basic_electronics/ac_waveform_analyzer.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def generate_waveform(wave_type, freq, amplitude, time):
    if wave_type == "Sine":
        return amplitude * np.sin(2 * np.pi * freq * time)
    elif wave_type == "Square":
        return amplitude * signal.square(2 * np.pi * freq * time)
    elif wave_type == "Triangle":
        return amplitude * signal.sawtooth(2 * np.pi * freq * time, 0.5)
    else:
        return np.zeros_like(time)

def run():
    st.title("🌊 AC Waveform Analyzer")
    st.markdown("""
    Analyze and visualize different **AC waveforms**:

    - 📈 Sine wave  
    - 🔳 Square wave  
    - 🔺 Triangle wave  

    Useful in analog signal design, power systems, and electronics labs.
    """)

    wave_type = st.selectbox("🔄 Select Waveform Type", ["Sine", "Square", "Triangle"])
    amplitude = st.slider("🔊 Amplitude (V)", 1.0, 10.0, 5.0)
    freq = st.slider("⏱️ Frequency (Hz)", 1, 1000, 50)
    duration = st.slider("⏱️ Duration (ms)", 1, 50, 10) / 1000  # convert to seconds

    time = np.linspace(0, duration, 1000)
    waveform = generate_waveform(wave_type, freq, amplitude, time)

    rms = np.sqrt(np.mean(waveform ** 2))
    peak = np.max(np.abs(waveform))

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(time * 1000, waveform, color='teal', label=f"{wave_type} Wave")
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Voltage (V)")
    ax.set_title(f"{wave_type} Waveform")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
    st.video('https://www.youtube.com/watch?v=G_ZHz3CPUb8')
    st.success(f"📌 RMS Value: **{rms:.2f} V**")
    st.success(f"📌 Peak Voltage: **{peak:.2f} V**")
