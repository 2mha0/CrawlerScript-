# import scrapy
# from ..items import FirstbloodItem
#
# class FirstSpider(scrapy.Spider):
#     # 爬虫文件的名称:就是爬虫源文件的一个唯一标识
#     name = "first"
#     # 允许的域名
#     # allowed_domains = ["www.xxx.com"]
#     # 起始的 url 列表:该列表中存放的 url 会被 scrapy 自动进行请求的发送
#     start_urls = ["https://www.shicimingju.com/book/sanguoyanyi.html"]
#
#     # 终端
#     # # 用作数据解析: response 参数表示的就是请求成功后对应的响应对象
#     # def parse(self, response):
#     #     ul_list = response.xpath('//*[@id="main_left"]/div/div[4]/ul/li')
#     #     # 用于保存所有的数据
#     #     all_data = []
#     #     for li in ul_list:
#     #         # xpath返回的是列表，但是列表元素一定是Selector类型的对象
#     #         # extract可以将Selector对象中data参数存储的字符串提取出来
#     #         name = li.xpath('./a/text()')[0].extract()
#     #         # 列表调用来extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取了出来
#     #         href = li.xpath('./a/@href').extract()[0]
#     #         # print(name)
#     #         # print(href)
#     #         dic = {
#     #             'name': name,
#     #             'href': href
#     #         }
#     #         all_data.append(dic)
#     #
#     #     return all_data
#
#     def parse(self, response):
#         ul_list = response.xpath('//*[@id="main_left"]/div/div[4]/ul/li')
#         # 用于保存所有的数据
#         all_data = []
#         for li in ul_list:
#             # xpath返回的是列表，但是列表元素一定是Selector类型的对象
#             # extract可以将Selector对象中data参数存储的字符串提取出来
#             name = li.xpath('./a/text()')[0].extract()
#             # 列表调用来extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取了出来
#             href = li.xpath('./a/@href').extract()[0]
#             # print(name)
#             # print(href)
#             item = FirstbloodItem()
#             item['name'] = name
#             item['href'] = href
#
#             # 将item提交给了管道
#             yield item
