import streamlit as st
import pandas as pd
import plotly.express as px
from dataset import df
from utils import format_number
from grafic import map_europe, grafic_rec_year
from coountry import grafic_country_trend
#####


def main():  # main function

    st.set_page_config(layout="wide")
    st.title("Production in Europe")
    st.sidebar.header("Filters")

    # select country
    selected_country = st.sidebar.selectbox(
        "Select a Country to View Production Trend:",
        options=df["Area"].unique(),
        index=0
    )

    st.subheader(f"Production Trend for {selected_country}")

    # filter to select the country
    country_data = df[df['Area'] == selected_country]

    # Check if there is data
    if country_data.empty:
        st.warning(f"No data available {
                   selected_country}")
    else:
        # line gráfic
        grafic_trend = px.line(
            country_data,
            x='Year',
            y='Value',
            markers=True,
            title=f'Production Trend in {selected_country}',
            labels={'Value': 'Production', 'Year': 'Year'}
        )

        # layout
        grafic_trend.update_layout(
            yaxis_title='Production',
            xaxis_title='Year',
            title_x=0.5  # Centralizar o título
        )

        # gráfic
        st.plotly_chart(grafic_trend, use_container_width=True)


#############

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

    # Comparison: Ireland vs Top
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
    st.write("## Content")
    st.write("""
    - Production trend of milk in Europe.
    - Total milk production by country.
    - Proportion of production by milk type.    
    - Comparison between Ireland and selected producers country.
    - Ireland's position compared to production leaders.
    """)


if __name__ == "__main__":
    main()
