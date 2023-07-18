#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from PIL import Image


image = Image.open("example.jpg")

st.image(image, caption="example", width=200, use_column_width="auto")

image = Image.open("example.jpg")

st.image(image, caption="width=100", width=100)


image = Image.open("example.jpg")

st.image(image, caption="example", width=200, use_column_width="auto")















