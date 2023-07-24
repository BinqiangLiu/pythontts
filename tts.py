#参考资料：https://medium.com/@pavlo_sydorenko/add-text-to-speech-to-your-web-app-with-5-lines-of-python-code-8c4707f2dc93
#https://github.com/pndurette/gTTS/tree/main
#https://gtts.readthedocs.io/en/latest/

import streamlit as st

#给定音频文件，让st.audio直接播放mp3_file_path = "./PythonTTS.mp3"
st.write("st.audio直接播放和app位于同一目录下的指定音频文件")
mp3_file_path = "PythonTTS.mp3"
with open(mp3_file_path, "rb") as file:
    audio_file = file.read()
st.audio(audio_file)

#但是，这个app是要测试tts即text to speech而不只是st.audio的音频播放功能
#下面用Google的gtts测试
st.write("Google gtts Function Test")

from gtts import gTTS
from io import BytesIO

mp3_fp = BytesIO()
text_input = st.text_input("请在下方文本框中输入要转换为语音的文本", value="请输入要转换为语音的文本")
tts = gTTS(text_input, lang='zh-TW')
tts.write_to_fp(mp3_fp)
st.write('mp3_fp')
# Playing sound directly
# Load `mp3_fp` as an mp3 file in
# the audio library of your choice

tts.save('ttsAudio.mp3')
st.write("---")

import streamlit as st
st.audio('ttsAudio.mp3')

#新增一个按钮测试直接播放语音文件
st.write("再测试增加一个按钮控制播放指定的音频文件（该文件同样是预先上传到与Streamlit app相同的根目录之下的某个位置（可以和app主程序位置不同）")
if st.button("直接播放上传语音文件"):
    st.audio("./audiofiles/xxxzyj.mp3")
