import streamlit as st
import xgboost
import sklearn
import pandas as pd
import joblib
import numpy as np
def app():
    data=pd.read_csv("asd (1).csv")
    st.title('Predict')
    model=st.radio("Select the Model using which you Want to Make Prediction",("RandomForestClassifier","XGBoostClassifier"))
    Sex=st.radio("Select the Gender",("Male","Female"))
    Age=st.number_input(min_value=25,max_value=80,label='Age in (years)')
    RestingBP=st.number_input(min_value=20,max_value=210,label="RestingBP in (mm Hg)")
    Cholesterol=st.number_input(min_value=30,max_value=650,label="Cholesterol in (mm/dl)")
    if(st.number_input(max_value=500,min_value=10,label="Fasting Blood Sugar Level in (mg/dl)")>120):
        FastingBS=1
    else:
        FastingBS=0
    RestingECG=st.radio("Select the RestingECG Type",("Normal","ST","LVH"))
    MaxHR=st.number_input(min_value=30,max_value=250,label="Heart Rate in (bpm)")
    ExerciseAngina=st.radio("Exercise induced angina",("Yes","No"))
    OldPeak=st.number_input(min_value=-3.0,max_value=7.0,label="Enter the value of ST")
    ST_Slope=st.radio("Enter the Slope of Peak Exercise ST segment",("Up","Flat","Down"))
    ChestPainType=st.radio("Enter the Type of Chest Pain",("TA","ATA","NAP","ASY"))
    xgboost=joblib.load('xgboostclf.sav')
    randomforest=joblib.load('rfc.sav')
    scaler=joblib.load('scaler.sav')
    if(st.button("Predict")):
        numerical_data=[Age,RestingBP,Cholesterol,FastingBS,MaxHR,OldPeak]
        numerical_data=scaler.transform(np.array(numerical_data).reshape(1,-1))[0].tolist()
        if(Sex=='Male'):
            numerical_data.append(1)
        else:
            numerical_data.append(0)
        if(ChestPainType=='ATA'):
            numerical_data.append(1)
        else:
            numerical_data.append(0)
        if(ChestPainType=='NAP'):
            numerical_data.append(1)
        else:
            numerical_data.append(0)
        if(ChestPainType=='TA'):
            numerical_data.append(1)
        else:
            numerical_data.append(0)
        if(RestingECG=='Normal'):
            numerical_data.append(1)
        else:
            numerical_data.append(0)
        if(RestingECG=='ST'):
            numerical_data.append(1)
        else:
            numerical_data.append(0)
        if(ExerciseAngina=='Y'):
            numerical_data.append(1)
        else:
            numerical_data.append(0)
        if(ST_Slope=='Flat'):
            numerical_data.append(1)
        else:
            numerical_data.append(0)
        if(ST_Slope=='Up'):
            numerical_data.append(1)
        else:
            numerical_data.append(0)
        input=np.array(numerical_data).reshape(1,-1)
        if(model=="XGBoostClassifier"):
            prediction=xgboost.predict(input)
        else:
            prediction=randomforest.predict(input)
        if(prediction==0):
            st.success("You are not having Heart Disease")
        else:
            st.error("Uh No! You may have Heart Disease. Please consult Doctor")
        st.write(input)
        st.write(model)
        
    


    