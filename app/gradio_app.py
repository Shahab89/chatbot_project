import gradio as gr
from chatbot_api.chatbot import ChatbotAPI
from AiChatBotApiClient.ai_chat_bot_api_client.client import AuthenticatedClient
from params import BASE_URL, API_KEY, BOT_ID

# Initialize ChatbotAPI
client = AuthenticatedClient(base_url=BASE_URL, token=API_KEY)
chatbot = ChatbotAPI(client=client)

# Maintain the chat session
chat_session = {"chat_id": None}


def initialize_chat():
    """
    Initializes a new chat session
    """
    try:
        chat_id = chatbot.create_chat(bot_id=BOT_ID)
        chat_session["chat_id"] = chat_id
        return f"Chat session initialized with ID: {chat_id}"
    except Exception as e:
        return f"Error initializing chat: {str(e)}"


def chatbot_response(user_message):
    """
    Handles user input and returns the chatbot's response.
    """
    try:
        # Initialize the chat session if not already initialized
        if not chat_session["chat_id"]:
            initialize_chat()

        # Use ChatbotAPI to send the user message
        response = chatbot.send_message(chat_id=chat_session["chat_id"], user_message=user_message)
        return response
    except Exception as e:
        return f"Error: {str(e)}"


# Define Gradio Interface
def gradio_chat(user_message):
    """
    Handles user input from Gradio and returns chatbot's response.
    """
    response = chatbot_response(user_message)
    return response


# Create Gradio Interface
demo = gr.Interface(
    fn=gradio_chat,
    inputs=gr.Textbox(lines=2, placeholder="Type your message..."),
    outputs=gr.Textbox(label="Chatbot Response"),
    title="Chatbot Interface",
)

if __name__ == "__main__":
    try:
        demo.launch(share=True)

    except Exception as e:
        import sys
        import traceback
        import ipdb
        print(f"❌ Error: {e}")
        traceback.print_exc()
        ipdb.post_mortem()
