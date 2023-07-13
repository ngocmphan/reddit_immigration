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
pr_intake = pd.read_csv("pr_intake.csv")
visitor_intake = pd.read_csv("visitor_intake.csv")
trv_intake = pd.read_csv("trv_intake.csv")
citizenship_intake = pd.read_csv("citizenship_intake.csv")

# Import images
study_permit = Image.open('study_permit_negative.png')
work_permit = Image.open('work_permit_negative.png')
express_entry = Image.open('express_entry_negative.png')
sponsorship = Image.open('sponsorship_negative.png')
quebec = Image.open('quebec_negative.png')

# Page 2
st.markdown("# Sentiment Analysis & Pain Points")
st.sidebar.markdown("# Page 2")

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
    st.subheader("Negative sentiment by year")
    fig = px.line(all_post_negative_scores, x='Year', y='negative_scores', color='Program', title='Negative sentiment by year and by program')
    st.plotly_chart(fig, theme='streamlit', user_container_width=True)
    st.markdown("TBD")

row5_1, row5_2 = st.columns([3,1.1], gap="small")

with row5_1: 
    st.subheader("Which program has the highest average negative sentiment scores?")
    fig = px.histogram(df_all_adj, x='link_flair_text', y='sentiment_negative', title="Histogram of average negative sentiment", histfunc='avg')
    st.plotly_chart(fig, theme='streamlit', user_container_width=True)
    
with row5_2:
    st.subheader("Highest negative sentiment scores sum?")
    fig = px.histogram(df_all_adj, x='link_flair_text', y='sentiment_negative', title='Histogram of sum negative sentiment')
    st.plotly_chart(fig, theme='streamlit', user_container_width=True)

line2_spacer1, line2_1 = st.columns((0.1, 1))

with line2_1:
    st.subheader(
        "The changes in the applications received for the programs with higher mean negative sentiment: Study Permit, Work Permit, Sponsorship, and Visitor Visa."
    )

line2_spacer2, line2_1 = st.columns((0.1, 1))

with line2_1:
    st.markdown("Noted that some of the category in Reddit will be aggregated due to the aggregation of government data collection: PR (Express Entry, Sponsorship, PNP, Quebec); Temporary resident (Study Permit, Work Permit, Working Holiday); Visitor (Visitor visa); Citizenship (Citizenship)")
    
row4_1, row4_2 = st.columns([3,1.1], gap='small')

with row4_1:
    st.subheader("Applications received for Permanent Resident")
    fig = px.line(pr_intake, x='Month', y='App_received', color='Year', title="Applications received for PR")
    st.plotly_chart(fig, theme="streamlit", user_container_width=True)
    st.markdown("TBD")

with row4_2:
    st.subheader("Applications received for Temporary Resident")
    fig = px.line(trv_intake, x='Month', y='App_received', color='Year', title="Applications received for TRV")
    st.plotly_chart(fig, theme="streamlit", user_container_width=True)
    st.markdown("TBD")
    
row5_1, row5_2 = st.columns([3,1.1], gap='small')

with row5_1:
    st.subheader("Applications received for Visitor Visa")
    fig = px.line(visitor_intake, x='Month', y='App_received', color='Year', title='Applications received for Visitor Visa')
    st.plotly_chart(fig, theme="streamlit", user_container_width=True)
    st.markdown("TBD")
    
with row5_2:
    st.subheader("Applications received for Citizenship")
    fig = px.line(citizenship_intake, x='Month', y='App_received', color='Year', title='Applications received for Citizenship')
    fig.update_layout(xaxis={"dtick":1})
    st.plotly_chart(fig, theme='streamlit', user_container_width=True)
    st.markdown("TBD")

line3_spacer1, line3_1 = st.columns((0.1, 1))

with line3_1:
    st.subheader(
        "Process Pain points: Extract repeated words in the submissions"
    )

line3_spacer2, line3_1 = st.columns((0.1, 1))

with line3_1:
    st.markdown("Utilize WordCloud to show the words that have highest repetition in the submissions with negative sentiment scores higher than its respective category average.")

    
st.subheader("Pain Points - Study Permit Negative Sentiment")
st.image(study_permit)

st.subheader("Pain Points - Work Permit Negative Sentiment")
st.image(work_permit)

st.subheader("Pain Points - Express Entry Negative Sentiment")
st.image(express_entry)

st.subheader("Pain Points - Sponsorship Negative Sentiment")
st.image(sponsorship)

st.subheader("Pain Points - Quebec Negative Sentiment")
st.image(quebec)

st.subheader("Relationship between number of applications received and negative sentiment by program")
fig_1 = px.scatter(apps_received_stats, x='App_received', y='sentiment_negative', color='App', marginal_x='histogram', marginal_y='histogram', title = "Relationship between number of applications received and negative sentiment")
st.plotly_chart(fig_1, theme="streamlit", user_container_width=True)