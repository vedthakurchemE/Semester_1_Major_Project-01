# modules/eco_product_feedback_collector.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

feedback_list = []


def run():
    st.title("🌱 Eco Product Feedback Collector")
    st.markdown("""
    Collect user feedback on **sustainable or eco-friendly products**.

    Useful for design iterations, environmental startups, and innovation workshops.
    """)

    st.subheader("🧾 Rate the Product")
    product = st.selectbox("Product Name",
                           ["Biodegradable Toothbrush", "Solar Power Bank", "Recycled Notebook", "Bamboo Cutlery"])
    usability = st.slider("Usability (1-5)", 1, 5, 3)
    eco_friendly = st.slider("Eco-Friendliness (1-5)", 1, 5, 4)
    durability = st.slider("Durability (1-5)", 1, 5, 3)
    comments = st.text_area("💬 Additional Feedback")

    if st.button("📩 Submit Feedback"):
        feedback = {
            "Product": product,
            "Usability": usability,
            "Eco_Friendly": eco_friendly,
            "Durability": durability,
            "Comments": comments
        }
        feedback_list.append(feedback)
        st.success("✅ Feedback submitted successfully!")

    if feedback_list:
        df = pd.DataFrame(feedback_list)
        st.subheader("📊 Feedback Summary")

        avg_scores = df.groupby("Product")[["Usability", "Eco_Friendly", "Durability"]].mean()
        st.dataframe(avg_scores.style.highlight_max(axis=0))

        st.subheader("📉 Average Ratings by Product")
        fig, ax = plt.subplots()
        avg_scores.plot(kind="bar", ax=ax)
        ax.set_ylabel("Average Rating")
        ax.set_ylim(0, 5)
        st.pyplot(fig)

        st.subheader("💬 All Comments")
        for i, row in df.iterrows():
            st.markdown(f"**{row['Product']}**: _{row['Comments']}_")

    st.caption("🔄 Refresh or restart app to reset feedback data (temporary memory only).")
