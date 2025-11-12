# modules/loan_emi_calculator.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def calculate_emi(P, R, N):
    r = R / (12 * 100)  # monthly interest rate
    emi = (P * r * (1 + r) ** N) / ((1 + r) ** N - 1)
    return round(emi, 2)

def run():
    st.title("🏦 Loan EMI Calculator")
    st.markdown("""
    This app calculates the **Equated Monthly Installment (EMI)** for your loan based on principal, rate, and tenure.

    ---
    ### 📘 EMI Formula:
    \[
    EMI = \frac{P \cdot r \cdot (1 + r)^N}{(1 + r)^N - 1}
    \]
    Where:  
    - *P* = Loan Amount  
    - *r* = Monthly Interest Rate  
    - *N* = Number of Months
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        P = st.number_input("💰 Loan Amount (₹)", min_value=1000.0, step=1000.0, value=100000.0)
    with col2:
        R = st.number_input("📈 Annual Interest Rate (%)", min_value=0.1, step=0.1, value=8.0)
    with col3:
        Y = st.slider("🗓️ Loan Tenure (in Years)", 1, 30, 5)

    N = Y * 12  # total number of months
    emi = calculate_emi(P, R, N)
    total_payment = emi * N
    total_interest = total_payment - P

    if st.button("🧮 Calculate EMI"):
        st.success(f"📌 Monthly EMI: ₹{emi:,}")
        st.info(f"📊 Total Payment: ₹{total_payment:,.2f} | Interest: ₹{total_interest:,.2f}")

        # 📈 Pie chart for loan breakdown
        labels = ['Principal Amount', 'Total Interest']
        values = [P, total_interest]
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FFC107'])
        ax.axis('equal')
        st.pyplot(fig)

        st.caption("🔍 Note: EMI remains fixed while interest/principal ratio changes over time.")
