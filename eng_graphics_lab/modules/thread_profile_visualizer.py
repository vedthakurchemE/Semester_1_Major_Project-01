# modules/thread_profile_visualizer.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def iso_thread(x, pitch, d):
    y = (pitch / 2) * (1 - np.abs((x % pitch - pitch / 2) / (pitch / 2)))
    return y

def square_thread(x, pitch, d):
    y = np.where((x % pitch) < pitch / 2, pitch / 2, 0)
    return y

def trapezoidal_thread(x, pitch, d):
    rise = pitch * 0.3
    run = pitch / 2
    y = rise * (1 - np.abs((x % pitch - run) / run))
    return y

def run():
    st.title("🔩 Thread Profile Visualizer")
    st.markdown("""
    Visualize **mechanical threads** with selectable profiles: *ISO Metric*, *Square*, and *Trapezoidal*.

    Adjust thread pitch and major diameter to generate the 2D thread form.
    """)

    thread_type = st.selectbox("🧵 Thread Type", ["ISO Metric", "Square", "Trapezoidal"])
    pitch = st.slider("Thread Pitch (mm)", 1, 10, 2)
    d = st.slider("Major Diameter (mm)", 5, 50, 20)
    turns = st.slider("Thread Turns", 5, 20, 10)

    x = np.linspace(0, pitch * turns, 1000)

    if thread_type == "ISO Metric":
        y = iso_thread(x, pitch, d)
    elif thread_type == "Square":
        y = square_thread(x, pitch, d)
    elif thread_type == "Trapezoidal":
        y = trapezoidal_thread(x, pitch, d)

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(x, y, color="black", label="Thread Profile")
    ax.set_title(f"{thread_type} Thread Profile")
    ax.set_xlabel("Thread Length (mm)")
    ax.set_ylabel("Profile Height (mm)")
    ax.set_ylim(0, pitch)
    ax.grid(True)
    st.pyplot(fig)

    st.info("🔧 This visual helps in **drawing correct thread shapes** for bolts, nuts, shafts in CAD or hand sketching.")
