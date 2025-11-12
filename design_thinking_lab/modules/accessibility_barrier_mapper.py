# modules/accessibility_barrier_mapper.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

barrier_data = []

def run():
    st.title("♿ Accessibility Barrier Mapper")
    st.markdown("""
    Map and log **real-world accessibility barriers** to improve inclusive design solutions.

    Ideal for use in design surveys, urban planning, and social impact projects.
    """)

    st.subheader("🧱 Log an Accessibility Barrier")

    location = st.text_input("📍 Location (e.g., 'Main Library Entrance')")
    barrier_type = st.selectbox("🚧 Barrier Type", [
        "No Ramp", "Narrow Doorway", "Uneven Surface", "No Signage",
        "Inaccessible Restroom", "High Counter", "Other"
    ])
    severity = st.radio("⚠️ Severity Level", ["Low", "Moderate", "High"])
    date_reported = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    suggestion = st.text_area("💡 Suggested Improvement (Optional)")

    if st.button("📌 Submit Entry"):
        record = {
            "Location": location,
            "Barrier Type": barrier_type,
            "Severity": severity,
            "Date": date_reported,
            "Suggestion": suggestion
        }
        barrier_data.append(record)
        st.success("✅ Barrier logged successfully!")

    if barrier_data:
        df = pd.DataFrame(barrier_data)
        st.subheader("📋 Barrier Log Table")
        st.dataframe(df)

        st.subheader("📊 Barrier Type Distribution")
        fig1, ax1 = plt.subplots()
        df["Barrier Type"].value_counts().plot.pie(
            autopct='%1.1f%%', startangle=90, counterclock=False, ax=ax1
        )
        ax1.set_ylabel("")
        st.pyplot(fig1)

        st.subheader("📈 Severity Breakdown")
        fig2, ax2 = plt.subplots()
        df["Severity"].value_counts().plot(kind='bar', color='coral', ax=ax2)
        ax2.set_ylabel("Count")
        ax2.set_title("Reported Severity Levels")
        st.pyplot(fig2)

    st.caption("🔍 Use this tool for accessibility audits and human-centric redesign initiatives.")
