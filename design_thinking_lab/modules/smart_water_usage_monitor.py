# modules/smart_water_usage_monitor.py

import streamlit as st
import matplotlib.pyplot as plt


def estimate_usage(shower, flush, dishes, laundry, others):
    return round(shower + flush + dishes + laundry + others, 2)


def suggest_improvements(total):
    tips = []
    if total > 300:
        tips.append("🚿 Reduce shower time or install low-flow showerheads.")
        tips.append("🚽 Use dual-flush toilets.")
        tips.append("🧼 Run full loads in dishwashers and washing machines.")
        tips.append("💧 Fix leaks to avoid hidden losses.")
    elif total > 200:
        tips.append("✅ You're doing fairly well, but can improve further.")
    else:
        tips.append("🌍 Excellent! You're conserving water effectively.")
    return tips


def run():
    st.title("💧 Smart Water Usage Monitor")
    st.markdown("""
    Estimate your **daily household water consumption** and get tips to reduce usage.

    🏠 This tool encourages **sustainable habits** and environmental awareness.
    """)

    st.subheader("🚿 Daily Usage Inputs (Litres)")
    shower = st.slider("Shower", 0, 150, 60)
    flush = st.slider("Toilet Flush", 0, 100, 40)
    dishes = st.slider("Washing Dishes", 0, 100, 30)
    laundry = st.slider("Laundry", 0, 100, 50)
    others = st.slider("Other Uses (cooking, plants, etc.)", 0, 100, 20)

    total = estimate_usage(shower, flush, dishes, laundry, others)
    st.success(f"💧 Estimated Daily Usage: **{total} Litres**")

    st.subheader("📊 Water Usage Breakdown")
    labels = ['Shower', 'Flush', 'Dishes', 'Laundry', 'Others']
    values = [shower, flush, dishes, laundry, others]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

    st.subheader("💡 Recommendations")
    for tip in suggest_improvements(total):
        st.markdown(f"- {tip}")

    st.caption("🔁 Try updating your values weekly to track improvement.")
