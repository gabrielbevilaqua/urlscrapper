FROM python:3.12-slim

WORKDIR /app

COPY urlscrapper /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "scrapy crawl dogimages && cp dogimages.db output/dogimages.db"]