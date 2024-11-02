from notification import Notification
from smsService import SmsService

class SmsNotificationAdapter(Notification):
    # Адаптер для інтеграції SMS з загальним інтерфейсом сповіщень

    def __init__(self, phone: str, sender: str) -> None:
        self.sms_service = SmsService(phone, sender)

    def send(self, title: str, message: str) -> None:
        self.sms_service.send_sms(title, message)
