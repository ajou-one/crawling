import ssl
import urllib.request
from bs4 import BeautifulSoup
import re
import json
hdr = {'User-Agent': 'Mozilla/5.0'}
baseUrl = 'https://youth.gg.go.kr/gg/info/housing-welfare.do'

context = ssl._create_unverified_context()

result = []

for offset in range(0, 190, 8):

    pageUrl = baseUrl + f'?mode=list&&pagerLimit=8&pager.offset={offset}'

    req = urllib.request.Request(pageUrl, headers=hdr)
    html = urllib.request.urlopen(req, context=context).read().decode('UTF-8')
    soup = BeautifulSoup(html, 'html.parser')

    notice_ul = soup.select('div.board-list > ul > li')

    for notice in notice_ul:

        source = 8  # gg

        title = notice.find("a")['title']

        url = notice.find("a")['href']

        data = {'source': source, 'title': title, 'url': baseUrl + url}

        result.append(data)

print(result)
