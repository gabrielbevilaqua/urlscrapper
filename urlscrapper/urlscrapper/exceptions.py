class ImageURLNotJPGException(Exception):
    def __init__(self, url: str) -> None:
        super().__init__(f"Image url is not of expected type jpg: {url}")
        self.url = url
