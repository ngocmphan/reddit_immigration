# Import libraries
import streamlit as st


# Page 3: Data sources, references and data limitation
st.markdown("# References & Others")
st.sidebar.markdown("# Page 3")

st.markdown("## References")


st.markdown("[1] Immigration, Refugees and Citizenship Canada. Operational Processing - Monthly IRCC Updates. Extracted on July 2023 via the following link: https://open.canada.ca/data/en/dataset/9b34e712-513f-44e9-babf-9df4f7256550")

st.markdown("[2] Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.")


st.markdown("## Tools")


st.markdown("- Pandas")
st.markdown("- Plotly")
st.markdown("- Seaborn")
st.markdown("- Streamlit")
st.markdown("- WordCloud")
st.markdown("- PMAW - Pushift Multithread API Wrapper")
st.markdown("- PRAW - Python Reddit API Wrapper")
st.markdown("- NLTK Vader")

st.markdown("## Data Sources & Data Limitation")
st.markdown("### Reddit Immigration data")


st.markdown("The data is obtained from Reddit directly through the use of Reddit API. The project used PMAW and PRAW to have access to Reddit API. The period under examination is Feb 2013 - Mar 2023. The total observations for the all data extracted were 63,217; however, after data cleaning and data transformation, the total observations were reduced to 39,058 submissions. The following variables are used for the project:")
st.markdown("- selftext: the content of the original post")
st.markdown("- author_fullname: author name account")
st.markdown("- title: title of the post")
st.markdown("- ups: Upvote of the post")
st.markdown("- link_flair_text: Program category of the post (Express Entry, Citizenship, Visitor Visa, Sponsorship, PNP, Meta, Public Policy Pathways, Study Permit, Work Permit, Quebec, Covid-19, Other")
st.markdown("- upvote_ratio: The ratio of the upvote of the post")
st.markdown("- created_utc: Post created time based on Unix timestamp")
st.markdown("num_comments: Number of comments of the post")
st.markdown("- id: unique ID of the post")
st.markdown("Please refer to the Immigration_Canada_Data_Extraction.ipynb for the process of data extraction using Reddit API.")

st.markdown("### Applications received by Immigration program - IRCC")
st.markdown("The datasets were obtained from IRCC, please refer to [1] IRCC, Operational Processing - Monthly IRCC reference above. The data available were monthly applications number from the period of Jan 2020 - May 2023. The following datasets were obtained:")

st.markdown("1. Source countries - Applications Received for Permanent Residency (in Persons) by Month")
st.markdown("The following variables were used: Year, Month, App_received (Applications received)")

st.markdown("2. Source countries - Applications Received for Temporary Residents (in Persons) by Month")

st.markdown("The following variables were used: Year, Month, App_received (Applications received)")

st.markdown("3. Source countries - Visitor Visas Approved (in Persons) by Month")

st.markdown("The following variables were used: Year, Month, App_received (Applications received")

st.markdown("4. Source countries - New Canadian Citizens (in Persons) by Month")

st.markdown("The following variables were used: Year, Month, App_received (Applications received")

st.markdown("### Data Limitation & Other considerations")
st.markdown("Due to the amount of data retrieved for the period 2012-2023, we noted that there is potential missing data in the Reddit Immigration data extraction. We noted that the number of submissions per month has some discrepancies with the number of submissions found on Reddit. However, the amount of data retrieved is sufficient to paint a broad picture of the type of questions and the demands of specific immigration program processes.")
st.markdown("The following dashboard is a summary of the results obtained. For more detailed analysis including the reasoning, data cleaning and data transformation, please visit Immigration_Canada_Analysis.ipynb on reddit_immigration project Github page: https://github.com/ngocmphan/reddit_immigration")
