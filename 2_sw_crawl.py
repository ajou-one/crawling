import requests
from bs4 import BeautifulSoup

def sw_crawl(page):
    url = "http://software.ajou.ac.kr/bbs/board.php?tbl=notice&&category=&findType=&findWord=&sort1=&sort2=&it_id=&shop_flag=&mobile_flag=&page=" + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser", from_encoding='utf-8')

    aTags = soup.select(".responsive03 > a")

    url = []
    title = []
    for a in aTags:
        if "/bbs" in a.get('href'):
            url.append("http://software.ajou.ac.kr/bbs/board.php" + a.get('href'))
            title.append(a.get_text().replace("\n","").replace("\t","").strip())

    return [url, title, [2 for i in range(len(url))]]