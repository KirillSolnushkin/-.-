from Lab4.emailNotification import EmailNotification
from Lab4.SlackNotificationAdapter import SlackNotificationAdapter
from Lab4.smsNotificationAdapter import SmsNotificationAdapter

def main():
    # Створення та відправка email сповіщення
    email_notification = EmailNotification("admin@example.com")
    email_notification.send("Hello", "No")

    # Створення та відправка Slack сповіщення
    slack_notification = SlackNotificationAdapter("user_login", "api_key", "chat123")
    slack_notification.send("Cool", "Release")

    # Створення та відправка SMS сповіщення
    sms_notification = SmsNotificationAdapter("1234567890", "MyCompany")
    sms_notification.send("Error", "Throw an error")

if __name__ == "__main__":
    main()