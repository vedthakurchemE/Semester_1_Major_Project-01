# modules/fastener_identifier.py

import streamlit as st

def run():
    st.title("🔩 Fastener Identifier")
    st.markdown("""
    Visually explore and identify **common mechanical fasteners** used in assemblies.

    Click on each fastener to view its description and drawing.
    """)

    fasteners = {
        "Hex Bolt": {
            "desc": "Standard bolt with hexagonal head used with nuts or threaded holes.",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/71/Hex_bolt.png"
        },
        "Nut": {
            "desc": "Hexagonal or square internal-threaded component to mate with a bolt.",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Nut_3d.png"
        },
        "Washer": {
            "desc": "Flat disc used to distribute load or prevent damage to surfaces.",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Washers_assortment.jpg"
        },
        "Phillips Screw": {
            "desc": "Screw with a cross-slotted head, turned using a Phillips screwdriver.",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/42/Phillips_head_screw.jpg"
        },
        "Socket Head Cap Screw": {
            "desc": "High-strength screw turned using an Allen key or hex driver.",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/5b/Socket_head_cap_screw.jpg"
        },
        "Wood Screw": {
            "desc": "Tapered screw with sharp thread used to fasten wood.",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Wood_screws.jpg"
        }
    }

    selected = st.selectbox("🛠️ Select Fastener Type", list(fasteners.keys()))
    st.image(fasteners[selected]["image_url"], width=300)
    st.markdown(f"**Description:** {fasteners[selected]['desc']}")

    st.success("✅ Recognize fasteners for drawing, workshop, or CAD work.")
