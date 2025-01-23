from AiChatBotApiClient.ai_chat_bot_api_client.models import ChatCreateRequestDto, ChatCompletionRequestDto
from AiChatBotApiClient.ai_chat_bot_api_client.api.chat import create_chat, chat_completion
import json
from uuid import UUID
from AiChatBotApiClient.ai_chat_bot_api_client.models import ChatCreateRequestDto
from chatbot_api.exceptions import ChatCreationError
from typing import Union


class ChatbotAPI:
    def __init__(self, client):
        """
        Initialize the chatbot API client.
        """
        self.client = client


    def create_chat(self, bot_id: Union[str, None]) -> str:
        """
        Create a new chat session with the given bot ID.

        :param client: The HTTP client instance used to make API calls.
        :param bot_id: The bot's unique identifier.
        :return: Chat ID for the created session.
        :raises ChatCreationError: If the chat creation fails.
        """
        # Step 1: Prepare the request payload
        try:
            request_body = ChatCreateRequestDto(bot_id=bot_id)



            request_payload = request_body.to_dict()
            print(f"✅ Request payload: {request_payload}")
        except Exception as e:
            raise ChatCreationError(
                message="❌ Failed to prepare the chat creation payload",
                details=str(e),
                bot_id=bot_id,
                status_code=None
            )

        #  create the chat session
        try:


            response =  create_chat.sync_detailed(client= self.client, body=request_body)
            print(f"✅ API response: {response}")

            # Inspect the response
            print(f"✅ Status Code: {response.status_code}")
            print(f"✅ Raw Content: {response.content}")
            print(f"✅ Parsed Response: {response.parsed}")

            # Step 3: Check the response status
            if response.status_code != 200:
                details = (
                    response.content.decode() if isinstance(response.content, bytes) else response.content
                )

            # Step 4: Parse the response
            if response.parsed is None or not hasattr(response.parsed, "chat_id"):
                print("❓ `parsed` response is None or `chat_id` attribute missing. Attempting fallback JSON parsing.")
                try:

                    response_data = response.content.decode() if isinstance(response.content, bytes) else response.content
                    parsed_data = json.loads(response_data)  # Convert JSON string to dictionary
                    chat_id = parsed_data.get("chatId")  # Extract `chatId`
                    if not chat_id:
                        raise ValueError("Missing `chatId` in fallback parsed data")
                    print(f"✅ Extracted chat_id: {chat_id}")
                    return chat_id
                except Exception as fallback_error:
                    raise ChatCreationError(
                        message="❌ Response parsing failed: chat_id not found (fallback parsing also failed)",
                        status_code=response.status_code,
                        bot_id=bot_id,
                        details=str(fallback_error)
                    )

            chat_id = response.parsed.chat_id
            chat_id = chat_id.strip('"')  # Strip any surrounding quotes
            return chat_id

        except Exception as e:
            print(f"❌ Error occurred while creating chat: {str(e)}")
            raise ChatCreationError(
                message="❌ Failed to create chat due to an unexpected error",
                bot_id=bot_id,
                status_code=None,
                details=str(e)
            )


    def send_message(self, chat_id: UUID, user_message: str) -> str:
        """
        Send a message to an existing chat session.
        """
        request_body = ChatCompletionRequestDto(user_message=user_message)
        try:
            # Call the API and get the response
            response = chat_completion.sync_detailed(chat_id=chat_id, client=self.client, body=request_body)

            if response.status_code != 200 or not response.content:
                raise ValueError(f"❌ Message sending failed: {response.content}")

            # Deserialize the response content into a dictionary
            response_data = json.loads(response.content)


            return response_data['assistantMessage']
        except Exception as e:
            raise ValueError(f"❌ Error sending message: {e}")
