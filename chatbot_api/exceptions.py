class ChatbotAPIError(Exception):
    """
    Base exception for errors raised by the ChatbotAPI.
    """
    def __init__(self, message: str, status_code: int = None, details: dict = None):
        super().__init__(message)
        self.status_code = status_code
        self.details = details

    def __str__(self):
        base_message = f"{self.__class__.__name__}: {self.args[0]}"
        if self.status_code:
            base_message += f" (Status Code: {self.status_code})"
        if self.details:
            base_message += f" | Details: {self.details}"
        return base_message


class ChatCreationError(ChatbotAPIError):
    """
    Raised when there is an error creating a chat session.
    """
    def __init__(self, message: str, status_code: int = None, bot_id: str = None, details: dict = None):
        super().__init__(message, status_code, details)
        self.bot_id = bot_id

    def __str__(self):
        base_message = super().__str__()
        if self.bot_id:
            base_message += f" | Bot ID: {self.bot_id}"
        return base_message


class ChatCompletionError(ChatbotAPIError):
    """
    Raised when there is an error during a chat completion request.
    """
    def __init__(self, message: str, status_code: int = None, chat_id: str = None, details: dict = None):
        super().__init__(message, status_code, details)
        self.chat_id = chat_id

    def __str__(self):
        base_message = super().__str__()
        if self.chat_id:
            base_message += f" | Chat ID: {self.chat_id}"
        return base_message
