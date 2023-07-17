# import libraries
import urllib.request
import pandas as pd
import plotly.express as px
import requests
import streamlit as st
config = {'scrollZoom': False, 
         "showAxisDragHandles": False,
         "showAxisRangeEntryBoxes": False, 
         "dragMode":False, 
         'modeBarButtonsToRemove': ['zoom', 'pan']}

def switch_page(page_name: str):
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")

    page_name = standardize_name(page_name)

    pages = get_pages("streamlit_app.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")


# Import data
df_all_count = pd.read_csv("dashboard/df_all_count.csv")
trend_month_all = pd.read_csv("dashboard/trend_month_all.csv")
total_comments_year = pd.read_csv("dashboard/total_comments_year.csv")
df_avg_comments = pd.read_csv("dashboard/df_avg_comments.csv")
df_all_adj = pd.read_csv("dashboard/df_all_adj.csv")
all_post_negative_scores = pd.read_csv("dashboard/all_post_negative_scores.csv")
apps_received_stats = pd.read_csv("dashboard/apps_received_stats.csv")


# Main Page
st.markdown("# Main Page")
st.sidebar.markdown("# Main Page")

row0_spacer1, row0_1 = st.columns(
    (0.1, 1)
)

row0_1.title("Analyzing Canadian immigration programs pain points & questions submitted on Reddit")

st.markdown("Author: Alicia Ngoc Phan")
st.markdown("Project completed: July 2023")

row1_spacer1, row1_1 = st.columns((0.1, 1))

with row1_1:
    st.markdown(
        "Hi! Welcome to Reddit Immigration Canada project. The project aims to explore issues and topics discussed on Reddit relating to immigration to Canada or any immigration related processes. We will be looking at number of Reddit submissions by year and by immigration programs, their respective engagements, and conduct sentiment analysis to identify the sentiment and pain points for each program. The timeline of analysis is Feb 2013 - March 2023"
    )
    st.markdown("Main page: Analysis of Reddit submissions and engagement rates")
    st.markdown("Page 2: Sentiment analysis and pain points identification.")
    st.markdown("Page 3: References, Data Sources, and Data Limitation")
    
line1_spacer1, line1_1 = st.columns((0.1, 1))

with line1_1:
    st.header(
        "Analyzing the Reddit submissions and engagement rates by program"
    )

line2_spacer2, line2_1 = st.columns((0.1, 1))

with line2_1:
    st.markdown("Tips on viewing the visualiations:")
    st.markdown("- Please click on the expand button for more information of the charts.")
    st.markdown("- For charts with legends of different categories, click once on the category in the legend to remove the category visualization.")
    st.markdown("- For charts with legends of difference categories, double click on the category in the legend to view the isolated category. Double click again on the category to reset the graph.")

    
row3_1, row3_space, row3_2 = st.columns([3,1.8,2], gap="small")
    
with row3_1:
    st.subheader("How submission per program changed by year?")
    fig = px.line(df_all_count, x='Year', y='Submission counts', color="Program", title='Submissions by program and by year')
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)
    st.plotly_chart(fig, theme='streamlit', user_container_width=True, config=config)
    st.markdown(
    "Please click on the chart expand for full details of the trend. In general, the submissions for each program increased from 2013 to 2023. In addition, Study Permit is the category with the highest submissions in all of the years. Noted that some of the category submissions peaked in 2020, and later in 2021. "
    )


with row3_2:
    st.subheader("Which month has the most submission?")
    fig = px.line(trend_month_all, x='Month', y="Submission counts", color="Program", title="Number of submissions monthly by program")
    fig.update_layout(xaxis={"dtick":1})
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)
    st.plotly_chart(fig, theme="streamlit", user_container_width=True, config=config)
    st.markdown(
    "Overall, the number of submissions monthly increased and peaked in December. Noted that there is issue in the Reddit data extracted. Please refer to data source limitation section above."
    )

row4_1, row4_space, row4_2 = st.columns([3,1.8, 2], gap='small'
)

with row4_1:
    st.subheader("Which program has the most submission?")
    st.markdown(" ")
    st.markdown("  ")
    fig = px.bar(df_all_count, x='Submission counts', y='Program', title="Total submissions per program", orientation='h')
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)
    st.plotly_chart(fig, theme="streamlit", user_container_width=True, config=config)
    st.markdown("Based on the bar chart, we noted that the following categories are among the top five highest submissions: Study permit, Express Entry, Work Permit, Sponsorship, and Visitor Visa")

with row4_2:
    st.subheader("Which program has the most comments?")
    fig = px.bar(total_comments_year, x='num_comments', y='Program', title="Total comments per program", orientation='h')
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)
    st.plotly_chart(fig, theme="streamlit", user_container_width=True, config=config)
    st.markdown("Based on the bar chart, Study permit has the highest engagement or the total comments. The remaining top engagements are: Express Entry, Sponsorship and Work Permit. Noted that Study Permit has significantly higher engagement with more than 70,000 comments.")

row5_1, row5_space, row5_2 = st.columns(
    [3,1.8,2], gap="small"
)
with row5_1:
    st.subheader("What program has the highest average engagement?")
    st.markdown("  ")
    st.markdown(" ")
    fig = px.histogram(df_avg_comments, x='avg_comments', y='Program', title="Average Comments by Program", orientation='h',  barmode='group', histfunc='avg')
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)
    st.plotly_chart(fig, theme="streamlit", user_container_width=True, config=config)
    st.markdown("Please click on chart expand for more information. Although the Study permit has significantly higher comments among all categories, the average comments per post by program for study permit and work permit are close to each other at around 40 comments per post. The top three categories in comments per post are: Study Permit, Work Permit, and Express Entry.")

with row5_2:
    st.subheader("Changes in engagement by year by program?")
    fig = px.line(df_avg_comments, x="Year", y="avg_comments", color="Program", title = "Changes in average comments per post by program by year")
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)
    st.plotly_chart(fig, theme="streamlit", user_container_width=True, config=config)
    st.markdown("There is significant changes in engagement for all immigration programs. There was a peak in engagement (comments per post) in 2019 and 2021 among the categories. In addition, there was also a dip in engagement in 2020, which could be due to the pandemic.")

row6_1, row6_2 = st.columns(2)
with row6_2: 
    next_page = st.button("Next Page")
    if next_page:
        switch_page("Sentiment Analysis & Pain Points")

