# modules/basic_electronics/digital_logic_gate_simulator.py

import streamlit as st

def logic_gates(a, b):
    return {
        "AND": a & b,
        "OR": a | b,
        "NOT A": int(not a),
        "NOT B": int(not b),
        "NAND": int(not (a & b)),
        "NOR": int(not (a | b)),
        "XOR": a ^ b,
        "XNOR": int(not (a ^ b))
    }

def run():
    st.title("🧠 Digital Logic Gate Simulator")
    st.markdown("""
    Simulate **basic logic gates** with two binary inputs (A & B).

    ---
    **Available Gates**:
    - AND, OR
    - NOT A, NOT B
    - NAND, NOR
    - XOR, XNOR
    """)

    col1, col2 = st.columns(2)
    with col1:
        a = st.selectbox("Input A", [0, 1], index=0)
    with col2:
        b = st.selectbox("Input B", [0, 1], index=0)

    st.subheader("📊 Gate Outputs")

    results = logic_gates(a, b)
    for gate, output in results.items():
        st.success(f"{gate}: {output}")

    st.info("💡 Used in digital circuits, processors, ALUs, and embedded systems.")
