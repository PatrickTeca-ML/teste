import streamlit as st
import pandas as pd
import plotly.express as px
from dataset import df
from utils import format_number
from map import map_europe,  grafic_rec_year
from map import grafic_country_trend


def main():

    # Dashboard title
    st.set_page_config(layout='wide')
    st.title("Milk Production in Europe")
    st.sidebar.header("Filters")

    aba1, aba2, aba3 = st.tabs(
        ['Dataset', 'Milk Production valeu', 'Producing Countries'])
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
            st.plotly_chart(grafic_country_trend, use_container_width=True)

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

    # Interactive filters
    countries = st.sidebar.multiselect(
        "Select countries:",
        options=df["Area"].unique(),
        default=["Ireland", "Belgium"]
    )
    categories = st.sidebar.multiselect(
        "Select milk type:",
        options=df["Item"].unique(),
        default=df["Item"].unique()
    )
    years = st.sidebar.slider(
        "Select year range:",
        int(df["Year"].min()),
        int(df["Year"].max()),
        (2010, 2022)
    )

    # Filtering the dataset
    df_filtered = df[
        (df["Area"].isin(countries)) &
        (df["Item"].isin(categories)) &
        (df["Year"].between(*years))
    ]

    # Production Chart by Country
    st.subheader("Total Milk Production by Country")
    fig1 = px.bar(
        df_filtered.groupby("Area")["Value"].sum().reset_index(),
        x="Area",
        y="Value",
        title="Total Production by Country"
    )
    st.plotly_chart(fig1)

    # Category Proportion Chart
    st.subheader("Proportion of Production by Milk Type")
    fig2 = px.pie(
        df_filtered,
        names="Item",
        values="Value",
        title="Proportion by Milk Type"
    )
    st.plotly_chart(fig2)

    # Comparison: Ireland vs Top 5
    top_countries = df_filtered.groupby("Area")["Value"].sum(
    ).sort_values(ascending=False).head(5).index
    df_comparison = df_filtered[df_filtered["Area"].isin(
        top_countries.union(["Ireland"]))]

    st.subheader("Comparison: Ireland vs Top 5 Producers")
    fig3 = px.line(
        df_comparison,
        x="Year",
        y="Value",
        color="Area",
        line_group="Item",
        title="Production Evolution"
    )
    st.plotly_chart(fig3)

    # Individual Analysis of Ireland
    df_ireland = df_filtered[df_filtered["Area"] == "Ireland"]

    st.subheader("Production in Ireland")
    fig4 = px.bar(
        df_ireland,
        x="Year",
        y="Value",
        color="Item",
        title="Production by Milk Type in Ireland"
    )
    st.plotly_chart(fig4)

    # Conclusions
    st.write("## Conclusions")
    st.write("""
    - Country with the highest milk production.
    - Most produced type of milk.
    - Ireland's position compared to production leaders.
    """)


main()
