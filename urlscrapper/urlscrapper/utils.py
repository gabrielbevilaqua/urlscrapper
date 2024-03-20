from urlscrapper.exceptions import ImageURLNotJPGException


def get_image_not_formatted_url(img_src: str):
    if ".jpg" not in img_src:
        raise ImageURLNotJPGException(img_src)

    return f"{img_src.split('.jpg')[0]}.jpg"
