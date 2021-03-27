from urllib import request
from bs4 import BeautifulSoup
import json
import re
from urllib.request import urlretrieve
import os
from http import cookiejar
import proxy
# comic website scrapy
# https://images.dmzj1.com/img/chapterpic/3059/14237/14395217739069.jpg


def comic_chapter(charpter_num, url):
    print(url)
    response = request.urlopen(url)
    html = response.read()
    html = html.decode("utf-8")
    html = BeautifulSoup(html, 'lxml')
    script_info = html.script
    # title = bs.find("title")
    pics = re.findall('\d{13,14}', str(script_info))
    for idx, pic in enumerate(pics):
        if len(pic) == 13:
            pics[idx] = pic + '0'
    pics = sorted(pics, key = lambda x: int(x))
    the_chapter = re.findall('\|(\d{5})\|', str(script_info))[0]
    cur = re.findall('\|(\d{4})\|', str(script_info))[0]
    chapterPics = []
    for pic in pics:
        if pic[-1] == '0':
            chapterPics.append(page_target(cur, the_chapter, pic[:-1]))
        else:
            chapterPics.append(page_target(cur, the_chapter, pic))
    chapter_dir = str.format('files/{}', charpter_num)
    if not os.path.exists(chapter_dir):
        os.mkdir(chapter_dir)
    for id, pic in enumerate(chapterPics):
        urlretrieve(pic, str.format('files/{}/{}.jpg', charpter_num, id))
    # return {'title': ts, 'source': url, 'auth': auth, 'content': content}


def page_target(cur, chapter, num):
    return str.format('https://images.dmzj1.com/img/chapterpic/{}/{}/{}.jpg', cur,chapter,num)


if __name__ == "__main__":
    proxy.set_proxy_and_test({'http': '218.60.8.99:3129', 'http': '61.220.204.25:3128',
           'http':'61.178.149.237:59042',
        'http':'220.174.236.211:8091',
           'http': '183.195.106.118:8118',
        'http': '124.117.100.213:8118',
           'http': '61.135.155.82:443'}, True)
    cookie = cookiejar.CookieJar()
    cookie_support = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(cookie_support)
    user_agent = r'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    content_target = 'http://www.qupu123.com/qiyue/gangqin/p336219.html'
    headers = {'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.8'}
    # response = request.urlopen(content_target)
    req2 = request.Request(url=content_target, headers=headers)
    response = opener.open(req2)
    html1 = response.read().decode('utf-8')
    bs = BeautifulSoup(html1, 'lxml')
    print(bs)
    img_list = bs.find("div", class_='imageList')
    contents = img_list.find_all('a')
    for a in contents:
        print('http://www.qupu123.com'+a.get('href'))
        print(a.get('title'))




