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

img = Image.open('/home/dizziebeatz/code/Cenedikt/yana/yana/Frontend/Content/Yana_logo_image.png')

st.set_page_config(page_title='YANA', page_icon=img)

def main():
    set_background('/home/dizziebeatz/code/Cenedikt/yana/yana/Frontend/Content/Yana_background_image.png')

    st.markdown("<h1 style='text-align: center;'>YANA: You are not alone</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Welcome to our Mental Health Platform powered by NLP</h3><p style='text-align: center;'>We use advanced technology to analyze data from popular mental health subreddits and provide valuable insights. Our platform connects individuals with similar needs, fostering a sense of community and support. We offer community-assessed solutions and a comprehensive overview of prevalent mental health struggles. Join us as we leverage technology and shared experiences to create a more empathetic and inclusive mental health landscape.</p>", unsafe_allow_html=True)
    st.markdown("<h4 class='big-text'>Mode:</h4>", unsafe_allow_html=True)
    mode = st.radio("", ["Query", "Fetch Similar Posts"])

    if mode == "Query":
        query = st.text_input("Enter your query:")
        if st.button("Submit"):
            headers = {'Content-Type': 'application/json'}
            url = "http://127.0.0.1:8000/query/"
            data = {"text": query}
            json_data = json.dumps(data)

            response = requests.post(url, headers=headers, data=json_data)

            if response.status_code == 200:
                results = response.json()
                st.write("Results:")
                for result in results['text']:
                    st.write(result)
            else:
                st.error("There was an error processing your query.")

    # if mode == "Query":
    #     query = st.text_input("Enter your query:")
    #     if st.button("Submit"):
    #         headers = {'Content-Type': 'application/json'}
    #         url = "http://127.0.0.1:8000/query/"
    #         data = {"text": query}
    #         json_data = json.dumps(data)

    #         response = requests.post(url, headers=headers, data=json_data)

    #         if response.status_code == 200:
    #             with st.spinner("Generating results..."):
    #                 max_attempts = 30
    #                 attempts = 0
    #                 while attempts < max_attempts:
    #                     results_url = f"http://127.0.0.1:8000/result/{query}"
    #                     results_response = requests.get(results_url)
    #                     if results_response.status_code == 200:
    #                         results = results_response.json()
    #                         st.spinner()
    #                         st.write("Results:")
    #                         for result in results:
    #                             st.write(result)
    #                         break
    #                     elif results_response.status_code == 202:
    #                         attempts += 1
    #                         time.sleep(1)
    #                     else:
    #                         st.error("There was an error retrieving the results.")
    #                         break
    #                 if attempts == max_attempts:
    #                     st.error("Result retrieval timed out.")
    #         else:
    #             st.error("There was an error processing your query.")

    # if mode == "Query":
    #     query = st.text_input("Enter your query:")
    #     if st.button("Submit"):
    #         url = "http://127.0.0.1:8000/query/"
    #         headers = {'Content-Type': 'application/json'}
    #         data = {"text": query}
    #         json_data = json.dumps(data)

    #         response = requests.post(url, headers=headers, data=json_data)

    #         if response.status_code == 200:
    #             with st.spinner("Generating results..."):
    #                 max_attempts = 3
    #                 attempts = 0
    #                 while attempts < max_attempts:
    #                     results_url = f"http://127.0.0.1:8000/result/{query}"
    #                     results_response = requests.get(results_url)
    #                     if results_response.status_code == 200:
    #                         results = results_response.json()
    #                         st.spinner()
    #                         st.write("Results:")
    #                         for result in results:
    #                             st.write(result)
    #                         break
    #                     attempts += 1
    #                     time.sleep(6)
    #                 if attempts == max_attempts:
    #                     st.error("Result retrieval timed out.")
    #         else:
    #             st.error("There was an error processing your query.")

    # if mode == "Query":
    #     query = st.text_input("Enter your query:")
    #     if st.button("Submit"):
    #         url = "http://127.0.0.1:8000/query/"
    #         headers = {'Content-Type': 'application/json'}
    #         data = {"text": query}
    #         json_data = json.dumps(data)

    #         response = requests.post(url, headers=headers, data=json_data)

    #         if response.status_code == 200:
    #             with st.spinner("Generating results..."):
    #                 while True:
    #                     results_url = f"http://127.0.0.1:8000/result/{query}"
    #                     results_response = requests.get(results_url)
    #                     if results_response.status_code == 200:
    #                         results = results_response.json()
    #                         st.spinner()
    #                         st.write("Results:")
    #                         for result in results:
    #                             st.write(result)
    #                         break
    #                     time.sleep(1)
    #         else:
    #             st.error("There was an error processing your query.")

    elif mode == "Fetch Similar Posts":
        similar_query = st.text_input("Enter your query:")
        if st.button("Submit"):
            with st.spinner("Fetching similar posts to your query..."):
                time.sleep(3)

                similar_posts = ["Example Post 1", "Example Post 2", "Example Post 3"]
                st.spinner()

                st.write("Similar Posts:")
                for post in similar_posts:
                    st.write(post)

if __name__ == "__main__":
    main()
