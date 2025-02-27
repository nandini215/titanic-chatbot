import streamlit as st
import requests

# Define backend API URL
BACKEND_URL = "http://your-backend-url.com"  # Replace with actual backend URL

st.title("Titanic Chatbot")
st.write("Ask a question about the Titanic dataset:")

# Input field for user query
query = st.text_input("Enter your question:", "")

if st.button("Get Answer"):
    if query.strip():  # Ensure the query is not empty
        try:
            response = requests.get(f"{BACKEND_URL}/predict", params={"query": query})
            
            if response.status_code == 200:
                st.write("### Answer:")
                st.write(response.json()["answer"])  # Adjust based on API response format
            else:
                st.error("Error: Unable to fetch data. Please try again.")
        except requests.exceptions.RequestException as e:
            st.error(f"Connection error: {e}")
    else:
        st.warning("Please enter a valid question before submitting.")
