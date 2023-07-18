#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np



# st.markdown 예시 1
st.markdown('#### *st.markdown 예시 1*')

st.markdown('Streamlit은 **_매우_ 훌륭하다**.')
st.markdown("이 문장은 :red[빨강], 그리고 이문장은 **:blue[파랑]** 그리고 볼드체이다.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] 피타고라스 항등식이다. :pencil:")

# st.markdown 예시 2
st.markdown('#### *st.markdown 예시 2*')

st.markdown(f"""## 안녕하세요
<font size=16>환영</font> 해요
""", unsafe_allow_html=True, help="unsafe_allow_html=True인 경우") # unsafe_allow_html가 True인 경우
st.markdown(f"""## 안녕하세요
<font size=16>환영</font> 해요
""", unsafe_allow_html=False, help="unsafe_allow_html=False인 경우") # unsafe_allow_html가 False인 경우



# st.title 예시 1
st.markdown('#### *st.title 예시 1*')

st.title("이것은 제목입니다.")
st.title("_이탤릭체 제목_ :blue[파랑색] 그리고 선글라스 이모지 :sunglasses:")

# st.title 예시 2
st.markdown('#### *st.title 예시 2*')

st.title("이것은 제목입니다", anchor="https://docs.streamlit.io/library/api-reference/text/st.title" , help="anchor 존재")  # anchor가 있는 경우
st.title('이것은 제목입니다', anchor=None) # anchor가 None인 경우



# st.header 예시 1
st.markdown('#### *st.header 예시 1*')

st.header("이것은 헤더입니다.")
st.header("_이탤릭체 헤더_ :red[빨강색] 그리고 선글라스 이모지 :sunglasses:")

# st.header 예시 2
st.markdown('#### *st.header 예시 2*')

st.header("이것은 헤더입니다.", anchor="https://docs.streamlit.io/library/api-reference/text/st.header" ,help="anchor 존재") # anchor가 있는 경우
st.header("이것은 헤더입니다.", anchor=None) # anchor가 None인 경우



# st.subheader 예시 1
st.markdown('#### *st.subheader 예시 1*')

st.subheader("이것은 서브헤더입니다.")
st.subheader("_이탤릭체 서브헤더_ :red[빨강색] 그리고 선글라스 이모지 :sunglasses:")

# st.subheader 예시 2
st.markdown('#### *st.subheader 예시 2*')

st.subheader("이것은 서브헤더입니다.", anchor="https://docs.streamlit.io/library/api-reference/text/st.subheader" ,help="anchor 존재") # anchor가 있는 경우
st.subheader("이것은 서브헤더입니다.", anchor=None) # anchor가 None 경우



# st.caption 예시 1
st.markdown('#### *st.caption 예시 1*')

st.caption("이것은 위의 내용을 설명하는 문자열입니다.")
st.caption("_이탤릭체 캡션_ :blue[파랑색] 그리고 이모티콘 :sunglasses:")

# st.caption 예시 2
st.markdown('#### *st.caption 예시 2*')

st.caption(f"""## 안녕하세요
<font size=16>환영</font> 해요
""", unsafe_allow_html=True, help="unsafe_allow_html=True인 경우") # unsafe_allow_html가 True인 경우
st.caption(f"""## 안녕하세요
<font size=16>환영</font> 해요
""", unsafe_allow_html=False, help="unsafe_allow_html=False인 경우") # unsafe_allow_html가 False인 경우



# st.code 예시 1
st.markdown('#### *st.code 예시 1*')

code = '''def text():
    print("안녕, Streamlit!")'''
st.code(code, language="python")

# st.code 예시 2
st.markdown('#### *st.code 예시 2*')

st.code("import streamlit as st", language="python", line_numbers=True) # line_numbers가 True인 경우
st.code("import streamlit as st", language="python", line_numbers=False) # line_numbers가 False인 경우



# st.text 예시 1
st.markdown('#### *st.text 예시 1*')

st.text("이것은 텍스트입니다.")

# st.text 예시 2
st.markdown('#### *st.text 예시 2*')

st.text("이것은 텍스트입니다.", help="help")



# st.latex 예시 1
st.markdown('#### *st.latex 예시 1*')

st.latex(r'''ax^3 + b x^2 + c x + d = 0''', help="3차 방정식")


# st.latex 예시 2
st.markdown('#### *st.latex 예시 2*')

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')



# st.divider 예시 1

st.markdown('#### *st.divider 예시 1*')

st.title("이것은 title입니다.")
st.header("이것은 header입니다.")
st.subheader("이것은 subheader입니다.")

st.divider()

code = '''def text():
    print("안녕, Streamlit!")'''
st.code(code, language="python")

st.divider()  

st.latex(r'''a + ar + a r^2 + a r^3''', help="3차 방정식")

st.divider()  



# st.image 예시 1
st.markdown('#### *st.image 예시 1*')
# st.image 예시 2
st.markdown('#### *st.image 예시 2*')
# st.image 예시 3
st.markdown('#### *st.image 예시 3*')


# st.audio 예시 1
st.markdown('#### *st.audio 예시 1*')
# st.audio 예시 2
st.markdown('#### *st.audio 예시 2*')


# st.video 예시 1
st.markdown('#### *st.video 예시 1*')
# st.video 예시 2
st.markdown('#### *st.video 예시 2*')


# st.dataframe 예시 1
st.markdown('#### *st.dataframe 예시 1*')
array = np.random.rand(10,5) # 배열 생성

df = pd.DataFrame(array, columns=["A", "B", "C", "D", "E"]) # 데이터 프레임 생성 

st.dataframe(df) # 데이터 프레임 출력

# st.dataframe 예시 2
st.markdown('#### *st.dataframe 예시 2*')

df_menu = pd.DataFrame({
    "메뉴명": ["아메리카노", "르완다 가토 케자 네추럴", "과테말라 아카테낭고 게이샤 워시드", "밀크티라떼"],
    "가격": [4500, 8000, 9000, 7500]
}) # 데이터 프레임 생성 

st.dataframe(df, width=10, height=50, use_container_width=True) # 데이터프레임 출력



# st.table 예시 1
st.markdown('#### *st.table 예시 1*')

st.markdown('#### *st.dataframe 예시 1*')
list_menu = ["Smoothie", "Coke", "Latte", "Americano", "Cake"] # 리스트 생성

st.table(list_menu) # 테이블 생성

# st.table 예시 2
st.markdown('#### *st.table 예시 2*')

array1 = np.random.randn(8, 4)
array2 = np.random.randint(1, 10, size=(8, 4)) # 배열 생성

st.table(array1) # 테이블 출력
st.table(array2)

# st.table 예시 3
st.markdown('#### *st.table 예시 3*')

df_cafe = pd.DataFrame({"메뉴명": ["Juice", "Americano", "Latte", "espresso"],
        "가격": [5000, 3000, 4000, 2000],
        "핫/아이스 가능 여부": ["불가능", "가능", "가능", "가능"]}) # 데이터프레임 생성

st.table(df_cafe) # 테이블 출력



# Pandas styler 예시 1: 데이터프레임 활용
st.markdown('#### *Pandas styler 예시 1: 데이터프레임 활용*')

df = pd.DataFrame(np.random.randint(0, 10, size=(5, 5)), columns=list("ABCDE"))

st.dataframe(df.style.highlight_max(axis=0)) 

# Pandas styler 예시 2: 데이터 프레임 활용 
st.markdown('#### *Pandas styler 예시 2: 데이터프레임 활용*')

df = pd.DataFrame(np.random.rand(10,5), columns=["A", "B", "C", "D", "E"])

st.dataframe(df.style.background_gradient())

# Pandas styler 예시 3: 테이블 활용 
st.markdown('#### *Pandas styler 예시 3: 테이블 활용 *')

df = pd.DataFrame(np.random.randn(10,4), columns=["A","B","C","D"])

st.table(df.style.bar())



# st.metric 예시 1
st.markdown('#### *st.metric 예시 1*')

col1, col2, col3 = st.columns(3)
col1.metric("온도", "25.4 °C", "1.2 °C")
col2.metric("풍속", "9 mph3", "-8%")
col3.metric("습도", "51%", "4%")

# st.metric 예시 2
st.markdown('#### *st.metric 예시 2*')

col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1,276.20 원", delta="-12.00원")
col2.metric(label="일본JPY", value="958.63 원", delta="-7.44 원")
col3.metric(label="유럽연합EUR", value="1,335.82 원", delta="11.44 원")




















