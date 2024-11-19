from abc import ABC, abstractmethod


class SocialNetwork(ABC):
    def __init__(self):
        self.is_connected = False

    @abstractmethod
    def connect(self, **credentials):
        pass

    @abstractmethod
    def post_message(self, message: str) -> bool:
        pass

    def disconnect(self):
        self.is_connected = False
        return True


class SocialNetworkFactory(ABC):
    @abstractmethod
    def create_network(self) -> SocialNetwork:
        pass