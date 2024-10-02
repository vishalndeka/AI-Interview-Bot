from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class User(BaseModel):
    username: str
    email: str
    password: str
    createdAt: datetime
    interview_ids: List[str]

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None