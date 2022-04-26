# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlDataItem(scrapy.Item):
    # define the fields for your item here like:
    link_download = scrapy.Field()  # https://nhacchuong.net/wp-content/uploads/2021/08/nhac-chuong-Happier-Than-Ever.mp3
    song_name = scrapy.Field()  # Happier Than Ever mp3
    singer_name = scrapy.Field()  # Billie Eilish
    num_download = scrapy.Field()  # 74
    category = scrapy.Field()  # Nhạc âu mỹ
    size = scrapy.Field()  # 632.57 KB
    lyric = scrapy.Field()  # Chưa có nội dung.
    link_source = scrapy.Field()  # https://nhacchuong.net/nhac-chuong/happier-than-ever-mp3/
    source_craw = scrapy.Field()  # nhacchuong.net
    num_listens = scrapy.Field()
