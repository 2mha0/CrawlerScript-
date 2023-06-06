# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline

# 继承了该类需要重写三个父类方法
class ImgsproPipeline(ImagesPipeline):
    # 根据图片地址对图片进行请求
    def get_media_requests(self, item, info):
        # 通过meta来将文件名进行传递
        yield scrapy.Request(item['href'], meta={'name': item['name']})

    # 指定图片的存储路径
    def file_path(self, request, response=None, info=None, *, item=None):
        # 由于item不可用，因此用request的meta来将名字进行传递
        return request.meta['name']
        # imgName = request.url.split('/')[-1]
        # return imgName

    # 如果没有一下个管道类可不重写此方法
    def item_completed(self, results, item, info):
        # 返回给下一个即将被执行的管道类，类似于process_item方法
        return item
