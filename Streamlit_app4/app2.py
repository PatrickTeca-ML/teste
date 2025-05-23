import pandas as pd
import plotly.express as px
from utils import df_rec_year  # Certifique-se de que utils.py esteja acessível


def grafic_country_trend(df, selected_country):
    """
    Generate a line chart showing the production trend of a selected country.

    Parameters:
    - df (DataFrame): Original dataset containing 'Area', 'Year', and 'Value'.
    - selected_country (str): The name of the country to filter.

    Returns:
    - Plotly Figure: Line chart of the production trend.
    """
    # Filter the dataset for the selected country
    country_data = df[df['Area'] == selected_country]

    # Verificar se o dataframe filtrado não está vazio
    if country_data.empty:
        raise ValueError(f"No data available for the selected country: {
                         selected_country}")

    # Create the line chart
    grafic_trend = px.line(
        country_data,
        x='Year',
        y='Value',
        markers=True,
        title=f'Production Trend in {selected_country}',
        labels={'Value': 'Production', 'Year': 'Year'}
    )

    # Customize the layout
    grafic_trend.update_layout(
        yaxis_title='Production',
        xaxis_title='Year',
        title_x=0.5  # Center the title
    )

    return grafic_trend


def main():
    # Carregar os dados
    df = pd.read_csv('df_new_4.csv')  # Substitua pelo caminho correto

    # Garantir que os dados estão no formato correto
    df['Year'] = pd.to_datetime(df['Year'], format='%Y')

    # Agrupar por país e item
    df_grouped = df.groupby(
        ['Area', 'Item'], as_index=False).agg({'Value': 'sum'})

    # Criar um mapa interativo
    map_europe = px.scatter_geo(
        df_grouped,
        scope='europe',
        locations='Area',
        locationmode='country names',
        size='Value',
        color='Item',
        hover_name='Area',
        hover_data={'Value': True, 'Item': True},
        title='Milk Production in Europe by Country and Type'
    )

    # Criar gráfico de linha para produção anual
    grafic_rec_year = px.line(
        df_rec_year,
        x='Year',
        y='Value',
        markers=True,
        range_y=(0, df_rec_year['Value'].max()),
        title='Production per year'
    )
    grafic_rec_year.update_layout(yaxis_title='Production')

    # Exibir os gráficos (ou implementar como preferir)
    map_europe.show()
    grafic_rec_year.show()


# Executar a função principal
if __name__ == "__main__":
    main()
