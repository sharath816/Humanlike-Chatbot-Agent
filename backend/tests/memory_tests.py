import requests
import time

BASE_URL = "http://localhost:8000/chat/"
user_id = "test_user_123"

# --- Existing Tests ---

def test_long_term_memory():
    print("\n➡️ Step 1: Set favorite color")
    requests.post(BASE_URL, json={"user_id": user_id, "message": "My favorite color is blue"})
    time.sleep(1)

    print("➡️ Step 2: Ask what my favorite color is")
    res = requests.post(BASE_URL, json={"user_id": user_id, "message": "Do you remember my favorite color?"})
    print("Bot:", res.json()["reply"])
    assert "blue" in res.json()["reply"].lower()

def test_tone_adaptation_sad():
    res = requests.post(BASE_URL, json={"user_id": user_id, "message": "I'm feeling really down today"})
    print("\nSad response:", res.json()["reply"])
    assert any(word in res.json()["reply"].lower() for word in ["sorry", "hear", "support", "understand"])

def test_tone_adaptation_happy():
    res = requests.post(BASE_URL, json={"user_id": user_id, "message": "I just got promoted!"})
    print("\nHappy response:", res.json()["reply"])
    assert any(word in res.json()["reply"].lower() for word in ["congrat", "awesome", "great", "happy"])

# --- New Tests ---

def test_identity_retention():
    print("\n➡️ Storing name for identity")
    requests.post(BASE_URL, json={"user_id": user_id, "message": "My name is Zia"})
    time.sleep(1)

    res = requests.post(BASE_URL, json={"user_id": user_id, "message": "What is my name?"})
    print("Bot:", res.json()["reply"])
    assert "zia" in res.json()["reply"].lower()

def test_consistent_personality_tone():
    messages = [
        "Hello there!",
        "What's the weather like?",
        "Tell me a joke.",
        "Do you remember my name?"
    ]
    print("\n➡️ Checking tone consistency across multiple messages")
    responses = [requests.post(BASE_URL, json={"user_id": user_id, "message": msg}).json()["reply"] for msg in messages]
    for res in responses:
        print("Bot:", res)
        assert any(greeting in res.lower() for greeting in ["hi", "sure", "glad", "of course", "😊", "hello"])

def test_chat_history_recall():
    print("\n➡️ Step 1: Saying something to test recall")
    requests.post(BASE_URL, json={"user_id": user_id, "message": "I'm going on a trip to Paris next week"})
    time.sleep(1)

    print("➡️ Step 2: Asking for recall")
    res = requests.post(BASE_URL, json={"user_id": user_id, "message": "Where did I say I was going?"})
    print("Bot:", res.json()["reply"])
    assert "paris" in res.json()["reply"].lower()

def test_vector_store_semantic_memory():
    print("\n➡️ Setting a semantic memory fact")
    requests.post(BASE_URL, json={"user_id": user_id, "message": "My dog’s name is Bruno"})
    time.sleep(1)

    print("➡️ Asking using different words")
    res = requests.post(BASE_URL, json={"user_id": user_id, "message": "Do you remember what I called my pet?"})
    print("Bot:", res.json()["reply"])
    assert "bruno" in res.json()["reply"].lower()
