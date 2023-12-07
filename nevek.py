import streamlit as st

name = st.text_input(".text_input: Enter Your name", "Type Here ...")

status = st.radio(".radio: Select Gender: ", ('Male', 'Female'))
