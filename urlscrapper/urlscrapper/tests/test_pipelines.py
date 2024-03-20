from unittest.mock import MagicMock, patch

import pytest

from urlscrapper.items import UrlItem
from urlscrapper.pipelines import DogImagesSQLitePipeline
from urlscrapper.spiders.dog_images import DogImagesSpider


class TestSQLitePipeline:
    @pytest.fixture
    # @patch("sqlite3.connect")
    def pipeline(self):
        # Mock SQLite connection adn cursor
        mock_cursor = MagicMock()
        mock_conn = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        with patch("urlscrapper.pipelines.sqlite3") as mock_sqlite:
            mock_sqlite.connect.return_value = mock_conn
            pipeline = DogImagesSQLitePipeline()
            yield pipeline

    @pytest.fixture
    def spider_mock(self):
        return MagicMock(spec=DogImagesSpider)

    @pytest.fixture
    def url_item(self):
        return UrlItem(
            url="https://images.freeimages.com/images/large-previews/c31/happy-dog-1410362.jpg"
        )

    def test_init(self, pipeline):
        # Assert the pipeline initializes with a connection to the database
        assert pipeline.conn is not None

    def test_process_item(self, pipeline, spider_mock, url_item):
        pipeline.cur.fetchone.return_value = None

        result = pipeline.process_item(url_item, spider_mock)

        assert result is url_item
        spider_mock.increment_saved_items.assert_called_once()
        pipeline.conn.cursor.return_value.execute.called == 3

    def test_process_duplicate_item(self, pipeline, spider_mock, url_item):
        pipeline.cur.fetchone.return_value = None
        result = pipeline.process_item(url_item, spider_mock)

        pipeline.cur.fetchone.return_value = result
        duplicate_result = pipeline.process_item(url_item, spider_mock)

        assert duplicate_result is url_item
        spider_mock.increment_saved_items.assert_called_once()
