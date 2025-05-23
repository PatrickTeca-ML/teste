import streamlit as st
import pandas as pd
import plotly.express as px
from dataset import df

# Carregar o dataset
df2 = df.copy()
# Função para gerar a URL da bandeira


def get_flag_url(country_name):
    # Formatar o nome do país para o formato esperado pela flagpedia.net
    formatted_name = country_name.lower().replace(" ", "-")
    return f"https://flagpedia.net/data/flags/h80/{formatted_name}.png",


# Criar uma coluna com URLs das bandeiras
df2['Flag_URL'] = df2['Area'].apply(get_flag_url)

# Somar os valores de produção por país
df_country_sum = df2.groupby('Area', as_index=False)['Value'].sum()

# Adicionar as URLs das bandeiras ao dataframe agregado
df_country_sum['Flag_URL'] = df_country_sum['Area'].apply(get_flag_url)
