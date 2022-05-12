from exsisting_customer import exsisting_customer
from new_customer import new_customer
import streamlit as st
import requests
import json
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import os

# add the data set used as the train dataset which will be the exsisiting customers 
#(at the moment it is the full dataset that is added)



#Creating sections of primary page to sort app layout
header = st.container()
dataset = st.container()
customer_reg = st.container()
customer_churn = st.container()


@st.cache
def get_data(dir_path):
    cc_data = pd.read_csv(dir_path)
    return (cc_data)

dir_path =os.path.join(os.getcwd(),'\data\WA_Fn-UseC_-Telco-Customer-Churn.csv') 

cc_data =get_data('data\WA_Fn-UseC_-Telco-Customer-Churn.csv')

st.title('Customer Churn Prediction')

selected = option_menu(
    menu_title = None,
    options =['New Customer','Exisiting Customer'],
    icons =['person-plus-fill','person-fill'],
    orientation = 'horizontal',
    default_index =1,
    )


if selected =='New Customer':
    new_customer(data=cc_data)

if selected =='Exisiting Customer':
    st.subheader('Please enter customer ID')
    customerID = st.text_input('Customer ID')

    if st.button('Enter'):
        #exsisting_customer(customerID = customerID,data=cc_data)
        new = cc_data.where(cc_data['customerID'] == customerID)
        new = new.dropna()
        new =new.reset_index(drop=True)

        

        # Display the customer information
        st.subheader('Customer Information')
        st.table(new.iloc[: , :11])
        st.table (new.iloc[: , 11:20])

        # get and display if the customer will churn
        churn = new.loc[0,'Churn']

        if churn == 'Yes':
            st.error('This customer did churn')
                        
        else:
            st.success('This customer did not churn')

