import streamlit as st
import os
import pandas as pd
import json
import requests
import matplotlib.pyplot as plt

def app():
    st.header('Exisiting Customer')

    st.subheader("Enter customer ID to predict if the customer will claim.")

    st.write('Please enter an exsisting customer ID')

    @st.cache
    def get_data(dir_path):
        data = pd.read_csv(dir_path)
        return (data)

    data =get_data('data\Car_insurance_test_predictions.csv')
    data = data.drop(columns=['Unnamed: 0'])


    with st.form('customerID'):
        customerID =st.text_input('Customer ID')

        submitted= st.form_submit_button('Submit')

    if submitted:
        st.write(customerID)

        if int(customerID) in data['customerID'].unique().tolist():

            df = data.where(data['customerID'] == int(customerID))
            df = df.dropna()
            df =df.reset_index(drop=True)
        

            col1, col2 = st.columns(2)
            with col1:
                # Display the customer information
                st.subheader('Customer Information')
                customer_info = df.columns
                df2 =pd.DataFrame()
                temp = df.drop(columns=['OUTCOME','Claim_pred','Claim_prob','not_Claim_prob'])
                temp = temp.applymap(str)
                customer_info = temp.columns

                customer_info2 = temp.loc[0, :].values.tolist()

                df2['Customer Information']= customer_info
                df2['Value']= customer_info2
                st.table(df2)


        
            with col2:

                st.subheader('Customer Insurance Claim Prediction')
                if df.loc[0,'Claim_pred'] == 1:
                    st.error('It is predicted that the customer will claim insurance')
                    
                elif df.loc[0,'Claim_pred'] == False:
                    st.success('It is predicted that the customer will not claim insurance')
                
                # display the probablities
                st.subheader('Probabilities of a Customer Claiming')
                st.write('The Probability that a customer will not claim is', df.loc[0,'not_Claim_prob'])
                st. write('The probability that a customer will claim is', df.loc[0,'Claim_prob'])
                st.write('The plot below shows the probablity of whether a customer will claim insurance or not')
                
                # bar plot of the probs
                claim = ['No Claim', 'Claim']
                probs =[df.loc[0,'not_Claim_prob'],df.loc[0,'Claim_prob']]
                plt.bar(claim,probs,color='#B1B5CE')
                plt.xlabel=('Cutomer Insurance Claim status')
                plt.ylabel('Predicted Probability')
                st.set_option('deprecation.showPyplotGlobalUse', False) # removes the warning
                st.pyplot()
        else:
            st.write('Incorrect customer ID entered')