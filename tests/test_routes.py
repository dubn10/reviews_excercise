
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_review_endpoint():
    response = client.post("/review", json={"text": "This product is excellent!"})
    assert response.status_code == 200
    data = response.json()
    assert "sentiment" in data
    assert "readability_score" in data
    assert "suggestions" in data

def test_positive_sentiment():
    response = client.post("/review", json={"text": "This product is amazing and perfect for my needs!"})
    data = response.json()
    assert data["sentiment"] == "positive"

def test_negative_sentiment():
    response = client.post("/review", json={"text": "This product is terrible and disappointing."})
    data = response.json()
    assert data["sentiment"] == "negative"

def test_neutral_sentiment():
    response = client.post("/review", json={"text": "I bought this product yesterday."})
    data = response.json()
    assert data["sentiment"] == "neutral"

def test_short_review_suggestion():
    response = client.post("/review", json={"text": "Good product"})
    data = response.json()
    assert "Add more detail to your review." in data["suggestions"]

def test_excessive_punctuation():
    response = client.post("/review", json={"text": "Great product!!!!!"})
    data = response.json()
    assert "Avoid using excessive punctuation." in data["suggestions"]

def test_all_caps_suggestion():
    response = client.post("/review", json={"text": "THIS PRODUCT IS AMAZING"})
    data = response.json()
    assert "Avoid writing in all capital letters." in data["suggestions"]

def test_no_specific_details():
    response = client.post("/review", json={"text": "The product is good and I like it a lot"})
    data = response.json()
    assert "Consider including specific details or examples." in data["suggestions"]

def test_repetitive_vocabulary():
    response = client.post("/review", json={"text": "good good good good good"})
    data = response.json()
    assert "Try to use more varied vocabulary." in data["suggestions"]

def test_no_sentences():
    response = client.post("/review", json={"text": "good product nice quality fast delivery"})
    data = response.json()
    assert "Break your review into sentences for better readability." in data["suggestions"]

