import ssl
import urllib.request
from bs4 import BeautifulSoup
import re
hdr = {'User-Agent': 'Mozilla/5.0'}


def school_notice(page):

    baseUrl = 'https://www.ajou.ac.kr/kr/ajou/notice.do'

    pageUrl = baseUrl + \
        f'?mode=list&&articleLimit=10&article.offset={(page-1)*10}'

    context = ssl._create_unverified_context()

    req = urllib.request.Request(pageUrl, headers=hdr)
    html = urllib.request.urlopen(req, context=context).read()
    soup = BeautifulSoup(html, 'html.parser')

    notice_div = soup.find_all(
        "div", attrs={'class': re.compile('^b-title-box')})

    urlList = []
    titleList = []

    for notice in notice_div:

        title = notice.find("a")['title']

        url = notice.find("a")['href']

        urlList.append(baseUrl + url)

        titleList.append(title)

    return [url, title, [0 for i in range(len(url))]]
