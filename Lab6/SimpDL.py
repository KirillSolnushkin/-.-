from DL import Downloader

class SimpDownload(Downloader):
    def download(self, url: str) -> bytes:
        print(f"Завантажено з: {url}")
        return "Приклад".encode("utf-8")
