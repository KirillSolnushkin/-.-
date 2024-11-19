class SmsService:
    def __init__(self, phone: str, sender: str) -> None:
        self.phone = phone
        self.sender = sender

    def send_sms(self, title: str, message: str) -> None:
        print(f"Надіслано SMS з '{self.sender}' до '{self.phone}' повідомлення '{message}'.")
