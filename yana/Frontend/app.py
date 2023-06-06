import streamlit as st
from PIL import Image

import numpy as np
import streamlit as st
import base64

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
    set_background('/home/emanuel/code/cenedikt/yana/yana/Frontend/Content/Yana_background_image.png')

    st.markdown("# Query App")

    query = st.text_input("Enter your query:")
    if st.button("Generate Result"):
        # Add your logic here to generate the result based on the query
        result = {"query": query, "result": "This is the result"}
        st.json(result)

if __name__ == "__main__":
    main()
