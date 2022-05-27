import streamlit as st
from multiapp import MultiApp
from apps import manual, customerID, top10

app = MultiApp()

st.markdown("""
# Customer Churn Prediction App
""")

# Add all your application here
app.add_app("Exisiting Customer", customerID.app)
app.add_app("Enter Customer Infomation Manually", manual.app)
app.add_app("Top 10 customers to churn", top10.app)
# The main app
app.run()