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







