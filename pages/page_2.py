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
    "The negative sentiment shows the differences in average negative sentiment with higher scores for the following program: Quebec, Study Permit, Work Permit, Visitor Visa, and Citizenship. Noted that overall all the programs have low negative sentiment with the scores lower than 0.15."
    )

with row3_2:
    st.subheader("Negative sentiment by year")
    fig = px.line(all_post_negative_scores, x='Year', y='negative_scores', color='Program', title='Negative sentiment by year and by program')
    st.plotly_chart(fig, theme='streamlit', user_container_width=True)
    st.markdown("The negative sentiment for each program has fluctuations. In general, there were dip in negative sentiment in 2020 and 2022, with an increase in negative sentiment in 2021. Based on the current line chart and the total of submissions dip in 2020 due to pandemic, it is reasonable that the negative sentiment also dipped.")

row5_1, row5_2 = st.columns([3,1.1], gap="small")

with row5_1: 
    st.subheader("Which program has the highest average negative sentiment scores?")
    fig = px.histogram(df_all_adj, x='link_flair_text', y='sentiment_negative', title="Histogram of average negative sentiment", histfunc='avg')
    st.plotly_chart(fig, theme='streamlit', user_container_width=True)
    st.markdown("Please click on the bar chart expand for more info. Quebec has significantly higher average negative sentiment than other categories. The remaining categories have average negative sentiment close to each other with leading categories include: Study Permit, Visitor Visa, Work Permit, and Visitor Visa.")
    
with row5_2:
    st.subheader("Highest negative sentiment scores sum?")
    fig = px.histogram(df_all_adj, x='link_flair_text', y='sentiment_negative', title='Histogram of sum negative sentiment')
    st.plotly_chart(fig, theme='streamlit', user_container_width=True)
    st.markdown("Overall, the sum of negative sentiment is highest for Study Permit; this is due to the fact Study Permit has significantly higher number of submissions than other categories. Similarly, Work permit, Express Entry and Sponsorship categories have high sum of negative sentiment.")

 
line3_spacer1, line3_1 = st.columns((0.1, 1))

with line3_1:
    st.subheader(
        "The changes in the applications received for the programs with higher mean negative sentiment: Study Permit, Work Permit, Sponsorship, and Visitor Visa. Period in examination: 2020 - 2023"
    )

line4_spacer4, line4_1 = st.columns((0.1, 1))

with line4_1:
    st.markdown("Noted that some of the category in Reddit will be aggregated due to the aggregation of government data collection: PR (Express Entry, Sponsorship, PNP, Quebec); Temporary resident (Study Permit, Work Permit, Working Holiday); Visitor (Visitor visa); Citizenship (Citizenship)")
    
row4_1, row4_2 = st.columns([3,1.1], gap='small')

with row4_1:
    st.subheader("Applications received for Permanent Resident")
    fig = px.line(pr_intake, x='Month', y='App_received', color='Year', title="Applications received for PR")
    st.plotly_chart(fig, theme="streamlit", user_container_width=True)
    st.markdown("Applications received for Permanent Resident was overall higher in 2021 than in other years. In addition, the number of applications peaked in May in 2021. Applications received for PR for other years (beside 2021) remained lower than 40,000 applications.")

with row4_2:
    st.subheader("Applications received for Temporary Resident")
    fig = px.line(trv_intake, x='Month', y='App_received', color='Year', title="Applications received for TRV")
    st.plotly_chart(fig, theme="streamlit", user_container_width=True)
    st.markdown("In general, applications received for temporary resident is overall higher in 2022 with a sign of continuation in 2023 (with available data). Noted that overall, there is a higher number of applications from March to June, with slight increase in September to November.")
    
row5_1, row5_2 = st.columns([3,1.1], gap='small')

with row5_1:
    st.subheader("Applications received for Visitor Visa")
    fig = px.line(visitor_intake, x='Month', y='App_received', color='Year', title='Applications received for Visitor Visa')
    st.plotly_chart(fig, theme="streamlit", user_container_width=True)
    st.markdown("Applications received for visitor visa increased are overall higher in 2022 than in 2020 and 2021, with significantly higher number of applications in 2023.")
    
with row5_2:
    st.subheader("Applications received for Citizenship")
    fig = px.line(citizenship_intake, x='Month', y='App_received', color='Year', title='Applications received for Citizenship')
    fig.update_layout(xaxis={"dtick":1})
    st.plotly_chart(fig, theme='streamlit', user_container_width=True)
    st.markdown("Overall, the applications received for citizenship are higher in 2022. There is usually a dip in April, with an increase gradually in the rest of the year.")

line5_spacer1, line5_1 = st.columns((0.1, 1))

with line5_1:
    st.subheader(
        "Process Pain points: Extract repeated words in the submissions"
    )

line6_spacer2, line6_1 = st.columns((0.1, 1))

with line6_1:
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
st.markdown("There is no strong relationship between negative sentiment scores and the number of applications received.")