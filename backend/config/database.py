from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(env_path)
uri = os.getenv("MONGODB_URI")
client = MongoClient(uri)

db = client.interview_db

interviews_collection = db["interview_collection"]
users_collection = db['users_collection']
print(uri)