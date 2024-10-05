import streamlit as st
st.write('Hello world!')

#버튼
st.header('st.button')

if st.button('sujeong hello'):
     st.write('sunwoong love')
else:
     st.write('Goodbye')


import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# 예제 1

st.write('Hello, *World!* :sunglasses:')

# 예제 2

st.write(1234)

# 예제 3

df = pd.DataFrame({
     '첫 번째 컬럼': [1, 2, 3, 4],
     '두 번째 컬럼': [10, 20, 30, 40]
     })
st.write(df)

# 예제 4

st.write('아래는 DataFrame입니다.', df, '위는 dataframe입니다.')

# 예제 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

# st.markdown
# st.header
# st.subheader
# st.caption
# st.text
# st.latex
# st.code

import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# 예제 1

st.subheader('Slider')

age = st.slider('당신의 나이는?', 0, 130, 25)
st.write("나는 ", age, '살입니다')

# 예제 2

st.subheader('범위 슬라이더')

values = st.slider(
     '값의 범위를 선택하세요',
     0.0, 100.0, (25.0, 75.0))
st.write('값:', values)

# 예제 3

st.subheader('시간 범위 슬라이더')

appointment = st.slider(
     "약속을 예약하세요:",
     value=(time(11, 30), time(12, 45)))
st.write("예약된 시간:", appointment)

# 예제 4

st.subheader('날짜 및 시간 슬라이더')

start_time = st.slider(
     "언제 시작하시겠습니까?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("시작 시간:", start_time)

# st.select_slider

st.header('라인 차트')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


import streamlit as st


#select box
st.header('st.selectbox')

option = st.selectbox(
     '가장 좋아하는 색상은 무엇인가요?',
     ('파랑', '빨강', '초록'))

st.write('당신이 좋아하는 색상은 ', option)

#multiselect
st.header('st.multiselect')

options = st.multiselect(
     '가장 좋아하는 색상은 무엇인가요',
     ['초록', '노랑', '빨강', '파랑'],
     ['노랑', '빨강'])

st.write('당신이 선택한 색상:', options)

#checkbox
st.header('st.checkbox')

st.write ('주문하고 싶은 것이 무엇인가요?')

icecream = st.checkbox('아이스크림')
coffee = st.checkbox('커피')
cola = st.checkbox('콜라')

if icecream:
     st.write("좋아요! 여기 더 많은 🍦")

if coffee: 
     st.write("알겠습니다, 여기 커피 있어요 ☕")

if cola:
     st.write("여기 있어요 🥤")

#latex
st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

st.title('Streamlit 앱의 테마 사용자 정의하기')

st.write('이 앱의 `.streamlit/config.toml` 파일 내용')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('숫자를 선택하세요:', 0, 10, 5)
st.write('슬라이더 위젯에서 선택된 숫자:', number)
