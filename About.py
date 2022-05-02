import streamlit as st
from PIL import Image
def app():
    st.title("About")
    image1=Image.open('unnamed-modified.png')
    col1,col2,col3=st.columns(3)
    col1.image(image1)
    col1.subheader("Kartik Chhipa")
    col1.write("B20CS084")
    col1.write("Computer Science and Engineering")
    image2=Image.open('WhatsApp Image 2022-05-02 at 7.30.05 PM-modified.png')
    col2.image(image2)
    col2.subheader("Rushil Shah")
    col2.write("B20AI036")
    col2.write("Artificial Intelligence and Data Science")
    image3=Image.open('WhatsApp Image 2022-05-02 at 9.07.01 PM-modified.png')
    col3.image(image3)
    col3.subheader("Ruthvik K")
    col3.write("B20CS037")
    col3.write("Artificial Intelligence and Data Science")

    