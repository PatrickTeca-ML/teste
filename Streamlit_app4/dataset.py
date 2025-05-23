import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o dataset
file = open('df_new_4.csv')
data = pd.read_csv(file)


# print(data.head())
df = pd.DataFrame.from_dict(data)
df2 = df.copy()
df2['Year'] = pd.to_datetime(df2['Year'], format='%Y')

print(df.head())

file.close()
