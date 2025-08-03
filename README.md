# Zia: Human-like Conversational Chatbot

Zia is an emotionally intelligent, memory-aware chatbot built using FastAPI and Google's Gemini API. It aims to replicate human-like interactions by understanding user tone, remembering context, and personalizing responses.

## 🔧 Features

- **Emotion Detection**: Adjusts tone based on user emotion.
- **Memory System**: Recalls previous conversations for context.
- **Name Recognition**: Learns and uses user's name.
- **Tone Adaptation**: Matches the emotional tone of the user input.
- **Context Awareness**: Responds contextually using prior messages.
- **Gemini API**: Uses Google’s Gemini 1.5 model for LLM-based conversation.

## 📁 Project Structure

```
backend/
├── main.py                # FastAPI app with main logic
├── services/
│   └── gemini_wrapper.py  # Gemini API integration
├── memory/
│   ├── context_builder.py # Builds prompt context from memory
│   └── memory_store.py    # Memory retrieval and storage
├── tone/
│   ├── analyzer.py        # Detects tone from input
│   └── adapter.py         # Adapts LLM response to detected tone
```

## 🛠️ Setup Instructions

1. Clone the repository.
2. Create a `.env` file and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the FastAPI app:
   ```bash
   uvicorn main:app --reload
   ```

## 🧠 Example Prompt Format

```
You are Zia, a human-like, emotionally intelligent AI chatbot...
Here is the prior conversation:
<User's 5 recent messages>
User: What's your name?
Zia:
```

## 📫 Contact

Developed by Sharath M T.