import streamlit as st
from PIL import Image
import requests
import time
import base64
import json

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

img = Image.open('/home/emanuel/code/cenedikt/yana/yana/Frontend/Content/Yana_background_image.png')

st.set_page_config(page_title='YANA', page_icon=img)

def main():
    set_background('/home/emanuel/code/cenedikt/yana/yana/Frontend/Content/Yana_background_image.png')

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

    # if mode == "Query":
    #     query = st.text_input("Enter your query:")
    #     if st.button("Submit"):
    #         headers = {'Content-Type': 'application/json'}
    #         # url = "http://127.0.0.1:8000/query/"
    #         url = "http://0.0.0.0:8890/query/"
    #         data = {"text": query}
    #         json_data = json.dumps(data)

    #         response = requests.post(url, headers=headers, data=json_data)

    #         if response.status_code == 200:
    #             results = response.json()
    #             st.write("Results:")
    #             for result in results['text']:
    #                 st.write(result)
    #         else:
    #             st.error("There was an error processing your query.")

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
