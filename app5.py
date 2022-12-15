import streamlit as st
import pandas as pd

# 이미지 처리를 위한 라이브러리 
from PIL import Image

def main() :
    img = Image.open('streamlit_data/image_03.jpg')

    print(img)
    st.image(img)
    
    st.image(img , use_column_width=True)
    
    image_url = 'https://t1.daumcdn.net/cfile/tistory/181FDB3650BC8ABA24'
    
    st.image(image_url)
    
    # 동영상
    video_file = open('streamlit_data/secret_of_success.mp4' , 'rb')
    
    st.video(video_file)
    
    
if __name__ == '__main__' :
    main()