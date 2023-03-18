import ssl
import urllib.request
from bs4 import BeautifulSoup
import re
hdr = {'User-Agent': 'Mozilla/5.0'}


def scholar(page):

    baseUrl = 'https://www.kosaf.go.kr/ko/notice.do'

    pageUrl = baseUrl + \
        f'?ctgrId1=&ctgrId2=&searchStr=&searchType=&page={page}&pg='

    context = ssl._create_unverified_context()

    req = urllib.request.Request(pageUrl, headers=hdr)
    html = urllib.request.urlopen(req, context=context).read()
    soup = BeautifulSoup(html, 'html.parser')

    notice_td = soup.find_all(
        "td", attrs={'class': re.compile('^subject')})

    urlList = []
    titleList = []

    for notice in notice_td:

        title = notice.find("a").get_text(strip=True)

        url = notice.find("a")['href']

        urlList.append(baseUrl + url)

        titleList.append(title)

    return [url, title, [9 for i in range(len(url))]]
