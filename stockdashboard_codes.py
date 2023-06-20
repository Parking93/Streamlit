#!/usr/bin/env python
# coding: utf-8

# In[ ]:





import streamlit as st

# 동영상 파일을 로컬 경로에서 재생하는 예시
video_file = open('example.mov', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)



video_file = open('example.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)






