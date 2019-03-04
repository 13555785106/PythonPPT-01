# -*- coding: utf-8 -*-
import sqlite3

from quotesbot.items import QuoteItem


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
class QuotePipeline(object):

    def __init__(self, sqlite_db_name):
        self.sqlite_db_name = sqlite_db_name

    @classmethod
    def from_crawler(cls, crawler):
        print(dir(crawler))
        return cls(
            sqlite_db_name=crawler.settings.get('SQLITE_DB_NAME'),
        )

    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.sqlite_db_name)
        self.conn.execute("CREATE TABLE IF NOT EXISTS quotes(text,author,tags)")

    def process_item(self, item, spider):
        text = None
        author = None
        tags = None
        if isinstance(item, dict):
            text = item["text"]
            author = item["author"]
            tags = ",".join(item["tags"])
        elif isinstance(item, QuoteItem):
            text = item["text"][0]
            author = item["author"][0]
            if "tags" in item:
                tags = ",".join(item["tags"])
            else:
                tags = ",".join([])

        self.conn.execute("INSERT INTO quotes(text,author,tags) VALUES(?,?,?)", (text, author, tags))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
