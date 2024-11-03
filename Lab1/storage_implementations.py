from storage_base import Storage

class LocalStorage(Storage):
    def upload_file(self, file_path: str) -> bool:
        # Деталі реалізації для завантаження локального сховища
        return True

    def download_file(self, file_name: str) -> bool:
        # Деталі впровадження для завантаження локального сховища
        return True

    def delete_file(self, file_name: str) -> bool:
        # Деталі реалізації видалення локального сховища
        return True

    def list_files(self) -> list:
        # Деталі реалізації для списку файлів локального сховища
        return []


class AmazonS3Storage(Storage):
    def upload_file(self, file_path: str) -> bool:
        # Деталі впровадження для завантаження S3
        return True

    def download_file(self, file_name: str) -> bool:
        # Деталі впровадження для завантаження S3
        return True

    def delete_file(self, file_name: str) -> bool:
        # Деталі впровадження для видалення S3
        return True

    def list_files(self) -> list:
        # Деталі впровадження для списку файлів S3
        return []