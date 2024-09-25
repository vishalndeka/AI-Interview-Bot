from fastapi import APIRouter
from models.interviews import Interview
from config.database import collection_name # collection inside mongodb client
from schema.schemas import individual_serial, list_serial
from bson import ObjectId

router = APIRouter()

# GET Request Method
@router.get("/")
async def get_interviews():
    interviews = collection_name.find()
    serialized_interviews = [
        {
            "id": str(interview["_id"]),
            "date": interview.get("date"),
            "name": interview.get("name"),
            "qa_list": interview.get("qa_list", [])
        }
        for interview in interviews
    ]
    return serialized_interviews

# POST Request method
@router.post("/")
async def post_interview(interview: Interview):
    serialized_interview = individual_serial(interview)
    collection_name.insert_one(serialized_interview)
    return {"message": "Interview added successfully"}

# PUT Request method
@router.put("/{id}")
async def put_interview(id: str, interview : Interview):
    serialized_interview = individual_serial(interview)
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": serialized_interview})
    return {"message": "Interview modified successfully"}

# DELETE Request Method
@router.delete("/{id}")
async def delete_interview(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})