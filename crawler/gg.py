import ssl
import urllib.request
from bs4 import BeautifulSoup
import re
hdr = {'User-Agent': 'Mozilla/5.0'}


def gg(page):

    baseUrl = 'https://youth.gg.go.kr/gg/intro/notice.do'

    pageUrl = baseUrl + \
        f'?mode=list&&articleLimit=10&article.offset={page}'

    context = ssl._create_unverified_context()

    req = urllib.request.Request(pageUrl, headers=hdr)
    html = urllib.request.urlopen(req, context=context).read()
    soup = BeautifulSoup(html, 'html.parser')

    notice_td = soup.find_all(
        "div", attrs={'class': re.compile('^b-title-box')})

    urlList = []
    titleList = []

    for notice in notice_td:

        title = notice.find("a")['title']

        url = notice.find("a")['href']

        urlList.append(baseUrl + url)

        titleList.append(title)

        return [url, title, [7 for i in range(len(url))]]