from abc import ABC, abstractmethod

class Guestable(ABC):
    @abstractmethod
    def accept(self, worker):
        pass