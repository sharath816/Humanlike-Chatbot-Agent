from fastapi import FastAPI, Request
from services.gemini_wrapper import GeminiChat
from memory.context_builder import build_context
from memory.memory_store import store_user_memory, fetch_user_memory
from tone.analyzer import detect_tone
from tone.adapter import adapt_response_by_tone

import re  # 🆕 For name extraction

app = FastAPI()
bot = GeminiChat()

def extract_user_name(text: str) -> str | None:
    """🆕 Extract user's name if they say 'my name is ___'."""
    match = re.search(r"\bmy name is (\w+)", text, re.IGNORECASE)
    return match.group(1) if match else None

@app.post("/chat/")
async def chat(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    user_input = data.get("message")

    # 1. Fetch user memory
    memory = fetch_user_memory(user_id)

    # 2. 🆕 Check if the user revealed their name
    name = extract_user_name(user_input)
    if name:
        memory += f"\nThe user's name is {name}."  # inject into context
        store_user_memory(user_id, f"My name is {name}", "Nice to meet you, {name}!")  # save for later

    # 3. Build full prompt from memory + new input
    system_prompt = (
        "You are Zia, a friendly and empathetic assistant. You remember the user's preferences, tone, and name if they mention it. Always respond warmly using prior memory if available."
    )
    prompt = system_prompt + build_context(user_id, memory, user_input)
    # 4. Detect user's emotional tone
    tone = detect_tone(user_input)

    # 5. Get raw response from Gemini
    response_raw = bot.get_response(prompt)

    # 6. Adapt the bot's response to user's tone
    response = adapt_response_by_tone(response_raw, tone)

    # 7. Store both user input and bot response in memory
    store_user_memory(user_id, user_input, response)

    # 8. Return the adapted response
    return {"reply": response}
