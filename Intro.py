import streamlit as st
from PIL import Image
def app():
    st.title('Introduction')
    image=Image.open('heart.jpg')
    st.image(image,width=500)
    st.write('Machine Learning has witnessed a phenomenal growth in the sector of Medical Science. This web app was created as a part of the Course Project for Pattern Recognition and Machine Learning mentored by Professor Richa Singh. This App can predict the Heart Disease(Heart Failure) with maximum accuracy of 92% overall the machine learning models.')