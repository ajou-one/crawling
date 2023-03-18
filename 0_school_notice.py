import ssl
import urllib.request
from bs4 import BeautifulSoup
import re
import json
hdr = {'User-Agent': 'Mozilla/5.0'}
baseUrl = 'https://www.ajou.ac.kr/kr/ajou/notice.do'

context = ssl._create_unverified_context()

result = []

for offset in range(0, 18260, 10):

    pageUrl = baseUrl + f'?mode=list&&articleLimit=10&article.offset={offset}'

    req = urllib.request.Request(pageUrl, headers=hdr)
    html = urllib.request.urlopen(req, context=context).read()
    soup = BeautifulSoup(html, 'html.parser')

    notice_div = soup.find_all(
        "div", attrs={'class': re.compile('^b-title-box')})

    for notice in notice_div:

        source = 0  # ajou_univ

        title = notice.find("a")['title']

        url = notice.find("a")['href']

        data = {'source': source, 'title': title, 'url': baseUrl + url}

        result.append(data)

print(result)
