import logging

import scrapy

from urlscrapper.exceptions import ImageURLNotJPGException
from urlscrapper.items import UrlItem
from urlscrapper.utils import get_image_not_formatted_url

logger = logging.getLogger(__name__)


class DogImagesSpider(scrapy.Spider):
    name = "dogimages"
    start_urls = ["https://www.freeimages.com/search/dog"]
    image_urls_count = 0
    current_page = 1

    def increment_saved_items(self):
        self.image_urls_count += 1

    def parse(self, response):
        if response.status != 200:
            return

        for photo in response.css("div.grid-item"):
            if self.image_urls_count == 1000:
                return

            try:
                url_item = UrlItem()
                url_item["url"] = get_image_not_formatted_url(
                    photo.css("img.grid-thumb").attrib["src"]
                )
                yield url_item
            except ImageURLNotJPGException as error:
                logger.warning(f"Skipping url: {error}")
            except Exception as error:
                logger.warning(f"Skipping url due to unexpected error: {error}")

        self.current_page += 1
        next_page = f"{self.start_urls[0]}/{self.current_page}"
        yield response.follow(next_page, callback=self.parse)
