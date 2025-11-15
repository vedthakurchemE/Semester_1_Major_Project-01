import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def run(*args, **kwargs):
    st.header("Constant-Size Graph with Large Dynamic Range")

    # Dynamic parameter, e.g., slider to control upper range
    units = st.slider("Number of Units (dynamic x axis)", min_value=1, max_value=10000, value=1000, step=50)
    x = np.arange(1, units+1)
    y = np.log(x)  # Example: logarithmic trend, but try any data you want

    fig, ax = plt.subplots(figsize=(6,4))  # Always the same size
    ax.plot(x, y)
    ax.set_xlim(1, 10000)
    ax.set_ylim(0, np.log(10000))
    ax.set_xlabel("X units")
    ax.set_ylabel("Y")
    ax.set_title("Stable Graph, 1 to 10,000 Units")
    ax.grid(True)
    plt.tight_layout()

    st.pyplot(fig)
