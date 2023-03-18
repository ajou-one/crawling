import ssl
import urllib.request
from bs4 import BeautifulSoup
import re
import json
hdr = {'User-Agent': 'Mozilla/5.0'}
baseUrl = 'https://dorm.ajou.ac.kr/dorm/board/board01.jsp'

context = ssl._create_unverified_context()

result = []

for offset in range(0, 780, 10):

    pageUrl = baseUrl + f'?mode=list&board_no=774&pager.offset={offset}'

    req = urllib.request.Request(pageUrl, headers=hdr)
    html = urllib.request.urlopen(req, context=context).read()
    soup = BeautifulSoup(html, 'html.parser')

    notice_td = soup.find_all(
        "td", attrs={'class': re.compile('^td title_comm')})

    for notice in notice_td:

        source = 6  # ajou_dorm

        title = notice.find("a").get_text(strip=True)

        url = notice.find("a")['href']

        data = {'source': source, 'title': title, 'url': baseUrl + url}

        result.append(data)

print(result)
