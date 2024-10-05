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

