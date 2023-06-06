import scrapy
from ..items import ResumeproScrapyItem

class FreepageSpider(scrapy.Spider):
    name = "freePage"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://sc.chinaz.com/jianli/free.html"]
    url_template = 'https://sc.chinaz.com/jianli/free_%d.html'
    page_num = 2

    def parse_detail(self, response):
        download_all = response.xpath('//*[@id="down"]')
        for li in download_all:
            item = response.meta['item']
            download_href = li.xpath('.//li[1]/a/@href').extract_first()
            # print(download_href)
            item['download_href'] = download_href
            yield item

    def parse(self, response):
        resume_all = response.xpath('//*[@id="container"]/div')
        for li in resume_all:
            name = li.xpath('./a/img/@alt').extract_first()
            # print(name)
            detail_href = li.xpath('./a/@href').extract_first()
            item = ResumeproScrapyItem()
            item['name'] = name
            item['detail_href'] = detail_href
            # print(detail_href)
            yield scrapy.Request(url=detail_href, callback=self.parse_detail, meta={'item': item})

            # 分页操作
            if self.page_num <= 3:
                new_url = format(self.url_template%self.page_num)
                self.page_num += 1
                yield scrapy.Request(url=new_url, callback=self.parse)

