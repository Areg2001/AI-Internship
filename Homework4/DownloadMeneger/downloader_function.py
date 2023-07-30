import requests

def downloade_file(url: str) -> None:

    """
        This function takes one paramter url: str,
        send request for url, and downloads the context,
        if it http/https or ftp file.
    """

    if url.startswith('http') or url.startswith('ftp'):
        try:
            target = requests.get(url)
            return target.content
        except:
            return f"Invalid url {url}..."