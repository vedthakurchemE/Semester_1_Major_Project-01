# student_grade_management_streamlit.py
# 📚 Student Grade & Result Management System (Streamlit Version)

import streamlit as st
import pandas as pd

def calculate_grade(marks):
    """Returns grade based on marks."""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def result_status(marks, pass_marks=40):
    """Determines pass or fail based on marks."""
    return "Pass ✅" if marks >= pass_marks else "Fail ❌"

def run():
    st.title("📚 Student Grade & Result Management System")

    students = []
    num_students = st.number_input("Enter number of students:", min_value=1, step=1)

    for i in range(num_students):
        st.subheader(f"Student {i + 1} Details")
        name = st.text_input(f"Enter name for Student {i + 1}", key=f"name_{i}")
        marks = st.number_input(
            f"Enter marks (out of 100) for {name if name else 'Student'}",
            min_value=0.0, max_value=100.0, step=0.5, key=f"marks_{i}"
        )

        if name and marks is not None:
            grade = calculate_grade(marks)
            status = result_status(marks)
            students.append({
                "Name": name,
                "Marks": marks,
                "Grade": grade,
                "Result": status
            })

    if students:
        st.subheader("📊 Student Report")
        st.table(students)

        # Download as CSV
        df = pd.DataFrame(students)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Report as CSV",
            data=csv,
            file_name='student_results.csv',
            mime='text/csv'
        )
