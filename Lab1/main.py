from storage_manager import StorageManager

def main():
    storage_manager = StorageManager()

    storage_manager.set_user_storage("user1", "local")
    storage_manager.set_user_storage("user2", "amazon")

    user1_storage = storage_manager.get_user_storage("user1")
    user2_storage = storage_manager.get_user_storage("user2")

    if user1_storage:
        user1_storage.upload_file("test.txt")
    if user2_storage:
        user2_storage.download_file("document.pdf")

if __name__ == "__main__":
    main()