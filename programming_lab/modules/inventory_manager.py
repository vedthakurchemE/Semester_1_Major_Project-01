# inventory_manager.py
# 📦 Inventory Management with Low Stock Alerts (Streamlit Version)

import streamlit as st
import pandas as pd

def run():
    st.title("📦 Inventory Management System with Low Stock Alerts")

    # Initial inventory data
    if "inventory" not in st.session_state:
        st.session_state.inventory = pd.DataFrame(
            columns=["Item Name", "Quantity", "Price per Unit", "Low Stock Threshold"]
        )

    # Add / Update Item
    st.subheader("➕ Add / Update Inventory Item")
    item_name = st.text_input("Item Name")
    quantity = st.number_input("Quantity", min_value=0, step=1)
    price = st.number_input("Price per Unit (₹)", min_value=0.0, step=0.5)
    low_stock_threshold = st.number_input("Low Stock Threshold", min_value=0, step=1)

    if st.button("Add / Update Item"):
        if item_name:
            if item_name in st.session_state.inventory["Item Name"].values:
                # Update existing item
                st.session_state.inventory.loc[
                    st.session_state.inventory["Item Name"] == item_name,
                    ["Quantity", "Price per Unit", "Low Stock Threshold"]
                ] = [quantity, price, low_stock_threshold]
                st.success(f"✅ Updated '{item_name}' in inventory.")
            else:
                # Add new item
                new_row = pd.DataFrame(
                    [[item_name, quantity, price, low_stock_threshold]],
                    columns=["Item Name", "Quantity", "Price per Unit", "Low Stock Threshold"]
                )
                st.session_state.inventory = pd.concat(
                    [st.session_state.inventory, new_row], ignore_index=True
                )
                st.success(f"✅ Added '{item_name}' to inventory.")
        else:
            st.error("⚠ Please enter an item name.")

    # Display Inventory
    st.subheader("📋 Current Inventory")
    if not st.session_state.inventory.empty:
        st.dataframe(st.session_state.inventory)

        # Low Stock Alerts
        low_stock_items = st.session_state.inventory[
            st.session_state.inventory["Quantity"] <= st.session_state.inventory["Low Stock Threshold"]
        ]
        if not low_stock_items.empty:
            st.warning("🚨 Low Stock Items Detected:")
            st.table(low_stock_items)
    else:
        st.info("No items in inventory. Please add some.")

    # Remove Item
    st.subheader("❌ Remove Item from Inventory")
    remove_item = st.selectbox(
        "Select item to remove", [""] + list(st.session_state.inventory["Item Name"].values)
    )
    if st.button("Remove Item"):
        if remove_item:
            st.session_state.inventory = st.session_state.inventory[
                st.session_state.inventory["Item Name"] != remove_item
            ]
            st.success(f"🗑 Removed '{remove_item}' from inventory.")
        else:
            st.error("⚠ Please select an item to remove.")
