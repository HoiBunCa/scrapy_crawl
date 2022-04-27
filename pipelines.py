import psycopg2
from sqlalchemy import create_engine, Table, Column, MetaData, Integer, Text
from scrapy.exceptions import DropItem


# class CrawlDataPipeline:
#     """Tweets pipeline for storing scraped items in the database"""
#
#     # Define function to configure the connection to the database & connect to it
#     def open_spider(self, spider):
#         hostname = 'localhost'
#         port = 5436
#         username = 'crawl_data'
#         password = 'qwerty123'
#         database = 'crawl_data'
#
#         self.connection = psycopg2.connect(host=hostname, user=username, password=password,
#                                            dbname=database, port=port)
#         self.cur = self.connection.cursor()
#
#     # Define function to disconnect from database
#     def close_spider(self, spider):
#         self.cur.close()
#         self.connection.close()
#
#     # Define function to process each scraped item and insert it into    PostgreSQL table
#     def process_item(self, item, spider):
#         try:
#             # Execute SQL command on database to insert data in table
#             self.cur.execute(
#                 "insert into nhac_chuong_data(link_download, song_name, singer_name, num_download, category, size, lyric, link_source, source_craw, num_listens) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
#                 (item['link_download'], item['song_name'], item['singer_name'], item['num_download'], item['category'],
#                  item['size'], item['lyric'], item['link_source'], item['source_craw'], item['num_listens']))
#             self.connection.commit()
#         except:
#             self.connection.rollback()
#             raise
#         return item


class CrawlDataPipeline:
    def __init__(self):
        _engine = create_engine("sqlite:///sqlite3.db")
        _connection = _engine.connect()
        _metadata = MetaData()
        _stack_items = Table("crawldataitem", _metadata,
                             Column("id", Integer, primary_key=True),
                             Column("link_download", Text),
                             Column("song_name", Text),
                             Column("singer_name", Text),
                             Column("num_download", Text),
                             Column("category", Text),
                             Column("size", Text),
                             Column("lyric", Text),
                             Column("link_source", Text),
                             Column("source_craw", Text),
                             Column("num_listens", Text))
        _metadata.create_all(_engine)
        self.connection = _connection
        self.stack_items = _stack_items

    def process_item(self, item, spider):
        is_valid = True
        for data in item:
            if not data:
                is_valid = False
                raise DropItem("Missing %s!" % data)
        if is_valid:
            ins_query = self.stack_items.insert().values(
                link_download=item["link_download"],
                song_name=item["song_name"],
                singer_name=item["singer_name"],
                num_download=item["num_download"],
                category=item["category"],
                size=item["size"],
                lyric=item["lyric"],
                link_source=item["link_source"],
                source_craw=item["source_craw"],
                num_listens=item["num_listens"])

            self.connection.execute(ins_query)
        return item