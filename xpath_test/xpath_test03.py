import requestsimport refrom lxml import etreeif __name__ == '__main__':    url = 'http://pic.netbian.com/4kbeijing/'    header = {        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'    }    res = requests.get(url=url, headers=header)    res.encoding = res.apparent_encoding    res_text = res.text    tree = etree.HTML(res_text)    src_list = tree.xpath('//li//img/@src')    name_list = tree.xpath('//li//b/text()')    for i in range(len(src_list)):        # print(src_list[i])        # print(name_list[i])        # 请求图片        src_url = 'http://pic.netbian.com' + src_list[i]        img = requests.get(url=src_url, headers=header).content        # 名字去掉空格与中英文逗号        name = name_list[i].replace(' ', '')        name = name.replace(',', '')        name = name.replace('，', '')        path = './pic/' + name + '.jpg'        # print(path)        with open(path, 'wb') as fp:            fp.write(img)            print(name + '下载成功')