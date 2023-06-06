# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ResumeproScrapyPipeline:
    fp = None
    def open_spider(self, spider):
        print('开始爬虫……')
        # self.fp = open('./res/%s.rar', 'wb')

    def process_item(self, item, spider):
        name = item['name']
        download_href = item['download_href']
        print(name + ':' + download_href)
        return item
