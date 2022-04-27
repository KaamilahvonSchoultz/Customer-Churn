import streamlit as st
import numpy as np
import pandas as pd

st.title("Testing")

#data = pd.read_csv("data\WA_Fn-UseC_-Telco-Customer-Churn.csv")

#st.dataframe(data)

#st.plotly_chart(data)

st.select_slider('Pick a size', range(0, 1000, 5))

st.sidebar.slider('Pick a number for tenure', 0, 100)

with st.sidebar.form(key='my_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login')

#with st.spinner(text='In progress'):
#    st.success(st.balloons())

#st.progress(progress_variable_1_to_100)

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

