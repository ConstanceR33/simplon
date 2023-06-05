import re
import requests
import streamlit as st


st.markdown("<h1 style='color: #31333F; font-size: 42px; text-align: center;'>Bienvenue sur le</h1><h1 style='font-style: italic; color: #EB94CF; font-size: 42px; text-align: center;'>⚝ générateur de texte ⚝</h1>", unsafe_allow_html=True)
st.title("\n\n\n\n\n\n\n\n\n\n")

prompt = st.text_input("Entrez votre texte de départ ici (en anglais) :", placeholder="Exemple : Hello world, it's raining today and")


URL = f"http://localhost:8000/?prompt={prompt}"


if st.button("Générer une suite"):
    with st.empty():
        if not prompt or re.sub(r"\s+", "", prompt) == "":
            st.error('Merci d\'ajouter votre texte')
        else:
            message = st.text("En cours d'exécution, merci de patienter...")
            response = requests.post(URL, json={'prompt': prompt})
            response = response.json()['result']
            st.write(response.replace(prompt, ''))
