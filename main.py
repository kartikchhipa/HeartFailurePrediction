import streamlit as st
import Predict
import Dataset
import Intro
import About
import streamlit as st
PAGES={
    "Introduction": Intro,
    "Dataset": Dataset,
    "Predict":Predict,
    "About":About   
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)