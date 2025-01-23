


# **Chatbot Project Documentation**

---

## **Overview**
This project is a chatbot application integrating API communication, error handling, and a web-based interface. It consists of the following components:

1. **chatbot.py**: Core logic for API interaction.
2. **main.py**: Demonstrates usage of the chatbot.
3. **test files**:
   - `test_app.py`: Tests for the FastAPI application.
   - `test_chatbot.py`: Unit tests for the ChatbotAPI class.
4. **exceptions.py**: Custom exception handling.
5. **app.py**: FastAPI app for the chatbot API.
6. **gradio_app.py**: Gradio interface for user interaction.
7. **Makefile**: Automation of common tasks.
8. **.env**: Configuration of environment variables.

---

## **Files and Components**

### **1. chatbot.py**
Core implementation of the chatbot API logic:
- **Key Functions**:
  - `create_chat(bot_id)`: Initializes a chat session with a specific bot.
  - `send_message(chat_id, user_message)`: Sends a user message and retrieves the assistant's response.

- **Mocked Component**: None.
- **Environment Variable Usage**: Relies on `BASE_URL` and `API_KEY` for API interactions.

---

### **2. main.py**
Demonstrates the usage of `ChatbotAPI`:
- **Workflow**:
  1. Creates a chat session.
  2. Sends a user message and retrieves the assistant's response.
- **Mocked Component**: None.

- **Environment Variable Usage**: Uses `BOT_ID`, `BASE_URL`, and `API_KEY`.

---

### **3. Test Files**

#### **test_app.py** (FastAPI Tests):
- **Purpose**:
  - Tests endpoints (`/api/chats` and `/api/chats/{chat_id}/completions`) in `app.py`.
- **Mocked Component**:
  - `TestClient`: Simulates HTTP requests to the FastAPI app.

---

#### **test_chatbot.py** (ChatbotAPI Tests):
- **Purpose**:
  - Validates the functionality of `ChatbotAPI`.
- **Mocked Components**:
  - `responses.add`: Mocks API endpoints.
  - `patch`: Simulates specific behaviors during API interaction.

---

### **4. exceptions.py**
Custom exceptions for structured error handling:
- **Classes**:
  - `ChatCreationError`: Handles chat creation errors.
  - `ChatCompletionError`: Handles message sending errors.

- **Mocked Component**: None.

---

### **5. app.py**
FastAPI application exposing API endpoints:
- **Endpoints**:
  - `POST /api/chats`: Initializes a chat session.
  - `POST /api/chats/{chat_id}/completions`: Sends messages to the assistant.
- **Mocked Component**:
  - `chats_db`: An in-memory dictionary to simulate a database.

- **Environment Variable Usage**:
  - `OPENAI_API_KEY` and `OPENAI_MODEL_NAME`: For OpenAI API integration.

---

### **6. gradio_app.py**
Gradio interface for user interaction:
- **Workflow**:
  - Initializes a chat session.
  - Sends user messages and retrieves responses.
- **Mocked Component**: None.
- **Environment Variable Usage**:
  - Relies on `BASE_URL`, `API_KEY`, and `BOT_ID`.

---

### **7. Makefile**
Automates common tasks:
- **Targets**:
  - `install`: Installs the project dependencies in editable mode.
  - `test`: Runs all tests in the `tests/` directory using `pytest`.
  - `run`: Executes `main.py`.
  - `run_app`: Starts the FastAPI application using Uvicorn.
  - `run_gradio`: Runs the Gradio interface for the chatbot.

---

### **8. .env**
Configuration for sensitive values:
- **Required Variables**:
  - `OPENAI_API_KEY`: API key for OpenAI integration. If you do not wish to use OpenAI, leave this variable unset or comment it out in the .env file. In this case, the chatbot will provide a predefined response that echoes the user message.
  - `BASE_URL`: Base URL of the API.
  - `BOT_ID`: ID of the chatbot.
  - `API_KEY`: General API key for authentication.

**Note**: Replace `OPENAI_API_KEY` if you want to run the OpenAI model.

---

## **Mocked Components**
1. **FastAPI Application (`app.py`)**:
   - `chats_db`: Simulates a database for chat sessions.
2. **Tests (`test_app.py` and `test_chatbot.py`)**:
   - `responses` and `patch` are used to mock API interactions.
3. **Main Script (`main.py`)**:
   - `responses.activate` is used to mock dynamic responses.

---

## **How to Run**

1. **Set Up Environment**:
   - Create a `.env` file with the following variables:
     ```env
     OPENAI_API_KEY=<your_openai_key>
     BASE_URL=<api_base_url>
     BOT_ID=<bot_id>
     API_KEY=<api_key>
     ```

2. **Install Dependencies**:
   ```bash
   make install

---

## **Code Example for Using `ChatbotAPI`**
Below is a concise example demonstrating the usage of the module:

```python
from chatbot_api.chatbot import ChatbotAPI
from AiChatBotApiClient.ai_chat_bot_api_client.client import AuthenticatedClient

# Initialize the API client
client = AuthenticatedClient(base_url="https://api.example.com", token="api-example-key")
chatbot = ChatbotAPI(client=client)

# Create a new chat session
chat_id = chatbot.create_chat(bot_id="example-bot-id")
print(f"Chat session created: {chat_id}")

# Send a message to the bot
response = chatbot.send_message(chat_id=chat_id, user_message="Hi, How are you today?")
print(f"Bot response: {response}")

