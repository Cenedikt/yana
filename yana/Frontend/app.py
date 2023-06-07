import streamlit as st

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
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True) # Apply the background image using Streamlit's markdown feature

def main():
    set_background('/home/emanuel/code/cenedikt/yana/yana/Frontend/Content/Yana_background_image.png')

    st.markdown("<h1>YANA: You are not alone</h1>", unsafe_allow_html=True)

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

if __name__ == "__main__":
    main()
