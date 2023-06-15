#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import streamlit as st
import FinanceDataReader as fdr
# import plotly.graph_objects as go
# import requests
# from bs4 import BeautifulSoup

def main():
    # 제목
    st.title("[주식 차트 대시보드]")
    st.title("KOSPI")
    st.subheader("KS11")
    
    stock = 'KS11'
    
    # 사용자로부터 시작 날짜와 종료 날짜 입력 받기
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input('시작 날짜')
    with col2:
        end_date = st.date_input('종료 날짜')
    
#     # 날짜를 문자열로 변환
#     start_date_str = start_date.strftime('%Y-%m-%d')
#     end_date_str = end_date.strftime('%Y-%m-%d')
    
    
#     # 데이터 생성
#     df = fdr.DataReader(stock, start_date_str, end_date_str)
    
    
    kospi = fdr.DataReader('KS11') 
    st.dataframe(kospi)
    
    # 라인 그래프 생성
    
    



if __name__ == "__main__":
    main()

                         
                         
                         
                         
                         
                         
