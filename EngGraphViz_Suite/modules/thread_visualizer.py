import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_metric_thread(ax, pitch=1.5, turns=5):
    x = np.linspace(0, turns * pitch, 1000)
    y = 0.5 * np.abs(np.mod(x, pitch) - pitch/2)
    ax.plot(x, y, label='Thread Profile')
    ax.set_title("Metric Thread (V-Profile)")
    ax.set_xlabel("Thread Length (mm)")
    ax.set_ylabel("Thread Height (mm)")

def plot_square_thread(ax, pitch=2, turns=5):
    x = []
    y = []
    height = 1
    for i in range(turns):
        base = i * pitch
        x += [base, base + pitch/2, base + pitch/2, base + pitch]
        y += [0, 0, height, height]
    ax.plot(x, y, label="Square Thread", color="green")
    ax.set_title("Square Thread")
    ax.set_xlabel("Length (mm)")
    ax.set_ylabel("Height (mm)")

def plot_acme_thread(ax, pitch=2, turns=5):
    x = []
    y = []
    height = 1
    for i in range(turns):
        base = i * pitch
        x += [base, base + pitch*0.25, base + pitch*0.5, base + pitch*0.75, base + pitch]
        y += [0, height, 0, height, 0]
    ax.plot(x, y, label="Acme Thread", color="purple")
    ax.set_title("ACME Thread (Trapezoidal)")
    ax.set_xlabel("Length (mm)")
    ax.set_ylabel("Height (mm)")

def run():
    st.title("🔩 Module 5: Thread Profile Visualizer")
    st.markdown("Visualize **mechanical thread profiles** used in fasteners and pipe connections.")

    thread_type = st.selectbox("🧵 Select Thread Type:", ["Metric (V-profile)", "Square", "ACME"])
    pitch = st.slider("📏 Thread Pitch (mm)", 1, 5, 2)
    turns = st.slider("🔁 Number of Thread Turns", 1, 10, 5)

    fig, ax = plt.subplots(figsize=(10, 3))

    if thread_type == "Metric (V-profile)":
        plot_metric_thread(ax, pitch, turns)
    elif thread_type == "Square":
        plot_square_thread(ax, pitch, turns)
    elif thread_type == "ACME":
        plot_acme_thread(ax, pitch, turns)

    ax.grid(True)
    st.pyplot(fig)
