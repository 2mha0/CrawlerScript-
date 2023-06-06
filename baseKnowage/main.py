import requests
import re
if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8'
    res_text = response.text
    with open('../html/sanguoyanyi.html', 'w', encoding='utf-8') as fp:
        fp.write(res_text)

    # 先提取出包含目录的整个div标签
    ex = '<div class="book-mulu">((.|\n|\r)*?)</div>'
    mulu_list = re.findall(ex, res_text, re.S)
    mulu_text = str(mulu_list)

    # 再提取目录
    ex = '<li><a href="/book/sanguoyanyi/[0-9]+.html">第[零一二三四五六七八九十百]*回·(.*?)</a></li>'
    mulu_list = re.findall(ex, mulu_text, re.S)
    print(mulu_list)