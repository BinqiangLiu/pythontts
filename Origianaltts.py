# https://medium.com/@pavlo_sydorenko/add-text-to-speech-to-your-web-app-with-5-lines-of-python-code-8c4707f2dc93

import streamlit as st
from gtts import gTTS
from io import BytesIO

sound_file = BytesIO()
tts = gTTS('AStreamlit is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps.', lang='en')
tts.write_to_fp(sound_file)

st.audio(sound_file)
