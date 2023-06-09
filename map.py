#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import streamlit as st
import pandas as pd
import numpy as np

st.header('st.map')

# seed 설정 
np.random.seed(100)


# 예시 1
st.subheader('예시 1')

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.57, 126.98],
    columns=['lat', 'lon'])

st.map(df)


# 예시 2
st.subheader('예시 2')

locations = {
  '서울' : [37.566418, 126.977950],#서울시청
  '부산' : [35.180152, 129.074980],#부산시청
  '대구' : [35.871468, 128.601757],#대구시청
  '인천' : [37.456445, 126.705873],#인천시청
  '광주' : [35.160068, 126.851426],#광주광역시청
  '대전' : [36.350664, 127.384819],#대전시청
  '울산' : [35.539772, 129.311486],#울산시청
  '세종' : [36.480838, 127.289181],#세종시청
  '경기' : [37.275221, 127.009382],#경기도청
  '강원' : [37.885300, 127.729835],#강원(강원도청)
  '충북' : [36.635947, 127.491345],#충북도청
  '충남' : [36.658826, 126.672849],#충남도청
  '전북' : [35.820599, 127.108759],#전북도청
  '전남' : [34.816351, 126.462924],#전남도청
  '경북' : [36.574108, 128.509303],#경북도청
  '경남' : [35.238398, 128.692371],#경남도청
  '제주' : [33.3617007, 126.511657]#제주
    }

df_locations = pd.DataFrame(locations).T

df_locations.columns = ['lat', 'lon']

st.map(df_locations, zoom=5.5, use_container_width=True)








