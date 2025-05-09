
from fastapi import APIRouter
from app.models.schemas import ReviewRequest, ReviewResponse
from app.services.review_service import process_review

router = APIRouter()

@router.post("/review", response_model=ReviewResponse)
def review_endpoint(review: ReviewRequest):
    return process_review(review.text)