from bson import ObjectId
from fastapi import APIRouter, HTTPException
from services.llmService import init_ollama, next_question
from models.llmPrompts import LLMSetup
from datetime import datetime
from config.database import interviews_collection
from models.interviews import QuestionAnswerPair

router = APIRouter()

@router.post("/beginInterview")
async def beginInterview(setup: LLMSetup):  # FastAPI will expect JSON with a "prompt" field
    try:
        # Initialize interview record
        new_interview = {
            "start_time": datetime.utcnow(),
            "topic_name": setup.topic,
            "model_name": setup.model,
            "qa_list": [],  # Empty for now, can be updated later
        }

        # Insert the interview into the database
        result = interviews_collection.insert_one(new_interview)
        inserted_id = str(result.inserted_id)  # Get the ObjectID as a string

        # Generate the stream using the provided setup
        stream = init_ollama(setup)

        # Return both the inserted ID and the stream
        return {"id": inserted_id, "stream": stream.message}
    except Exception as e:
        return {"error": str(e)}

@router.post("/pushAnswer/{interview_id}")
async def push_answer(interview_id: str, qa_pair: dict):
    try:
        # Validate interview ID
        interview = interviews_collection.find_one({"_id": ObjectId(interview_id)})
        if not interview:
            raise HTTPException(status_code=404, detail="Interview not found")

        # Validate question and answer
        question = qa_pair.get("question")
        answer = qa_pair.get("answer")
        if not question or not answer:
            raise HTTPException(status_code=400, detail="Invalid question or answer")

        # Append question-answer pair to qa_list
        updated_qa_list = interview.get("qa_list", [])
        updated_qa_list.append({"question": question, "answer": answer})

        # Update the document in the database
        interviews_collection.update_one(
            {"_id": ObjectId(interview_id)},
            {"$set": {"qa_list": updated_qa_list}}
        )

        # Generate the next question
        qa_pairs = [
            QuestionAnswerPair(question=qa["question"], answer=qa["answer"])
            for qa in updated_qa_list
        ]
        next_q_stream = next_question(qa_pairs, interview["model_name"])
        next_question_content = next_q_stream.message.content

        return {"question": next_question_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
