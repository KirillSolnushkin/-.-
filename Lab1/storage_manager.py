from typing import Optional
from storage_base import Storage
from storage_implementations import LocalStorage, AmazonS3Storage


class StorageManager:
    _instance = None
    _user_storage = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StorageManager, cls).__new__(cls)
        return cls._instance

    def set_user_storage(self, user_id: str, storage_type: str) -> None:
        if storage_type == "local":
            self._user_storage[user_id] = LocalStorage()
        elif storage_type == "amazon":
            self._user_storage[user_id] = AmazonS3Storage()
        else:
            raise ValueError("Unsupported storage type")

    def get_user_storage(self, user_id: str) -> Optional[Storage]:
        return self._user_storage.get(user_id)