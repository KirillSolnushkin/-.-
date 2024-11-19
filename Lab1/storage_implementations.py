from storage_base import Storage

class LocalStorage(Storage):
    def upload_file(self, file_path: str) -> bool:
        return True

    def download_file(self, file_name: str) -> bool:
        return True

    def delete_file(self, file_name: str) -> bool:
        return True

    def list_files(self) -> list:
        return []


class AmazonS3Storage(Storage):
    def upload_file(self, file_path: str) -> bool:
        return True

    def download_file(self, file_name: str) -> bool:
        return True

    def delete_file(self, file_name: str) -> bool:
        return True

    def list_files(self) -> list:
        return []