# modules/logic_gate_circuit.py

import streamlit as st

def logic_gate_output(gate, A, B):
    if gate == "AND":
        return A & B
    elif gate == "OR":
        return A | B
    elif gate == "NOT A":
        return int(not A)
    elif gate == "NOT B":
        return int(not B)
    elif gate == "XOR":
        return A ^ B
    elif gate == "NAND":
        return int(not (A & B))
    elif gate == "NOR":
        return int(not (A | B))
    else:
        return None

def run():
    st.title("🔘 Logic Gate Simulator")
    st.markdown("""
    Simulate basic **digital logic gates** using binary inputs A and B.

    Supports: `AND`, `OR`, `NOT`, `XOR`, `NAND`, `NOR`

    ⚡ Perfect for digital fundamentals in electronics!
    """)

    col1, col2 = st.columns(2)
    with col1:
        A = st.radio("Input A", [0, 1], index=1, horizontal=True)
    with col2:
        B = st.radio("Input B", [0, 1], index=0, horizontal=True)

    gate = st.selectbox("🔀 Select Logic Gate", ["AND", "OR", "NOT A", "NOT B", "XOR", "NAND", "NOR"])

    output = logic_gate_output(gate, A, B)

    st.subheader("🧮 Logic Gate Output")
    st.write(f"**{gate} Gate Output = `{output}`**")

    st.divider()
    st.subheader("📘 Truth Table Preview")

    if gate in ["AND", "OR", "XOR", "NAND", "NOR"]:
        st.markdown("### Inputs: A, B")
        st.table({
            "A": [0, 0, 1, 1],
            "B": [0, 1, 0, 1],
            "Output": [logic_gate_output(gate, a, b) for a, b in [(0,0), (0,1), (1,0), (1,1)]]
        })
    else:
        st.markdown("### Inputs: A")
        st.table({
            "Input": [0, 1],
            "Output": [logic_gate_output(gate, x, 0) for x in [0, 1]]
        })
    st.video("https://www.youtube.com/watch?v=oBbnINBWUoY")
    st.caption("🔍 Designed for quick testing of Boolean logic concepts.")
