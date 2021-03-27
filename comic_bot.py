from urllib import request
from bs4 import BeautifulSoup
import json
import re
from urllib.request import urlretrieve
import os
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
    content_target = 'https://www.dmzj.com/info/yaoshenji.html'
    response = request.urlopen(content_target)
    html = response.read()
    html = html.decode("utf-8")
    bs = BeautifulSoup(html, 'lxml')
    # title = bs.find("title")
    contents = bs.find('ul', class_='list_con_li autoHeight')
    lists = contents.find_all("a")
    chapters = []
    print(contents)
    for comic in lists:
        href = comic.get('href')
        name = comic.text
        chapters.insert(0, {'name': name, 'href': href})
    print(json.dumps(chapters))
    # comic_chapter(0, chapters[0]['href'])
    for chap in chapters[46:]:
        comic_chapter(chap['name'], chap['href'])




