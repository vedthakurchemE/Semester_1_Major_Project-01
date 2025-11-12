# hospital_scheduler.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

appointments = []

def run():
    st.title("🏥 Hospital Scheduler")
    st.markdown("""
    Manage **patient appointments** with an easy-to-use scheduler.

    Ideal for hospital front desks, clinics, and healthcare centers.
    """)

    st.subheader("📅 Schedule a New Appointment")

    patient_name = st.text_input("👤 Patient Name")
    doctor_name = st.text_input("🩺 Doctor Name")
    department = st.selectbox("🏢 Department", [
        "General Medicine", "Pediatrics", "Orthopedics",
        "Cardiology", "Dermatology", "ENT", "Other"
    ])
    appointment_date = st.date_input("📆 Appointment Date")
    appointment_time = st.time_input("⏰ Appointment Time")
    symptoms = st.text_area("📝 Symptoms / Notes (Optional)")
    date_booked = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if st.button("✅ Book Appointment"):
        record = {
            "Patient Name": patient_name,
            "Doctor Name": doctor_name,
            "Department": department,
            "Appointment Date": appointment_date.strftime("%Y-%m-%d"),
            "Appointment Time": appointment_time.strftime("%H:%M"),
            "Symptoms": symptoms,
            "Date Booked": date_booked
        }
        appointments.append(record)
        st.success("📌 Appointment booked successfully!")

    if appointments:
        df = pd.DataFrame(appointments)
        st.subheader("📋 Appointment Schedule")
        st.dataframe(df)

        st.subheader("📊 Appointments by Department")
        fig1, ax1 = plt.subplots()
        df["Department"].value_counts().plot.pie(
            autopct='%1.1f%%', startangle=90, counterclock=False, ax=ax1
        )
        ax1.set_ylabel("")
        st.pyplot(fig1)

        st.subheader("📈 Appointments by Doctor")
        fig2, ax2 = plt.subplots()
        df["Doctor Name"].value_counts().plot(kind='bar', color='skyblue', ax=ax2)
        ax2.set_ylabel("Count")
        ax2.set_title("Number of Appointments per Doctor")
        st.pyplot(fig2)

    st.caption("💡 Use this tool for clinic scheduling and patient management.")
