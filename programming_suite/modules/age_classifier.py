# modules/age_classifier.py

import streamlit as st
from datetime import date

def classify_age(age):
    if age < 1:
        return "Infant 👶"
    elif 1 <= age <= 12:
        return "Child 🧒"
    elif 13 <= age <= 19:
        return "Teenager 🧑‍🎓"
    elif 20 <= age <= 35:
        return "Young Adult 🧑"
    elif 36 <= age <= 59:
        return "Adult 👨‍💼"
    else:
        return "Senior Citizen 👴"

def run():
    st.title("👥 Age Group Classifier")
    st.markdown("""
    This app classifies your **age group** based on your date of birth.

    ---
    💡 **Categories:**
    - Infant: 0 – 1 year  
    - Child: 1 – 12 years  
    - Teenager: 13 – 19 years  
    - Young Adult: 20 – 35 years  
    - Adult: 36 – 59 years  
    - Senior Citizen: 60+ years  
    """)

    dob = st.date_input("📅 Enter Your Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    if st.button("🔍 Classify Age Group"):
        group = classify_age(age)
        st.success(f"You are **{age}** years old and belong to the **{group}** category.")
