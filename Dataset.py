import streamlit as st
import pandas as pd
import plotly.express as px
def app():
    st.title('Dataset')
    st.header('Meet and Greet the Dataset')
    data=pd.read_csv('https://raw.githubusercontent.com/KartikChhipa01/datasets/main/heart.csv')
    st.dataframe(data)
    st.header('Dataset Features Explanation')
    st.write("Age - age of the person in years")
    st.write("Sex - sex of the person (M: Male, F: Female)")
    st.write("  ChestPainType - chest pain type (TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic)")
    st.write("RestingBP: resting blood pressure (mm Hg)")
    st.write("Cholesterol: serum cholesterol (mm/dl)")
    st.write("FastingBS: fasting blood sugar (1: if FastingBS > 120 mg/dl, 0: otherwise)")
    st.write("RestingECG: resting electrocardiogram results (Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria)")
    st.write("MaxHR: maximum heart rate (Numeric value between 60 and 202)")
    st.write("ExerciseAngina: exercise-induced angina (Y: Yes, N: No)")
    st.write("Oldpeak: oldpeak = ST (Numeric value measured in depression)")
    st.write("ST_Slope: the slope of the peak exercise ST segment (Up: upsloping, Flat: flat, Down: downsloping)")
    st.write("HeartDisease: output class (1: Heart Disease, 0: No Heart Disease)"")")
    df_copy=data.copy()
    df_copy['HeartDisease']=df_copy['HeartDisease'].map({1:'HeartDisease',0:'No HeartDisease'})
    df_copy['Sex']=df_copy['Sex'].map({'M':'Male','F':'Female'})
    fig1=px.sunburst(df_copy,path=['HeartDisease','Sex'],color='HeartDisease',color_discrete_map={'HeartDisease':'#0e2756',
    'No HeartDisease':'#0853c5','Male':'#95d3ff','Female':'#e1f9ff'},title='Sex',width=400,height=400)
    fig1.update_traces(textinfo='label+percent parent',name='Sex')
    fig1.update_layout()
    st.plotly_chart(fig1)
    fig2=px.sunburst(df_copy,path=['HeartDisease','ExerciseAngina'],color='HeartDisease',color_discrete_map={'HeartDisease':'#0e2756',
    'No HeartDisease':'#0853c5','Y':'#95d3ff','N':'#e1f9ff'},title='ExerciseAngina',width=400,height=400)
    fig2.update_traces(textinfo='label+percent parent',name='ExerciseAngina')
    fig2.update_layout()
    st.plotly_chart(fig2)
    fig4=px.histogram(df_copy,color='ST_Slope',x='HeartDisease',barmode='group',color_discrete_map={'Up':'#0e2756',
    'Flat':'#0853c5','Down':'#088cff'},opacity=0.8,height=500,width=500,title='Heart Disease vs ST_Slope')
    fig4.update_traces()
    st.plotly_chart(fig4)
    fig5=px.histogram(df_copy,color='HeartDisease',x='ChestPainType',barmode='group',color_discrete_map={'HeartDisease':'#0e2756',
    'No HeartDisease':'#0853c5'},opacity=0.8,height=500,width=700,title='Chest Pain Type vs Heart Disease')
    st.plotly_chart(fig5)