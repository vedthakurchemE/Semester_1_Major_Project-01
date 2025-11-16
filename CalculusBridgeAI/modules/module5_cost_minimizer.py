import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header("🏭 Module 5: Manufacturing Cost Minimizer")

    st.markdown(r"""
    Minimize the **total production cost**:

    \[
    C(q) = F + a \cdot q + \frac{b}{q}
    \]

    Where:
    - \( F \): fixed cost (₹)
    - \( a \): variable cost per item (₹)
    - \( b \): setup/maintenance cost component
    - \( q \): units produced

    Find the optimum \( q \) that minimizes cost.
    """)

    # Inputs
    F = st.slider("Fixed Cost (₹)", 1000, 100000, 20000, 1000)
    a = st.slider("Variable Cost per Item (a)", 1, 1000, 100)
    b = st.slider("Setup Cost Component (b)", 100, 100000, 50000, 1000)

    # Find minimum using calculus
    # C(q) = F + a*q + b/q --> dC/dq = a - b/q^2 = 0 --> q_opt = sqrt(b/a)
    try:
        q_opt = np.sqrt(b / a)
        min_cost = F + a * q_opt + b / q_opt
        valid = np.isfinite(q_opt) and q_opt > 0
    except Exception:
        q_opt, min_cost, valid = None, None, False

    # Display
    st.latex(r"C(q) = F + a \cdot q + \frac{b}{q}")
    st.latex(f"Optimal quantity: q^* = \\sqrt{{b/a}} = {q_opt:.2f}" if valid else "Could not compute optimal q.")
    if valid:
        st.success(f"✅ Optimal Quantity: q = {q_opt:.2f} units")
        st.info(f"💸 Minimum Total Cost: ₹{min_cost:.2f}")
    else:
        st.error("Could not compute minimum cost. Try different parameters.")

    # Plot
    q_vals = np.linspace(max(1, q_opt - 50), q_opt + 100 if valid else 1000, 500)
    cost_vals = F + a * q_vals + b / q_vals

    fig, ax = plt.subplots()
    ax.plot(q_vals, cost_vals, label="Total Cost C(q)", color="blue")
    if valid:
        ax.axvline(q_opt, color="red", linestyle="--", label=f"Optimal q ≈ {q_opt:.2f}")
    ax.set_xlabel("Quantity (q)")
    ax.set_ylabel("Cost (₹)")
    ax.set_title("Cost Minimization Curve")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    st.markdown("""
    **How to use:**  
    Find the most cost-efficient quantity to produce by balancing material, labor, and setup costs.
    """)
