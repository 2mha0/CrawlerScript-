import sys

import requests

if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    response = requests.request(url=url, method='get')
    res_text = response.text
    res_text.encode(encoding='utf-8')
    print(res_text)
    with open('../html/baidu.html', 'w', encoding='utf-8') as fp:
        fp.write(res_text)
    # with关键字是 try-except-finally 的简化版，上面两行可用一下代码代替:
    # try:
    #     fp = open('./baidu.html', 'w', encoding='utf-8')
    #     fp.write(res_text)
    # except IOError as e:
    #     print("文件操作出错:", str(e))
    # finally:
    #     if fp:
    #         fp.close()
    print('爬取结束')
