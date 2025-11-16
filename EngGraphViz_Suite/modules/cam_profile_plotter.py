import streamlit as st
import numpy as np
import plotly.graph_objects as go

def uniform_motion(theta, h):
    return h * theta / np.max(theta)

def shm_motion(theta, h):
    return h * (1 - np.cos(np.pi * theta / np.max(theta))) / 2

def cycloidal_motion(theta, h):
    return h * (theta / np.max(theta) - (1 / (2 * np.pi)) * np.sin(2 * np.pi * theta / np.max(theta)))

def run():
    st.title("📘 Module 7: Cam Profile Plotter")
    st.markdown("Visualize **displacement diagrams** for cam-follower systems based on motion laws.")

    motion_type = st.selectbox("📈 Select Follower Motion", ["Uniform", "Simple Harmonic (SHM)", "Cycloidal"])
    total_angle = st.slider("🔁 Cam Rotation Angle (degrees)", 90, 360, 180)
    h = st.slider("📏 Total Lift/Displacement (mm)", 10, 100, 50)

    theta = np.linspace(0, total_angle, 500)
    if motion_type == "Uniform":
        y = uniform_motion(theta, h)
        eq = r"s = h \cdot \theta / \theta_{max}"
    elif motion_type == "Simple Harmonic (SHM)":
        y = shm_motion(theta, h)
        eq = r"s = \frac{h}{2}(1 - \cos(\pi \theta / \theta_{max}))"
    elif motion_type == "Cycloidal":
        y = cycloidal_motion(theta, h)
        eq = r"s = h \left(\frac{\theta}{\theta_{max}} - \frac{1}{2\pi}\sin\left(2\pi \frac{\theta}{\theta_{max}}\right)\right)"

    # Plot with Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=theta, y=y, mode='lines', name='Displacement', line=dict(color='royalblue')))
    fig.add_trace(go.Scatter(x=theta, y=y, fill='tozeroy', mode='none', name='Area'))
    fig.update_layout(
        title=f"{motion_type} Displacement Diagram",
        xaxis_title="Cam Angle (°)",
        yaxis_title="Follower Displacement (mm)",
        template='plotly_white',
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("📘 Motion Law Equation"):
        st.markdown(f"**{motion_type} Law Equation:**")
        st.latex(eq)
