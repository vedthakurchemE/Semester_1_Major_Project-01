import streamlit as st
import matplotlib.pyplot as plt

def draw_fastener_diagram(fastener_type):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axis('off')
    ax.set_title(f"{fastener_type} Diagram", fontsize=16)

    if fastener_type == "Hex Bolt":
        ax.plot([1, 1], [1, 3], color='black', linewidth=8, label='Shank')
        ax.plot([1, 2], [3, 3], color='black', linewidth=8, label='Head')
        ax.text(2.1, 3, 'Hex Head', va='center', fontsize=12)
        ax.text(1.1, 2, 'Shank', va='center', fontsize=12)
        ax.plot([1, 1.6], [1, 1], color='blue', linewidth=6)
        ax.text(1.65, 1, 'Threaded End', va='center', fontsize=12)

    elif fastener_type == "Nut":
        ax.add_patch(plt.Rectangle((1, 1), 2, 1, edgecolor='black', facecolor='gray'))
        ax.text(2, 1.5, 'Hex Nut', ha='center', va='center', fontsize=12)

    elif fastener_type == "Washer":
        washer = plt.Circle((2, 2), 1, color='grey')
        hole = plt.Circle((2, 2), 0.4, color='white')
        ax.add_patch(washer)
        ax.add_patch(hole)
        ax.text(2, 0.8, 'Plain Washer', ha='center', fontsize=12)

    elif fastener_type == "Rivet":
        ax.plot([2, 2], [1, 3], color='black', linewidth=8)
        ax.plot([1.5, 2.5], [3, 3], color='black', linewidth=8)
        ax.text(2, 3.2, 'Rivet Head', ha='center', fontsize=12)
        ax.text(2, 2, 'Shank', ha='center', fontsize=12)

    elif fastener_type == "Screw":
        ax.plot([2, 2], [1, 2.5], color='black', linewidth=4)
        ax.plot([1.5, 2.5], [2.5, 2.5], color='black', linewidth=6)
        ax.text(2, 2.7, 'Head', ha='center', fontsize=12)
        ax.text(2, 1.5, 'Threaded Body', ha='center', fontsize=12)

    st.pyplot(fig)

def run():
    st.title("🔧 Module 6: Fasteners Identifier")
    st.markdown("Visually understand and label basic **mechanical fasteners** used in Engineering Drawing.")

    fastener = st.selectbox("Select a Fastener Type", [
        "Hex Bolt", "Nut", "Washer", "Rivet", "Screw"
    ])

    if st.button("🔍 Show Diagram"):
        draw_fastener_diagram(fastener)
