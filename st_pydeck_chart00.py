#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#  서울 경도위도 좌표를 중심으로 만들어진 랜덤 데이터를 활용한 st.pydeck_chart 
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# 서울 경도 위도 좌표를 중심으로 랜덤 데이터를 활용한 st.pydeck_chart 
# ScatterplotLayer

# 서울시 좌표 중심으로 랜덤 데이터 생성
np.random.seed(100)
df = pd.DataFrame(
    np.random.randn(1000, 2) / [20, 20] + [37.57, 126.98],
    columns=['lat', 'lon'])

# ScatterplotLayer로 시각화
layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position=['lon', 'lat'],
    get_radius=200,
    get_color=[255, 0, 0],
)

# Deck 객체 생성
deck = pdk.Deck(
    map_style='light',
    layers=[layer],
    initial_view_state=pdk.ViewState(
        latitude=37.57,
        longitude=126.98,
        zoom=10,
        pitch=50,
    ),
)

# PyDeck 차트 출력
st.pydeck_chart(deck)


# 서울 경도 위도 좌표를 중심으로 랜덤 데이터를 활용한 st.pydeck_chart 
# HexagonLayer
st.write('---')

# 서울시 좌표 중심으로 랜덤 데이터 생성
np.random.seed(100)
df = pd.DataFrame(
    np.random.randn(1000, 2) / [20, 20] + [37.57, 126.98],
    columns=['lat', 'lon'])

# HexagonLayer로 시각화
layer = pdk.Layer(
    "HexagonLayer",
    data=df,
    get_position=['lon', 'lat'],
    radius=200,
    elevation_scale=4,
    elevation_range=[100, 1000],
    pickable=False,
    extruded=True,
)

# Deck 객체 생성
deck = pdk.Deck(
    map_style='light',
    layers=[layer],
    initial_view_state=pdk.ViewState(
        latitude=37.57,
        longitude=126.98,
        zoom=10,
        pitch=50,
    ),
)

# PyDeck 차트 출력
st.pydeck_chart(deck)

# 서울 경도 위도 좌표를 중심으로 랜덤 데이터를 활용한 st.pydeck_chart   
# HeatmapLayer
st.write('---')

# 서울시 좌표 중심으로 랜덤 데이터 생성
df = pd.DataFrame(
    np.random.randn(1000, 2) / [20, 20] + [37.57, 126.98],
    columns=['lat', 'lon'])

# HexagonLayer로 시각화
layer = pdk.Layer(
    "HeatmapLayer",
    data=df,
    get_position=['lon', 'lat'],
)

# Deck 객체 생성
deck = pdk.Deck(
    map_style='light',
    layers=[layer],
    initial_view_state=pdk.ViewState(
        latitude=37.57,
        longitude=126.98,
        zoom=10,
        pitch=50,
    ),
)

# PyDeck 차트 출력
st.pydeck_chart(deck)

st.write('---')
