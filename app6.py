import streamlit as st
import pandas as pd

def main() :
  

    # 텍스트를 입력받는 방법
    name = st.text_input('이름을 입력하세요')
    st.title(name)
    
    
    name2 = st.text_input('이름 입력! ' , max_chars=5)
    st.title(name2)
    
    message = st.text_area('메세지를 입력하시오' , height=2)
    st.text(message)
    
    # 숫자 입력 받는 방법 ( ,  최대값 , 최소값)
    year = st.number_input('출생년도를 입력하세요' , 1 , 10000 )
    st.text(year)
    
    number = st.number_input('실수를 입력하세요' , 0.5 ,100.0 , step= 0.3)
    
    # 날짜 입력 받는 방법
    my_date = st.date_input('날짜를 입력하시오')
    st.title(my_date)
    st.text(my_date.strftime('%Y년 %m월 %d일'))
    
    # 시간 입력 받는 방법
    my_time = st.time_input('약속 시간을 입력 하시오')
    st.text(my_time)
    st.text(my_time.strftime('%H:%M'))
    
    # 비밀번호를 입력 받는 방법
    st.text_input('비밀번호 입력' , type='password')

    # 색깔 입력(색깔은 16진수로 표현 , R G B )
    color = st.color_picker('색을 선택하시오')

    st.text(color)
    
    
    
    
if __name__ == '__main__' :
    main()