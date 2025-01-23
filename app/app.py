
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import uuid
from uuid import UUID
from openai import OpenAI
from params import *



app = FastAPI()

# Mocked database for simplicity
chats_db: Dict[UUID, Dict[str, str]] = {}

# Request models
class ChatCreateRequest(BaseModel):
    botId: str


class ChatCompletionRequest(BaseModel):
    userMessage: str


# Response models
class ChatCreateResponse(BaseModel):
    chatId: UUID


class ChatCompletionResponse(BaseModel):
    assistantMessage: str


@app.get("/")
def read_root():
    return {"message": "Hello, Wellcome to Chatbot Project!"}


@app.post("/api/chats")
def create_chat(chat: ChatCreateRequest):
    """
    Create a new chat session.
    """
    if not chat.botId:
        raise HTTPException(status_code=400, detail="Bot ID is required")

    # Generate a unique chat ID
    chat_id = uuid.uuid4()

    chats_db[chat_id] = {"botId": chat.botId, "history": []}

    return chat_id


@app.post("/api/chats/{chat_id}/completions", response_model=ChatCompletionResponse)
def chat_completion(chat_id: UUID, completion: ChatCompletionRequest):
    """
    Send a message to an existing chat session.
    """
    # Check if the chat ID exists
    if chat_id not in chats_db:
        raise HTTPException(status_code=404, detail="Chat session not found")

    user_message = completion.userMessage

    if OPENAI_API_KEY :
        # OpenAI to assist the user
        def get_assistant_message(user_message):
            client= OpenAI(api_key = OPENAI_API_KEY)
            response = client.chat.completions.create(
            model=OPENAI_MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are an expert at describing images in detail."},
                {"role": "user", "content": user_message}
            ]
            )
            return response.choices[0].message.content.strip().strip()
        assistant_message = get_assistant_message(user_message)
    else:
        # Simple bot logic: Echo the user's message
        # placeholder for a chatbot system.
        assistant_message = f"I received your message: {user_message}"

    # Store the conversation in the history
    chats_db[chat_id]["history"].append({"user": user_message, "assistant": assistant_message})

    return {"assistantMessage": assistant_message}
