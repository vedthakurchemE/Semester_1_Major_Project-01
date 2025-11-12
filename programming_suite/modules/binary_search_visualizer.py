# modules/binary_search_visualizer.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

def binary_search_steps(arr, target):
    steps = []
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        steps.append((low, mid, high))

        if arr[mid] == target:
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return steps

def run():
    st.title("🔎 Binary Search Visualizer")
    st.markdown("""
    Visualize the steps of a **Binary Search** algorithm on a sorted list.

    ---
    ### 📘 Binary Search Logic:
    Repeatedly divide the search range in half until the target is found or the list is exhausted.
    """)

    arr = list(range(10, 101, 10))  # [10, 20, ..., 100]
    target = st.selectbox("🎯 Pick a Target Number", arr)

    if st.button("🚀 Start Search"):
        steps = binary_search_steps(arr, target)

        plot_area = st.empty()
        progress = st.progress(0)

        for i, (low, mid, high) in enumerate(steps):
            fig, ax = plt.subplots(figsize=(10, 2))
            bars = ax.bar(range(len(arr)), arr, color="lightgray")
            bars[low].set_color("orange")
            bars[mid].set_color("blue")
            bars[high].set_color("red")
            ax.set_xticks(range(len(arr)))
            ax.set_xticklabels(arr)
            ax.set_title(f"Step {i+1}: Low={arr[low]}, Mid={arr[mid]}, High={arr[high]}")
            plot_area.pyplot(fig)
            progress.progress((i + 1) / len(steps))
            time.sleep(0.5)

        if arr[steps[-1][1]] == target:
            st.success(f"✅ Target `{target}` found at index {steps[-1][1]}!")
        else:
            st.error(f"❌ Target `{target}` not found.")
