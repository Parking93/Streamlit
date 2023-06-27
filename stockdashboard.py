#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import FinanceDataReader as fdr
import matplotlib.pyplot as plt 
import koreanize_matplotlib
import datetime 
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def main():
    # 제목
    st.title("주식 차트 대시보드")


    # 주식 시장 종목 선택 

    market = st.selectbox("주식시장을 선택하세요", ["KRX", "KOSPI", "KOSDAQ", "KONEX"])
    df = fdr.StockListing(market)
    st.write((df['Marcap'][:10])[::-1])
    
    
    fig = go.Figure(data=go.Bar(
    x=df['Marcap'][:10],
    y=df['Name'][:10],
    orientation='h',
    ))
    st.plotly_chart(fig)



    

    # 종목 선택 

    kospi_list = fdr.StockListing('KOSPI')
    stocks = kospi_list['Name'].tolist()
    stock = st.multiselect('종목을 선택해주세요.', stocks) 

    stock_list = []
    for i in stock:
        stock_list.append(kospi_list['Code'][kospi_list['Name'] == i].values[0])
    
    # 사용자로부터 시작 날짜와 종료 날짜 입력 받기
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input('시작 날짜', datetime.date(2022,1,1))
    with col2:
        end_date = st.date_input('종료 날짜')
   
    # 날짜를 문자열로 변환
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')


    
    # 매트릭 생성 
    for i in range(len(stock_list)):
        stock_value1 = fdr.DataReader(stock_list[i], start_date_str, end_date_str)["Close"].iloc[-1] # 종료 날짜의 해당 주식 종가
        stock_value2 = fdr.DataReader(stock_list[i], start_date_str, end_date_str)["Close"].iloc[-2] # 종료 날짜 전날의 해당 주식 종가
        st.metric(label=f'{stock[i]}', value=f'{stock_value1}원', delta = f'{stock_value1 - stock_value2}원')
                  



    # Tab 생성 
    tab1, tab2 = st.tabs(['라인 그래프', '캔들스틱 그래프'])
    with tab1:
        st.subheader('📈라인 그래프')
        
        df = fdr.DataReader('KRX:'+','.join(stock_list), start_date_str, end_date_str)

        if len(stock) == 1:
            pass
        if len(stock) >= 2:
            df.columns = stock
            st.line_chart(df)
        
  
        for i in range(len(stock_list)):
            st.subheader(f'{stock[i]}')
            st.line_chart(fdr.DataReader(stock_list[i], start_date_str, end_date_str)['Close'])
   
    with tab2:
        st.subheader('캔들스틱 그래프')

        for i in range(len(stock_list)):
            st.subheader(f'{stock[i]}')
            df = fdr.DataReader(stock_list[i], start_date_str, end_date_str)
            fig = go.Figure(data=[go.Candlestick(x=df.index,
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'])])
            st.plotly_chart(fig)


                       
if __name__ == "__main__":
    main()
                         
                         
                         
                         
