import responses
from chatbot_api.chatbot import ChatbotAPI
from AiChatBotApiClient.ai_chat_bot_api_client.client import AuthenticatedClient
import uuid
from params import *


# Generate dynamic chatId
def generate_chat_id(request):
    return 200, {}, {"chatId": uuid.uuid4()}


@responses.activate
def main():


    # Initialize the client

    client = AuthenticatedClient(base_url=BASE_URL, token=API_KEY)
    try:
        # Step 1: Create a chat session
        print("🚀 Creating chat session...")
        # breakpoint()
        chatbot = ChatbotAPI(client=client)
        chat_id =   chatbot.create_chat(bot_id=BOT_ID)
        print(f"✅ Chat session created: {chat_id}")

        # Step 2: Send a message
        print("🚀 Sending message to assistant...")
        #breakpoint()
        response = chatbot.send_message(chat_id=chat_id, user_message=USER_MESSAGE)
        print(f"✅ Assistant responded: {response}")


        # Add debug to check responses setup
        for response in responses.calls:
            print(f"✅ Mocked Call: {response.request.url}")

    except Exception as e:
        import sys
        import traceback
        import ipdb
        print(f"❌ Error: {e}")
        traceback.print_exc()
        ipdb.post_mortem()


if __name__ == "__main__":

    main()
