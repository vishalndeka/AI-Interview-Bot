from fastapi import APIRouter
from models.interviews import Interview
from config.database import collection_name # collection inside mongodb client
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

# GET Request Method
@router.get("/")
async def get_interviews():
    interviews = list_serial(collection_name.find())
    return interviews

# POST Request method
@router.post("/")
async def post_interview(interview : Interview):
    collection_name.insert_one(dict(interview))

# PUT Request method
@router.put("/{id}")
async def put_interview(id: str, interview : Interview):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(interview)})

# DELETE Request Method
@router.delete("/{id}")
async def delete_interview(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})