import scrapy


class FptshopSpider(scrapy.Spider):
    name = 'fptshop'
    allowed_domains = ['fptshop.com.vn']
    start_urls = ['https://fptshop.com.vn/dien-thoai']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        products = response.xpath('//div[@class="fs-mntd fs-mntd3"]/ul/li/div/span/a//text()').getall()
        print("products: ", products)
