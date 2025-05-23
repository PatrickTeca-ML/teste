import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number
from grafic import map_europe, grafic_rec_year
from pages.Country import grafic_country_trend
from map import grafic_country_trend


def main():

    # Dashboard title
    st.set_page_config(layout='wide')
    st.title("Milk Production in Europe")
    st.sidebar.header("Filters")

# menus de cima em linha
    aba1, aba2, aba3 = st.tabs(
        ['Dataset', 'Total Milk Production valeu', 'Producing Countries'])
    with aba1:
        st.dataframe(df)
    with aba2:
        coluna1, coluna2 = st.columns(2)
        with coluna1:
            st.metric('Total Milk Production',
                      format_number(df['Value'].sum()))
            st.plotly_chart(map_europe, use_container_width=True)
        with coluna2:
            st.metric('Quantity of poduction', format_number(df.shape[0]))
            st.plotly_chart(grafic_rec_year, use_container_width=True)

            # Sidebar filter for country selection
    st.sidebar.header("Country Filter")
    selected_country = st.sidebar.selectbox(
        "Select a country:",
        options=df["Area"].unique(),
        index=0  # Default to the first country in the list
    )

    # Generate the trend chart for the selected country
    st.subheader(f"Production Trend for {selected_country}")
    grafic_trend = grafic_country_trend(df, selected_country)
    st.plotly_chart(grafic_trend, use_container_width=True)


main()
