from storage_manager import StorageManager


def main():
    # Create storage manager instance
    storage_manager = StorageManager()

    # Set storage type for users
    storage_manager.set_user_storage("user1", "local")
    storage_manager.set_user_storage("user2", "amazon")

    # Get storage for specific users
    user1_storage = storage_manager.get_user_storage("user1")
    user2_storage = storage_manager.get_user_storage("user2")

    # Use storage
    if user1_storage:
        user1_storage.upload_file("test.txt")
    if user2_storage:
        user2_storage.download_file("document.pdf")


if __name__ == "__main__":
    main()