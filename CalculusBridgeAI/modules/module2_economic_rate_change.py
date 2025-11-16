import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def run():
    st.header("💰 Module 2: Economic Rate of Change (Marginal Analysis)")

    st.markdown(r"""
    Use numeric methods for **marginal cost**, **marginal revenue**, and **profit maximization**:
    - **Marginal Cost (MC):** derivative of \( C(q) \)
    - **Marginal Revenue (MR):** derivative of \( R(q) \)
    - **Profit Maximization:** Find where MR = MC
    """)

    st.subheader("Define Parameters")
    a_cost = st.slider("Cost: Linear Coefficient (a)", 0.1, 50.0, 5.0)
    b_cost = st.slider("Cost: Quadratic Coefficient (b)", 0.0, 0.1, 0.01)
    fixed_cost = st.slider("Fixed Cost", 0, 500, 100)
    a_rev = st.slider("Revenue: Per Unit (a)", 0.1, 50.0, 10.0)

    # Quantity range
    q_vals = np.linspace(1, 300, 500)
    C_vals = a_cost * q_vals + b_cost * q_vals ** 2 + fixed_cost
    R_vals = a_rev * q_vals
    MC_vals = np.gradient(C_vals, q_vals)
    MR_vals = np.gradient(R_vals, q_vals)
    Profit_vals = R_vals - C_vals

    # Find optimal quantity (MR ≈ MC)
    diff = np.abs(MC_vals - MR_vals)
    idx_opt = np.argmin(diff)
    q_opt = q_vals[idx_opt]
    profit_at_opt = Profit_vals[idx_opt]

    # Display functions
    st.latex(r"C(q) = a\,q + b\,q^2 + \text{fixed}")
    st.latex(r"R(q) = a_{rev}\,q")
    st.latex(r"MC = \frac{dC}{dq}")
    st.latex(r"MR = \frac{dR}{dq}")
    st.latex(r"\text{Profit} = R(q) - C(q)")

    # Plot
    fig, ax = plt.subplots()
    ax.plot(q_vals, C_vals, label="Cost C(q)", color="red")
    ax.plot(q_vals, R_vals, label="Revenue R(q)", color="green")
    ax.plot(q_vals, MC_vals, "--", label="Marginal Cost", color="orange")
    ax.plot(q_vals, MR_vals, "--", label="Marginal Revenue", color="blue")
    ax.axvline(q_opt, color="purple", linestyle="--", label=f"MR=MC @ q ≈ {q_opt:.1f}")
    ax.set_xlabel("Quantity q")
    ax.set_ylabel("Amount")
    ax.set_title("Cost, Revenue & Marginal Analysis")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    # Show optimal results
    st.success(f"📌 Maximum Profit when q ≈ {q_opt:.1f} (MR ≈ MC)")
    st.info(f"💹 Maximum Profit: ₹{profit_at_opt:.2f},  Revenue: ₹{R_vals[idx_opt]:.2f},  Cost: ₹{C_vals[idx_opt]:.2f}")

    st.markdown("""
    **How to use:**  
    Adjust cost and revenue parameters to optimize production for maximum profit.
    """)
