from faulthandler import cancel_dump_traceback_later
import streamlit as st
import numpy as np
import pandas as pd
import plotly as pl

#Creating sections of primary page to sort app layout
header = st.container()
dataset = st.container()
new_customer_reg = st.container()
customer_churn = st.container()

#Chaching dataset to improve runtime of app
@st.cache
def get_data(filename):
    cc_data = pd.read_csv('data\WA_Fn-UseC_-Telco-Customer-Churn.csv')
    
    return (cc_data)

with header:
    st.title('Customer churn app')
    st.text('This is an app where customer churn data is presented. You can register new customers and know imediatly if they are likekly to churn. This way you can start different initiatives towards those customers and make them loyal to the company.')

with dataset:
    st.subheader('Customer churn dataset')
    st.text('The dataset is downloaded from kaggle.com')
    
    cc_data = get_data('data\WA_Fn-UseC_-Telco-Customer-Churn.csv')
    st.dataframe(cc_data.head())

with new_customer_reg:
    gender = ['Female', 'Male']
    partner_status = ['Partner', 'No partner']
    paperless = ['Yes', 'No']
    
    with st.sidebar.form('reg_form'):
        st.title('Register a new customer')
        gender_val = st.radio('Selecet gender', 
                            gender)
        partner_val = st.radio('Selecet partner status', 
                            partner_status)
        tenure_val = st.number_input('Select years of tenure', 
                                    min_value = 0, 
                                    max_value = 100, 
                                    value = 0, 
                                    help = 'Insert number between 0 and 100')
        paperless_val = st.radio('Paperless billing', paperless)
    
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)

with customer_churn:
   st.subheader('This is a plot') 