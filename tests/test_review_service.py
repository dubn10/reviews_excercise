
from app.services.review_service import process_review

def test_process_review():
    review = "This is a good product."
    result = process_review(review)
    assert result['sentiment'] == "positive"
    assert isinstance(result['readability_score'], float)
    assert isinstance(result['suggestions'], list)
    