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


# Main Page
st.markdown("# Main Page")
st.sidebar.markdown("# Main Page")

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
        "Analyzing the Reddit submissions and engagement rates per Program through time: Feb 2013 - March 2023"
    )

line2_spacer2, line2_1 = st.columns((0.1, 1))

with line2_1:
    st.markdown("Please click on the expand button for more information of the charts")
    
row3_1, row3_2 = st.columns([3,1.1], gap="small")
    
with row3_1:
    st.subheader("How submission per program changed by year?")
    fig = px.line(df_all_count, x='Year', y='Submission counts', color="Program", title='Submissions by program and by year')
    st.plotly_chart(fig, theme='streamlit', user_container_width=True)
    st.markdown(
    "TBD"
    )


with row3_2:
    st.subheader("Which month has the most submission?")
    fig = px.line(trend_month_all, x='Month', y="Submission counts", color="Program", title="Number of submissions monthly by program")
    fig.update_layout(xaxis={"dtick":1})
    st.plotly_chart(fig, theme="streamlit", user_container_width=True)
    st.markdown(
    "TBD"
    )

row4_1, row4_2 = st.columns([2,1.1], gap='small'
)

with row4_1:
    st.subheader("Which program has the most submission?")
    fig = px.bar(df_all_count, x='Submission counts', y='Program', title="Total submissions per program", orientation='h')
    st.plotly_chart(fig, theme="streamlit", user_container_width=True)
    st.markdown("TBD")

with row4_2:
    st.subheader("Which program has the most comments?")
    fig = px.bar(total_comments_year, x='num_comments', y='Program', title="Total comments per program", orientation='h')
    st.plotly_chart(fig, theme="streamlit", user_container_width=True)
    st.markdown("TBD")

row5_1, row5_2 = st.columns(
    [3.5,3], gap="small"
)
with row5_1:
    st.subheader("What program has the highest average engagement?")
    fig = px.bar(df_avg_comments, x='avg_comments', y='Program', title="Average Comments by Program", orientation='h')
    st.plotly_chart(fig, theme="streamlit", user_container_width=True)
    st.markdown("TBD")

with row5_2:
    st.subheader("Changes in engagement by year by program?")
    fig = px.line(df_avg_comments, x="Year", y="avg_comments", color="Program")
    st.plotly_chart(fig, theme="streamlit", user_container_width=True)
    st.markdown("TBD")


