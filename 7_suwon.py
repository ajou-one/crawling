import ssl
import urllib.request
from bs4 import BeautifulSoup
import re
import json
hdr = {'User-Agent': 'Mozilla/5.0'}
baseUrl = 'https://www.swyouth.kr/?p=67'

context = ssl._create_unverified_context()

for page in range(0, 42, 1):

    pageUrl = baseUrl + f'&page={page}'

    req = urllib.request.Request(pageUrl, headers=hdr)
    html = urllib.request.urlopen(
        # req, context=context).read().decode('utf-8')
        req, context=context).read()
    print(html)
    soup = BeautifulSoup(html, 'html.parser')

    notice_td = soup.find_all(
        "td", attrs={'class': re.compile('^txt_left')})

    for notice in notice_td:

        source = 7  # suwon

        title = notice.find("a").get_text(strip=True)

        url = notice.find("a")['href']

        data = {'source': source, 'title': title, 'url': baseUrl + url}

        json_data = json.dumps(data, ensure_ascii=False)

        print(json_data)
