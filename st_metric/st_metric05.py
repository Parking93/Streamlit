#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st


st.subheader("label_visibility = 'hidden'")
st.metric(label='Temperature', value="70 °F", delta="1.2 °F",label_visibility='hidden')

st.subheader("label_visibility = 'collapsed'")
st.metric(label='Temperature', value="70 °F", delta="1.2°F",label_visibility='collapsed')
