import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plost
from dataset import df
from utils import format_number
from grafic import map_europe, grafic_rec_year
from coountry import grafic_country_trend


def main():
    # Page setting
    st.set_page_config(layout="wide")
    st.title("Production in Europe")

    col_pie, col_Country = st.columns(2)

    with col_pie:
        pie_chart = px.pie(
            df,
            names='Item',
            values='Value',
            title='Milk type'
        )
        st.plotly_chart(pie_chart, use_container_width=True)

    with col_Country:
        st.subheader("Top 15 of the biggest producers in the EU")

        # sum production values ​​by country
        df_top5 = df.groupby('Area', as_index=False)['Value'].sum()

        # select the top 15
        df_top5 = df_top5.sort_values(by='Value', ascending=False).head(15)

        # horizontal bar chart
        bar_chart = px.bar(
            df_top5,
            x='Value',
            y='Area',
            orientation='h',  # horizontal
            title="Top 15 Producers by Production Value",
            labels={'Value': 'Production Value', 'Area': 'Country'}
        )
        st.plotly_chart(bar_chart, use_container_width=True)

        # Create abas
    aba1, aba2, aba3 = st.tabs(
        ['Dataset', 'Producing Countries', 'Producing per Year']
    )

    with aba1:
        st.dataframe(df)

    with aba2:
        st.metric('Total Milk Production', format_number(df['Value'].sum()))
        st.plotly_chart(map_europe, use_container_width=True)

    with aba3:
       # st.metric('Quantity of production', format_number(df.shape[0]))
        st.plotly_chart(grafic_rec_year, use_container_width=True)

        # Conclusions
    st.write("## Content")
    st.write("""
    - Country with the highest milk production.
    - Most produced type of milk in the EU.
    - Abas wiht Dataset, Producing Countries and Producing per Year.
    """)


main()
