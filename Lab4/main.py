from Lab4.emailNotification import EmailNotification
from Lab4.SlackNotificationAdapter import SlackNotificationAdapter
from Lab4.smsNotificationAdapter import SmsNotificationAdapter

def main():
    email_notification = EmailNotification("admin@example.com")
    email_notification.send("Привіт :D", "Нііі :(")

    slack_notification = SlackNotificationAdapter("user_login", "api_key", "chat123")
    slack_notification.send("Cool", "Release")

    sms_notification = SmsNotificationAdapter("0665672024", "RelaxCorp")
    sms_notification.send("Помилка :(", "Виникає помилка :(")

if __name__ == "__main__":
    main()