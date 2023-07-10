#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st

tab1, tab2 = st.tabs(["탭 이름 1", "탭 이름 2"])

tab1.write("이것은 첫 번째 탭입니다.") 

tab2.write("이것은 두 번째 탭입니다.")


import streamlit as st
import numpy as np

tab1, tab2 = st.tabs(["선그래프 탭", "데이터 탭"])
data = np.random.randn(10, 3)

with tab1:
    st.subheader("📈선그래프")
    st.line_chart(data)

with tab2:
    st.subheader("🗃데이터")
    st.dataframe(data)