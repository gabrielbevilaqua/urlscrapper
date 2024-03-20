import logging
import sqlite3

logger = logging.getLogger(__name__)


class DogImagesSQLitePipeline:

    def __init__(self):

        ## Create/Connect to database
        self.conn = sqlite3.connect("dogimages.db")

        ## Create cursor, used to execute commands
        self.cur = self.conn.cursor()

        ## Create quotes table if none exists
        self.cur.execute(
            """
        CREATE TABLE IF NOT EXISTS urls(
            url TEXT
        )
        """
        )

    def process_item(self, item, spider):

        ## Check to see if text is already in database
        self.cur.execute("SELECT * FROM urls WHERE url = ?", (item["url"],))
        result = self.cur.fetchone()

        if result:
            logger.warning(f"Image url is already in database: {item["url"]}")
        else:
            self.cur.execute(
                """
                INSERT INTO urls (url) VALUES (?)
            """,
                (item["url"],),
            )
            self.conn.commit()
            spider.increment_saved_items()

        return item
