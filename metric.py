#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st


# 온도 풍속 습도를 보여주는 매트릭 예시 1
st.subheader('예시 1')

col1, col2, col3 = st.columns(3)
col1.metric("온도", "25.4 °C", "1.2 °C")
col2.metric("풍속", "9 mph3", "-8%")
col3.metric("습도", "51%", "4%")


# 달러 엔화 유로화를 보여주는 매트릭 예시 2
st.subheader('예시 2')

col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1,276.20 원", delta="-12.00원")
col2.metric(label="일본JPY", value="958.63 원", delta="-7.44 원")
col3.metric(label="유럽연합EUR", value="1,335.82 원", delta="11.44 원")











