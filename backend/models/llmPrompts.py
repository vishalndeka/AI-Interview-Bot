from pydantic import BaseModel

class LLMSetup(BaseModel):
    topic: str
    model: str

    def __repr__(self):
        return self.topic + " : " + self.model