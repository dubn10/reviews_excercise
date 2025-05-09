
from pydantic import BaseModel

class ReviewRequest(BaseModel):
    text: str

class ReviewResponse(BaseModel):
    sentiment: str
    readability_score: float
    suggestions: list[str]
    