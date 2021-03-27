from urllib import request
from bs4 import BeautifulSoup
import json
# story website scrapy


def chapter(url):
    print(url)
    response = request.urlopen(url)
    html = response.read()
    html = html.decode("gbk")
    bs = BeautifulSoup(html)
    title = bs.find("title")
    author_infos = bs.find_all('div', class_='info cl6e')
    txts = bs.find_all("p")
    ts = title.text
    print(ts)
    auth = ''
    for author_info in author_infos:
        auth += author_info.text.replace('\n', '')
    print(auth)
    content = []
    for line in txts:
        content.append(line.text)
        print(line.text)
    print(content)
    return {'title': ts, 'source': url, 'auth': auth, 'content': content}


def page_target(num):
    return str.format('http://www.shuhai.com/read/55051/{}.html', num)


if __name__ == "__main__":
    content_target = 'http://www.shuhai.com/read/101468/34.html'
    response = request.urlopen(content_target)
    html = response.read()
    html = html.decode("gbk")
    print(html)
    for i in range(1, 5):
       pass
    # print(json.dumps(chapter(page_target(i))))




