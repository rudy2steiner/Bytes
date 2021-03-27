from urllib import request
from bs4 import BeautifulSoup

# real 106.11.34.247
# opener


def set_proxy_and_test(proxies, test=False):
    set_proxy(proxies)
    if test:
        url = 'http://httpbin.org/ip'
        #req = request.Request(url)
        response = request.urlopen(url)
        #读取相应信息并解码
        html = response.read().decode("utf-8")
        print(html)


def set_proxy(proxies):
    proxy_support = request.ProxyHandler(proxies)
    #创建Opener
    opener = request.build_opener(proxy_support)
    #添加User Angent
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装OPener
    request.install_opener(opener)


if __name__ == "__main__":
    set_proxy_and_test({}, True)
