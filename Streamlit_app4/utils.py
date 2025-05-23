from dataset import df
import pandas as pd


def format_number(value, prefix=''):
    for unit in ['liters', 'Thousands', 'Tons']:
        if unit == 'tons' or value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} million tons'


try:
    df_rec_country = df.groupby('Area')[['Value']].sum()
    df_rec_country = df.drop_duplicates(subset='Area')[['Area']].merge(
        df_rec_country, left_on='Area', right_index=True).sort_values('Value', ascending=False)
except KeyError as e:
    raise ImportError(
        f"Error while creating df_rec_country: Missing column {e}")
# 2 Dataframe Anual Value by Country
df2 = df.copy()

# Converter 'Year' para o formato de data
df2['Year'] = pd.to_datetime(df2['Year'], format='%Y')

df_rec_year = df2.set_index('Year').groupby(pd.Grouper(freq='Y'))[
    ['Value']].sum().reset_index()
df_rec_year['Year'] = df_rec_year['Year'].dt.year


######
