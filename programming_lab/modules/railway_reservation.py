# railway_reservation.py
# 🚆 Railway Reservation System with Seat Allocation (Streamlit Version)

import streamlit as st

def run():
    st.title("🚆 Railway Reservation System with Seat Allocation")

    # Initialize trains with seats
    if "trains" not in st.session_state:
        st.session_state.trains = {
            "Rajdhani Express": 50,
            "Shatabdi Express": 40,
            "Duronto Express": 30
        }

    # Display available trains
    st.subheader("📋 Available Trains")
    for train, seats in st.session_state.trains.items():
        st.write(f"**{train}**: {seats} seats available")

    # Booking section
    train_choice = st.selectbox("Select Train", list(st.session_state.trains.keys()))
    seats_required = st.number_input("Number of seats to book", min_value=1, max_value=100, value=1)

    passenger_name = st.text_input("Passenger Name")
    passenger_age = st.number_input("Passenger Age", min_value=1, max_value=120, value=25)

    if st.button("🎟 Book Ticket"):
        if seats_required <= st.session_state.trains[train_choice]:
            # Deduct seats
            st.session_state.trains[train_choice] -= seats_required

            # Store booking in session state
            if "bookings" not in st.session_state or not isinstance(st.session_state.bookings, list):
                st.session_state.bookings = []

            st.session_state.bookings.append({
                "Name": passenger_name,
                "Age": passenger_age,
                "Train": train_choice,
                "Seats": seats_required
            })

            st.success(f"✅ Booking Confirmed! {seats_required} seats booked in {train_choice} for {passenger_name}.")
        else:
            st.error("❌ Not enough seats available!")

    # Show bookings
    if "bookings" in st.session_state and st.session_state.bookings:
        st.subheader("📝 Booking History")
        st.table(st.session_state.bookings)
