# import libraries
import urllib.request
import pandas as pd
import plotly.express as px
import requests
import streamlit as st


# Import data
df_all_count = pd.read_csv("df_all_count.csv")
trend_month_all = pd.read_csv("trend_month_all.csv")
total_comments_year = pd.read_csv("total_comments_year.csv")
df_avg_comments = pd.read_csv("df_avg_comments.csv")
df_all_adj = pd.read_csv("df_all_adj.csv")
all_post_negative_scores = pd.read_csv("all_post_negative_scores.csv")
apps_received_stats = pd.read_csv("apps_received_stats.csv")

# Page 2
st.markdown("# Page 2")
st.sidebar.markdown("# Page 2")

row0_spacer1, row0_1 = st.columns(
    (0.1, 1)
)

row0_1.title("Analyzing Canadian immigration programs pain points & questions submitted on Reddit")

row1_spacer1, row1_1, row1_spacer2 = st.columns((0.1, 3.2, 0.1))

with row1_1:
    st.markdown(
        "Hi! Welcome to Reddit Immigration Canada project. The project aims to explore issues and topics discussed on Reddit relating to immigration to Canada or any immigration related processes. We will be looking at number of Reddit submissions by year and by immigration programs, their respective engagements, and conduct sentiment analysis to identify the sentiment and pain points for each program."
    )
    
line1_spacer1, line1_1 = st.columns((0.1, 1))

with line1_1:
    st.header(
        "Conduct sentiment analysis by program & identify process pain points: Feb 2013 - March 2023"
    )

line2_spacer2, line2_1 = st.columns((0.1, 1))

with line2_1:
    st.markdown("Please click on the expand button for more information of the charts")