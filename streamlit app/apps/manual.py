from turtle import color
import streamlit as st
import pandas as pd
import requests
import json
import requests
import matplotlib.pyplot as plt

def app():
    st.header('Enter Customer Information')

    st.write("Manually enter customer information in the left form to predict Churn.")

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

        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Customer Information Provided.')

            tenure_string = str(tenure) 
            MonthlyCharges_string= str(MonthlyCharges)
            TotalCharges_string = str(TotalCharges)

            # display the customer information provided
            customer_info1 ={'Gender':gender, 'SeniorCitizen':SeniorCitizen, 'Partner':Partner, 'Dependents':Dependents, 'tenure':tenure, 'PhoneService':PhoneService, 'MultipleLines':MultipleLines, 
            'InternetService':InternetService, 'OnlineSecurity':OnlineSecurity,'OnlineBackup':OnlineBackup }
            df1 = pd.DataFrame(customer_info1, index=[0])

            customer_info_list1 = ['Gender','SeniorCitizen','Partner','Dependents','tenure','PhoneService','MultipleLines', 'InternetService','OnlineSecurity','OnlineBackup',
            'DeviceProtection','TechSupport', 'StreamingTV','StreamingMovies','Contract', 'PaperlessBilling', 'PaymentMethod','MonthlyCharges', 'TotalCharges']

            customer_info_list2=[gender,SeniorCitizen,Partner, Dependents, tenure_string,PhoneService, MultipleLines, InternetService, OnlineSecurity,OnlineBackup,
            DeviceProtection,TechSupport, StreamingTV,StreamingMovies,Contract, PaperlessBilling,PaymentMethod,MonthlyCharges_string, TotalCharges_string]
            
            df = pd.DataFrame()

            df['Customer Information']= customer_info_list1
            df['Value']= customer_info_list2

            st.table(df)

            #st.table(df1)

            customer_info2 ={'DeviceProtection':DeviceProtection,'TechSupport':TechSupport, 'StreamingTV':StreamingTV,'StreamingMovies':StreamingMovies,'Contract':Contract, 'PaperlessBilling':PaperlessBilling, 'PaymentMethod':PaymentMethod,
            'MonthlyCharges':MonthlyCharges, 'TotalCharges':TotalCharges}

            df2 = pd.DataFrame(customer_info2, index = [0])
            #st.table(df2)


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
 
        d ={'gender':gender, 'SeniorCitizen':SeniorCitizen, 'Partner':Partner, 'Dependents':Partner, 'tenure':tenure, 'PhoneService':PhoneService, 'MultipleLines':MultipleLines, 
        'InternetService':InternetService,'OnlineSecurity':OnlineSecurity,'OnlineBackup':OnlineBackup, 'DeviceProtection':DeviceProtection, 'TechSupport':TechSupport, 
        'StreamingTV':StreamingTV,'StreamingMovies':StreamingMovies,'Contract':Contract, 'PaperlessBilling':PaperlessBilling,'PaymentMethod':PaymentMethod,
        'MonthlyCharges':MonthlyCharges, 'TotalCharges':TotalCharges,'monthly=tenure/charges':charges_divided_tenure,'numServices':services}
        

        json_data = json.dumps(
            {
                "Inputs":{
                    "data":
                    d
                }

            }
        )

        primaryKey ='GRzmqdzyXweOfD58mthYrVqtE2SSTMiM'
        rest_endpoint = 'http://bb1e52fa-8d04-4d3f-b395-989a5617444f.northeurope.azurecontainer.io/score'

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
            plt.bar(churn,probs,color='#B1B5CE')
            plt.xlabel=('Cutomer Churn status')
            plt.ylabel('Predicted Probability')
            st.set_option('deprecation.showPyplotGlobalUse', False) # removes the warning
            st.pyplot()
        