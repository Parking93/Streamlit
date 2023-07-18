#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from PIL import Image


image = Image.open("example.jpg")

st.image(image, caption="example", width=200, use_column_width="auto")

image = Image.open("example.jpg")

st.image(image, caption="width=100", width=100)


image = Image.open("example.jpg")

st.image(image, caption="example", width=200, use_column_width="auto")

# 동영상 파일을 로컬 경로에서 재생하는 예시
video_file = open("example.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)


# 동영상 파일을 로컬 경로에서 재생하는 예시
video_file = open("example1.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)


import streamlit as st

audio_file = open("example.mp3", "rb")

audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/mp3", start_time=5)


import numpy as np

sample_rate = 44100  # 44100 초당 샘플수
seconds = 2  # 2초 동안 음이 지속됩니다.
frequency_la = 440  # 재생할 음파를 나타냅니다.

t = np.linspace(0, seconds, seconds * sample_rate, False) 
note_la = np.sin(frequency_la * t * 2 * np.pi) #440 헤르쯔의 사인파를 만듭니다.

st.audio(note_la, sample_rate=sample_rate)




