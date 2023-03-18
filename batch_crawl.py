import mysql.connector

from crawler.school_notice import school_notice
from crawler.sf_crawl import sf_crawl
from crawler.sw_crawl import sw_crawl
from crawler.cs_crawl import cs_crawl
from crawler.dm_crawl import dm_crawl
from crawler.lib_crawl import lib_crawl
from crawler.ajou_dorm import ajou_dorm
from crawler.gg import gg
from crawler.scholar import scholar

crawlers = [ school_notice, sf_crawl, sw_crawl, cs_crawl, dm_crawl, lib_crawl, ajou_dorm, gg, scholar ]

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="ajouone"
)
cursor = db.cursor()
sql = "INSERT INTO NOTICE (url, title, clasify_code, age) VALUES (%s, %s, %s, %s)"

def crawling(crawler):
    crawl = crawler(0)
    for j in range(len(crawl[0])):
        val = (crawl[0][j], crawl[1][j], crawl[2][j], "new")

        try:
            cursor.execute(sql,val)
        except mysql.connector.errors.IntegrityError:
            print("중복 에러")

    db.commit()

for crawler in crawlers:
    crawling(crawler)

sf_crawl(0)