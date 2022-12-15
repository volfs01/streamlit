# 웹에서만 쓸 수 있는 차트
import streamlit as st
import plotly.express as px 
import pandas as pd
# altair 라이브러리
import altair as alt

def main() :
    df = pd.read_csv('streamlit_data/lang_data.csv')

    st.dataframe(df.head())
    column_menu = df.columns[1 : ]
    choice_list = st.multiselect('프로그래밍 언어를 선택하세요' , column_menu)
    if len(choice_list) != 0 :
        # 유저가 선택한 언어만 차트를 그린다.
        df_selected = df[choice_list]
        ## streamlit에서 제공하는 라인차트
        st.line_chart(df_selected)
        ## streamlit에서 제공하는 영역차트
        st.area_chart(df_selected)
        ## streamlit에서 제공하는 bar차트
        st.bar_chart(df_selected)
    if len(choice_list) != 0 :
        df2 = pd.read_csv('streamlit_data/iris.csv')
        
        ### altair 라이브러리의 mark_cicle 함수 사용법 
        chart = alt.Chart(df2).mark_circle().encode(
            x='petal_length', 
            y='petal_width' ,
            color ='species'
        )
    
        st.altair_chart(chart)
        
        ### 위치정보를 지도에 표시하는 방법
        ### 스트림릿의 map차트 
        df3 = pd.read_csv('streamlit_data/location.csv', index_col=0)
        
        st.dataframe(df3.head(3))
        
        st.map(df3,zoom=10)
        
        df4 = pd.read_csv('streamlit_data/prog_languages_data.csv',index_col=0)
        
        st.dataframe(df4.head(3))
        
        ### plotly의 pie차트 그리는 방법 
        fig6 = px.pie(df4,'lang' , 'Sum' ,title= '각 언어별 파이차트')
        
        st.plotly_chart(fig6)
        ### plotly의 bar 차트 그리는 방법
        df_sorted = df4.sort_values('Sum' , ascending= False)
        fig7 = px.bar(df_sorted , x= 'lang' ,y='Sum')
        st.plotly_chart(fig7)
        
        st.dataframe(df4)
        
if __name__ == '__main__' :
    main()