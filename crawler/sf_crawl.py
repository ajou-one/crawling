import requests
from bs4 import BeautifulSoup

def sf_crawl(page):
    url = "https://sw.ajou.ac.kr/sw/board/notice.do?mode=list&&articleLimit=10&article.offset=" + str((page-1) * 10)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser", from_encoding='utf-8')

    aTags = soup.select(".b-title-box > a")
    
    if(len(aTags) == 5):
        return [[],[],[]] 
    
    url = []
    title = []
    for a in aTags:
        url.append("https://sw.ajou.ac.kr/sw/board/notice.do" + a.get('href'))
        title.append(a.get_text().replace("\n","").replace("\t","").replace("\r","").strip())

    return [url, title, [1 for i in range(len(url))]]

# print(sf_crawl(1))