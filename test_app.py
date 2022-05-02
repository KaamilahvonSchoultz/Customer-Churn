import pandas as pd

def get_data(path):
    cc_data = pd.read_csv(path)
    return (cc_data)

cc_data = get_data('data\WA_Fn-UseC_-Telco-Customer-Churn.csv')