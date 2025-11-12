# modules/leap_year_checker.py

import streamlit as st

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def run():
    st.title("📅 Leap Year Checker")
    st.markdown("""
    Check if a given year is a **leap year** using Python logic.

    ---
    ### 📘 Leap Year Rules:
    - Divisible by 4 ✅  
    - **Not** divisible by 100 ❌  
    - Except divisible by 400 ✅
    """)

    year = st.number_input("Enter a Year", min_value=1, max_value=9999, step=1, value=2024)

    if st.button("🔍 Check Leap Year"):
        if is_leap_year(year):
            st.success(f"✅ Yes! {year} is a **Leap Year**.")
        else:
            st.error(f"❌ No, {year} is **not** a Leap Year.")

    st.markdown("---")
    st.caption("✔️ Leap years have 366 days instead of 365.")
