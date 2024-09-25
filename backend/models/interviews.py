from pydantic import BaseModel
from typing import List
from  datetime import datetime

class QuestionAnswerPair(BaseModel):
    question: str
    answer: str

class Interview(BaseModel):
    date: datetime
    qa_list: List[QuestionAnswerPair]