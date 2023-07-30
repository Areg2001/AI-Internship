from download_meneger import DownloadMeneger

if __name__ == "__main__":
    obj = 'https://www.instagram.com'
    obj1 = 'https://www.facebook.com'

    download_meneger = DownloadMeneger(max_threads=3, max_processes=3)

    download_meneger.download(obj, 'file.txt')
    download_meneger.download(obj1, 'file.txt')
    download_meneger.start()
    download_meneger.wait()