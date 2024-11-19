from notification import Notification

class EmailNotification(Notification):
    def __init__(self, admin_email: str) -> None:
        self.admin_email = admin_email

    def send(self, title: str, message: str) -> None:
        print(f"Надіслано електронний лист із заголовком '{title}' до '{self.admin_email}' говорить... '{message}'.")