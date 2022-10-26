from email.policy import default
import pandas as pd
#import seaborn as sb
#import numpy as np
import warnings
import plotly.express as px
import streamlit as st

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Mon Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")

df = pd.read_csv(r'Twitch_lol_data.csv', encoding='cp1252')

# ----- SIDEBAR -----
st.sidebar.header("Filtrer les jeux:")
Game = st.sidebar.multiselect(
    "Choisissez un jeu :",
    options=df['Game'].unique(),
    default=df["Game"].unique()
)

st.sidebar.header("Filtrer l'année:")
Year = st.sidebar.multiselect(
    "Choisissez un jeu :",
    options=df['Year'].unique(),
    default=df["Year"].unique()
)

st.sidebar.header("Filtrer le mois:")
Month = st.sidebar.multiselect(
    "Choisissez un jeu :",
    options=df['Month'].unique(),
    default=df["Month"].unique()
)


df_selection = df.query(
    "Game== @Game & Year == @Year & Month== @Month"
)


# ---- MAINPAGE ----
st.title(":smiling_imp: Dashboard - Twitch")
st.markdown("##")

total_views = int(df_selection["Hours_watched"].sum())
average_rank = round(df_selection["Rank"].mean(), 1)
star_rank = ":star:"*int(round(average_rank, 0))
average_viewers = round(df_selection['Avg_viewers'].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total d'heures de visionnages:")
    st.subheader(f"{total_views:,}")
with middle_column:
    st.subheader("Rang Moyen:")
    st.subheader(f"{average_rank}")
with right_column:
    st.subheader("Moyenne de visiteurs:")
    st.subheader(f"{average_viewers}")

st.markdown("---")

total_by_games = (
    df_selection.groupby(by=['Game']).sum()[
        ['Hours_watched']].sort_values(by=['Hours_watched'])
)
fig_product = px.bar(
    total_by_games,
    x="Hours_watched",
    y=total_by_games.index,
    orientation="h",
    title="<b>Total d'heures par jeu</b>",
    color_discrete_sequence=["#0083B8"] * len(total_by_games),
    template="plotly_white",
)

fig_product.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


viewer_by_month = (df_selection.groupby(
    by=['Month']).sum()[['Avg_viewers']].sort_values(by=['Avg_viewers']))
fig_product_month = px.bar(
    viewer_by_month,
    x=viewer_by_month.index,
    y="Avg_viewers",
    title="<b>Visiteurs Mensuelle</b>",
    color_discrete_sequence=["#0083B8"] * len(viewer_by_month),
    template="plotly_white",
)

fig_product_month.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(tickmode="linear")),
    yaxis=(dict(showgrid=False))
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_product, use_container_width=True)
right_column.plotly_chart(fig_product_month, use_container_width=True)
