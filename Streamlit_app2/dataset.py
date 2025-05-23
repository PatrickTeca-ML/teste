import streamlit as st
import pandas as pd
import plotly.express as px



import os
import pandas as pd

try:
    # Assuming df_new_4.csv is in the same directory as dataset.py
    file_path = os.path.join(os.getcwd(), 'df_new_4.csv')
    file = open(file_path)
    data = pd.read_csv(file)

    # Rest of your code using the data
except FileNotFoundError:
    print("Error: The file 'df_new_4.csv' could not be found. Please check the file path.")

# Carregar o dataset
#file = open('df_new_4.csv')
#data = pd.read_csv(file)


# print(data.head())
df = pd.DataFrame.from_dict(data)
df2 = df.copy()
df2['Year'] = pd.to_datetime(df2['Year'], format='%Y')

print(df.head())

file.close()
