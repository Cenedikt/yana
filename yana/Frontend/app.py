import streamlit as st
import os
import requests
import base64



def http_encoder(sentence: str) -> str :
    '''
    encodes the querry into http frindy format
    takes : sentence as  string
    return string
    '''
    words = sentence.split()
    sentence = '%20'.join(words)

    return sentence

# Construct OS-agnostic paths & load images
script_path = os.path.abspath(__file__)
parent_dir = os.path.dirname(os.path.dirname(script_path))
yana_logo_path = os.path.join(parent_dir, 'Frontend', 'Content', 'Yana_logo.png')
yana_background_path = os.path.join(parent_dir, 'Frontend', 'Content', 'yana_background.jpeg')
bukhari_script_path = os.path.join(parent_dir, 'Frontend', 'Content', 'Bukhari_Script.ttf')
base_url = 'https://yanaimage-pg2zxhxypa-ey.a.run.app'

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
    footer {visibility: hidden;}
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)


# Load the Bukhari Script font file
with open(bukhari_script_path, "rb") as font_file:
    font_data = font_file.read()

# Create a base64 encoded string for the font
font_base64 = base64.b64encode(font_data).decode()

# Define the CSS style for the Bukhari Script font
font_style = f"""
@font-face {{
    font-family: 'Bukhari Script';
    src: url(data:font/ttf;base64,{font_base64});
}}

.title-box h1 {{
    font-family: 'Bukhari Script', sans-serif;
    color: #F6F3E4;  /* Set the color to #F6F3E4 */
    text-shadow: 0px 0px 5px rgba(255, 83, 100, 0.9),
                 6px 6px 0px rgba(255, 83, 100, 0.6),
                 12px 12px 0px rgba(255, 83, 100, 0.4),
                 18px 18px 0px rgba(255, 83, 100, 0.2);
}}
"""

def main():
    set_background(yana_background_path)

    st.markdown('''
    <style>
    .description-box {
        background-color: rgba(255, 83, 100, 0.5);  /* Set the background color to #BFD786 with 0.1 transparency */
        padding: 20px;
        border-radius: 10px;
        color: #F6F3E4;
        text-shadow: 2px 2px 1px rgba(86, 197, 165, 0.8);

    }
    .results-box {
        background-color: rgba(255, 83, 100, 0.5);  /* Set the background color to #BFD786 with 0.1 transparency */
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: #F6F3E4;
        box-shadow: 0 0 20px rgba(255, 83, 100, 0.6),
                    0 0 30px rgba(255, 83, 100, 0.4),
                    0 0 40px rgba(255, 83, 100, 0.2);
    }
    .result-card {
        background-color: rgba(255, 83, 100, 0.5);  /* Set the background color to #BFD786 with 0.1 transparency */
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
        color: #F6F3E4;
        backdrop-filter: blur(5px);
        text-shadow: 2px 2px 1px rgba(255, 83, 100, 0.6);

    }
    </style>
    ''', unsafe_allow_html=True)
    # Apply the font style using st.markdown
    st.markdown(f"<style>{font_style}</style>", unsafe_allow_html=True)

    # Display the title with the Bukhari Script font
    st.markdown("<div class='title-box'><h1 style='font-size: 55px; text-align: center; margin-bottom: 55px;'> Yana - you are not alone</h1></div>", unsafe_allow_html=True)
    st.markdown("<div class='description-box' style='background-color: rgba(86, 197, 165, 0.65); padding: 20px; border-radius: 10px; color: #F6F3E4; backdrop-filter: blur(5px); margin-bottom: 20px;'><h3 style='text-align: center; color: #F6F3E4; text-shadow: 2px 2px 1px rgba(86, 197, 165, 0.8);'>Welcome to our Mental Health Platform powered by Natural Language Processing</h3><p style='text-align: center; font-size: 18px; color: #F6F3E4; text-shadow: 2px 2px 1px rgba(86, 197, 165, 0.8);'><strong>We use advanced technology to analyze data from popular mental health subreddits and provide valuable insights. Our platform connects individuals with similar needs, fostering a sense of community and support. We offer community-assessed solutions and a comprehensive overview of prevalent mental health struggles. Join us as we leverage technology and shared experiences to create a more empathetic and inclusive mental health landscape.</strong></p></div>", unsafe_allow_html=True)

    mode = st.radio("Select an option:", ["Fetch Similar Reddit Posts", "Get Advice*"])

    if mode == "Fetch Similar Reddit Posts":
        query = st.text_input("Enter your query:")
        if st.button("Submit"):
            url = f'{base_url}/query_1'
            params =  {'query' : http_encoder(query)}

            response = requests.get(url, params=params)

            if response.status_code == 200:
                results = response.json()
                st.write("<style>div[role='main'] div[data-testid='stDecoration'] { font-size: 14px; }</style>", unsafe_allow_html=True)
                st.write("<style>div[role='main'] div[data-testid='stDecoration'] { font-size: 18px; }</style>", unsafe_allow_html=True)
                st.markdown("<div class='result-card'><h3 style='text-align: center; color: #F6F3E4;'>According to our Model, the following Reddit posts are similar to your query:</h3></div>", unsafe_allow_html=True)
                for result in results['text']:
                    st.markdown(f'''
                        <div class="result-card">
                            <p style="font-size: 20px;"><strong>👤 Username:</strong> <span style="font-size: 18px;"><a href="https://www.reddit.com/user/{result['author']}" target="_blank" style="color: #DF4D60; font-weight: bold;">u/{result['author']}</a></span></p>
                            <p style="font-size: 20px;"><strong><span style="font-size: 25px;">{result['title']}</span></strong></p>
                            <p style="font-size: 20px;"><strong></strong> <span style="font-size: 18px;">{result['selftext']}</span></p>
                            <p style="font-size: 20px;"><strong>🤖 Subreddit:</strong> <span style="font-size: 18px;"><a href="https://www.reddit.com/r/{result['subreddit']}" target="_blank" style="color: #DF4D60; font-weight: bold;">r/{result['subreddit']}</a></span></p>
                            <p style="font-size: 20px;"><strong>👍 Upvotes: </strong> <span style="font-size: 18px;">{result['ups']}</span></p>
                        </div>
                '''.format(result=result), unsafe_allow_html=True)

            else:
                st.error("There was an error processing your query.")


    if mode == "Get Advice*":
        query = st.text_input("Enter your query:")
        if st.button("Submit"):
            url = f'{base_url}/query_2'
            params =  {'query' : http_encoder(query)}

            response = requests.get(url, params=params)

            if response.status_code == 200:
                results = response.json()
                st.write("<style>div[role='main'] div[data-testid='stDecoration'] { font-size: 14px; }</style>", unsafe_allow_html=True)
                st.write("<style>div[role='main'] div[data-testid='stDecoration'] { font-size: 18px; }</style>", unsafe_allow_html=True)
                st.markdown(f"<div class='result-card'><h3 style='text-align: center; color: #F6F3E4;'>According to other Redditors, the following advice is considered the most suitable by our Model for your situation: <span style='font-size: 28px; color: #DF4D60'>{results['text'][-1]['advice']}</span></h3></div>", unsafe_allow_html=True)
                for result in results['text']:
                    if len(result)>1:
                     st.markdown(f'''
                         <div class="result-card">
                             <p style="font-size: 20px;"><strong>👤 Username:</strong> <span style="font-size: 18px;"><a href="https://www.reddit.com/user/{result['author']}" target="_blank" style="color: #DF4D60; font-weight: bold;">u/{result['author']}</a></span></p>
                             <p style="font-size: 20px;"><strong><span style="font-size: 25px;">{result['title']}</span></strong></p>
                             <p style="font-size: 20px;"><strong></strong> <span style="font-size: 18px;">{result['selftext']}</span></p>
                             <p style="font-size: 20px;"><strong>🤖 Subreddit:</strong> <span style="font-size: 18px;"><a href="https://www.reddit.com/r/{result['subreddit']}" target="_blank" style="color: #DF4D60; font-weight: bold;">r/{result['subreddit']}</a></span></p>
                         </div>
                     '''.format(result=result), unsafe_allow_html=True)
                    else:
                        continue
            else:
                st.error("There was an error processing your query.")

if __name__ == "__main__":
    main()
