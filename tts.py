# https://medium.com/@pavlo_sydorenko/add-text-to-speech-to-your-web-app-with-5-lines-of-python-code-8c4707f2dc93

import streamlit as st

#mp3_file_path = "./PythonTTS.mp3"
mp3_file_path = "PythonTTS.mp3"

with open(mp3_file_path, "rb") as file:
    audio_file = file.read()

st.audio(audio_file)

#新增一个按钮测试直接播放语音文件
if st.button("翻译文本转语音"):
    st.audio(/audiofiles/xxxzyj.mp3)
