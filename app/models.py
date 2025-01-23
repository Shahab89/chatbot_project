from pydantic import BaseModel


class CreateChatRequest(BaseModel):
    bot_id: str


class CreateChatResponse(BaseModel):
    chat_id: str


class MessageRequest(BaseModel):
    user_message: str


class MessageResponse(BaseModel):
    assistant_message: str
