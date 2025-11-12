# modules/sorting_visualizer.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
import time

def bubble_sort(arr):
    steps = []
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                steps.append(a.copy())
    return steps

def run():
    st.title("🔃 Sorting Algorithm Visualizer")
    st.markdown("""
    Watch how a **Bubble Sort** algorithm works, step-by-step.

    ---
    💡 Bubble Sort repeatedly steps through the list, compares adjacent items and swaps them if they’re in the wrong order.
    """)

    size = st.slider("🧮 Number of Elements", min_value=5, max_value=30, value=10)
    if st.button("🔀 Generate & Sort"):

        data = random.sample(range(1, 100), size)
        st.info(f"Original List: {data}")

        steps = bubble_sort(data)

        progress = st.progress(0)
        plot_area = st.empty()

        for i, step in enumerate(steps):
            fig, ax = plt.subplots()
            ax.bar(range(len(step)), step, color="skyblue")
            ax.set_title(f"Step {i+1} / {len(steps)}")
            plot_area.pyplot(fig)
            progress.progress((i + 1) / len(steps))
            time.sleep(0.2)

        st.success("✅ Sorting Complete!")

        st.code(f"Sorted List: {steps[-1]}")
