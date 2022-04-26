import scrapy
from crawl_data.items import CrawlDataItem


class NhacchuongSpider(scrapy.Spider):
    name = 'nhacchuong'
    allowed_domains = ['nhacchuong.net']
    start_urls = ['https://nhacchuong.net/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse_menu)

    def parse_menu(self, response):
        all_menu = response.xpath(
            '//div[@class="cat-ringtones-show"]/ul[@class="list-cat list-cat-pc-mb"]/li/a//@href').getall()
        for url in all_menu[0:1]:
            yield scrapy.Request(url=url, callback=self.parse_category)

    def parse_category(self, response):
        # get songs in page
        songs = response.xpath('//div[@class="info"]/div[@class="name"]/a//@href').getall()
        for song in songs[0:1]:
            yield scrapy.Request(song, callback=self.parse_song)

        nextPage = response.xpath('//a[@class="next page-numbers"]/@href').get()
        # if nextPage:
        #     yield scrapy.Request(nextPage, callback=self.parse_category)
        # else:
        #     print("NO NEXT PAGE")

    def parse_song(self, response):
        try:
            item = CrawlDataItem()

            item['link_download'] = response.xpath('//div[@class="ringtones-information-audio ringtones-fv"]/a//@href').get()
            item['song_name'] = response.xpath('//div[@class="breadcrumb-ringtone"]/span//text()').get()
            item['singer_name'] = response.xpath('//div[@class="title-single-audio"]/h1//text()')[2].get().replace("-", " ").strip()
            item['num_download'] = response.xpath('//div[@class="ringtones-count-view ringtones-count-download"]/span//text()').get()
            item['category'] = response.xpath('//div[@class="ringtone-content-title ringtones-category-single"]/p/b/a//text()').get()
            item['size'] = response.xpath('//div[@class="ringtones-information-audio ringtones-fv"]/a//text()')[1].get().replace("Tải xuống", "").replace("(", "").replace(")", "").strip()
            item['lyric'] = response.xpath('//div[@class="content-lyrics"]/div[@class="wrap-content-lyrics"]//text()').get().strip()
            item['link_source'] = response.url
            item['source_craw'] = response.url.split("//")[1].split("/")[0]
            item['num_listens'] = response.xpath('//div[@class="ringtones-count-view"]//text()')[1].get().strip()

            print("AAAAAAAAAA", item)
            yield item


            # print("link_download: ", link_download)
            # print("-" * 50)
            # print("ten_bai_hat: ", ten_bai_hat)
            # print("-"*50)
            # print("ten_ca_si: ", ten_ca_si)
            # print("-" * 50)
            # print("luot_tai: ", luot_tai)
            # print("-" * 50)
            # print("the_loai: ", the_loai)
            # print("-" * 50)
            # print("kich_thuoc: ", kich_thuoc)
            # print("-" * 50)
            # print("lyric: ", lyric)
            # print("-" * 50)
            # print("link_source: ", link_source)
            # print("-" * 50)
            # print("sourceCrawl: ", sourceCrawl)
            # print("-" * 50)
            # print("luot_nghe: ", luot_nghe)
            # print("-" * 50)

        except Exception as e:
            print("Exception: ", e)