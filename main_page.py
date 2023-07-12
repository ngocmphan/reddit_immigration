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

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns(
    (0.1, 2, 0.2, 1, 0.1)
)

row0_1.title("Analyzing immigration programs questions & pain points on Reddit")

with row1_1:
    st.markdown(
        "Hi! Welcome to Reddit Immigration Canada project. The project aims to explore issues and topics discussed on Reddit relating to immigration to Canada or any immigration related processes. We will be looking at number of Reddit submissions by year and by immigration programs, their respective engagements, and conduct sentiment analysis to identify the sentiment and pain points for each program."
    )
    
line1_spacer1, line1_1, line1_spacer2 = st.columns((0.1, 3.2, 0.1))

with line1_1:
    st.header(
        "Analyzing the Reddit submissions and engagement rates per Program through time: Feb 2013 - March 2023"
    )
 
row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns(
    (0.1, 1, 0.1, 1, 0.1)
)
    
with row3_1:
    st.subheader("How submissions per program changed by year?")
    fig = px.line(df_all_count, x='Year', y='Submission counts', color="Program", title='Submissions by program and by year - All posts')
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)
    st.markdown(
    "TBD"
    )

with row3_2:
    st.subheader("Which month during the year has the most submission?")
    fig = px.line(trend_month_all, x='Month', y="Submission counts", color="Program", title="Number of submissions monthly by program - Total all")
    fig.update_layout(xaxis={"dtick":1})
    st.plotly_chart(fig, theme="streamlit", user_container_width=True)
    st.markdown(
    "TBD"
    )

row4_space1, row4_1, row4_space2, row4_2, row4_space3 = st.columns(
    (0.1, 1, 0.1, 1, 0.1)
)

with row4_1:
    st.subheader("Which program has the most submission?")
    fig = px.bar(df_all_count, x='Program', y='Submission counts', title="Total submissions per program")
    st.plotly_chart(fig, theme="streamlit", user_container_width=True)
    st.markdown("TBD")


