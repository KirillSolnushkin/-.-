from notification import Notification

class EmailNotification(Notification):
    """Клас для відправки email сповіщень"""

    def __init__(self, admin_email: str) -> None:
        self.admin_email = admin_email

    def send(self, title: str, message: str) -> None:
        print(f"Sent email with title '{title}' to '{self.admin_email}' says... '{message}'.")