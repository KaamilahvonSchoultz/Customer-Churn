from soupsieve import select
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import matplotlib.pyplot as plt
import numpy as np

def app ():
    st.header('Top 10 customers to churn')

    @st.cache
    def get_data(dir_path):
        data = pd.read_csv(dir_path)
        return (data)

    data =get_data('data\customer_Churn_train_predictions.csv')
            
    df = data.where(data['Churn'] == True)
    df = df.dropna()
    df =df.reset_index(drop=True)

    df = df.sort_values(by='Churn_prob',ascending=False)
    df1 = df.filter(['customerID','Churn'], axis=1)
    df1 =df1.reset_index(drop=True)
    df1['Features']='View factors effecting customer churn'
    first_col = df1.pop('Features')
    df1.insert(0,'Features',first_col)

    # get the shap values
    shap_values =get_data('data\Customer_Churn_Shap_values.csv')


    #build interactive table 

        # make check box

    gd=GridOptionsBuilder.from_dataframe(df1.head())
    gd.configure_selection(selection_mode='single',use_checkbox=True)
    gridoptions = gd.build()

    grid_table = AgGrid(df1.head(10), gridOptions=gridoptions,
                    update_mode= GridUpdateMode.SELECTION_CHANGED,
                    height= 300,
                    width=10,
                    color='#B1B5CE')

    sel_row = grid_table['selected_rows']

    

    try:
        customerID =sel_row[0]
        customerID=customerID['customerID']

        vals = shap_values.where(shap_values['customerID'] == customerID)
        vals = vals.dropna()
        vals =vals.reset_index(drop=True)
        vals= vals.set_index('customerID')
        vals = vals.sort_values(by=customerID,axis=1)
        

        #plot the values
        # bar plot of the probs
        Y = vals.columns
        shap_vals =list(vals.iloc[0])
        plt.barh(Y,shap_vals,color='#B1B5CE')
        plt.xlabel=('Feature Importance')
        plt.ylabel('Feature Name')
        st.set_option('deprecation.showPyplotGlobalUse', False) # removes the warning
        st.pyplot()

    except IndexError:
        print(' ')

# from the interactive plot have a check box which will be the output 
# When you have the output use it to get feature NB