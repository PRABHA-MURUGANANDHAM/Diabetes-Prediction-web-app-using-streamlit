# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 18:47:27 2024

@author: muruga
"""

import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open('C:/Users/muruga/Downloads/MLpart 5/trained_model.sav','rb'))
# creating a function for prediction
def diabetes_prediction(input_data):
    
    input_data_as_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_array.reshape(1,-1)
    prediction =loaded_model.predict(input_data_reshaped)
    print(prediction)
    if(prediction[0] == 0):
      return "The person is not diabetic"
    else:
      return "The person is diabetic"
  
    
def main():
    
    #title of the web app
    st.title('Diabetes Prediction Web app')
    #getting the values from the user
    Pregnancies=st.text_input('No of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('BloodPressure level')
    SkinThickness = st.text_input('SkinThickness value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
    Age = st.text_input('Age of the person')
    
    #code for prediction
    diagnosis = ''
    #creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
        st.success(diagnosis)
if __name__ == '__main__':
    main()
    