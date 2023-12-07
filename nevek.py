import streamlit as st

name = st.text_input("Email cím:")
name = st.text_input("Név:")
level = st.slider(" Élet korod:", 1, 100)
status = st.radio("Fiú/Lány: ", ('Fiú', 'Lány'))


macskak = st.multiselect("Macskák:",
[st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_mxfQLdeTesZj3N8sEMnFF2EoibjeQZpY0Q&usqp=CAU', caption='HUH'),


st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdzCSmWdeTEqCcZrjtqwQ8_cjwSIzuyjEGzA&usqp=CAU', caption='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'),

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7ttfYzs-dO8Bu9dvO7Npd6p5HY_9u1qMa2w&usqp=CAU', caption='I see you...'),

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmUbKgrB7t9H0TUGIopnkuFl2IolxqCh0q-w&usqp=CAU', caption='... I farted...'),

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTF2m9RlCfJBiRWavnABDv5X7CFIwI2o49YOw&usqp=CAU', caption='Angy'),

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_ScMEueg7hFb5uyay0MZza-Z_lJJyIMb43w&usqp=CAU', caption='Hmmm...'),

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIpTL_ogwa1jCH2dZryWU6JcvAGuZQMSwH5A&usqp=CAU', caption='TÁVOZZ INNEN SÁTÁN'),

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvMv7kljyvB-BWWJpHJaASY6b2cDH8jyoOHA&usqp=CAU', caption='You kidding me right now'),

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9Yu6LRBh9IIevsI37KVbeMp9rbZA0WAfPR55id-UiGgJuJ2mvXbANcIY_bmku3RiZbKE&usqp=CAU', caption='Autism'),

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUBSLFmPv__8G4_yyueqzJjrGMpfl761eQQw&usqp=CAU', caption='Bonk cat'),

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREskN3-Pu3KeMGyzbR7whrqEXfs0U4sfK19Q&usqp=CAU', caption='I am not fat!>:O')])






if(st.button("Beküldés")):
  st.success("Válaszodat rögzítettük")
