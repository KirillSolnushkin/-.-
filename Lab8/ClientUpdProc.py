from EntityUpdProc import EntityUpdProc
from Client import Client

class ClientUpdProc(EntityUpdProc):
    def get_entity(self):
        return Client()

    def validate_data(self, entity) -> bool:
        return True

    def save_data(self, entity):
        print("Збереження даних користувача (email не може бути змінений!!!)")

    def validation_failure(self, entity):
        print("Перевірка помилки користувача")