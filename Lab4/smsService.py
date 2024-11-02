class SmsService:
    #Клас для роботи з SMS сервісом

    def __init__(self, phone: str, sender: str) -> None:
        self.phone = phone
        self.sender = sender

    def send_sms(self, title: str, message: str) -> None:
        print(f"Sent SMS from '{self.sender}' to '{self.phone}' message '{message}'.")
