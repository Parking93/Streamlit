#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st

# help
st.subheader('help')

st.metric(label='Temperature', value="70 °F", delta="1.2 °F", help='온도를 보여줍니다.')


