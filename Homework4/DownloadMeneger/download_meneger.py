"""
    Download manager module, which manages our program.
"""

from downloaders import ThreadingDownloader, MultiprocessingDownloader
import threading
import multiprocessing

class DownloadMeneger:

    """
        This class manages downloaders, takes two arguments
        max_threads: int, min_threads: int.
    """

    def __init__(self, max_threads: int, max_processes: int):
        self.__max_threads = max_threads
        self.__max_processes = max_processes
        self.__downloads = []
    
    @property
    def max_threads(self):
        return self.__max_threads
    
    @property
    def max_processes(self):
        return self.__max_processes
    
    @property
    def downloads(self):
        return self.__downloads
    
    def download(self, url: str, filename: str) -> None:
        """
            This method downloads and added it into downloaders list.
        """

        download_file = ThreadingDownloader(url, filename)  # It is my choice, you can change Multi.
        self.downloads.append(download_file)

    def start(self) -> None:
        """
            This method starts downloading and checks count
                 of threads and multiprocessing.
        """

        for download_file in self.downloads:
            if threading.active_count() < self.max_threads:
                ThreadingDownloader.start_download(download_file)

            elif len(multiprocessing.active_children()) < self.max_processes:
                MultiprocessingDownloader.start_download(download_file)
                
    def wait(self) -> str:

        """
            This method waits while all downloads don't
                     downloaded successfully.
        """

        if len(self.downloads) > 0:
            for download_file in self.downloads:
                while not download_file._complete:
                    pass
            print("Installed Successfully...")
