import logging

import scrapy
from scrapy.http import FormRequest

logger = logging.getLogger(__name__)


class LoginSpider(scrapy.Spider):
    name = "login"
    start_urls = ["https://www.freeimages.com/signin"]
    username = ""
    password = ""

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
    }

    def parse(self, response):
        csrf_token = response.css(
            'input[name="csrfmiddlewaretoken"]::attr(value)'
        ).extract_first()

        yield FormRequest.from_response(
            response,
            formdata={
                "username": self.username,
                "password": self.password,
                "csrf_token": csrf_token,
            },
            method="POST",
            headers={"Referer": "https://www.freeimages.com"},
            callback=self.after_login,
        )

    def after_login(self, response):
        if (
            response.status == 200
            and response.css("button#btn-profile").css("span::text").get()
            == self.username
        ):
            logger.info("Login successful!")
        else:
            logger.error("Login failed: please verify existing credentials.")
