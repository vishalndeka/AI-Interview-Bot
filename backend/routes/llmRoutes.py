from fastapi import APIRouter
from services.llmService import init_ollama

router = APIRouter()

@router.post("/beginInterview")
async def beginInterview(info):  # FastAPI will expect JSON with a "prompt" field
    try:
        response = init_ollama(info)  # Extract the "prompt" field
        return {"question": response}
    except Exception as e:
        return {"error": str(e)}