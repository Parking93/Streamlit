#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st

# delta_color='normal'
st.subheader("delta_color='normal'")

st.metric(label='Temperature', value="70 °F", delta="1.2 °F", delta_color='normal')
st.metric(label='Temperature', value="70 °F", delta="-1.2 °F", delta_color='normal')

# delta_color='inverse'
st.subheader("delta_color='inverse'")

st.metric(label='Temperature', value="70 °F", delta="1.2 °F", delta_color='inverse')
st.metric(label='Temperature', value="70 °F", delta="-1.2 °F", delta_color='inverse')

# delta_color='off'
st.subheader("delta_color='off'")

st.metric(label='Temperature', value="70 °F", delta="-1.2 °F", delta_color='off')