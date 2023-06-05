#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st


st.metric(label="Temperature", value="70 °F")






# delta가 양수인 경우 
st.write('delta가 양수인 경우')

st.metric(label='Temperature', value="70 °F", delta="1.2 °F")

# delta가 음수인 경우 
st.write('delta가 음수인 경우 ')

st.metric(label='Temperature', value="70 °F", delta="-1.2 °F")
st.metric(label='Temperature', value="70 °F", delta="-1.2 °F")


# delta_color='normal'
st.write('delta_color="normal"')

st.metric(label='Temperature', value="70 °F", delta="1.2 °F", delta_color='normal')
st.metric(label='Temperature', value="70 °F", delta="-1.2 °F", delta_color='normal')

# delta_color='inverse'
st.write('delta_color="inverse"')

st.metric(label='Temperature', value="70 °F", delta="1.2 °F", delta_color='inverse')
st.metric(label='Temperature', value="70 °F", delta="-1.2 °F", delta_color='inverse')
# delta_color='off'
st.metric(label='Temperature', value="70 °F", delta="-1.2 °F", delta_color='off')


# help

st.metric(label='Temperature', value="70 °F", delta="1.2 °F", help='이건 help입니다.')



# label_visibility='hidden' or 'collapsed' or 

st.metric(label='Temperature', value="70 °F", delta="1.2 °F",label_visibility='hidden')

st.metric(label='Temperature', value="70 °F", delta="1.2 °F",label_visibility='collapsed')


st.markdown('---')


st.metric(label='Temperature', value="70 °F", delta="1.2 °F", label_visibility='hidden')
st.metric(label='Temperature', value="70 °F", delta="1.2 °F", label_visibility='collapsed')




















