# modules/cement_fineness_analyzer.py

import streamlit as st
import matplotlib.pyplot as plt

def run():
    st.title("🧪 Fineness of Cement Analyzer (Sieve Method)")
    st.markdown("""
    Simulate **sieve analysis** to determine the **fineness of cement** using a 90-micron IS sieve.

    ---
    ### 🧮 Formula:
    **% Retained = (W_retained / W_sample) × 100**

    ✅ IS Code Limit: Not more than **10% retained** on 90µ sieve.
    """)

    st.subheader("📥 Enter Experimental Values (grams)")
    sample_weight = st.number_input("Initial Weight of Cement Sample (W_sample)", min_value=50.0, value=100.0, step=1.0)
    retained_weight = st.number_input("Weight Retained on 90µ Sieve (W_retained)", min_value=0.0, value=5.0, step=0.1)

    if st.button("🧮 Calculate Fineness"):
        if sample_weight <= 0:
            st.error("❌ Sample weight must be greater than zero.")
        else:
            percent_retained = round((retained_weight / sample_weight) * 100, 2)
            fineness = 100 - percent_retained
            st.success(f"✅ % Fineness of Cement: **{fineness:.2f}%**")
            st.info(f"📌 % Retained on 90µ Sieve: **{percent_retained:.2f}%**")

            if percent_retained <= 10:
                st.success("🟢 Fineness is within IS specifications.")
            else:
                st.warning("🔴 Cement may be too coarse. Not acceptable per IS code.")

    st.divider()
    st.subheader("📊 Visualization")

    fig, ax = plt.subplots(figsize=(6, 6))  # Fixed size figure here
    ax.pie(
        [retained_weight, sample_weight - retained_weight],
        labels=["Retained", "Passed"],
        autopct="%1.1f%%",
        colors=["#FF9999", "#90EE90"]
    )
    ax.set_title("Cement Sieving Distribution")
    st.pyplot(fig)

    st.caption("📘 As per IS:4031 (Part 1) – Fineness by Dry Sieving.")
