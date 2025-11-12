# optical_fiber_visualizer.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calc_acceptance_angle(n1, n2):
    NA = np.sqrt(n1**2 - n2**2)
    theta_accept_rad = np.arcsin(NA / n1)
    return np.degrees(theta_accept_rad), NA

def run():
    st.markdown("<h1 style='text-align: center;'>🌐 Optical Fiber Visualizer</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>🔦 Simulate Total Internal Reflection & Acceptance Angle</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # Sidebar inputs
    st.sidebar.header("🧪 Fiber Parameters")
    n1 = st.sidebar.slider("Core Refractive Index (n₁)", 1.4, 1.6, 1.5, step=0.01)
    n2 = st.sidebar.slider("Cladding Refractive Index (n₂)", 1.2, 1.49, 1.45, step=0.01)
    angle_in = st.sidebar.slider("Ray Entry Angle (°)", 0.0, 90.0, 20.0, step=1.0)

    # Calculations
    if n2 >= n1:
        st.error("Cladding index must be less than core index for total internal reflection.")
        return

    critical_angle = np.degrees(np.arcsin(n2 / n1))
    acceptance_angle, NA = calc_acceptance_angle(n1, n2)

    # Ray analysis
    accepted = angle_in <= acceptance_angle

    # Plot setup
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.set_title("Ray Propagation in Optical Fiber")
    ax.set_xlabel("Distance →")
    ax.set_ylabel("Height")

    # Draw core boundaries
    ax.axhline(y=1, color='black', linestyle='--')
    ax.axhline(y=-1, color='black', linestyle='--')
    ax.fill_between([0, 10], -1, 1, color='lightblue', alpha=0.3, label="Core")

    # Draw ray path
    if accepted:
        x, y = [0], [0]
        direction = np.tan(np.radians(angle_in))
        x0, y0 = 0, 0
        for i in range(8):
            x1 = x0 + 1.2
            y1 = y0 + direction * 1.2
            if abs(y1) > 1:
                direction *= -1
                y1 = y0 + direction * 1.2
            x.append(x1)
            y.append(y1)
            x0, y0 = x1, y1
        ax.plot(x, y, color='red', lw=2, label="Accepted Ray")
    else:
        ax.plot([0, 2], [0, np.tan(np.radians(angle_in)) * 2], 'gray', lw=2, label="Lost Ray")

    ax.legend()
    st.pyplot(fig)

    # Output results
    st.subheader("📊 Analysis")
    st.markdown(f"- **Critical Angle (Core→Cladding):** {critical_angle:.2f}°")
    st.markdown(f"- **Acceptance Angle:** {acceptance_angle:.2f}°")
    st.markdown(f"- **Numerical Aperture (NA):** {NA:.3f}")
    if accepted:
        st.success("✅ Ray is accepted and propagates via total internal reflection.")
    else:
        st.error("❌ Ray exceeds acceptance angle and is lost.")
