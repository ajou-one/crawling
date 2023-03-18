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
cursor.execute("drop table notice")
cursor.execute("create table notice (id int primary key not null auto_increment, url varchar(200) not null, title varchar(200) not null unique, classify_code int not null, age varchar(10) not null)")

def crawling(crawler):
    for i in range(1,1000):
        crawl = crawler(i)
        
        sql = "INSERT INTO NOTICE (url, title, classify_code, age) VALUES (%s, %s, %s, %s)"
        for j in range(len(crawl[0])):
            val = (crawl[0][j], crawl[1][j], crawl[2][j], "old")

            try:
                cursor.execute(sql,val)
            except:
                pass

        if crawl == [[],[],[]]:
            break
        
    db.commit()
        
for crawler in crawlers:
    crawling(crawler)