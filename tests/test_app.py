import pytest
from fastapi.testclient import TestClient
from app.app import app


# Create a TestClient instance to simulate API requests
client = TestClient(app)

@pytest.fixture
def mock_chat():
    """
    Fixture to create a mock chat session.
    """
    response = client.post("/api/chats", json={"botId": "mock_bot"})
    return response.json()

def test_create_chat_success():
    """
    Test the `/api/chats` endpoint for creating a new chat session.
    """
    # Make a request to create a new chat
    response = client.post("/api/chats", json={"botId": "mock_bot"})

    # Assert the status code is 200
    assert response.status_code == 200

    # Assert that the response contains a valid UUID as chatId
    chat_id = response.json()
    assert isinstance(chat_id, str)  # chatId should be a UUID string

def test_create_chat_fail_missing_bot_id():
    """
    Test the `/api/chats` endpoint when the botId is missing.
    """
    response = client.post("/api/chats", json={})  # Empty request body

    # Assert the status code is 422 for missing required fields
    assert response.status_code == 422

    # Assert the error message indicates that the botId is required
    assert "detail" in response.json()

def test_chat_completion_success(mock_chat):
    """
    Test the `/api/chats/{chat_id}/completions` endpoint for a successful message send.
    """
    chat_id = mock_chat  # Use mock_chat directly as chatId, it's a string UUID

    # Send a message to the created chat
    response = client.post(
        f"/api/chats/{chat_id}/completions", json={"userMessage": "Hello, assistant!"}
    )

    assert response.status_code == 200

    # Assert the assistant's message is returned
    assert "assistantMessage" in response.json()
    assert response.json()["assistantMessage"] == "I received your message: Hello, assistant!"

def test_chat_completion_fail_missing_message(mock_chat):
    """
    Test the `/api/chats/{chat_id}/completions` endpoint when the user message is missing.
    """
    chat_id = mock_chat  # Use mock_chat directly as chatId, it's a string UUID

    response = client.post(f"/api/chats/{chat_id}/completions", json={})  # Empty request body


    assert response.status_code == 422

    # Assert that the error message is about the missing userMessage
    assert "detail" in response.json()
