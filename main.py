# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 18:35:29 2023

@author: Anand Chavan
"""

import streamlit as st
import joblib

def main():
    html_temp= """
    <div style = "background-color:lightblue;padding:16px">
    <h2 style = "color:black";text-align:center> Health Insurance Cost Prediction </h2>
    </div>
    
    """
    st.markdown (html_temp,unsafe_allow_html=True)
    
    model = joblib.load('model_Lr')
    p1 = st.slider('Enter Your Age',18,100)
    s1 = st.selectbox('sex',('Male','Female'))
    
    if s1 =='Male':
        p2=0
    else:
        p2=1
        
    p3 = st.number_input("Enter Your BMI Value")
    
    p4 = st.slider("Enter Number of Children",0,4)
    
    s2 = st.selectbox('Smoker',("Yes","No"))
    
    if s2 =='Yes':
        p5=1
    else:
        p5=0
        
    p6 = st.slider("Enter Your Region ",1,4)
    
    
    if st.button('Predict '):
        pred=model.predict([[p1,p2,p3,p4,p5,p6]])
        
        
        st.success('Your Insurance Premium is  {}'.format(round(pred[0]),2))
        
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()