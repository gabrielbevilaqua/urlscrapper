import io

import pytest
from scrapy.http import HtmlResponse, Request

from urlscrapper.spiders.dog_images import DogImagesSpider


class TestDogImagesSpider:
    @pytest.fixture
    def sample_response_body(self):
        with io.open(
            "urlscrapper/urlscrapper/tests/fixtures/dog_images_sample_response.html",
            "r",
        ) as f:
            response_body = f.read()
        return response_body

    @pytest.fixture
    def spider(self):
        spider = DogImagesSpider()
        return spider

    def test_parse(self, spider, sample_response_body):
        sample_response = HtmlResponse(
            url=spider.start_urls[0],
            body=sample_response_body,
            encoding="utf-8",
        )

        results = list(spider.parse(sample_response))
        print(results)

        assert isinstance(results, list)
        assert (
            len(results) == 61
        )  # results have 60 valid image urls of the sample html response + one call to the next page
        assert isinstance(
            results[-1], Request
        )  # asserts last element is the call to next page
