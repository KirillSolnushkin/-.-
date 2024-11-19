from EntityUpdProc import EntityUpdProc
from Product import Product

class ProductUpdProc(EntityUpdProc):
    def get_entity(self):
        return Product()

    def validate_data(self, entity) -> bool:
        return True

    def save_data(self, entity):
        print("Збереження даних про товар")

    def validation_failure(self, entity):
        print("Sending a notification to the administrator via messenger")
