import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.auth.transport.requests import Request
from google.oauth2 import service_account
import streamlit as st
from vision import get_gemini_response

# Load environment variables from .env file
load_dotenv()

# Configure the Generative API client with the API key
genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Initialize the Streamlit app
st.header("Gemini Application")

text_input_key = "text_input"
image_upload_key = "image_upload"

input = st.text_input("Input: ", key=text_input_key)
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key=image_upload_key)
submit = st.button("Ask the question")

if submit:
    if uploaded_file is not None:
        response = get_gemini_response(input, uploaded_file)
        st.subheader("The Response is")
        st.write(response)
    else:
        response = get_gemini_response(input, None)
        st.subheader("The Response is")
        st.write(response)

#END