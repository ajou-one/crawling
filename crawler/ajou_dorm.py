import ssl
import urllib.request
from bs4 import BeautifulSoup
import re
hdr = {'User-Agent': 'Mozilla/5.0'}


def ajou_dorm(page):

    baseUrl = 'https://dorm.ajou.ac.kr/dorm/board/board01.jsp'

    pageUrl = baseUrl + \
        f'?mode=list&board_no=774&pager.offset={((page-1))*10}'

    context = ssl._create_unverified_context()

    req = urllib.request.Request(pageUrl, headers=hdr)
    html = urllib.request.urlopen(req, context=context).read()
    soup = BeautifulSoup(html, 'html.parser')

    notice_td = soup.find_all(
        "td", attrs={'class': re.compile('^td title_comm')})

    urlList = []
    titleList = []

    for notice in notice_td:

        title = notice.find("a").get_text(strip=True)

        url = notice.find("a")['href']

        urlList.append(baseUrl + url)

        titleList.append(title)

    return [urlList, titleList, [6 for i in range(len(urlList))]]
