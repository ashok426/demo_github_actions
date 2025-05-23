import streamlit as st
from math_operations import add, subtract

st.title("Simple Math Operations")

a = st.number_input("Enter first number (a):", value=0)
b = st.number_input("Enter second number (b):", value=0)

operation = st.selectbox("Choose operation:", ("Add", "Subtract"))

if st.button("Calculate"):
    if operation == "Add":
        result = add(a, b)
        st.success(f"Result: {a} + {b} = {result}")
    else:
        result = subtract(a, b)
        st.success(f"Result: {a} - {b} = {result}")