def adapt_response_by_tone(response: str, tone: str) -> str:
    if tone == "positive":
        return response + " 😊"
    elif tone == "negative":
        return "I'm here for you. " + response
    elif tone == "neutral":
        return response
    else:
        return response
