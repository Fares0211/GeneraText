from email import header
import streamlit as st
import pandas as pd
from PIL import Image

st.balloons()
st.title('Text Generator')
st.header('Choissisez votre oeuvre')


option = st.selectbox(
     'Choississez votre générateur',
     ('Shakespear', 'Star-Wars', 'Harry Potter',''))
if option == 'Shakespear':
    st.subheader('Voici le texte générer : ')
    image = Image.open("C:/Users/chams/Pictures/romeeo.png")

    st.image(image, caption='Shakespear le retour')
if option == 'Star-Wars':
    st.subheader('Voici le texte générer : ')
    image = Image.open("C:/Users/chams/Pictures/dark.png")

    st.image(image, caption='Dark vador is watching u')
if option == 'Harry Potter':
    st.subheader('En cours de production')
else : 
    st.text("")

st.write('You selected:', option)