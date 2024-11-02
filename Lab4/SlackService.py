class SlackService:
    #Клас для роботи з Slack API

    def __init__(self, login: str, api_key: str, chat_id: str) -> None:
        self.login = login
        self.api_key = api_key
        self.chat_id = chat_id

    def send_message(self, title: str, message: str) -> None:
        print(f"Sent Slack message to chatId '{self.chat_id}' with title '{title}' + message '{message}'.")


