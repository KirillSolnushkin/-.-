from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def upload_file(self, file_path: str) -> bool:
        pass

    @abstractmethod
    def download_file(self, file_name: str) -> bool:
        pass

    @abstractmethod
    def delete_file(self, file_name: str) -> bool:
        pass

    @abstractmethod
    def list_files(self) -> list:
        pass