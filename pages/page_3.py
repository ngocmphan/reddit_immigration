# Import libraries
import streamlit as st


# Page 3: Data sources, references and data limitation
st.markdown("# References & Others")
st.sidebar.markdown("# Page 3")

st.markdown("## References")


st.markdown("Immigration, Refugees and Citizenship Canada. Operational Processing - Monthly IRCC Updates. Extracted on July 2023 via the following link: https://open.canada.ca/data/en/dataset/9b34e712-513f-44e9-babf-9df4f7256550")

st.markdown("Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.")


st.markdown("## Tools")


st.markdown("- Pandas")
st.markdown("- Plotly")
st.markdown("- Streamlit")
st.markdown("- WordCloud")
st.markdown("- PMAW - Pushift Multithread API Wrapper")
st.markdown("- PRAW - Pushift Reddit API Wrapper")
st.markdown("- NLTK Vader")

st.markdown("## Data Sources & Data Limitation")
st.markdown("### Reddit Immigration data")


st.markdown("The data is obtained from Reddit directly through the use of Reddit API. The project used PMAW and PRAW to have access to Reddit API. The following variables are used for the project:")
st.markdown("- selftext: the content of the original post")
st.markdown("- author_fullname: author name account")
st.markdown("- title: title of the post")
st.markdown("- ups: Upvote of the post")
st.markdown("- link_flair_text: Program category of the post (Express Entry, Citizenship, Visitor Visa, Sponsorship, PNP, Meta, Public Policy Pathways, Study Permit, Work Permit, Quebec, Covid-19, Other")
st.markdown("- upvote_ratio: The ratio of the upvote of the post")
st.markdown("- created_utc: Post created time based on Unix timestamp")
st.markdown("num_comments: Number of comments of the post")
st.markdown("- id: unique ID of the post")


st.markdown("### Applications received by Immigration program - IRCC")
st.markdown("The datasets were obtained from IRCC. The following datasets were obtained:")

st.markdown("#### 1. Source countries - Applications Received for Permanent Residency (in Persons) by Month")
st.markdown("The following variables were used: Year, Month, App_received (Applications received)")

st.markdown("#### 2. Source countries - Applications Received for Temporary Residents (in Persons) by Month")

st.markdown("The following variables were used: Year, Month, App_received (Applications received)")

st.markdown("#### 3. Source countries - Visitor Visas Approved (in Persons) by Month")

st.markdown("The following variables were used: Year, Month, App_received (Applications received")

st.markdown("#### 4. Source countries - New Canadian Citizens (in Persons) by Month")

st.markdown("The following variables were used: Year, Month, App_received (Applications received")
