import streamlit as st

name = st.text_input("Email cím:")
name = st.text_input("Név:")
level = st.slider(" Élet korod:", 1, 100)
status = st.radio("Fiú/Lány: ", ('Fiú', 'Lány'))

import Image from pillow to open images
from PIL import Image
img = Image.open("streamlit.png")



if(st.button("Beküldés")):
  st.success("Válaszodat rögzítettük")
