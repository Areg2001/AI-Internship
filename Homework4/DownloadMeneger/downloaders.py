"""
    Downloader module, which contain thrading and multiprocessing downloaders.
"""

from abc import ABC, abstractmethod
import threading
import multiprocessing
from downloader_function import downloade_file

class Download(ABC):

    """
        This is a abstract class with start_download abstract method.
        Takes twomondatory arguments url: str and filename: str.
        This class helps download HTTP/HTTPS/FTP files.
    """

    def __init__(self, url: str, filename: str) -> None:
        self._url = url
        self._filename = filename
        self._complete = False
    
    @property
    def url(self) -> str:
        return self._url
    
    @property
    def filename(self) -> str:
        return self._filename
    

    @abstractmethod
    def start_download(self) -> None:
        ...

    def save_file(self, content: bytes) -> None:

        """
            This method takes one paramter content: bytes and
            writing it into file.
        """

        with open(self._filename, 'wb') as file:
            print(f"Writing content of {self.url} into {self._filename}...")
            file.write(content)

    def download_complete(self) -> None:

        """
            This method helps us to know that downloading
                successfully finished.
        """
        print(f"Download completed ({self.url})...")
        self._complete = True


class ThreadingDownloader(Download):

    """
        This class extends Download Class and implements start_download method,
                         where use threads.
    """

    def start_download(self) -> None:

        """
            Use this function for start downloading, using threading.
        """
        downloaded_file = downloade_file(self.url)
        thread = threading.Thread(target=self.save_file, args=(downloaded_file,))
        print(f"Download started {self.url} with {thread.getName}...")
        thread.start()
        self.download_complete()

class MultiprocessingDownloader(Download):

    """
    This class extends Download Class and implements start_download method,
                    where use multiprocessing.
    """

    def start_download(self) -> None:

        """
            Use this function for start downloading, using multiprocessing.
        """

        downloaded_file = downloade_file(self.url)
        process = multiprocessing.Process(target=self.save_file, args=(downloaded_file,))
        process.start()
        self.download_complete()
