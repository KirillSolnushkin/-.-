from abc import ABC, abstractmethod

class QueryBuilder(ABC):
    def __init__(self):
        self.query = {}
        self.query["select"] = "*"
        self.query["where"] = None
        self.query["limit"] = None

    @abstractmethod
    def select(self, columns: list) -> 'QueryBuilder':
        pass

    @abstractmethod
    def where(self, condition: str) -> 'QueryBuilder':
        pass

    @abstractmethod
    def limit(self, limit: int) -> 'QueryBuilder':
        pass

    @abstractmethod
    def getSQL(self) -> str:
        pass