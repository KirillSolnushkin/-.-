from abc import ABC, abstractmethod

class Agent(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass