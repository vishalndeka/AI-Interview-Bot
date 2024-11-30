import requests
import json
import os
from dotenv import load_dotenv
from pathlib import Path
import ollama

# not using ollama endpoint
env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(env_path)
ollama_endpoint = os.getenv("OLLAMA_ENDPOINT")


messages = []

def init_ollama(self, prompt):
    messages = []
    system_prompt = f"You are a smart and friendly interviewer, capable of seeing through a person and can accurately gauge their tecnical ability. You are proficient in coding and computer science topics, and you briefly comment on the received prompt, before asking a relevant follow up question or moving onto a new topic. Begin with the topic {topic}"

    pass