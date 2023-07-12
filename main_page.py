# import libraries
import urllib.request
import pandas as pd
import plotly.express as px
import requests
import streamlit as st


# Import data
df_all_count = pd.read_csv("df_all_count.csv")



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
    
