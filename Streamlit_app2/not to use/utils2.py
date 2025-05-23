import pandas as pd


def format_number(value, prefix=''):
    for unit in ['liters', 'Thousands', 'Tons']:
        if unit == 'tons' or value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} million tons'


# Processar os dados para análise anual
def prepare_rec_year(df):
    # Criar uma cópia do dataframe para não alterar o original
    df2 = df.copy()
    df2['Year'] = pd.to_datetime(df2['Year'], format='%Y')

    # Agrupar por ano
    df_rec_year = df2.set_index('Year').groupby(pd.Grouper(freq='Y'))[
        ['Value']].sum().reset_index()
    df_rec_year['Year'] = df_rec_year['Year'].dt.year
    return df_rec_year


# Carregar o dataset original
df = pd.read_csv('df_new_4.csv')
df_rec_year = prepare_rec_year(df)
