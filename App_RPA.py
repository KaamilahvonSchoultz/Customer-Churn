import streamlit as st
import numpy as np
import pandas as pd

st.title("Testing")

#data = pd.read_csv("data\WA_Fn-UseC_-Telco-Customer-Churn.csv")

#st.dataframe(data)

#st.plotly_chart(data)

st.select_slider('Pick a size', range(0, 1000, 5))



#with st.sidebar.form(key='my_form'):
    #username = st.text_input('Username')
    #password = st.text_input('Password')
    #st.form_submit_button('Login')

gender = ['Female', 'Male']
partner_status = ['Partner', 'No partner']
paperless = ['Yes', 'No']

st.sidebar.title("Register a new customer")

#Register new customer
with st.sidebar.form("reg_form"):
    gender_val = st.radio('Selecet gender', gender)
    partner_val = st.radio('Selecet partner status', partner_status)
    tenure_val = st.number_input('Select years of tenure', min_value=0, max_value=100, value=0, help='Insert number between 0 and 100')
    paperless_val = st.radio('Paperless billing', paperless)
    
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

options = ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
clicked = left_column.button('Press me!')
random_index = 0
if clicked:
   random_index = np.random.randint(0, len(options)) 
   clicked = False
# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        options,
        random_index
        )
    st.write(f"You are in {chosen} house!")

