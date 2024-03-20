from scrapy.item import Field, Item


class UrlItem(Item):
    url = Field()
