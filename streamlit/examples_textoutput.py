#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import streamlit as st
# import pandas as pd
# import numpy as np


# # st.title('저의 첫번째 Streamlit Dashboard에 오신것을 환영합니다.:sunglasses:')

# # st.header('이것은 헤더입니다.')

# # st.subheader('이것은 서브헤더입니다.')

# # st.caption('이것은 캡션입니다.')
# # st.caption('이렇게 조그만하고 옅게 쓰입니다.')

# # st.write('이것은 write기능이구요. 아래에 파이썬 코드를 입력해보겠습니다.')
# # sample_code ='''
# # def sum_list(list):
# #     return sum(list)
# # '''
# # st.code(sample_code, language = 'python')


# # st.text('이것은 일반 텍스트입니다.')
# # st.write('이것은 write이구요. 차이가 있나요?')

# # st.text('제가 지금까지 썼던 것들은 st.title, st.header, st.subheader, st.caption, st.write, st.text, st.code + language 이정도네요.')
# # st.write('제가 지금까지 썼던 것들은 st.title, st.header, st.subheader, st.caption, st.write, st.text, st.code + language 이정도네요.')

# # st.latex('\sqrt{x^2 + y^2}= 1')


# dataframe = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40],
# })


# st.dataframe(dataframe, use_container_width=False)

# st.table(dataframe)

# st.metric(label='온도', value='10°C', delta='1.2')
# st.metric(label='SK하이닉스', value='61,000원', delta='-12,000원')

# st.header('주식 : :tired_face:')
# col1, col2, col3, col4 = st.columns(4)
# col1.metric(label='SK하이닉스', value='61,000원', delta='-12,000원')
# col2.metric(label='삼성전자', value='120,000원', delta='30,000원')
# col3.metric(label='(주)우아한형제들', value='30,000원', delta='-30,000원')
# col4.metric(label='LGCNS', value='120,000원', delta='3000원')

# st.header('날씨 : :sunglasses:')
# coll1, coll2 = st.columns(2)
# coll1.metric(label='오늘날씨', value='10°C', delta='1.2°C')
# coll2.metric(label='내일날씨', value='15°C', delta='5°C')


# ############

# import numpy as np
# import matplotlib.pyplot as plt

# # Fixing random state for reproducibility
# np.random.seed(19680801)

# dt = 0.01
# t = np.arange(0, 30, dt)
# nse1 = np.random.randn(len(t))                 # white noise 1
# nse2 = np.random.randn(len(t))                 # white noise 2

# # Two signals with a coherent part at 10 Hz and a random part
# s1 = np.sin(2 * np.pi * 10 * t) + nse1
# s2 = np.sin(2 * np.pi * 10 * t) + nse2

# fig, axs = plt.subplots(2, 1)
# axs[0].plot(t, s1, t, s2)
# axs[0].set_xlim(0, 2)
# axs[0].set_xlabel('Time')
# axs[0].set_ylabel('s1 and s2')
# axs[0].grid(True)

# cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
# axs[1].set_ylabel('Coherence')

# fig.tight_layout()

# st.pyplot(fig)


# ###############

# labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# men_means = [20, 35, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]
# men_std = [2, 3, 4, 1, 2]
# women_std = [3, 5, 2, 3, 3]
# width = 0.35       # the width of the bars: can also be len(x) sequence

# fig, ax = plt.subplots()

# ax.bar(labels, men_means, width, yerr=men_std, label='Men')
# ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
#        label='Women')

# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.legend()

# st.pyplot(fig)


from datetime import datetime
import streamlit as st
import time
import pandas as pd

st.title("Streamlit Deploy Test")

st.markdown(
"""
Hello Likelions,

This is a demo of Streamlit deployment.

""")

name = st.text_input("What's your name?", "Lion")

date = st.date_input("Choose a date", datetime.now().date())


st.markdown(f"## Hello {name}!\n## The date is {date.strftime('%Y-%m-%d')}")



st.subheader("A cached dataframe")

@st.cache_data()
def get_data(date):
    for i in range(10):
        time.sleep(0.1)
    return pd.DataFrame(
        {"date": pd.date_range(date, periods=3), "c": [7, 8, 5], "d": [10, 11, 7]}
    ).set_index("date")


df = get_data(date)
st.write(df)

