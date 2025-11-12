import streamlit as st
import pandas as pd

def run():
    st.title("🧾 Smart Billing System with Discount Engine")
    st.write("Easily calculate total bills with itemized prices, quantities, and discounts.")

    # ✅ Force session state variable to be a list, even if previously corrupted
    if "items" not in st.session_state or not isinstance(st.session_state["items"], list):
        st.session_state["items"] = []

    # Add item form
    with st.form("add_item_form", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            item_name = st.text_input("Item Name")
        with col2:
            price = st.number_input("Price per Unit", min_value=0.0, step=0.01)
        with col3:
            quantity = st.number_input("Quantity", min_value=1, step=1)

        discount = st.slider("Discount (%)", min_value=0, max_value=100, value=0)
        submitted = st.form_submit_button("Add Item")

        if submitted and item_name.strip():
            st.session_state["items"].append({
                "Item": item_name.strip(),
                "Price": float(price),
                "Quantity": int(quantity),
                "Discount (%)": int(discount)
            })

    # Display table safely
    if st.session_state["items"]:
        df = pd.DataFrame(st.session_state["items"])
        if not df.empty:
            df["Total"] = df.apply(
                lambda row: row["Price"] * row["Quantity"] * (1 - row["Discount (%)"] / 100), axis=1
            )

            st.subheader("🛒 Cart Items")
            st.dataframe(df, use_container_width=True)

            # Calculate grand total
            grand_total = df["Total"].sum()
            st.markdown(f"### 💰 Grand Total: ₹ {grand_total:,.2f}")

            # Option to clear cart
            if st.button("🗑 Clear Cart"):
                st.session_state["items"] = []
                st.success("Cart cleared successfully!")
        else:
            st.info("No items added yet.")
    else:
        st.info("No items added yet.")
