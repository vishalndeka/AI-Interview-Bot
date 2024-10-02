from models.interviews import Interview, QuestionAnswerPair

# Serialize individual QuestionAnswerPair
def serialize_question_answer_pair(qap: QuestionAnswerPair) -> dict:
    return {
        "question":qap.question,
        "answer": qap.answer
    }

# Serialize Interview object to BSON-compatible format
def individual_serial_interview(interview: Interview) -> dict:
    return {
        # "_id": interview._id,
        "start_time": interview.start_time,
        "end_time": interview.end_time,  # datetime is already BSON-compatible
        "user_id": interview.user_id,
        "topic_name": interview.topic_name,
        "qa_list": [serialize_question_answer_pair(qap) for qap in interview.qa_list]
    }

def list_serial_interview(interviews: list) -> list:
    return [individual_serial_interview(interview) for interview in interviews]