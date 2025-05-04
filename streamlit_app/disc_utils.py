
import openai
import streamlit as st

openai.api_key = st.secrets["openai_api_key"]

def generate_feedback(text, disc_type):
    prompt = f"""
    Tu es un coach expert en communication DISC.
    Profil DISC : {disc_type}
    Voici le pitch :
    \"""{text}\"""

    Donne un retour constructif, empathique, en lien avec le style {disc_type}, avec des conseils concrets.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500
    )
    return response["choices"][0]["message"]["content"]
