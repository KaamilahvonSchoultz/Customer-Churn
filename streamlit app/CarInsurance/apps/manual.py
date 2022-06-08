from turtle import color
import streamlit as st
import pandas as pd
import requests
import json
import requests
import matplotlib.pyplot as plt

def app():
    st.header('Enter Customer Information')

    st.write("Manually enter customer information in the left form to predict if the customer will claim insurance.")

    with st.sidebar.form('reg_form'):
        st.header('Customer Information')
        CREDIT_SCORE = st.number_input('What is the customers credit score?')

        SPEEDING_VIOLATIONS = st.number_input('How many speeding violations has the customer had?')

        DUIS = st.number_input('How many DUIs does the customer have?')

        PAST_ACCIDENTS = st.number_input('How many past accidents has the customer been in?')

        


        # drop down enteries

        AGE = st.radio(
            ' Age',
            ('16-25', '26-39','40-64','65+'))

        GENDER = st.radio(
            ' Gender',
            ('female', 'male'))


        RACE = st.radio(
            ' What is the customers race?',
            ('minority', 'majority'))


        DRIVING_EXPERIENCE = st.radio(
            ' What driving experience does the customer have?',
            ('0-9y', '10-19y','20-29y','30y+'))


        EDUCATION = st.radio(
            'What eduction does the customer have?',
            ('none', 'high school','university'))


        INCOME = st.radio(
            ' What income bracket does the customer have?',
            ('poverty', 'working class','middle class','upper class'))


        VEHICLE_OWNERSHIP = st.radio(
            'Does the customer own the vehicle?',
            ('Yes', 'No'))

        MARRIED = st.radio(
            'Is the customer married?',
            ('Yes', 'No'))

        CHILDREN = st.radio(
            'Does the customer have children?',
            ('Yes', 'No'))

        VEHICLE_YEAR = st.radio(
            'What year is the vehicle?',
            ('before 2015', 'after 2015'))


        VEHICLE_TYPE = st.radio(
            'What type of vehicle is it?',
            ('sedan', 'sports car'))

        ANNUAL_MILEAGE = st.radio(
            'What is the vehicle average mileage?',
            ('1000', '2000','3000','4000','5000','6000','7000','8000','9000',
            '10000','11000','12000','13000','14000','15000','16000',
            '17000','18000','19000','20000','21000','22000'))
        

        submitted = st.form_submit_button('Submit')

    if submitted:


        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Customer Information Provided.')

            CREDIT_SCORE_string = str(CREDIT_SCORE) 
            SPEEDING_VIOLATIONS_string= str(SPEEDING_VIOLATIONS)
            DUIS_string = str(DUIS)
            PAST_ACCIDENTS_string = str(PAST_ACCIDENTS)

            # display the customer information provided


            customer_info_list1 = ['AGE', 'GENDER', 'RACE', 'DRIVING_EXPERIENCE', 'EDUCATION', 'INCOME','CREDIT_SCORE', 'VEHICLE_OWNERSHIP', 'VEHICLE_YEAR', 'MARRIED',
            'CHILDREN', 'ANNUAL_MILEAGE', 'VEHICLE_TYPE', 'SPEEDING_VIOLATIONS','DUIS', 'PAST_ACCIDENTS']

            customer_info_list2=[AGE, GENDER, RACE, DRIVING_EXPERIENCE,EDUCATION, INCOME,CREDIT_SCORE_string, VEHICLE_OWNERSHIP, VEHICLE_YEAR, MARRIED,CHILDREN, ANNUAL_MILEAGE, VEHICLE_TYPE, 
            SPEEDING_VIOLATIONS_string,DUIS_string, PAST_ACCIDENTS_string]
            
            df = pd.DataFrame()

            df['Customer Information']= customer_info_list1
            df['Value']= customer_info_list2

            st.table(df)

        if VEHICLE_OWNERSHIP == 'YES':
            VEHICLE_OWNERSHIP=1
        else:
            VEHICLE_OWNERSHIP=0
        
        if MARRIED == 'YES':
            MARRIED=1
        else:
            MARRIED=0
        
        if CHILDREN == 'YES':
            CHILDREN=1
        else:
            CHILDREN=0
        




       
        d ={'AGE':AGE, 'GENDER':GENDER, 'RACE':RACE, 'DRIVING_EXPERIENCE':DRIVING_EXPERIENCE, 'EDUCATION':EDUCATION, 'INCOME':INCOME,
            'CREDIT_SCORE':CREDIT_SCORE, 'VEHICLE_OWNERSHIP':VEHICLE_OWNERSHIP, 'VEHICLE_YEAR':VEHICLE_YEAR, 'MARRIED':MARRIED,
            'CHILDREN':CHILDREN, 'ANNUAL_MILEAGE':ANNUAL_MILEAGE, 'VEHICLE_TYPE':VEHICLE_TYPE, 'SPEEDING_VIOLATIONS':SPEEDING_VIOLATIONS,
            'DUIS':DUIS, 'PAST_ACCIDENTS':PAST_ACCIDENTS}
        

        json_data = json.dumps(
            {
                "Inputs":{
                    "data":
                    d
                }

            }
        )
        primaryKey ='jdWeP4lDQnqbi9FNFfXnefpC0xh0gmRf'
        rest_endpoint = 'http://49096c29-521e-4f17-93ce-51b4b661857a.northeurope.azurecontainer.io/score'

        # Set the content type
        headers = {'Content-Type': 'application/json'}
        # authentication is enabled, therefore set the authorization header
        headers['Authorization'] = 'Bearer {}'.format(primaryKey)


        response = requests.post(rest_endpoint, headers = headers,
                    json = eval(json_data))

        model_output = response.json()
       
        results = model_output['Results']
        prob = model_output['Probability']

        with col2:
            st.subheader('Customer Insurance Claim Prediction')
            if results[0] == True:
                st.error('It is predicted that the customer will claim insurance')
                
            elif results[0] == False:
                st.success('It is predicted that the customer will not claim insurance')
            
            # display the probablities
            st.subheader('Probabilities of Customer Claiming Insuranced')
            st.write('The Probability that a customer will not claim insurance is', prob[0][0])
            st. write('The probability that a customer will calim insurance is', prob[0][1])
            st.write('The plot below shows the probablity of whether a customer will calim insurance or not')
            
            # bar plot of the probs
            claim = ['No claim', 'claim']
            probs =prob[0]
            plt.bar(claim,probs,color='#B1B5CE')
            plt.xlabel=('Cutomer Insurance Claim Status')
            plt.ylabel('Predicted Probability')
            st.set_option('deprecation.showPyplotGlobalUse', False) # removes the warning
            st.pyplot()
        