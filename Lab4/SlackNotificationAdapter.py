from notification import Notification
from SlackService import SlackService

class SlackNotificationAdapter(Notification):
    def __init__(self, login: str, api_key: str, chat_id: str) -> None:
        self.slackService = SlackService(login, api_key, chat_id)

    def send(self, title: str, message: str) -> None:
        self.slackService.send_message(title, message)
