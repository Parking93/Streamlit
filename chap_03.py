#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


image = Image.open("example.jpg")

st.image(image, caption="example", width=200, use_column_width="auto")




















