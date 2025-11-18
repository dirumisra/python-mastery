import streamlit as st

st.title("Streamlit Text Input")

name=st.text_input("Enter your name:")

if name:
    st.write(f"Hello {name}")

age=st.slider("Select your age:",0,100,18)

st.write(f"Your age is {age}.")