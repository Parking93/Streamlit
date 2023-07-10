#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.graph_objects as go

# 예시 1 
st.write('예시 1')

arr = np.random.normal(1, 1, size=100)

fig, ax = plt.subplots()

ax.hist(arr, bins=20,color='skyblue', alpha=1)

st.pyplot(fig)



# 예시 2 

st.write('예시 2')

arr = np.random.normal(1, 1, size=100)

fig, ax = plt.subplots()

sns.histplot(arr, bins=20, color='pink', kde=True)

st.pyplot(fig)



# 예시 3 

st.write('예시 3')

arr = np.random.normal(1, 1, size=100)

fig = go.Figure(data=[go.Histogram(x=arr, nbinsx=10, marker_color='green', opacity=0.7)])

st.plotly_chart(fig)













