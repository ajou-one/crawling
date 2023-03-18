import requests
from bs4 import BeautifulSoup

def dm_crawl(page):
    url = "https://media.ajou.ac.kr/media/board/board01.jsp?mode=list&board_no=304&pager.offset=" + str(page * 10)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser", from_encoding='utf-8')

    aTags = soup.select(".title_comm > a")

    url = []
    title = []
    for a in aTags:
        url.append("https://media.ajou.ac.kr/media/board/board01.jsp" + a.get('href'))
        title.append(a.get_text().replace("\n","").replace("\t","").replace("\r","").strip())

    return [url, title, [4 for i in range(len(url))]]

# print(dm_crawl(0))