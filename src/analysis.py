import pandas as pd
pd.set_option('display.max_columns', 500)
data = pd.read_csv('data/labeled_data.csv')
data.drop(columns=['Unnamed: 0'], inplace=True)
