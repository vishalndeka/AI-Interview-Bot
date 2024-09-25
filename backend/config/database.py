from pymongo import MongoClient

uri = "mongodb+srv://neerzmu4l:4vmPQousjn5JJxlg@cluster0.bduo4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

db = client.interview_db

collection_name = db["interview_collection"]