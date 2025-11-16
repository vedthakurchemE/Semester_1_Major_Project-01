import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header("🏭 Module 5: Manufacturing Cost Optimization")
    st.markdown(r"""
    We minimize the **total production cost function** using calculus.

    ### Cost Function:
    \[
    C(q) = F + a \cdot q + \frac{b}{q}
    \]
    Where:
    - \( F \): fixed cost (in ₹)
    - \( a \): variable cost per item (in ₹)
    - \( b \): setup/maintenance cost component
    - \( q \): number of units produced

    We use differentiation to find the quantity \( q \) that **minimizes** the cost.
    """)

    # Inputs
    F = st.slider("Fixed Cost (₹)", min_value=1000, max_value=100000, value=20000, step=1000)
    a = st.slider("Cost per Item (a)", min_value=1, max_value=1000, value=100, step=10)
    b = st.slider("Setup Cost Component (b)", min_value=100, max_value=100000, value=50000, step=1000)

    q = sp.Symbol('q', positive=True)
    C_expr = F + a * q + b / q
    dC = sp.diff(C_expr, q)
    d2C = sp.diff(dC, q)

    # Solve for minimum
    try:
        q_opt = sp.solve(dC, q)
        q_min_val = float(q_opt[0].evalf()) if q_opt else None
    except:
        q_min_val = None

    st.latex(f"C(q) = {sp.latex(C_expr)}")
    st.latex(f"\\frac{{dC}}{{dq}} = {sp.latex(dC)}")
    st.latex(f"\\text{{Second Derivative }} \\frac{{d^2C}}{{dq^2}} = {sp.latex(d2C)}")

    if q_min_val and q_min_val > 0:
        st.success(f"✅ Optimal Quantity to Minimize Cost: q = {q_min_val:.2f} units")
        min_cost = F + a * q_min_val + b / q_min_val
        st.info(f"💸 Minimum Total Cost: ₹{min_cost:.2f}")
    else:
        st.error("Could not compute minimum cost. Try different parameters.")

    # Plotting
    q_vals = np.linspace(1, 2 * q_min_val if q_min_val else 1000, 500)
    C_func = sp.lambdify(q, C_expr, 'numpy')
    C_vals = C_func(q_vals)

    fig, ax = plt.subplots()
    ax.plot(q_vals, C_vals, label="Total Cost C(q)", color="blue")
    if q_min_val:
        ax.axvline(q_min_val, color="red", linestyle="--", label=f"Optimal q ≈ {q_min_val:.2f}")
    ax.set_xlabel("Quantity (q)")
    ax.set_ylabel("Cost (₹)")
    ax.set_title("Cost Minimization Curve")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    st.markdown("""
    **Use Case:**  
    Determine how many units to produce to achieve minimal manufacturing cost by balancing material, labor, and setup cost trade-offs.
    """)
