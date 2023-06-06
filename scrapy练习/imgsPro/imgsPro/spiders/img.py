import scrapy
from ..items import ImgsproItem

class ImgSpider(scrapy.Spider):
    name = "img"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://sc.chinaz.com/tupian/fengjing.html"]

    def parse(self, response):
        item = ImgsproItem()
        div_list = response.xpath('/html/body/div[3]/div[2]/div')
        for li in div_list:
            href = 'https:' + li.xpath('./img/@data-original').extract_first()
            name = li.xpath('./img/@alt').extract_first() + '.jpg'
            item['href'] = href
            item['name'] = name
            print(name + ':' + href)
            yield item
