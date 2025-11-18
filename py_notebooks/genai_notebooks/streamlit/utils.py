import os
from dotenv import load_dotenv
from openai import OpenAI

def get_openai_client():
    import streamlit as st  # Importing Streamlit within the function to access st.secrets

    key = None  # Initialize the key variable
    
    # Check if the API key is available in Streamlit secrets (cloud environment)
    if "OPENAI_API_KEY" in st.secrets:
        key = st.secrets["OPENAI_API_KEY"]
    else:
        # Fallback to loading from .env file (for local development)
        load_dotenv()
        key = os.getenv("OPENAI_API_KEY")
    
    # If the key is not found, raise an error
    if not key:
        raise RuntimeError("OPENAI_API_KEY not found in st.secrets or .env")
    
    # Return the OpenAI client initialized with the API key
    return OpenAI(api_key=key)
