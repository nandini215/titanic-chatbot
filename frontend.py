import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO

# FastAPI backend URL
BACKEND_URL = "http://127.0.0.1:9000"


st.title("Titanic Chatbot")

query = st.text_input("Ask a question about the Titanic dataset:")

if st.button("Get Answer"):
    if query:
        response = requests.get(f"{BACKEND_URL}/predict", params={"query": query})
        
        if response.status_code == 200:
            result = response.json()

            if "answer" in result:
                st.write("### Answer:", result["answer"])
            
            if "image" in result:
                image_data = base64.b64decode(result["image"])
                image = Image.open(BytesIO(image_data))
                st.image(image, caption="Generated Visualization")

        else:
            st.error("Error fetching response from the backend.")
    else:
        st.warning("Please enter a question.")
