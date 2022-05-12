import streamlit as st
import os
import pandas as pd

def exsisting_customer(customerID,data):



    new = data.where(data['customerID'] == customerID)
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
        
   # NB still to add:
   # add in an error message if an incorrect customer ID is entered

