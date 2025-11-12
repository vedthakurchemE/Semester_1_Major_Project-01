import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def run():
    st.header("💰 Module 2: Economic Rate of Change (Marginal Analysis)")

    st.markdown(r"""
    Analyze cost and revenue functions using **calculus**:

    - **Marginal Cost (MC)**: \( \frac{dC}{dq} \)
    - **Marginal Revenue (MR)**: \( \frac{dR}{dq} \)
    - **Profit Maximization**: Solve where MR = MC
    """)

    st.subheader("Define Functions")
    cost_expr_str = st.text_input("Cost Function C(q)", value="5*q + 0.01*q**2 + 100")
    revenue_expr_str = st.text_input("Revenue Function R(q)", value="10*q")

    q = sp.Symbol('q')
    try:
        C = sp.sympify(cost_expr_str)
        R = sp.sympify(revenue_expr_str)
    except:
        st.error("❌ Invalid expression. Please use 'q' as the variable.")
        return

    # Derivatives
    MC = sp.diff(C, q)
    MR = sp.diff(R, q)
    Profit = R - C

    # Display formulas
    st.latex(f"C(q) = {sp.latex(C)}")
    st.latex(f"R(q) = {sp.latex(R)}")
    st.latex(f"\\text{{Marginal Cost}} = {sp.latex(MC)}")
    st.latex(f"\\text{{Marginal Revenue}} = {sp.latex(MR)}")
    st.latex(f"\\text{{Profit}} = R(q) - C(q) = {sp.latex(Profit)}")

    st.subheader("📊 Plot and Analyze")

    q_vals = np.linspace(0, 300, 500)

    # Convert symbolic expressions to numerical functions
    C_func = sp.lambdify(q, C, modules=["numpy"])
    R_func = sp.lambdify(q, R, modules=["numpy"])
    MC_func = sp.lambdify(q, MC, modules=["numpy"])
    MR_func = sp.lambdify(q, MR, modules=["numpy"])

    # Force element-wise evaluation
    C_func = np.vectorize(C_func)
    R_func = np.vectorize(R_func)
    MC_func = np.vectorize(MC_func)
    MR_func = np.vectorize(MR_func)

    # Evaluate all functions
    C_vals = C_func(q_vals)
    R_vals = R_func(q_vals)
    MC_vals = MC_func(q_vals)
    MR_vals = MR_func(q_vals)

    # Plotting
    fig, ax = plt.subplots()
    ax.plot(q_vals, C_vals, label="Cost C(q)", color='red')
    ax.plot(q_vals, R_vals, label="Revenue R(q)", color='green')
    ax.plot(q_vals, MR_vals, '--', label="Marginal Revenue", color='blue')
    ax.plot(q_vals, MC_vals, '--', label="Marginal Cost", color='orange')
    ax.set_xlabel("Quantity q")
    ax.set_ylabel("Amount")
    ax.set_title("Cost, Revenue & Marginal Analysis")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    # Solving MR = MC
    try:
        q_opt = sp.solve(MC - MR, q)
        q_opt_val = [float(val.evalf()) for val in q_opt if val.is_real and val >= 0]
        if q_opt_val:
            st.success(f"📌 Optimal Quantity (MR = MC): q = {q_opt_val[0]:.2f}")
        else:
            st.warning("⚠️ No valid real solution for MR = MC.")
    except Exception as e:
        st.warning(f"❌ Unable to solve MR = MC.\nError: {str(e)}")

    st.info("Use this module to optimize production, price strategy, and profit margins.")
