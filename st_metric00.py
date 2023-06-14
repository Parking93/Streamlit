#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
st.write('---')


st.metric(label="Temperature", value="70 °F")


st.write('---')



# delta가 양수인 경우 


st.metric(label='Temperature', value="70 °F", delta="1.2 °F")

st.write('---')

# delta가 음수인 경우 

st.metric(label='Temperature', value="70 °F", delta="-1.2 °F")

st.write('---')

# delta_color='normal'


st.metric(label='Temperature', value="70 °F", delta="1.2 °F", delta_color='normal')
st.metric(label='Temperature', value="70 °F", delta="-1.2 °F", delta_color='normal')

st.write('---')

# delta_color='inverse'


st.metric(label='Temperature', value="70 °F", delta="1.2 °F", delta_color='inverse')
st.metric(label='Temperature', value="70 °F", delta="-1.2 °F", delta_color='inverse')

st.write('---')

# delta_color='off'

st.metric(label='Temperature', value="70 °F", delta="-1.2 °F", delta_color='off')

st.write('---')

# help

st.metric(label='Temperature', value="70 °F", delta="1.2 °F", help='온도를 표시하는 매트릭입니다.')

st.write('---')

# label_visibility='hidden' or 'collapsed' or 

st.metric(label='Temperature', value="70 °F", delta="1.2 °F",label_visibility='hidden')

st.write('---')

st.metric(label='Temperature', value="70 °F", delta="1.2 °F",label_visibility='collapsed')

st.write('---')

# 온도 풍속 습도를 보여주는 매트릭 예시 1

col1, col2, col3 = st.columns(3)
col1.metric("온도", "25.4 °C", "1.2 °C")
col2.metric("풍속", "9 mph3", "-8%")
col3.metric("습도", "51%", "4%")

st.write('---')

# 달러 엔화 유로화를 보여주는 매트릭 예시 2

col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1,276.20 원", delta="-12.00원")
col2.metric(label="일본JPY", value="958.63 원", delta="-7.44 원")
col3.metric(label="유럽연합EUR", value="1,335.82 원", delta="11.44 원")

st.write('---')


import pandas as pd 
import os 

os.getcwd()+"city_location_korea.xlsx"

df = pd.read_excel('city_location_korea.xlsx')

st.dataframe(df)



































