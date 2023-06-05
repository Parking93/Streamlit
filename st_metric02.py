#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st


# delta가 양수인 경우 
st.subheader('delta가 양수인 경우')

st.metric(label='Temperature', value="70 °F", delta="1.2 °F")

# delta가 음수인 경우 
st.subheader('delta가 음수인 경우 ')

st.metric(label='Temperature', value="70 °F", delta="-1.2 °F")

# None 경우
# 이는 매트릭의 변화를 시각적으로 나타내지 않고, 단순히 현재 값을 표시하도록 설정하는 데 사용됩니다.
st.subheader('delta가 None인 경우')

st.metric(label='Temperature', value="70 °F", delta=None)
