# import libraries
import urllib.request
import pandas as pd
import plotly.express as px
import requests
import streamlit as st
from PIL import Image


# Import data
df_all_count = pd.read_csv("df_all_count.csv")
trend_month_all = pd.read_csv("trend_month_all.csv")
total_comments_year = pd.read_csv("total_comments_year.csv")
df_avg_comments = pd.read_csv("df_avg_comments.csv")
df_all_adj = pd.read_csv("df_all_adj.csv")
all_post_negative_scores = pd.read_csv("all_post_negative_scores.csv")
apps_received_stats = pd.read_csv("apps_received_stats.csv")

# Import images
study_permit = Image.open('study_permit_negative.png')
work_permit = Image.open('work_permit_negative.png')
express_entry = Image.open('express_entry_negative.png')
sponsorship = Image.open('sponsorship_negative.png')

# Page 2
st.markdown("# Sentiment Analysis & Pain Points")
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
    
    
row3_1, row3_2 = st.columns([3,1.1], gap="small")

with row3_1:
    st.subheader("Is there any difference in negative sentiment by program?")
    fig = px.box(df_all_adj, x='sentiment_negative', y='link_flair_text', title="Sentiment Boxplot by Program")
    st.plotly_chart(fig, theme='streamlit', user_container_width=True)
    st.markdown(
    "TBD"
    )

with row3_2:
    st.subheader("Changes of negative sentiment by year")
    fig = px.line(all_post_negative_scores, x='Year', y='sentiment_negative', color='Program', title='Negative sentiment by year and by program')
    st.plotly_chart(fig, theme='streamlit', user_container_width=True)
    st.markdown("TBD")


st.subheader("Pain Points - Study Permit Negative Sentiment")
st.image(study_permit)

st.subheader("Pain Points - Work Permit Negative Sentiment")
st.image(work_permit)

st.subheader("Pain Points - Express Entry Negative Sentiment")
st.image(express_entry)

st.subheader("Pain Points - Sponsorship Negative Sentiment")
st.image(sponsorship)

st.subheader("Relationship between number of applications received and negative sentiment by program")
fig_1 = px.scatter(apps_received_stats, x='App_received', y='sentiment_negative', color='App', marginal_x='histogram', marginal_y='histogram', title = "Relationship between number of applications received and negative sentiment")
st.plotly_chart(fig_1, theme="streamlit", user_container_width=True)