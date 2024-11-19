from EntityUpdProc import EntityUpdProc
from Order import Order

class OrderUpdProc(EntityUpdProc):
    def get_entity(self):
        return Order()

    def validate_data(self, entity) -> bool:
        return True

    def save_data(self, entity):
        print("Збереження даних про замовлення")

    def get_additional_response_data(self):
        return {"Замовлення": "JSON"}

    def validation_failure(self, entity):
        print("Перевірка помилки замовлення")