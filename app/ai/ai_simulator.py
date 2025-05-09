
import textstat

def analyze_review(text: str):
    # Simulate sentiment
    lower = text.lower()
    if any(word in lower for word in ["bad", "terrible", "worst", "horrible", "awful", "disappointing", "not good", "not great", "not bad", "not awful", "not disappointing", "not terrible", "not worst"]):
        sentiment = "negative"
    elif any(word in lower for word in ["good", "excellent", "perfect", "great", "amazing", "fantastic", "wonderful", "terrific", "superb", "incredible", "outstanding", "excellent", "superb", "fantastic", "wonderful", "terrific", "incredible", "outstanding"]):
        sentiment = "positive"
    else:
        sentiment = "neutral"

    # Readability score
    score = textstat.flesch_reading_ease(text)

    # Suggestions (improved rules)
    suggestions = []
    
    # Length checks
    word_count = len(text.split())
    if word_count < 5:
        suggestions.append("Add more detail to your review.")
    elif word_count > 500:
        suggestions.append("Consider making your review more concise.")
    
    # Formatting checks
    if "!" in text:
        suggestions.append("Avoid using excessive punctuation.")
    if text.isupper():
        suggestions.append("Avoid writing in all capital letters.")
    
    # Content checks
    if not any(char.isdigit() for char in text):
        suggestions.append("Consider including specific details or examples.")
    if len(set(text.split())) < 5:
        suggestions.append("Try to use more varied vocabulary.")
    
    # Structure checks
    if "." not in text:
        suggestions.append("Break your review into sentences for better readability.")
    if len(text.split(".")) > 5 and not any("\n" in text):
        suggestions.append("Consider breaking your review into paragraphs.")

    return {
        "sentiment": sentiment,
        "readability_score": score,
        "suggestions": suggestions,
    }