import streamlit as st
import os
import requests
import time
import base64
import json


# Construct OS-agnostic paths & load images
script_path = os.path.abspath(__file__)
parent_dir = os.path.dirname(os.path.dirname(script_path))
yana_logo_path = os.path.join(parent_dir, 'Frontend', 'Content', 'Yana_logo.png')
yana_background_path = os.path.join(parent_dir, 'Frontend', 'Content', 'yana_background.jpeg')

# Call st.set_page_config() as the first Streamlit command
st.set_page_config(page_title='YANA', page_icon=yana_logo_path)


# Function to convert a binary file to base64 encoding
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set the background image of the Streamlit application
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    .stTextInput input {
        color: black;
    }
    h1, h2, h3, h4, h5, h6 {
        color: black;
    }
    .smaller-text {
        font-size: 14px;
        front-weight: bold;
    }
    .big-text {
        font-size: 20px;
        font-weight: bold;
    }
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)



def main():
    set_background(yana_background_path)

    st.markdown('''
    <style>
    .title-box {
        background-color: rgba(242, 242, 242, 0.3);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(0, 0, 0, 0.1);
    }
    .description-box {
        background-color: rgba(242, 242, 242, 0.3);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(0, 0, 0, 0.1);
    }
    .results-box {
        background-color: rgba(242, 242, 242, 0.3);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .result-item {
        margin-bottom: 10px;
        background-color: rgba(242, 242, 242, 0.3);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(0, 0, 0, 0.1);
    }
    </style>
    ''', unsafe_allow_html=True)

    st.markdown("<div class='title-box'><h1 style='text-align: center;'>YANA: You are not alone</h1></div>", unsafe_allow_html=True)
    st.markdown("<div class='description-box'><h3 style='text-align: center;'>Welcome to our Mental Health Platform powered by NLP</h3><p style='text-align: center;'>We use advanced technology to analyze data from popular mental health subreddits and provide valuable insights. Our platform connects individuals with similar needs, fostering a sense of community and support. We offer community-assessed solutions and a comprehensive overview of prevalent mental health struggles. Join us as we leverage technology and shared experiences to create a more empathetic and inclusive mental health landscape.</p></div>", unsafe_allow_html=True)

    mode = st.radio("", ["Query", "Fetch Similar Posts"])

    if mode == "Query":
        query = st.text_input("Enter your query:")
        if st.button("Submit"):
            url = "https://yanaapii-pg2zxhxypa-ey.a.run.app/query/"
            headers = {'Content-Type': 'application/json'}

            url = "https://yanaapii-pg2zxhxypa-ey.a.run.app/query/"


            if response.status_code == 200:
                results = response.json()
                st.write("<style>div[role='main'] div[data-testid='stDecoration'] { font-size: 14px; }</style>", unsafe_allow_html=True)
                st.write("<style>div[role='main'] div[data-testid='stDecoration'] { font-size: 18px; }</style>", unsafe_allow_html=True)
                st.markdown("<div class='results-box'><h3>According to our model, the following posts are similar to your query:</h3></div>", unsafe_allow_html=True)
                results_html = ""
                for result in results['text']:
                    results_html += "<div class='result-item'>•s " + result + "</div>"

                    st.markdown(results_html, unsafe_allow_html=True)
            else:
                st.error("There was an error processing your query.")


    elif mode == "Fetch Similar Posts":
        similar_query = st.text_input("Enter your query:")
        if st.button("Submit"):
            with st.spinner("Fetching similar posts to your query..."):
                time.sleep(3)

                similar_posts = ["Example Post 1", "Example Post 2", "Example Post 3"]
                st.spinner()

                st.write("<style>div[role='main'] div[data-testid='stDecoration'] { font-size: 14px; }</style>", unsafe_allow_html=True)
                st.markdown("<div class='results-box'><h3>Similar Posts:</h3></div>", unsafe_allow_html=True)
                posts_html = "<div class='result-item'>" + "<br>".join(similar_posts) + "</div>"
                st.markdown(posts_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
