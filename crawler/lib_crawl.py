import requests
from bs4 import BeautifulSoup

def lib_crawl(page):
    url = "https://library.ajou.ac.kr/pyxis-api/1/bulletin-boards/1/bulletins?max=10&offset=" + str((page-1) * 10);
    response = requests.get(url)
    datas = response.json().get('data').get('list')
    url = []
    title = []
    for data in datas:
        url.append("https://library.ajou.ac.kr/#/bbs/notice/"+ str(data.get('id')))
        title.append(data.get('title').replace("\n","").replace("\t","").replace("\r","").strip())

    return [url, title, [5 for i in range(len(url))]]

# print(lib_crawl(1))