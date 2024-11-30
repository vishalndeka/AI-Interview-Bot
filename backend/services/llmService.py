import os
from dotenv import load_dotenv
from pathlib import Path
import ollama
from models.llmPrompts import LLMSetup
from models.interviews import QuestionAnswerPair
from typing import List

# not using ollama endpoint
env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(env_path)
ollama_endpoint = os.getenv("OLLAMA_ENDPOINT")


messages = []
topic = ""

def init_ollama(setup: LLMSetup):
    messages = []
    topic = setup.topic
    system_prompt = f"You are a smart and friendly interviewer, capable of seeing through a person and can accurately gauge their tecnical ability. You are proficient in coding and computer science topics, and you briefly comment on the received prompt, before asking a relevant follow up question or moving onto a new topic. Begin with the topic {setup.topic}"
    messages.append({'role': 'system', 'content': system_prompt})
    stream = ollama.chat(model=setup.model, messages=messages, stream=False)
    return stream

def next_question(qa_list: List[QuestionAnswerPair], model: str):
    try:
        messages = []
        system_prompt = (
            "You are a smart and friendly interviewer, capable of seeing through a "
            "person and can accurately gauge their technical ability. You are proficient "
            "in coding and computer science topics and ask a relevant follow-up question or move on."
        )
        messages.append({"role": "system", "content": system_prompt})

        # Add previous QA pairs to the context
        for qa in qa_list:
            messages.append({"role": "system", "content": qa.question})
            messages.append({"role": "user", "content": qa.answer})

        # Generate the next question
        stream = ollama.chat(model=model, messages=messages, stream=False)
        return stream
    except Exception as e:
        raise ValueError(f"Failed to generate the next question: {str(e)}")


