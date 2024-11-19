class SlackService:
    def __init__(self, login: str, api_key: str, chat_id: str) -> None:
        self.login = login
        self.api_key = api_key
        self.chat_id = chat_id

    def send_message(self, title: str, message: str) -> None:
        print(f"Надіслано повідомлення до ChatId '{self.chat_id}' з назвою '{title}' + повідомлення '{message}'.")


