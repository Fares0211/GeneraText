import openai
import streamlit as st
from PIL import Image

openai.api_key = "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" 

st.balloons()
st.title('Text Generator')
st.header('Choissisez votre oeuvre')

option = st.selectbox(
     'Choississez votre générateur',
     ('Shakespeare', 'Star Wars', 'Harry Potter','')
)

if option == 'Shakespeare':
    st.subheader('Voici le texte généré : ')
    model_engine = 'text-davinci-002' # Le moteur de modèle OpenAI GPT-3 à utiliser
    prompt = 'To be or not to be, that is the question.' # La phrase à compléter
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    st.write(response.choices[0].text)
    image = Image.open('shakespeare.jpg')
    st.image(image, caption='Shakespeare le retour')

if option == 'Star Wars':
    st.subheader('Voici le texte généré : ')
    model_engine = 'text-davinci-002' # Le moteur de modèle OpenAI GPT-3 à utiliser
    prompt = 'A long time ago in a galaxy far, far away...' # La phrase à compléter
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    st.write(response.choices[0].text)
    image = Image.open('star-wars.jpg')
    st.image(image, caption='Dark vador is watching u')

if option == 'Harry Potter':
    st.subheader('En cours de production')
else:
    st.text("")

st.write('You selected:', option)
