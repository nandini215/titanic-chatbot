import streamlit as st
import requests

BACKEND_URL = "http://your-backend-url.com"  # Replace with actual URL

st.title("Titanic Chatbot")
st.write("Ask a question about the Titanic dataset:")

query = st.text_input("Enter your question:", "")

if st.button("Get Answer"):
    if query.strip():
        try:
            response = requests.get(f"{BACKEND_URL}/predict", params={"query": query})

            if response.status_code == 200:
                try:
                    data = response.json()  # Handle JSON errors
                    if "answer" in data:
                        st.write("### Answer:")
                        st.write(data["answer"])
                    else:
                        st.error("Unexpected response format from backend.")
                except ValueError:
                    st.error("Error: Backend returned an empty or invalid JSON response.")
            else:
                st.error(f"Error {response.status_code}: Unable to fetch data.")
        except requests.exceptions.RequestException as e:
            st.error(f"Connection error: {e}")
    else:
        st.warning("Please enter a valid question before submitting.")

