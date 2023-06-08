import streamlit as st
from PIL import Image

import time

import numpy as np
import streamlit as st
import base64


# Function to convert a binary file to base64 encoding
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


# Function to set the background image of the Streamlit application
def set_background(png_file):
    bin_str = get_base64(png_file) # Convert the PNG image file to base64 encoding and setting image as backgrouond.
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
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
    #MainMenu {visibility: hidden; } # Hide Menu
        footer {visibility: hidden;} # Hide footer
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True) # Apply the background image using Streamlit's markdown feature

img = Image.open('/home/emanuel/code/cenedikt/yana/yana/Frontend/Content/Yana_logo_image.png')

st.set_page_config(page_title='YANA', page_icon=img) # Setting the page title and icon

def main():
    set_background('/home/emanuel/code/cenedikt/yana/yana/Frontend/Content/Yana_background_image.png')

    st.markdown(
    """
    <h1 style='text-align: center;'>YANA: You are not alone</h1>
    """,
    unsafe_allow_html=True
) # Display a header1
    st.markdown(
    """
    <h3 style='text-align: center;'>Welcome to our Mental Health Platform powered by NLP</h3>
    <p style='text-align: center;'>We use advanced technology to analyze data from popular mental health subreddits and provide valuable insights. Our platform connects individuals with similar needs, fostering a sense of community and support. We offer community-assessed solutions and a comprehensive overview of prevalent mental health struggles. Join us as we leverage technology and shared experiences to create a more empathetic and inclusive mental health landscape. Together, we can navigate the complexities of mental health and improve well-being.</p>
    """,
    unsafe_allow_html=True
)
    st.markdown("<h4 class='big-text'>Mode:</h4>", unsafe_allow_html=True) # Display a header2
    mode = st.radio("", ["Query", "Fetch Similar Posts"]) # Radio button to select the mode

    if mode == "Query":
        query = st.text_input("Enter your query:") # Get the user's query
        if st.button("Submit"): # If the submit button is pressed
            # Add your logic here to generate the result based on the query

            # Display a loading spinner
            with st.spinner("Generating results..."):
                # Simulate a delay to show the loading animation
                time.sleep(3)

                # Generate the result
                result = {"query": query}

                # Clear the loading spinner
                st.spinner()

                # Display the result
                st.json(result)
    elif mode == "Fetch Similar Posts":
        similar_query = st.text_input("Enter your query:") # Get the user's query for similar posts
        if st.button("Submit"): # If the fetch button is pressed
            # Add your logic here to fetch similar posts based on the query

            # Display a loading spinner
            with st.spinner("Fetching similar posts to your query..."):
                # Simulate a delay to show the loading animation
                time.sleep(3)

                # Generate the result
                similar_posts = ["Example Post 1", "Example Post 2", "Example Post 3"]  # Example data, replace with your logic

                # Clear the loading spinner
                st.spinner()

                # Display the similar posts
                st.write("Similar Posts:")
                for post in similar_posts:
                    st.write(post)

if __name__ == "__main__":
    main()
