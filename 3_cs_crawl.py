import requests
from bs4 import BeautifulSoup

def cs_crawl(page):
    url = "http://security.ajou.ac.kr/security/board/board01.jsp?mode=list&board_no=1403&pager.offset=" + str(page * 10)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser", from_encoding='utf-8')

    aTags = soup.select(".title_comm > a")

    url = []
    title = []
    for a in aTags:
        url.append("http://security.ajou.ac.kr/security/board/board01.jsp" + a.get('href'))
        title.append(a.get_text().replace("\n","").replace("\t","").replace("\r","").strip())

    return [url, title, [3 for i in range(len(url))]]

# print(cs_crawl(1))