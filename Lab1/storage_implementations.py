from storage_base import Storage

class LocalStorage(Storage):
    def upload_file(self, file_path: str) -> bool:
        # Implementation details for local storage upload
        return True

    def download_file(self, file_name: str) -> bool:
        # Implementation details for local storage download
        return True

    def delete_file(self, file_name: str) -> bool:
        # Implementation details for local storage delete
        return True

    def list_files(self) -> list:
        # Implementation details for local storage file listing
        return []


class AmazonS3Storage(Storage):
    def upload_file(self, file_path: str) -> bool:
        # Implementation details for S3 upload
        return True

    def download_file(self, file_name: str) -> bool:
        # Implementation details for S3 download
        return True

    def delete_file(self, file_name: str) -> bool:
        # Implementation details for S3 delete
        return True

    def list_files(self) -> list:
        # Implementation details for S3 file listing
        return []