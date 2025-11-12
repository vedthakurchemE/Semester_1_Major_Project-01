# modules/bridge_rectifier_simulator.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def generate_rectified_wave(frequency, amplitude, duration, sample_rate, with_filter=False, capacitance=1e-6, load=1e3):
    t = np.linspace(0, duration, int(sample_rate * duration))
    input_wave = amplitude * np.sin(2 * np.pi * frequency * t)
    output_wave = np.abs(input_wave)

    if with_filter:
        dt = 1 / sample_rate
        rc = load * capacitance
        filtered = np.zeros_like(output_wave)
        for i in range(1, len(output_wave)):
            filtered[i] = filtered[i-1] + (dt / rc) * (output_wave[i] - filtered[i-1])
        return t, input_wave, filtered
    return t, input_wave, output_wave

def run():
    st.title("🔌 Bridge Rectifier Output Simulator")
    st.markdown("""
    Visualize a **full-wave bridge rectifier** circuit's output waveform  
    with or without a **capacitor filter**.

    **Includes:**
    - AC Input waveform
    - Rectified Output waveform
    - Optional Capacitor Filtering (for ripple smoothing)
    """)

    col1, col2 = st.columns(2)
    with col1:
        freq = st.slider("⚡ Input Frequency (Hz)", 10, 100, 50)
        amp = st.slider("🔋 Input Amplitude (V)", 1, 20, 5)
        duration = st.slider("⏱️ Duration (s)", 0.01, 0.1, 0.05)
    with col2:
        sample_rate = st.slider("🎛️ Sample Rate", 500, 5000, 1000)
        use_filter = st.checkbox("🔧 Add Capacitor Filter", value=True)
        if use_filter:
            cap_uF = st.slider("🔋 Capacitance (µF)", 1, 1000, 100)
            resistance = st.slider("🧱 Load Resistance (Ω)", 100, 10000, 1000)
            cap = cap_uF * 1e-6
        else:
            cap = 1e-9
            resistance = 1e3

    t, input_wave, output_wave = generate_rectified_wave(
        frequency=freq,
        amplitude=amp,
        duration=duration,
        sample_rate=sample_rate,
        with_filter=use_filter,
        capacitance=cap,
        load=resistance
    )

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t * 1000, input_wave, label="AC Input", linestyle="--", color="gray")
    ax.plot(t * 1000, output_wave, label="Rectified Output", color="red")
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Voltage (V)")
    ax.set_title("Bridge Rectifier Output")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    if use_filter:
        st.success("✅ Filter capacitor applied to reduce ripple.")
    else:
        st.warning("⚠️ No filter applied — waveform is unfiltered full-wave rectification.")
