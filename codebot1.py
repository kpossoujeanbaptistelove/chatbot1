# Importer les packages
import streamlit as st
st.set_page_config(page_title="Mon premier Chatbot",page_icon="robot_face")
from nltk.chat.util import *

# Définir le dialogue
pairs = [
    ["Mon nom c'est (.*)",["Hello %1"]],
    ["(bonjour|salut|coucou)",["Salut toi","hello","en quoi je peux aider"]],
    ["je veux une (.*) taille (.*)",["Ok J'ai compris Je vais vous préparer une %1 taille %2"]],
    ["(.*)(ville|adresse)",["Nous sommes à SO-AVA au Bénin"]],
    ["(.*)aider(.*)",["Je peux vous aider"]],
    ["(.*)merci(.*)",["Bienvenue...et à bientot"]],
    ["(.*)(contact|numéro|numero)(.*)",["Nous sommes joignables au +229 00 00 00 00"]]
]

def chatbot_response(user_input):
    chat = Chat(pairs, reflections)
    return chat.respond(user_input)

# Interface utilisateur Streamlit
st.title("Chatbot")
user_input = st.text_input("Vous: ", "")
if user_input:
    response = chatbot_response(user_input)
    st.text_area("Chatbot: ", value=response, height=200)
