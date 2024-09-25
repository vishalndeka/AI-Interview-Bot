# def individual_serial(interview) -> dict:
#     return {
#         "id": str(interview["_id"]),
#         "date": interview["date"],
#         "qa_list": dict(interview["qa_list"])
#     }

# # serializes all data into a dictionary of key and value pairs
# def list_serial(interviews) -> list:
#     return [individual_serial(interview) for interview in interviews]

from models.interviews import Interview, QuestionAnswerPair

# Serialize individual QuestionAnswerPair
def serialize_question_answer_pair(qap: QuestionAnswerPair) -> dict:
    return {
        "question":qap.question,
        "answer": qap.answer
        }

# Serialize Interview object to BSON-compatible format
def individual_serial(interview: Interview) -> dict:
    return {
        "date": interview.date,  # datetime is already BSON-compatible
        "name": interview.name,
        "qa_list": [serialize_question_answer_pair(qap) for qap in interview.qa_list]
    }

def list_serial(interviews: list) -> list:
    return [individual_serial(interview) for interview in interviews]