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





















