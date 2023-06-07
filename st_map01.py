#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np


seoul_coords = [[37.57, 126.98]]

df = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [37.57, 126.98],
    columns=['lat', 'lon'])

st.map(df)


import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.57, 126.98],
    columns=['lat', 'lon'])

st.map(df, zoom=7, use_container_width=True)