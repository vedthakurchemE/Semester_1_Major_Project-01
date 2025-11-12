import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header("📈 Module 1: Population Growth Modeling (Logistic Model)")

    st.markdown("""
    This model uses the **logistic growth equation**:
    \n\n
    $$\\frac{dP}{dt} = rP\\left(1 - \\frac{P}{K}\\right)$$

    Where:
    - **P** is the population at time **t**
    - **r** is the growth rate
    - **K** is the carrying capacity
    - This equation accounts for limited resources
    """)

    # User Inputs
    r = st.slider("Growth Rate (r)", min_value=0.1, max_value=2.0, value=0.5, step=0.1)
    K = st.slider("Carrying Capacity (K)", min_value=500, max_value=10000, value=5000, step=100)
    P0 = st.slider("Initial Population (P₀)", min_value=10, max_value=1000, value=100, step=10)
    T = st.slider("Time Duration (T)", min_value=10, max_value=200, value=100, step=10)

    # Time points
    t = np.linspace(0, T, 1000)

    # Logistic Growth Equation
    P = K / (1 + ((K - P0) / P0) * np.exp(-r * t))

    # Plot
    fig, ax = plt.subplots()
    ax.plot(t, P, color='green', linewidth=2, label='Population P(t)')
    ax.axhline(K, linestyle='--', color='red', label='Carrying Capacity (K)')
    ax.set_xlabel("Time (t)")
    ax.set_ylabel("Population (P)")
    ax.set_title("Population vs Time")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    st.markdown(f"""
    **Observations**:
    - Population starts at {P0}
    - Approaches carrying capacity (K = {K}) over time
    - Controlled by growth rate r = {r}
    """)
