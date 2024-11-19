from abc import ABC, abstractmethod

class DelStr(ABC):
    @abstractmethod
    def calculate_cost(self, distance: float, weight: float) -> float:
        pass