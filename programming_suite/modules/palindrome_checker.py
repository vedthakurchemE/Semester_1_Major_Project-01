# modules/palindrome_checker.py

import streamlit as st

def is_palindrome(text):
    clean_text = ''.join(filter(str.isalnum, text)).lower()
    return clean_text == clean_text[::-1]

def run():
    st.title("🔁 Palindrome Checker")
    st.markdown("""
    Check whether a word, number, or sentence is a **palindrome** — same forward and backward!

    ---
    ### 📘 What’s a Palindrome?
    A palindrome is a string that reads the same from the **left and right**, ignoring case and special characters.
    """)

    user_input = st.text_input("🔤 Enter text or number", value="racecar")

    if st.button("🔍 Check Palindrome"):
        if is_palindrome(user_input):
            st.success(f"✅ '{user_input}' is a **Palindrome**.")
        else:
            st.error(f"❌ '{user_input}' is **not** a Palindrome.")

    st.caption("ℹ️ Spaces, punctuation, and case are ignored.")
