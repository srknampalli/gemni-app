from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Streamlit app
st.set_page_config(page_title=" Image Details")
st.header("Gemini Application")

def get_gemini_response(input, uploaded_file):
    model = genai.GenerativeModel('gemini-pro-vision')
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(input)
    return response.text

input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
submit = st.button("Tell me about the image")

if submit:
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        response = get_gemini_response(input, uploaded_file)
        st.subheader("The Response is")
        st.write(response)
    else:
        response = get_gemini_response(input, None)
        st.subheader("The Response is")
        st.write(response)


        #END