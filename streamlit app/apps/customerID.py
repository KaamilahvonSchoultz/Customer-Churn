import streamlit as st
import os
import pandas as pd
import json
import requests
import matplotlib.pyplot as plt

def app():
    st.header('Exisiting Customer')

    st.subheader("Enter customer ID to predict customer churn.")

    st.write('Please enter an exsisting customerID')

    @st.cache
    def get_data(dir_path):
        data = pd.read_csv(dir_path)
        return (data)

    data =get_data('data\customer_Churn_test_predictions.csv')


    with st.form('customerID'):
        customerID =st.text_input('Customer ID')

        submitted= st.form_submit_button('Submit')

    if submitted:

        if customerID in data['customerID'].unique():

            df = data.where(data['customerID'] == customerID)
            df = df.dropna()
            df =df.reset_index(drop=True)

            col1, col2 = st.columns(2)
            with col1:
                # Display the customer information
                st.subheader('Customer Information')
                customer_info = df.columns
                df2 =pd.DataFrame()
                temp = df.drop(columns=['Unnamed: 0','Churn','Churn_pred','Churn_prob','not_churn_prob'])
                temp = temp.applymap(str)
                customer_info = temp.columns

                customer_info2 = temp.loc[0, :].values.tolist()

                df2['Customer Information']= customer_info
                df2['Value']= customer_info2
                st.table(df2)


        
            with col2:

                st.subheader('Customer Churn Prediction')
                if df.loc[0,'Churn'] == True:
                    st.error('It is predicted that the customer will churn')
                    
                elif df.loc[0,'Churn'] == False:
                    st.success('It is predicted that the customer will not churn')
                
                # display the probablities
                st.subheader('Probabilities of Customer Churn')
                st.write('The Probability that a customer will not churn is', df.loc[0,'not_churn_prob'])
                st. write('The probability that a customer will churn is', df.loc[0,'Churn_prob'])
                st.write('The plot below shows the probablity of whether a customer will churn or not')
                
                # bar plot of the probs
                churn = ['No Churn', 'Churn']
                probs =[df.loc[0,'not_churn_prob'],df.loc[0,'Churn_prob']]
                plt.bar(churn,probs,color='#B1B5CE')
                plt.xlabel=('Cutomer Churn status')
                plt.ylabel('Predicted Probability')
                st.set_option('deprecation.showPyplotGlobalUse', False) # removes the warning
                st.pyplot()
        else:
            st.write('Incorrect customer ID entered')