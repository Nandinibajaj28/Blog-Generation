from langchain_groq import GroqChat
import os
from dotenv import load_dotenv



class GroqLLM:
    def __init__(self):
        load_dotenv()

    def get_model(self):
        try:
            os.environ["GROQ_API_KEY"] = self.groq_api_key = os.getenv("GROQ_API_KEY")
            llm = GroqChat(model_name="", api_key=self.groq_api_key)
            return llm
        except Exception as e:
            raise ValueError(f"Error loading Groq LLM: {e}")