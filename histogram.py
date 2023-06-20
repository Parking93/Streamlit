#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.write('---')

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20,color='skyblue', alpha=1)

st.pyplot(fig)


import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
st.write('---')

arr = np.random.normal(1, 1, size=100)

fig = plt.figure(figsize=(10,4))

sns.histplot(arr, bins=20, color='pink', kde=True)

st.pyplot(fig)


import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.write('---')

arr = np.random.normal(1, 1, size=100)

fig = go.Figure(data=[go.Histogram(x=arr, nbinsx=10, marker_color='skyblue', opacity=0.7)])

st.plotly_chart(fig)

st.write('---')














