# create a new ID 
# fill in the info in the UI
# call the model and make a prediction 

import streamlit as st
import pandas as pd
import requests
import json
import pandas as pd
import random
import string
import requests
import matplotlib.pyplot as plt

def new_customer(data):

    #define containers 

    customer_info = st.container()
    new_customer = st.container()

  
    st.write('Please fill in the customer information form on the left and press submit.')
    
    with customer_info:
        #create the submit for in a side bar

        
        with st.sidebar.form('reg_form'):
            st.header('Customer Information')
            tenure = st.number_input('What is the customers current tenure')

            MonthlyCharges = st.number_input('What is the customers monthly charges')

            TotalCharges = st.number_input('What is the customers total charges')

            # drop down enteries

            gender = st.radio(
                ' Gender',
                ('Female', 'Male'))


            SeniorCitizen = st.radio(
                ' Is the cutomer a senior citizen?',
                ('Yes', 'No'))


            Partner = st.radio(
                ' Does the customer have a partner?',
                ('Yes', 'No'))


            Dependents = st.radio(
                ' Does the customer have dependents?',
                ('Yes', 'No'))


            PhoneService = st.radio(
                ' Does the customer have a phone service?',
                ('Yes', 'No'))


            MultipleLines = st.radio(
                'Does the customer have multiple phone lines?',
                ('Yes', 'No'))

            InternetService = st.radio(
                'What internet service does the customer have?',
                ('DSL', 'Fiber optic','No'))

            OnlineSecurity = st.radio(
                'Does the customer have online security?',
                ('Yes', 'No'))

            DeviceProtection = st.radio(
                'Does the customer have device protection?',
                ('Yes', 'No'))

            OnlineBackup = st.radio(
                'Does the customer have online backup?',
                ('Yes', 'No'))


            TechSupport = st.radio(
                'Does the customer have tech support?',
                ('Yes', 'No'))

            StreamingTV = st.radio(
                'Does the customer stream TV?',
                ('Yes', 'No'))


            StreamingMovies = st.radio(
                'Does the customer stream Movies?',
                ('Yes', 'No'))


            Contract = st.radio(
                'What contract type does the customer have?',
                ('Month-to-Month', 'One year', 'Two year'))


            PaperlessBilling = st.radio(
                'Does the customer have paperless billing?',
                ('Yes', 'No'))


            PaymentMethod = st.radio(
                'What payment method does the customer have?',
                ('Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check'))

            

            submitted = st.form_submit_button('Submit')


    if submitted:

        st.subheader('Customer Information Provided.')

        with new_customer: # container for customer ID
        #function to generate new ID
            def generate_id():
                alphabet = list(string.ascii_uppercase)
                id_numbers = [str(random.randint(0,9)) for _ in range(4)]
                id_letters = [random.choice(alphabet) for _ in range(5)]
                new_customer_id = f"{''.join(id_numbers)}-{''.join(id_letters)}"
        
                return new_customer_id

            id_taken = True
            while id_taken:
                new_customer_id = generate_id()
                if not new_customer_id in data.customerID:
                    id_taken = False


        # display the customer information provided
        customer_info1 ={'CustomerID':new_customer_id,'Gender':gender, 'SeniorCitizen':SeniorCitizen, 'Partner':Partner, 'Dependents':Dependents, 'tenure':tenure, 'PhoneService':PhoneService, 'MultipleLines':MultipleLines, 
        'InternetService':InternetService, 'OnlineSecurity':OnlineSecurity,'OnlineBackup':OnlineBackup }
        df1 = pd.DataFrame(customer_info1, index = [0])

        st.table(df1)

        customer_info2 ={'DeviceProtection':DeviceProtection,'TechSupport':TechSupport, 'StreamingTV':StreamingTV,'StreamingMovies':StreamingMovies,'Contract':Contract, 'PaperlessBilling':PaperlessBilling, 'PaymentMethod':PaymentMethod,
        'MonthlyCharges':MonthlyCharges, 'TotalCharges':TotalCharges}

        df2 = pd.DataFrame(customer_info2, index = [0])
        st.table(df2)

        internet_dsl =0
        internet_optic =0
        internet_no =0
        if InternetService == 'DSL':
            internet_dsl = 1
        elif InternetService == 'Fiber optic':
            internet_optic = 1
        elif InternetService == 'No':
            internet_no = 1

        contract_month = 0 
        contract_1 =0
        contract_2 =0
        if Contract == 'Month-to-Month':
            contract_month = 1
                
        elif Contract == 'One year':
            contract_1 =1

        elif Contract == 'Two year':
            contract_2 = 1

        pay_bank=0
        pay_credit = 0
        pay_electronic = 0
        pay_mail = 0

        if PaymentMethod == 'Bank transfer (automatic)':
            pay_bank = 1
        elif PaymentMethod == 'Credit card (automatic)':
            pay_credit = 1
        elif PaymentMethod == 'Electronic check':
            pay_electronic = 1
        elif PaymentMethod == 'Mailed check':
            pay_mail = 1


        if gender== 'Female':
            gender = 1
        else:
            gender = 0

        if (SeniorCitizen =='Yes'):
            SeniorCitizen=1
        else:
            SeniorCitizen=0

        if Partner == 'Yes':
            Partner = 1
        else:
            Partner = 0

        if Dependents == 'Yes':
            Dependents = 1
        else:
            Dependents = 0

        if PhoneService == 'Yes':
            PhoneService = 1
        else:
            PhoneService = 0


        if MultipleLines == 'Yes':
            MultipleLines = 1
        else:
            MultipleLines = 0

        if OnlineSecurity == 'Yes':
            OnlineSecurity = 1
        else:
            OnlineSecurity = 0

        if OnlineBackup == 'Yes':
            OnlineBackup = 1
        else:
            OnlineBackup = 0

        if DeviceProtection == 'Yes':
            DeviceProtection = 1
        else:
            DeviceProtection = 0


        if TechSupport == 'Yes':
            TechSupport = 1
        else:
            TechSupport = 0

        if StreamingTV == 'Yes':
            StreamingTV = 1
        else:
            StreamingTV = 0

        if StreamingMovies == 'Yes':
            StreamingMovies = 1
        else:
            StreamingMovies = 0


        if PaperlessBilling == 'Yes':
            PaperlessBilling = 1
        else:
            PaperlessBilling = 0

        if Contract == 'Yes':
            Contract = 1
        else:
            Contract = 0

        try:
            charges_divided_tenure= TotalCharges/tenure

        except ZeroDivisionError:
            charges_divided_tenure =0

        if charges_divided_tenure == MonthlyCharges:
            charges_divided_tenure =1
        else:
            charges_divided_tenure = 0

        services =0
        service = [PhoneService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies]

        for s in service:
            if s == 1:
                services = services +1
        
            
        #if st.button('Predict Customer Churn'):
        d ={'gender':gender, 'SeniorCitizen':SeniorCitizen, 'Partner':Partner, 'Dependents':Dependents, 'tenure':tenure, 'PhoneService':PhoneService, 'MultipleLines':MultipleLines, 
        'OnlineSecurity':OnlineSecurity,'OnlineBackup':OnlineBackup, 'DeviceProtection':DeviceProtection, 'TechSupport':TechSupport, 
        'StreamingTV':StreamingTV,'StreamingMovies':StreamingMovies,  'PaperlessBilling':PaperlessBilling,
        'MonthlyCharges':MonthlyCharges, 'TotalCharges':TotalCharges,'charges_divided_tenure':charges_divided_tenure,'numServices':services,'InternetService_DSL':internet_dsl,
        'InternetService_Fiber optic':internet_optic,'InternetService_No':internet_no,'Contract_Month-to-Month':contract_month,'Contract_One year':contract_1,'Contract_Two year':contract_2,
        'PaymentMethod_Bank transfer (automatic)':pay_bank,'PaymentMethod_Credit card (automatic)':pay_credit,'PaymentMethod_Electronic check':pay_electronic,'PaymentMethod_Mailed check':pay_mail}


        
        json_data = json.dumps(
            {
                "Inputs":{
                    "data":
                    d
                }

            }
        )

        primaryKey ='c77fYXljfBIXJkDOp17ha9FDMAzM4M96'
        rest_endpoint = 'http://b75f4436-0877-492e-bb3d-329e5b36d484.northeurope.azurecontainer.io/score'

        # Set the content type
        headers = {'Content-Type': 'application/json'}
        # authentication is enabled, therefore set the authorization header
        headers['Authorization'] = 'Bearer {}'.format(primaryKey)


        response = requests.post(rest_endpoint, headers = headers,
                    json = eval(json_data))

        model_output = response.json()
        results = model_output['Results']
        prob = model_output['Probability']

        st.subheader('Customer Churn Prediction')
        if results[0] == True:
            st.error('It is predicted that the customer will churn')
            
        elif results[0] == False:
            st.success('It is predicted that the customer will not churn')
        
        # display the probablities
        st.subheader('Probabilities of Customer Churn')
        st.write('The Probability that a customer will not churn is', prob[0][0])
        st. write('The probability that a customer will churn is', prob[0][1])
        st.write('The plot below shows the probablity of whether a customer will churn or not')
        
        # bar plot of the probs
        churn = ['No Churn', 'Churn']
        probs =prob[0]
        plt.bar(churn,probs)
        plt.xlabel=('Cutomer Churn status')
        plt.ylabel('Predicted Probability')
        st.set_option('deprecation.showPyplotGlobalUse', False) # removes the warning
        st.pyplot()

    return