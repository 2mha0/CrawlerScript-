import scrapy
from ..items import FirstbloodItem

class GettitleSpider(scrapy.Spider):
    name = "getTitle"
    # allowed_domains = ["www.baidu.com"]
    start_urls = ["http://www.521609.com/vodtype/6.html"]

    # url 模板
    url_template = 'http://www.521609.com/vodtype/6-%d.html'
    page = 2

    def parse(self, response):
        list_li = response.xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[2]/ul/li')
        for li in list_li:
            title = li.xpath('./div/div/h4/a/text()').extract()[0]
            # print(title)
            item = FirstbloodItem()
            item['title'] = title
            yield item
        if self.page <= 125:
            new_url = format(self.url_template%self.page)
            self.page += 1

            yield scrapy.Request(url=new_url, callback=self.parse)




