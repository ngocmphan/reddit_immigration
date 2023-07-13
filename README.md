# Reddit Immigration

## Summary Result Dashboard
https://redditimmigration.streamlit.app/

## Topic
The topic of the project is to explore the issues and topics discussed on Reddit relating to immigrating to Canada. Immigration here can relate to the early inquiring stage, applying stage, processing stage, and obtaining results stage. 

## Problem statement and background
The permanent residence (PR) process is a lengthy process which starts from the preparation of the experience, skills and finances for the immigration program, to the time the applicant obtained the permanent residence. The total process can take up to six years with significant financial decisions involved: application fees, lawyer fees, self-sustaining expenses, etc. 

As the PR process requires significant preparations, there are many questions regarding the process from applicants. The ideal option is to consult with lawyers or contract a legal firm to prepare the application on behalf of the applicant; however, this path is known for being costly. Therefore, it is very common that people would post their questions regarding the process on social media or public forums. From this, the project aims to understand the questions and concerns posted on Reddit with emphasis on common issues asked, topics mentioned and the general review of the process or point of improvements. 

For the scope of the project, we focus on the data and posts for the period of 10 years: Jan 2013 - Jan 2023. 

## Data sources and variables 
The data is obtained from Reddit directly through the use of Reddit API. The project used PRAW - Python Reddit API Wrapper to directly access Reddit. 
The following variables are used for analysis in the project: 
* selftext: The content of the original post
* author_fullname: Author name account
* title: Title of the post
* ups: Upvote of the post (noted that PMAW uses score as ups)
* link_flair_text: Program category of the post (Express entry, Citizenship, Visitor Visa, Sponsorship, PNP, Meta, Public Policy pathways, Study Permit, Work Permit, Quebec, Covid-19, Other)
* upvote_ratio: The ratio of the upvote of the post
* media_embed: Embedded links in the post
* created_utc: Post created time based on Unix timestamp. 
* num_comments: Number of comments of the post. 
* id: Unique ID of the post. 

## Language and Tools used
* Python and related libraries (pandas, matplotlib, etc.)
* PRAW - Python Reddit API Wrapper
* PMAW - Python Pushift API Wrapper

## Deliverables
### Understanding of the posts and questions asked: Issues/questions, topics, and immigration programs
* Which topics/programs have the most discussion based on timeline (all time, by year, current year)? 
* What are the most mentioned issues in general for the Canadian Immigration application? Mentioned issues by program? (All time, by year, current year)
* Sentimental analysis: Positive of negative review of the experience/process by program. Include analysis of sentiments per program by year. 
* What kind of reference was linked in the post? Was it an official source? 
* Is there specific time of the year (seasonality) that a specific program requires more attention due to the amount of questions received? 

### Point of improvements summary
* Topics that are considered controversial, which might indicate unclear instructions and lack of resource (all time, by year, current year)
* Which part of the process is the pain point? Ranking by issues. 
* Which program requires the most improvement? Number of applications and analysis of pain points. 

### Visualization deliverable: Summary dashboard
Please refer to the Summary dashboard as follows: https://redditimmigration.streamlit.app/


