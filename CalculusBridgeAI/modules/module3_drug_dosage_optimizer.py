import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def run():
    st.header("💊 Module 3: Drug Dosage Optimization")

    st.markdown(r"""
    This model uses **exponential decay** to simulate drug concentration in the bloodstream:

    \[
    C(t) = C_0 e^{-kt}
    \]

    Where:
    - \( C(t) \): drug concentration at time \( t \)
    - \( C_0 \): initial dose (mg)
    - \( k \): elimination rate constant
    - \( t \): time (hours)

    We optimize **dosage frequency** so that concentration stays between therapeutic limits.
    """)

    # User Inputs
    C0 = st.slider("Initial Dose (C₀ in mg)", min_value=50, max_value=1000, value=300, step=10)
    k = st.slider("Elimination Rate Constant (k)", min_value=0.01, max_value=1.0, value=0.15, step=0.01)
    T = st.slider("Time Duration (hours)", min_value=6, max_value=72, value=24, step=1)
    dose_interval = st.slider("Dose Interval (hours)", min_value=2, max_value=24, value=8, step=1)

    therapeutic_min = st.number_input("Minimum Therapeutic Concentration (mg)", value=50.0)
    therapeutic_max = st.number_input("Maximum Safe Concentration (mg)", value=500.0)

    time = np.linspace(0, T, 1000)
    concentration = np.zeros_like(time)

    # Repeated Dosing Model: Add decaying doses every dose_interval
    for t_dose in range(0, T, dose_interval):
        concentration += C0 * np.exp(-k * (time - t_dose)) * (time >= t_dose)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(time, concentration, label="Drug Concentration C(t)", color="purple")
    ax.axhline(therapeutic_min, color="green", linestyle="--", label="Min Therapeutic")
    ax.axhline(therapeutic_max, color="red", linestyle="--", label="Max Safe")
    ax.set_xlabel("Time (hours)")
    ax.set_ylabel("Concentration (mg)")
    ax.set_title("Drug Level Over Time with Repeated Doses")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    # Evaluate Safety and Effectiveness
    if np.all((concentration >= therapeutic_min) & (concentration <= therapeutic_max)):
        st.success("✅ Drug concentration stays within therapeutic range for entire duration.")
    else:
        st.warning("⚠️ Concentration goes outside therapeutic range. Adjust dosage or interval.")

    st.markdown("""
    **Tips**:
    - Reduce `Dose Interval` if drug falls below minimum too early.
    - Lower `C₀` if concentration exceeds the safe limit.
    - Tune `k` based on actual metabolism data for better prediction.
    """)
