# Create virtual env => python -m venv demoenv
# activate => source demoenv/bin/activate
# pip freeze > requirement.txt.  ==> requiremnet 
import pandas as pd
import streamlit as st
import numpy as np
import joblib

# load model 
model = joblib.load('naive_byes.h5')


st.title('Heart Disease Prediction App')
st.write("Enter patient's information to predict the likelihood of heart disease.")

age = st.number_input('Age', min_value=1, max_value=120)
current_smoker = st.selectbox('Current Smoker', ['Yes', 'No'])
cigsPerDay = st.number_input('Cigarettes per Day', min_value=0, max_value=100)
BPMeds = st.selectbox('On Blood Pressure Medication', ['Yes', 'No'])
totChol = st.number_input('Total Cholesterol (mg/dL)', min_value=100, max_value=400)
sysBP = st.number_input('Systolic Blood Pressure (mmHg)', min_value=80, max_value=250)
diaBP = st.number_input('Diastolic Blood Pressure (mmHg)', min_value=50, max_value=150)
BMI = st.number_input('Body Mass Index (BMI)', min_value=10.0, max_value=50.0)
heartRate = st.number_input('Heart Rate (bpm)', min_value=30, max_value=200)
glucose = st.number_input('Glucose Level (mg/dL)', min_value=50, max_value=300)


#making prediction butto

if st.button('Predict'):
    # create array with input data and pass array to model for prediction
    input_data = np.array([[age,]])
    prediction = model.predict(input_data)

    #display the prediciton result 
    if prediction[0]==1:
        st.error('Have Heart Disease')
    else:
        st.success('No Heart Disease ')
