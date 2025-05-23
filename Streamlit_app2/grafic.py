import pandas as pd
import plotly.express as px
from dataset import df
from utils import df_rec_year

# from utils import df_rec_year
# Carregar os dados (ajuste conforme necessário para o seu arquivo ou função)
df = pd.read_csv('df_new_4.csv')

# Agrupar por país e item, somando as produções
df_grouped = df.groupby(['Area', 'Item'], as_index=False).agg(
    {'Value': 'sum'})  # aqui

# Resolver duplicatas somando os valores
f_resolved = df.groupby(
    ['Area', 'Year'], as_index=False).agg({'Value': 'sum'})

# Criar o mapa interativo scatter_geo
map_europe = px.scatter_geo(
    df_grouped,
    scope='europe',
    locations='Area',
    locationmode='country names',
    size='Value',
    color='Item',
    hover_name='Area',
    hover_data={'Value': True, 'Item': True},
    title='Milk Production in Europe by Country and Type',

)

grafic_rec_year = px.line(
    df_rec_year,
    x='Year',  # categorica
    y='Value',
    markers=True,
    range_y=(0, df_rec_year['Value'].max()),
    color='Year',
    line_dash='Year',
    title='Production per year'
)
grafic_rec_year.update_layout(yaxis_title='Production')

############
