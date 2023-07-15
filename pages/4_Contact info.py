# Import libraries
import streamlit as st
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

# Contact information
st.markdown("# Contact Information")
st.sidebar.markdown("# Contact Info")

st.markdown("## Project Page:")
st.markdown("[Github Project: Reddit Immigration](https://github.com/ngocmphan/reddit_immigration)")

st.markdown("## Connect with me - Linkedin")
st.markdown("[Linkedin - Alicia .P](https://www.linkedin.com/in/ngocmphan/)")

st.markdown("Please don't hesitate to contact me if you want to talk about the project, collaborate or discuss on different ideas. Thank you for reading.")

row6_1, row_6_2 = st.columns(2)

with row6_1:
    previous_page = st.button("Previous Page")
    if previous_page:
        switch_page("References & Others")
        
with row6_2: 
    next_page = st.button("Main Page")
    if next_page:
        switch_page("main page")