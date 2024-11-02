# social_network.py
from abc import ABC, abstractmethod


class SocialNetwork(ABC):
    # Abstract base class for social networks

    def __init__(self):
        self.is_connected = False

    @abstractmethod
    def connect(self, **credentials):
        # Підключення до соціальної мережі
        pass

    @abstractmethod
    def post_message(self, message: str) -> bool:
        # Публікація повідомлення в соціальній мережі
        pass

    def disconnect(self):
        # Відключення від соціальної мережі
        self.is_connected = False
        return True


class SocialNetworkFactory(ABC):
    # Створення екземплярів соціальної мережі

    @abstractmethod
    def create_network(self) -> SocialNetwork:
        # Створення та повернення екземпляру соціальної мережі
        pass