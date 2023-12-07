import streamlit as st

name = st.text_input("Email cím:")
name = st.text_input("Név:")
level = st.slider(" Élet korod:", 1, 100)
status = st.radio("Fiú/Lány: ", ('Fiú', 'Lány'))

import Image from pillow to open images
from PIL import Image
img = Image.open("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_mxfQLdeTesZj3N8sEMnFF2EoibjeQZpY0Q&usqp=CAU")


if(st.button("Beküldés")):
  st.success("Válaszodat rögzítettük")
