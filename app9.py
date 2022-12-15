import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sb

def main() :
    st.title('차트 그리기')
    
    df = pd.read_csv('streamlit_data/iris.csv')
    
    st.dataframe(df.head())
    
    # sepal_length 와 sepal_width 의 관계를 차트로 그리시오
    fig = plt.figure()
    plt.scatter(data= df ,x='sepal_length' , y='sepal_width')
    plt.title('sepal Length Vs Width')
    plt.xlabel('sepal_length')
    plt.ylabel('sepal_width')
    st.pyplot(fig)
    
    fig2 = plt.figure()
    sb.regplot(data=df ,x='sepal_length' , y='sepal_width')
    st.pyplot(fig2)
    
    # 히스토그램
    # petal_length 로 히스토그램 그리기
    
    fig3 = plt.figure()
    plt.hist(data=df , x= 'petal_length' ,bins=10 ,rwidth=0.3 )
    st.pyplot(fig3)
    
    fig4 = plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.hist(data=df , x= 'petal_length' ,bins=10 ,rwidth=0.3 )
    
    plt.subplot(1,2,2)
    plt.hist(data=df , x= 'petal_length' ,bins=20 ,rwidth=0.3 )
    
    st.pyplot(fig4)
    
    ###우리가 주피터노트북에서 그렸던 ,  plt,sb차트는
    ### 스트림릿에서 표시하려면 plt.figure로 먼저 영역을 잡아주고 
    ### st.pyplot()함수로 웹 화면에 그려준다.
   
    ### 그리고 데이터프레임의 내장차트도 마찬가지로 해준다.
    
    
    # df의 species 컬럼의 각 종별로 몇개의 데이터가 있는지 차트로 나타내시오
    fig5 = plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig5)
    
    fig6 = plt.figure()
    df['배고파죽겠다...........']
    

if __name__ == '__main__' :
    main()