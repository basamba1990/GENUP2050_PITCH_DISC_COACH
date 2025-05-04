
import streamlit as st
import tempfile
from transcription_utils import transcribe_audio
from disc_utils import generate_feedback
from pdf_generator import create_pdf
import base64

st.set_page_config(page_title="GENUP2050 - Coach Pitch", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #F0F8FF; }
    h1 { color: #1D3557; }
    .stButton > button { background-color: #457B9D; color: white; }
    </style>
""", unsafe_allow_html=True)

st.image("logo_genup2050.png", width=180)

st.title("GENUP2050 - Générateur de Pitch & Feedback DISC")
st.markdown("""
Bienvenue sur **GENUP2050**, ton coach interactif.

**Étapes à suivre :**
1. Téléverse ta vidéo/audio de pitch
2. Transcription automatique avec IA
3. Choisis ton profil DISC
4. Obtiens un retour personnalisé
5. Télécharge ton rapport PDF
""")
st.video("https://www.youtube.com/watch?v=TON_LIEN_VIDEO")

video_file = st.file_uploader("Téléverse ta vidéo ou audio de pitch :", type=["mp4", "mov", "m4a", "wav", "mp3"])

if video_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=video_file.name) as temp_file:
        temp_file.write(video_file.read())
        temp_file_path = temp_file.name

    st.success("Vidéo reçue. Transcription en cours...")

    try:
        transcription = transcribe_audio(temp_file_path)
        st.text_area("Transcription :", transcription, height=200)

        profile = st.selectbox(
            "Quel est ton profil DISC ?",
            ["Dominant (D)", "Influent (I)", "Stable (S)", "Conforme (C)"]
        )

        if profile and transcription:
            feedback = generate_feedback(transcription, profile)
            st.markdown("### Feedback IA personnalisé :")
            st.info(feedback)

            if st.button("Télécharger le rapport PDF"):
                pdf_bytes = create_pdf(transcription, profile, feedback)
                b64 = base64.b64encode(pdf_bytes).decode()
                href = f'<a href="data:application/pdf;base64,{b64}" download="genup2050_rapport.pdf">Clique ici pour télécharger ton rapport PDF</a>'
                st.markdown(href, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Erreur lors de la transcription : {e}")
