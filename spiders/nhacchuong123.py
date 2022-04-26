import scrapy
from scrapy.selector import Selector


class NhacChuong123(scrapy.Spider):
    name = 'nhacchuong123'

    start_urls = [
        'https://nhacchuong123.com',
    ]

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse_menu)

    def parse_menu(self, response):

        all_menu = response.xpath('//div[@class="all-menu"]/b/div[@class="menu"]/h3/a//@href').getall()
        for menu in all_menu:
            url = self.start_urls[0] + menu
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # get next page
        nextPage = response.xpath('//a[@class="nextpostslink"]/@href').get()

        # get songs in page
        songs = response.xpath('//div[@class="right-row right-row-2"]/h3/a//@href').getall()
        for song in songs:
            yield scrapy.Request(song, callback=self.parse_song)

        if nextPage:
            yield scrapy.Request(nextPage, callback=self.parse)
        else:
            print("NO NEXT PAGE")

        print(response)

    def parse_download(self, response):
        linkDownload = response.xpath('//a[@class="downloadlh"]//@href').get()
        print("linkDownload: ", linkDownload)
        print("-" * 50)

    def parse_song(self, response):

        try:
            tieude = response.xpath('//h1[@class="tieude"]/a//text()').get()
            loiBaiHat = response.xpath('//div[@class="content-post"]/p/em//text()').getall()
            loiBaiHat_str = "-".join(loiBaiHat)
            luotTai = response.xpath('//div[@class="content-post"]/b//text()').get()

            sourceCrawl = response.url.split("//")[1].split("/")[0]
            downloadBtn = response.xpath(
                '//div[@class="row singlerow"]/div[@class="right-row right-row-2"]/p/a//@href').get()

            pageDownloadUrl = "https://" + sourceCrawl + downloadBtn
            yield scrapy.Request(pageDownloadUrl, callback=self.parse_download)

            # hard code
            kichthuoc = response.xpath('//div[@class="content-post"]/p//text()')[5].get()
            theLoai = response.xpath('//div[@class="content-post"]/p//text()')[3].get() \
                      + response.xpath('//div[@class="content-post"]/p//text()')[4].get()
            tenCaSi = tieude.split("–")[1]

            print("loi bai hat: ", loiBaiHat_str)
            print("-" * 50)
            print("luot tai: ", luotTai)
            print("-" * 50)
            print("tieu de: ", tieude)
            print("-" * 50)
            print("linkSource: ", response.url)
            print("-" * 50)
            print("sourceCrawl: ", sourceCrawl)  # https://nhacchuong123.com
            print("-" * 50)
            print("the loai: ", theLoai)
            print("-" * 50)
            print("kichthuoc: ", kichthuoc)
            print("-" * 50)
            print("tenCaSi: ", tenCaSi.strip())
            print("-" * 50)
        except Exception as e:
            print("Exception: ", e)
