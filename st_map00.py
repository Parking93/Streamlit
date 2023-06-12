#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# 서울 경도위도를 중심으로 만들어진 랜덤 데이터를 활용한 st.map 1
import streamlit as st
import pandas as pd
import numpy as np

st.header('st.map')
st.write('서울 경도위도를 중심으로 만들어진 랜덤 데이터를 활용한 st.map')
st.caption('st.map(df)')

df = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [37.57, 126.98],
    columns=['lat', 'lon'])

st.map(df)

st.write('---')



# 서울 경도위도를 중심으로 만들어진 랜덤 데이터를 활용한 st.map 2


st.write('서울 경도위도를 중심으로 만들어진 랜덤 데이터를 활용한 st.map')
st.caption('st.map(df, zoom=10, use_container_width=True)')

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.57, 126.98],
    columns=['lat', 'lon'])

st.map(df, zoom=10, use_container_width=True)

st.write('---')



# 전국 시도 좌표 데이터를 활용한 st.map 3 (예시)

st.subheader('예시1')
st.write('전국 시도 위치 데이터를 활용한 st.map')

df = pd.read_excel('city_location_korea.xlsx')
                   

st.map(df, zoom = 5.7)

st.write('---')

# 2022년 한반도에 지진이 발생한 위치 데이터를 활용한 st.map 4(예시)
# 출처: 기상청 기상자료개방포털
st.subheader('예시2')
st.write('2022년에 지진이 발생한 위치 데이터를 활용한 st.map')

df = pd.read_csv('earthquake(2022).csv')

st.map(df, zoom = 5)

st.write('---')

# 스타벅스 데이터를 활용한 st.map 5 (예시)

st.subheader('예시3')
st.write('서울 내에 스타벅스 매장 위치 데이터를 활용한 st.map')

df = pd.read_excel('starbucks_seoul.xlsx')

st.map(df, zoom = 10)

st.write('---')










