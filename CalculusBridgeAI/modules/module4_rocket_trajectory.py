import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def run():
    st.header("🚀 Module 4: Rocket Trajectory Analysis")

    st.markdown(r"""
    This simulation models a rocket launched vertically under thrust, then decelerated by gravity.

    ### Phase 1: Powered Ascent
    \[
    a(t) = \frac{F - mg}{m}
    \]

    ### Phase 2: Free Fall (after engine cutoff)
    \[
    a(t) = -g
    \]

    We calculate:
    - Height vs time: \( s(t) \)
    - Velocity vs time: \( v(t) \)
    - Acceleration vs time: \( a(t) \)

    using integration and piecewise motion equations.
    """)

    # Inputs
    mass = st.slider("Rocket Mass (kg)", 100, 5000, 1000, 100)
    thrust = st.slider("Thrust Force (N)", 1000, 100000, 30000, 1000)
    burn_time = st.slider("Engine Burn Time (s)", 1, 120, 30)
    total_time = st.slider("Total Simulation Time (s)", burn_time + 5, 200, 60)
    g = 9.81  # Gravity (m/s^2)

    # Time array
    t = np.linspace(0, total_time, 1000)
    a = np.piecewise(t,
                     [t <= burn_time, t > burn_time],
                     [lambda t: (thrust - mass * g) / mass, -g]
                     )

    # Integration to get velocity and height
    v = np.cumsum(a) * (t[1] - t[0])
    s = np.cumsum(v) * (t[1] - t[0])

    # Plots
    fig, axs = plt.subplots(3, 1, figsize=(8, 9))
    axs[0].plot(t, a, color='red')
    axs[0].set_ylabel("Acceleration (m/s²)")
    axs[0].grid(True)
    axs[0].axvline(burn_time, color='gray', linestyle='--', label="Engine Cutoff")
    axs[0].legend()

    axs[1].plot(t, v, color='blue')
    axs[1].set_ylabel("Velocity (m/s)")
    axs[1].grid(True)
    axs[1].axvline(burn_time, color='gray', linestyle='--')

    axs[2].plot(t, s, color='green')
    axs[2].set_ylabel("Height (m)")
    axs[2].set_xlabel("Time (s)")
    axs[2].grid(True)
    axs[2].axvline(burn_time, color='gray', linestyle='--')

    fig.suptitle("Rocket Trajectory Simulation")
    st.pyplot(fig)

    max_height = np.max(s)
    st.success(f"🚀 Maximum Height Achieved: {max_height:.2f} meters")

    st.markdown("""
    **Insights**:
    - Increase thrust or burn time to gain more altitude.
    - Observe how gravity takes over after engine cutoff.
    """)
