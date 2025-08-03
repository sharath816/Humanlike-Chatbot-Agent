import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("chat_memory")

def store_user_memory(user_id, question, answer):
    collection.add(
        documents=[f"Q: {question}\nA: {answer}"],
        ids=[user_id + f"-{len(fetch_user_memory(user_id))}"],
        metadatas=[{"user": user_id}]
    )

def fetch_user_memory(user_id):
    results = collection.get(
        where={"user": user_id}
    )
    return results["documents"]
