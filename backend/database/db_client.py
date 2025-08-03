import redis 
import os

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

def save_to_redis(user_id, message, reply):
    history = r.get(user_id)
    new_entry = f"Q: {message}\nA: {reply}"
    updated_history = f"{history}\n{new_entry}" if history else new_entry
    r.set(user_id, updated_history)

def get_from_redis(user_id):
    history = r.get(user_id)
    return history.split("\n") if history else []
