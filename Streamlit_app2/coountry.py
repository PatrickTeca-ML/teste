import streamlit as st
from dataset import df
import plotly.express as px


def grafic_country_trend(df, selected_country):
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
