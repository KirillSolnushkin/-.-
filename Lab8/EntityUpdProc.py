from abc import ABC, abstractmethod

class EntityUpdProc(ABC):
    def update_entity(self):
        entity = self.get_entity()
        if self.validate_data(entity):
            self.save_data(entity)
            self.send_response(228, "Успішно! :D", self.get_additional_response_data())
        else:
            self.validation_failure(entity)
            self.send_response(404, "Помилка під час перевірки :(", None)

    @abstractmethod
    def get_entity(self):
        pass

    @abstractmethod
    def validate_data(self, entity) -> bool:
        pass

    @abstractmethod
    def save_data(self, entity):
        pass

    def validation_failure(self, entity):
        pass

    def get_additional_response_data(self):
        return None

    def send_response(self, status_code: int, status: str, additional_data):
        print(f"Код статусу: {status_code}, Статус: {status}, Дані: {additional_data}")