from fastapi import FastAPI
from routes.route import router
app = FastAPI()

# to run this server, in terminal: uvicorn main:app --reload

# from pymongo.mongo_client import MongoClient

# uri = "mongodb+srv://neerzmu4l:4vmPQousjn5JJxlg@cluster0.bduo4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

app.include_router(router)

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import json
# import os
# import torch
# from transformers import AutoModelForCausalLM, AutoTokenizer
# from pydantic import BaseModel

# app = FastAPI()

# # Load the Qwen2.5 model and tokenizer
# model_name = "Qwen/Qwen2.5-7B-Instruct"
# model = AutoModelForCausalLM.from_pretrained(
#     model_name,
#     torch_dtype="auto",
#     device_map="auto"
# )
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# # CORS setup for frontend communication
# origins = [
#     "http://localhost:5174",
#     "http://localhost:5173",
#     "http://localhost:8000",
#     "http://localhost:3000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load chat history from a JSON file
# def load_messages():
#     file = 'database.json'
#     messages = []

#     # Check if the file exists and is not empty
#     if os.path.exists(file) and os.stat(file).st_size != 0:
#         with open(file) as db_file:
#             data = json.load(db_file)
#             for item in data:
#                 messages.append(item)
#     else:
#         # If the file is empty, start a new conversation
#         messages.append({
#             "role": "system",
#             "content": "You are interviewing the user for a front-end React developer position. Ask short questions that are relevant to a junior-level developer. Your name is Greg. The user is Travis. Keep responses under 30 words and be funny sometimes."
#         })
#         messages.append({
#             "role": "assistant",
#             "content": "Hi Travis! Let's start with a simple one. Can you tell me what JSX is in React?"
#         })
#     return messages

# # Save chat history
# def save_messages(user_message, qwen_response):
#     file = 'database.json'
#     messages = load_messages()
#     messages.append({"role": "user", "content": user_message})
#     messages.append({"role": "assistant", "content": qwen_response})
#     with open(file, 'w') as f:
#         json.dump(messages, f)

# # Function to get a response from the Qwen model
# def get_chat_response(user_message):
#     messages = load_messages()
#     messages.append({"role": "user", "content": user_message})

#     # Convert the chat into a format suitable for Qwen
#     text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
#     model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

#     # Generate response using Qwen model
#     generated_ids = model.generate(
#         **model_inputs,
#         max_new_tokens=512
#     )

#     generated_ids = [
#         output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
#     ]

#     # Decode the model response
#     qwen_response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

#     # Save messages
#     save_messages(user_message, qwen_response)

#     return qwen_response

# # Define the input model for the request body
# class TextInput(BaseModel):
#     message: str  # Expecting a 'message' field in the JSON

# @app.get("/")
# async def root():
#     return {"message": "Hello! Greg the interview bot is ready to ask questions!"}

# @app.post("/talk")
# async def post_text(text_input: TextInput):
#     user_message = text_input.message  # Extract message from the JSON body
#     chat_response = get_chat_response(user_message)  # Get chat response from your logic
#     return {"response": chat_response}  # Return response as JSON

# @app.get("/clear")
# async def clear_history():
#     file = 'database.json'
#     open(file, 'w').close()  # Clear the contents of the file
#     return {"message": "Chat history has been cleared"}
