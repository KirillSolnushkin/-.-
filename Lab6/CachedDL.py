from DL import Downloader
from SimpDL import SimpDownload

class CachedDownload(Downloader):
    def __init__(self, SimpDL: SimpDownload) -> None:
        self.simple_downloader = SimpDL
        self.cache = {}

    def download(self, url: str) -> bytes:
        if url in self.cache:
            print(f"Отримання...: {url}")
            return self.cache[url]
        else:
            print(f"Завантаження...: {url}")
            data = self.simple_downloader.download(url)
            self.cache[url] = data
            return data
