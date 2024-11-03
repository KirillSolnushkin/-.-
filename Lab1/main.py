from storage_manager import StorageManager

def main():
    # Створення екземпляру диспетчера зберігання
    storage_manager = StorageManager()

    # Встановлення типу зберігання для користувачів
    storage_manager.set_user_storage("user1", "local")
    storage_manager.set_user_storage("user2", "amazon")

    # Отримання сховища для певних користувачів
    user1_storage = storage_manager.get_user_storage("user1")
    user2_storage = storage_manager.get_user_storage("user2")

    # Використання сховища
    if user1_storage:
        user1_storage.upload_file("test.txt")
    if user2_storage:
        user2_storage.download_file("document.pdf")

if __name__ == "__main__":
    main()