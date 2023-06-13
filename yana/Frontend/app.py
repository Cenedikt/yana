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


# Load the Bukhari Script font file
with open("BukhariScript-Regular.ttf", "rb") as font_file:
    font_data = font_file.read()

# Create a base64 encoded string for the font
font_base64 = base64.b64encode(font_data).decode()

# Define the CSS style for the Bukhari Script font
font_style = f"""
@font-face {{
    font-family: 'Bukhari Script';
    src: url(data:font/ttf;base64,{font_base64});
}}
"""

# Apply the font style using st.markdown
st.markdown(f"<style>{font_style}</style>", unsafe_allow_html=True)

def main():
    set_background(yana_background_path)

    st.markdown('''
    <style>
    .title-box {

        background-color: rgba(0, 0, 0, 0.05);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(0, 0, 0, 0.4);
    }
    .description-box {
        background-color: rgba(0, 0, 0, 0.05);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(0, 0, 0, 0.4);
    }
    .results-box {
        background-color: rgba(0, 0, 0, 0.05);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(0, 0, 0, 0.4);
        text-align: center;
    }
    .result-card {
        background-color: rgba(0, 0, 0, 0.05);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(0, 0, 0, 0.4);

        margin-bottom: 20px;
    }
    </style>
    ''', unsafe_allow_html=True)

    st.markdown("<div class='title-box'><h1 style='text-align: center; font-family: Bukhari Script;'>YANA: You are not alone</h1></div>", unsafe_allow_html=True)
    st.markdown("<div class='description-box'><h3 style='text-align: center;'>Welcome to our Mental Health Platform powered by NLP</h3><p style='text-align: center;'>We use advanced technology to analyze data from popular mental health subreddits and provide valuable insights. Our platform connects individuals with similar needs, fostering a sense of community and support. We offer community-assessed solutions and a comprehensive overview of prevalent mental health struggles. Join us as we leverage technology and shared experiences to create a more empathetic and inclusive mental health landscape.</p></div>", unsafe_allow_html=True)

    mode = st.radio("Select an option:", ["Fetch Similar Reddit Posts", "Get Advice*"])

    if mode == "Fetch Similar Reddit Posts":
        query = st.text_input("Enter your query:")
        if st.button("Submit"):
            url = "https://yanaapii-pg2zxhxypa-ey.a.run.app/query/"
            headers = {'Content-Type': 'application/json'}
            data = {"text": query}
            json_data = json.dumps(data)

            response = requests.post(url, headers=headers, data=json_data)

            if response.status_code == 200:
                results = response.json()
                st.write("<style>div[role='main'] div[data-testid='stDecoration'] { font-size: 14px; }</style>", unsafe_allow_html=True)
                st.write("<style>div[role='main'] div[data-testid='stDecoration'] { font-size: 18px; }</style>", unsafe_allow_html=True)
                st.markdown("<h3 style='text-align: center;'>According to our Model, the following Reddit posts are similar to your query:</h3>", unsafe_allow_html=True)
                for result in results['text']:
                    st.markdown('''
                        <div class="result-card">
                            <h4>👤Username: Username</h4>
                            <h4>📌Title: Title</h4>
                            <p style="font-size: 20px;"><strong>📄Post:</strong> <span style="font-size: 18px;">{result}</span></p>
                            <h4>/🇷🇪 Subreddit: Subreddit</h4>
                            <h4>👍Upvotes: Upvotes</h4>
                        </div>
                '''.format(result=result), unsafe_allow_html=True)

            else:
                st.error("There was an error processing your query.")

    elif mode == "Get Advice*":
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
