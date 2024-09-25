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