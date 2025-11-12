# modules/fibonacci_plotter.py

import streamlit as st
import matplotlib.pyplot as plt

def generate_fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def run():
    st.title("🌀 Fibonacci Sequence Plotter")
    st.markdown("""
    Visualize the famous **Fibonacci sequence** — where each number is the sum of the two preceding ones.

    ---
    ### 📘 Fibonacci Rule:
    \[
    F(n) = F(n-1) + F(n-2)
    \]
    """)

    n = st.slider("🔢 How many terms to generate?", min_value=5, max_value=100, value=20, step=1)

    fib = generate_fibonacci(n)
    st.success(f"🧮 First {n} Fibonacci numbers:")
    st.code(fib)

    # 📈 Plot the sequence
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(fib, marker='o', linestyle='-', color='purple')
    ax.set_title(f"Fibonacci Sequence (First {n} Terms)")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.grid(True)

    st.pyplot(fig)
    st.caption("🌱 Fibonacci numbers appear in nature, art, architecture, and more.")
