import streamlit as st
import requests
import time

# Page setup
st.set_page_config(page_title="Zia – Human-like AI", layout="wide")

# Sidebar with Zia Memory
with st.sidebar:
    st.header("🧠 Zia Remembers...")
    st.markdown("This sidebar will soon show saved facts about you or recent context.")
    mode = st.radio("🎭 Conversation Mode", ["Human", "Professional"])
    if "history" in st.session_state:
        st.markdown("**Last Few Messages**")
        for role, msg in st.session_state.history[-4:][::-1]:
            icon = "🧍" if role == "user" else "🤖"
            st.write(f"{icon} {msg[:50]}...")

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
        background-color: #f6f9fc;
    }
    .top-bar {
        background-color: #1111;
        padding: 18px 30px;
        border-radius: 18px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.04);
        text-align: center;
    }
    .chat-container {
        max-width: 860px;
        margin: auto;
    }
    .chat-row {
        display: flex;
        align-items: flex-end;
        margin-bottom: 12px;
    }
    .chat-bubble {
        padding: 14px 20px;
        border-radius: 18px;
        max-width: 70%;
        font-size: 16px;
        line-height: 1.6;
        display: inline-block;
    }
    .user-row {
        justify-content: flex-end;
    }
    .bot-row {
        justify-content: flex-start;
    }
    .user {
        background: linear-gradient(135deg, #4f46e5, #6366f1);
        color: white;
        border-bottom-right-radius: 4px;
    }
    .bot {
        background-color: #e6e9f0;
        color: #2c3e50;
        border-bottom-left-radius: 4px;
    }
    .avatar {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        margin: 0 10px;
    }
    .suggestions {
        text-align: center;
        margin: 20px 0;
    }
    .suggestion-btn {
        display: inline-block;
        margin: 4px 6px;
        background-color: #e0e7ff;
        color: #1e3a8a;
        padding: 8px 14px;
        border-radius: 20px;
        font-size: 14px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
st.markdown("<div class='top-bar'><h2>🤖 Zia – Your AI Assistant</h2></div>", unsafe_allow_html=True)

# ID Input
user_id = st.text_input("👤 Your Name or ID", "shaanu")

# Chat History
if "history" not in st.session_state:
    st.session_state.history = []

# Suggestions Row
suggestions = ["Tell me a fun fact", "What’s the weather like?", "Give me motivation", "Who are you?"]
st.markdown("<div class='suggestions'>", unsafe_allow_html=True)
for s in suggestions:
    if st.button(s):
        st.session_state.suggestion_input = s
st.markdown("</div>", unsafe_allow_html=True)

# Chat Input (with adaptive state)
user_input = st.chat_input("💬 Talk to Zia...")

# Handle suggestion as input
if "suggestion_input" in st.session_state:
    user_input = st.session_state.pop("suggestion_input")

# Backend interaction
if user_input:
    st.session_state.history.append(("user", user_input))

    # Fake Typing Delay
    with st.spinner("🤖 Zia is typing..."):
        time.sleep(1.6)
        try:
            response = requests.post("http://localhost:8000/chat/", json={
                "user_id": user_id,
                "message": user_input,
                "mode": mode
            }).json()
            bot_reply = response.get("reply", "Zia is thinking...")
        except:
            bot_reply = "⚠️ Backend not reachable."

    st.session_state.history.append(("bot", bot_reply))

# Render chat bubbles
for role, msg in st.session_state.history:
    if role == "user":
        st.markdown(f"""
        <div class="chat-row user-row">
            <div class="chat-bubble user">{msg}</div>
            <img src="https://img.icons8.com/ios-filled/50/ffffff/user-male-circle.png" class="avatar" />
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-row bot-row">
            <img src="https://img.icons8.com/ios-filled/50/000000/robot-2--v2.png" class="avatar" />
            <div class="chat-bubble bot">{msg}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
