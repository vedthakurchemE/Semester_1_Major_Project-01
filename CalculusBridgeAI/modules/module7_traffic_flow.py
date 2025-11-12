import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header("🚦 Module 7: Traffic Flow Optimization")

    st.markdown(r"""
    This module models **vehicle traffic density** over time using calculus principles.

    ### Traffic Flow Equation:
    \[
    Q(t) = k(t) \cdot v(t)
    \]
    Where:
    - \( Q(t) \): flow rate (vehicles/hour)
    - \( k(t) \): vehicle density (vehicles/km)
    - \( v(t) \): average speed (km/h)

    We explore how traffic congestion develops and how density affects flow rate.
    """)

    st.subheader("Choose Traffic Scenario")
    scenario = st.selectbox("Traffic Pattern", [
        "Rush Hour Jam",
        "Smooth Highway",
        "Construction Zone Slowdown",
        "Custom Flow"
    ])

    T = st.slider("Simulation Duration (hours)", 1, 12, 4)
    t = np.linspace(0, T, 500)

    if scenario == "Rush Hour Jam":
        k = 100 + 50 * np.sin(2 * np.pi * t / T)
        v = 60 - 30 * np.sin(2 * np.pi * t / T)
    elif scenario == "Smooth Highway":
        k = 20 + 5 * np.sin(2 * np.pi * t / T)
        v = 100 - 10 * np.sin(2 * np.pi * t / T)
    elif scenario == "Construction Zone Slowdown":
        k = 80 + 20 * np.exp(-t)
        v = 40 - 10 * np.exp(-t)
    elif scenario == "Custom Flow":
        base_k = st.slider("Base Vehicle Density (vehicles/km)", 10, 150, 50)
        amp_k = st.slider("Density Amplitude", 0, 100, 30)
        base_v = st.slider("Base Speed (km/h)", 20, 120, 60)
        amp_v = st.slider("Speed Drop Amplitude", 0, 60, 20)
        k = base_k + amp_k * np.sin(2 * np.pi * t / T)
        v = base_v - amp_v * np.sin(2 * np.pi * t / T)

    Q = k * v

    fig, ax = plt.subplots(3, 1, figsize=(8, 9), sharex=True)
    ax[0].plot(t, k, label="Density k(t)", color="darkred")
    ax[0].set_ylabel("vehicles/km")
    ax[0].legend()
    ax[0].grid(True)

    ax[1].plot(t, v, label="Speed v(t)", color="navy")
    ax[1].set_ylabel("km/h")
    ax[1].legend()
    ax[1].grid(True)

    ax[2].plot(t, Q, label="Flow Rate Q(t)", color="green")
    ax[2].set_ylabel("vehicles/hour")
    ax[2].set_xlabel("Time (hours)")
    ax[2].legend()
    ax[2].grid(True)

    st.pyplot(fig)

    st.success(f"📈 Max Flow Rate: {np.max(Q):.2f} vehicles/hour")
    st.info(f"🧮 Average Traffic Density: {np.mean(k):.2f} vehicles/km")
