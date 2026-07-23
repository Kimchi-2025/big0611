import streamlit as st
from streamlit_autorefresh import st_autorefresh

#1000ms(1초)마다 페이지 자동 새로고침
count = st_autorefresh(interval=1000, key="datarefresh")

# 제목과 헤더 만들기
st.title('이것은 가장 큰 제목입니다')
st.header('이것은 큰 헤더입니다')
st.subheader('이것은 작은 헤더입니다')


# 일반 텍스트 표시하기
st.text('이것은 일반적인 텍스트입니다')
st.text('여러 줄로 텍스트를 작성할 수도 있습니다')

# 마크다운으로 꾸미기
st.markdown('**이것은 굵은 글씨입니다**')
st.markdown('*이것은 기울어진 글씨입니다*')
st.markdown('이것은 `코드`처럼 보이는 글씨입니다')


# 만능 출력 함수
st.write('안녕하세요!')
st.write(123)

# 선택 상자 만들기 - 좋아하는 과일 선택
fruit = st.selectbox(
    '좋아하는 과일을 선택하세요',
    ['사과', '바나나', '오렌지', '포도']
)
st.write(f'당신이 선택한 과일은 {fruit}입니다')

# 텍스트 입력받기
name = st.text_input('이름을 입력하세요')
age = st.number_input('나이를 입력하세요', min_value=0, max_value=120)

if name and age:
    st.write(f'{name}님은 {age}살입니다')

# 슬라이더로 값 조정하기
temperature = st.slider('온도를 선택하세요', 0, 40, 25)
st.write(f'선택한 온도는 {temperature}도입니다')

# 체크박스
agree = st.checkbox('이용약관에 동의합니다')

if agree:
    st.write('동의해주셔서 감사합니다!')

# 여러 개 선택하기
hobbies = st.multiselect(
    '취미를 선택하세요 (여러 개 선택 가능)',
    ['독서', '영화감상', '운동', '여행', '음악감상']
)

if hobbies:
    st.write('선택한 취미:', hobbies)


# 날짜와 시간 입력
from datetime import datetime

today = st.date_input('날짜를 선택하세요')
current_time = st.time_input('시간을 선택하세요')

st.write(f'선택한 날짜: {today}')
st.write(f'선택한 시간: {current_time}')

# 인터넷 이미지 표시
st.image(r'C:\ajb\Python\Python_basic\images\1.jpg', caption='예시 이미지')

# 유튜브 비디오 표시
st.video('https://www.youtube.com/watch?v=dQw4w9WgXcQ')



# 유튜브 오디오 보관함
# 무료소리창고
