#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import streamlit as st
import FinanceDataReader as fdr
# import plotly.graph_objects as go
# import requests
# from bs4 import BeautifulSoup
import matplotlib.pyplot as plt 
import koreanize_matplotlib


def main():
    # 제목
    st.title("주식 차트 대시보드")
    st.title("📈")
    st.subheader("삼성전자 VS SK 하이닉스")
    
    stock_list = ['삼성전자', 'sk하이닉스']
    stock = st.multiselect('종목을 선택해주세요.', stock_list) 
    stock_dict = {'삼성전자':'005930', 'sk하이닉스':'000660'}

    
    # 사용자로부터 시작 날짜와 종료 날짜 입력 받기
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input('시작 날짜')
    with col2:
        end_date = st.date_input('종료 날짜')
   
    
    # 날짜를 문자열로 변환
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')
    
    

    # 막대 그래프 생성
    for i in range(len(stock)):
        st.bar_chart(fdr.DataReader(stock_dict[i], start_date_str, end_date_str)['Close'])
    
    # # 라인 그래프 생성 with for문
    # for i in range(len(stock)):
    #     st.line_chart(fdr.DataReader(stock[i], start_date_str, end_date_str)['Close'])
        
    # # create matplotlib line     
    # for i in range(len(stock)):
    #     plt.plot(fdr.DataReader(stock[i], start_date_str, end_date_str)['Close'])
    # st.pyplot(plt)



    # # Tab 생성 
    # tab1, tab2, tab3 = st.tabs(['겹쳐진 그래프' , '개별 라인 그래프', '개별 막대 그래프'])
    # with tab1:
    #     for i in range(len(stock)):
    #         plt.plot(fdr.DataReader(stock[i], start_date_str, end_date_str)['Close'])
    #     st.pyplot(plt)
    # with tab2:
    #     for i in range(len(stock)):
    #         st.line_chart(fdr.DataReader(stock[i], start_date_str, end_date_str)['Close'])
    # with tab3:
    #     for i in range(len(stock)):
    #         st.bar_chart(fdr.DataReader(stock[i], start_date_str, end_date_str)['Close'])
    





if __name__ == "__main__":
    main()

                         
                         
                         
                         
                         
                         
