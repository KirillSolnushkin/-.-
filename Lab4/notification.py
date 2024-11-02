from abc import ABC, abstractmethod

class Notification(ABC):
    # Базовий абстрактний клас для всіх типів сповіщень

    @abstractmethod
    def send(self, title: str, message: str) -> None:
        pass
