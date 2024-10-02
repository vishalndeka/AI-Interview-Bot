from pydantic import BaseModel
from typing import List
from  datetime import datetime

class QuestionAnswerPair(BaseModel):
    question: str
    answer: str

class Interview(BaseModel):
    #_id: str # changed
    start_time: datetime
    end_time: datetime
    user_id: str
    topic_name: str
    qa_list: List[QuestionAnswerPair]
    