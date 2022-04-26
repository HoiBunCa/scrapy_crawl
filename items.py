# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlDataItem(scrapy.Item):
    # define the fields for your item here like:
    link_download = scrapy.Field()
    song_name = scrapy.Field()
    singer_name = scrapy.Field()
    num_download = scrapy.Field()
    category = scrapy.Field()
    size = scrapy.Field()
    lyric = scrapy.Field()
    link_source = scrapy.Field()
    source_craw = scrapy.Field()