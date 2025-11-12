# modules/prime_visualizer.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def run():
    st.title("🔢 Prime Number Visualizer")
    st.markdown("""
    This app finds and plots all **prime numbers** up to a number `N`.

    ---
    ### 💡 What is a Prime Number?
    A number greater than 1 that has no positive divisors other than 1 and itself.
    """)

    N = st.slider("🔍 Find primes up to:", min_value=10, max_value=1000, value=100)

    primes = [x for x in range(2, N + 1) if is_prime(x)]

    st.success(f"✅ Found {len(primes)} primes between 1 and {N}")
    st.code(primes, language='python')

    # 📊 Plotting primes
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.plot(primes, 'ro', markersize=4)
    ax.set_title(f"Prime Numbers up to {N}")
    ax.set_xlabel("Index")
    ax.set_ylabel("Prime Value")
    st.pyplot(fig)

    st.info("📈 Plot helps visualize how primes become sparse as numbers grow.")
