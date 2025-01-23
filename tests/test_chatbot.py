import pytest
from unittest.mock import patch
from chatbot_api.chatbot import ChatbotAPI
from AiChatBotApiClient.ai_chat_bot_api_client.client import AuthenticatedClient
from AiChatBotApiClient.ai_chat_bot_api_client.models import ChatCreateRequestDto, ChatCompletionRequestDto
from unittest.mock import ANY
import responses
from uuid import uuid4
from params import *

# BASE_URL = 'https://chatbot-dev.example.com'

@responses.activate
def test_authenticated_client():
    """
    Test the AuthenticatedClient for correct authentication header and successful request.
    """

    # Mock the API endpoint response for the /api/test endpoint
    responses.add(
        responses.POST,
        f"{BASE_URL}/api/chats",
        str(uuid4()),
        content_type="application/json",
    )

    # Initialize the AuthenticatedClient with base URL and token
    client = AuthenticatedClient(base_url=BASE_URL, token=API_KEY)

    # Make a GET request to the mocked API endpoint
    response = client.get_httpx_client().post(f"{BASE_URL}/api/chats", json={"botId": "mock_bot_id_123"})


    # Assert the response contains the chatId
    chat_id = {'chatId':response.json()}
    assert "chatId" in chat_id
    assert isinstance(chat_id["chatId"], str)  # chatId should be a string (UUID)

    # Check if the Authorization header is set correctly
    assert response.request.headers["Authorization"] == f"Bearer {API_KEY}"



@pytest.fixture
def client():
    """
    Fixture to create a mock AuthenticatedClient.
    """

    return AuthenticatedClient(base_url=BASE_URL, token=API_KEY)


@pytest.fixture
def chatbot(client):
    """
    Fixture to initialize ChatbotAPI with a mock client.
    """
    return ChatbotAPI(client=client)


def test_create_chat_success(chatbot):
    """
    Test the create_chat method for a successful chat creation.
    """
    with patch("AiChatBotApiClient.ai_chat_bot_api_client.api.chat.create_chat.sync_detailed") as mock_sync_detailed:
        mock_sync_detailed.return_value.status_code = 200
        mock_sync_detailed.return_value.parsed = type("MockParsed", (), {"chat_id": "mock_chat_id_123"})()

        chat_id = chatbot.create_chat(bot_id="mock_bot_id_123")

        assert chat_id == "mock_chat_id_123"
        mock_sync_detailed.assert_called_once_with(
            client=chatbot.client,
            body=ChatCreateRequestDto(bot_id="mock_bot_id_123")
        )


def test_create_chat_failure(chatbot):
    """
    Test the create_chat method for failure due to a server error.
    """
    with patch("AiChatBotApiClient.ai_chat_bot_api_client.api.chat.create_chat.sync_detailed") as mock_sync_detailed:
        mock_sync_detailed.return_value.status_code = 500
        mock_sync_detailed.return_value.parsed = None

        with pytest.raises(Exception) as exc_info:
            chatbot.create_chat(bot_id="mock_bot_id_123")

        assert "❌ Failed to create chat" in str(exc_info.value)
        mock_sync_detailed.assert_called_once_with(
            client=chatbot.client,
            body=ChatCreateRequestDto(bot_id="mock_bot_id_123")
        )


def test_send_message_success(chatbot):
    """
    Test the send_message method for a successful message send.
    """
    with patch("AiChatBotApiClient.ai_chat_bot_api_client.api.chat.chat_completion.sync_detailed") as mock_sync_detailed:
        mock_sync_detailed.return_value.status_code = 200
        mock_sync_detailed.return_value.content = '{"assistantMessage": "Hello, user!"}'

        assistant_message = chatbot.send_message(chat_id="mock_chat_id_123", user_message="Hello!")

        assert assistant_message == "Hello, user!"
        mock_sync_detailed.assert_called_once_with(
            chat_id="mock_chat_id_123",
            client=chatbot.client,
            body=ChatCompletionRequestDto(
                user_message="Hello!",
                ignore_chat_history=ANY,
                is_admin_chat=ANY,
                is_trace_log_enabled=ANY
            )
        )


def test_send_message_failure(chatbot):
    """
    Test the send_message method for failure due to a server error.
    """
    with patch("AiChatBotApiClient.ai_chat_bot_api_client.api.chat.chat_completion.sync_detailed") as mock_sync_detailed:
        mock_sync_detailed.return_value.status_code = 400
        mock_sync_detailed.return_value.content = b"Failed to send message"

        with pytest.raises(ValueError) as exc_info:
            chatbot.send_message(chat_id="mock_chat_id_123", user_message="Hello!")

        assert "❌ Error sending message" in str(exc_info.value)
        mock_sync_detailed.assert_called_once_with(
            chat_id="mock_chat_id_123",
            client=chatbot.client,
            body=ChatCompletionRequestDto(
                user_message="Hello!",
                ignore_chat_history=ANY,
                is_admin_chat=ANY,
                is_trace_log_enabled=ANY
            )
        )
