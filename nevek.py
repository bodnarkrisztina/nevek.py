import streamlit as st

name = st.text_input("Email cím:")
name = st.text_input("Név:")
level = st.slider(" Élet korod:", 1, 100)
status = st.radio("Fiú/Lány: ", ('Fiú', 'Lány'))

import Image from pillow to open images
from PIL import Image
img = Image.open("data:image/jpeg;base64,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")



if(st.button("Beküldés")):
  st.success("Válaszodat rögzítettük")
