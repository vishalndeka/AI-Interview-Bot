from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models.interviews import Interview
from models.users import User
from config.database import interviews_collection, users_collection # collection inside mongodb client
from schema.schemas import individual_serial_interview
from bson import ObjectId
from services.hashing import Hash
from services.jwttoken import create_access_token

router = APIRouter()

# GET Request Method
@router.get("/")
async def get_interviews():
    interviews = interviews_collection.find()
    serialized_interviews = [
        {
            "id": str(interview["_id"]), # mongo-db generated id
            "start_time": interview.get("start_time"),
            "end_time": interview.get("end_time"),
            "user_id": interview.get("user_id"),
            "topic_name": interview.get("topic_name"),
            "qa_list": interview.get("qa_list", [])
        }
        for interview in interviews
    ]
    return serialized_interviews

# POST Request method
@router.post("/")
async def post_interview(interview: Interview):
    serialized_interview = individual_serial_interview(interview)
    interviews_collection.insert_one(serialized_interview)
    return {"message": "Interview added successfully"}

# PUT Request method
@router.put("/{id}")
async def put_interview(id: str, interview : Interview):
    serialized_interview = individual_serial_interview(interview)
    interviews_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": serialized_interview})
    return {"message": "Interview modified successfully"}

# DELETE Request Method
@router.delete("/{id}")
async def delete_interview(id: str):
    interviews_collection.find_one_and_delete({"_id": ObjectId(id)})

# @router.post('/register')
# def create_user(request:User):
#    hashed_pass = Hash.bcrypt(request.password)
#    user_object = dict(request)
#    user_object["password"] = hashed_pass
#    user_id = users_collection.insert_one(user_object)
#    return {"res":"created"}

# @router.post('/login')
# def login(request:OAuth2PasswordRequestForm = Depends()):
#     user = users_collection.find_one({"username":request.username})
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#     if not Hash.verify(user["password"],request.password):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#     access_token = create_access_token(data={"sub": user["username"] })
#     return {"access_token": access_token, "token_type": "bearer"}