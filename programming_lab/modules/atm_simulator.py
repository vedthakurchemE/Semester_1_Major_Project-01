# atm_banking_simulator.py
import streamlit as st
from datetime import datetime

def run():
    st.title("🏦 ATM Banking Simulator with Transaction History")

    # Initialize session state variables
    if "balance" not in st.session_state:
        st.session_state.balance = 5000  # Starting balance
    if "transactions" not in st.session_state:
        st.session_state.transactions = []  # List to store transaction history

    st.write(f"💰 **Current Balance:** ₹{st.session_state.balance}")

    # Operation selection
    operation = st.selectbox(
        "Select an operation",
        ["Withdraw", "Deposit", "Check Balance", "View Transaction History"]
    )

    if operation == "Withdraw":
        amount = st.number_input("Enter withdrawal amount", min_value=1, step=100)
        if st.button("Withdraw"):
            if amount <= st.session_state.balance:
                st.session_state.balance -= amount
                # Add to history
                st.session_state.transactions.append({
                    "Type": "Withdrawal",
                    "Amount": amount,
                    "Balance": st.session_state.balance,
                    "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                st.success(f"✅ Withdrawn ₹{amount}. New balance: ₹{st.session_state.balance}")
            else:
                st.error("❌ Insufficient balance.")

    elif operation == "Deposit":
        amount = st.number_input("Enter deposit amount", min_value=1, step=100)
        if st.button("Deposit"):
            st.session_state.balance += amount
            # Add to history
            st.session_state.transactions.append({
                "Type": "Deposit",
                "Amount": amount,
                "Balance": st.session_state.balance,
                "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success(f"✅ Deposited ₹{amount}. New balance: ₹{st.session_state.balance}")

    elif operation == "Check Balance":
        st.info(f"💳 Your current balance is ₹{st.session_state.balance}")

    elif operation == "View Transaction History":
        if st.session_state.transactions:
            st.subheader("📜 Transaction History")
            st.table(st.session_state.transactions)
        else:
            st.warning("No transactions yet.")
