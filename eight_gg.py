import ssl
import urllib.request
from bs4 import BeautifulSoup
hdr = {'User-Agent': 'Mozilla/5.0'}


def gg(page):

    baseUrl = 'https://youth.gg.go.kr/gg/info/housing-welfare.do'

    pageUrl = baseUrl + \
        f'?mode=list&&articleLimit=10&article.offset={(page-1)*8}'

    context = ssl._create_unverified_context()

    req = urllib.request.Request(pageUrl, headers=hdr)
    html = urllib.request.urlopen(req, context=context).read()
    soup = BeautifulSoup(html, 'html.parser')

    notice_ul = soup.select('div.board-list > ul > li')

    urlList = []
    titleList = []

    for notice in notice_ul:

        title = notice.find("a")['title']

        url = notice.find("a")['href']

        urlList.append(baseUrl + url)

        titleList.append(title)

    return [url, title, [8 for i in range(len(url))]]
