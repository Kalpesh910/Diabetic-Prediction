# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 15:06:19 2023

@author: Kalpesh Somwanshi
"""

import numpy as np
import pickle 
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('C:/Users/Kalpesh Somwanshi/Documents/Diabetic Prediction/trained_model.sav','rb'))

#creating function for prediction

def diabetes_prediction(input_data):

    # changing the input data to a numpy_array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==0):
        return 'The person is not diabetic'
    else:
        return 'The person is a diabetic'
    
def main():
    
    
    # Giving a title
    st.title('Diabetes Prediction Web App')
    
    #Getting the input data from users
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text.input('Skin Thickness value')
    Insulin = st.text.input('Insulin Level')
    BMI = st.text.input('BMI value')
    DiabetesPedigreeFunction = st.text.input('Diabetes Pedigree Function')
    Age = st.text.input('Age of the person')


    # Code for Prediction
    diagnosis = ""
    
    # creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)

    st.success(diagnosis)
    
    
if __name__=='__main__':
    main()