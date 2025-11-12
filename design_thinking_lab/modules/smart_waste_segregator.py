# modules/smart_waste_segregator.py

import streamlit as st

def classify_waste(item):
    item = item.lower()

    dry_items = ['plastic bottle', 'newspaper', 'cardboard', 'can', 'glass', 'chips packet']
    wet_items = ['banana peel', 'vegetable waste', 'food scraps', 'egg shell']
    hazardous_items = ['battery', 'paint', 'chemical', 'medicine', 'syringe']

    if item in dry_items:
        return "Dry Waste ♻️", "🟫 Recyclable dry waste. Dispose in dry bin."
    elif item in wet_items:
        return "Wet Waste 🌱", "🟩 Biodegradable organic waste. Compostable or for wet bin."
    elif item in hazardous_items:
        return "Hazardous Waste ☣️", "🟥 Dangerous to handle. Use special disposal methods."
    else:
        return "Unknown ❓", "⚠️ Cannot identify. Please check item or describe more clearly."

def run():
    st.title("🗑️ Smart Waste Segregator")
    st.markdown("""
    Use this app to classify household waste items into **Dry**, **Wet**, or **Hazardous** categories.

    Helps promote **sustainable disposal** and supports smart city waste systems.
    """)

    st.image("https://cdn-icons-png.flaticon.com/512/2986/2986374.png", width=120)

    st.subheader("🔍 Enter a Household Item")
    item = st.text_input("E.g. plastic bottle, banana peel, battery", "")

    if item:
        category, advice = classify_waste(item)
        st.success(f"🔎 **Category:** {category}")
        st.info(advice)

        if category != "Unknown ❓":
            st.balloons()

    with st.expander("📚 Example Items"):
        st.markdown("""
        - **Dry Waste**: newspaper, plastic bottle, cardboard
        - **Wet Waste**: banana peel, vegetable waste, egg shells
        - **Hazardous Waste**: battery, paint, medicine
        """)

    st.caption("♻️ Built using Python + Streamlit as part of Design Thinking Lab Project")
