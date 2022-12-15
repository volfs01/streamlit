import streamlit as st
import pandas as pd

# UI 요소들을 처리하는 방법
# 버튼, 라디오 버튼 , 셀렉트박스 , 멀티 셀렉트 , 슬라이더 

def main() :
    df = pd.read_csv('streamlit_data/iris.csv')
# 버튼을 클릭하면 데이터 프레임이 보이도록 만들라.
# 버튼을 누르는 순간 True로 바뀜
    if st.button('데이터 프레임 보기') :
        st.dataframe(df)
    
    name = 'Make'
    
    if st.button('대문자로') :
        st.text(name.upper())

    if st.button('소문자로') :
        st.text(name.lower())

    status = st.radio('정렬을 선택하세요', ['오름차순 정렬' , '내림차순 정렬 ','다른정렬'])
    
    if status == '오름차순정렬' :
        # df의 petal_length 컬럼을 오름차순으로 정렬해서 보여주시오
        st.dataframe(df.sort_values('petal_length'))
    elif   status == '내림차순정렬' :
        # df의 petal_length 컬럼을 내림차순으로 정렬해서 보여주시오 
        st.dataframe(df.sort_values('petal_length' , ascending= False))   

    
    
    #체크박스를 체크하면 데이터 프레임이 나오고 
    #해제하면 데이터프레임이 나오지 않게
    
    if st.checkbox('show/hide') :
        st.dataframe(df)
    else :
        st.write(' ')
    # 셀렉트 박스 : 여러개 중에 한개 선택 
    language = ['pythin' , 'Java' , 'C' , 'PHP' , 'GO']
    
    my_choice = st.selectbox('좋아하는 언어를 선택하세요' , language)
    
    # 유저가 선택하면, 해당 언어를 다음처럼 표시한다
    # 저는 python언어를 가장 좋아합니다.
    # 저는 Java 언어를 가장 좋아합니다.
    st.text('저는 ' + my_choice + ' 언어를 가장 좋아합니다.')
    
    # 만약 유저가 선택한 언어가 , 파이썬이나 ,PHP ,go언어이면 
    # 배우기 쉽습니다 .
    # 자바나 씨언어면
    # 배우기 어렵습니다.
    if my_choice in ['Java' , 'C'] :
        st.text('배우기어렵습니다.')
    else :
        st.text('배우기 쉽습니다.')
        
    # 여러개를 선택할 수 있게 하는 multiselect
    # 아이리스 데이터프레임의 컬럼이름을 가져오시오 
    
   
    selected_list = st.multiselect('원하는 컬럼을 선택하세요' , df.columns)
    # 유저가 컬럼을 선택하면 해당 컬럼을 화면에 보여주고
    # 유저가 아무 컬럼도 선택하지 않으면 데이터 프레임을 보여주지 않는다.
    if len(selected_list) == 0 :
        st.text('')
    else :
        st.dataframe(df[selected_list])
    
    # 슬라이더
    age = st.slider('나이' , 1 , 100)    
    
    st.text('당신이 선택한 나이는' + str(age) + '입니다')
    
    st.slider('데이터' ,1 , 200 , step=5)
    
    st.slider('데이터' , 1 ,value= 75)
    
    st.slider('데이터' , 0.0 ,1.0,step=0.1)
    
    with st.expander('hello') :
        st.text('안녕하세요~')
    
if __name__ == '__main__' :
    main()