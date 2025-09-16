import os
import streamlit as st
from langchain_groq import ChatGroq

class   GROQLLM:
    def __init__(self, user_control_input):
        self.user_control_input = user_control_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_control_input.get("GROQ_API_KEY")
            selected_model = self.user_control_input.get("selected_model")
            if groq_api_key == '' and os.environ["GROQ_API_KEY"] == '':
                st.error("GROQ_API_KEY is not set. Please provide a valid API key.")
            
            llm = ChatGroq(api_key=groq_api_key, model=selected_model)

        except Exception as e:
            raise ValueError(f"Error initializing GROQ LLM: {e}")
        return llm