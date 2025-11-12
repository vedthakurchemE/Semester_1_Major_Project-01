# library_tracker.py
# 📚 Library Book Borrowing & Return Tracker (Streamlit Version)

import streamlit as st
import datetime

def run():
    st.title("📚 Library Book Borrowing & Return Tracker")

    # Initialize session state
    if "books" not in st.session_state or not isinstance(st.session_state["books"], list):
        st.session_state["books"] = []

    st.sidebar.header("➕ Add New Book Transaction")

    book_name = st.sidebar.text_input("Book Name")
    borrower_name = st.sidebar.text_input("Borrower Name")
    borrow_date = st.sidebar.date_input("Borrow Date", datetime.date.today())
    return_date = st.sidebar.date_input(
        "Expected Return Date", datetime.date.today() + datetime.timedelta(days=7)
    )

    if st.sidebar.button("Add Transaction"):
        if book_name and borrower_name:
            st.session_state["books"].append({
                "Book Name": book_name,
                "Borrower Name": borrower_name,
                "Borrow Date": borrow_date,
                "Return Date": return_date,
                "Status": "Borrowed"
            })
            st.sidebar.success("✅ Transaction Added Successfully!")
        else:
            st.sidebar.error("⚠ Please fill in both Book Name and Borrower Name.")

    st.subheader("📖 Current Transactions")
    if st.session_state["books"]:
        st.table(st.session_state["books"])
    else:
        st.info("No transactions yet.")

    st.subheader("🔄 Update Book Return Status")
    if st.session_state["books"]:
        book_options = [
            f"{b['Book Name']} - {b['Borrower Name']}"
            for b in st.session_state["books"] if b["Status"] == "Borrowed"
        ]
        if book_options:
            selected_book = st.selectbox("Select Book to Mark as Returned", book_options)

            if st.button("Mark as Returned"):
                for book in st.session_state["books"]:
                    if f"{book['Book Name']} - {book['Borrower Name']}" == selected_book:
                        book["Status"] = "Returned"
                        st.success(f"✅ {book['Book Name']} returned by {book['Borrower Name']}.")
                        break
        else:
            st.info("No borrowed books to return.")
    else:
        st.info("No borrowed books to return.")
