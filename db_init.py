import mysql.connector
from sw_crawl import sw_crawl

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="ajouone"
)
cursor = db.cursor()

cursor.execute("create table notice (id int primary key not null auto_increment, url varchar(200) not null, title varchar(200) not null, code int not null, new varchar(10) not null)")

for i in range(1,1000):
    crawl = sw_crawl(i)
    
    sql = "INSERT INTO NOTICE (url, title, code, new) VALUES (%s, %s, %s, %s)"
    for j in range(len(crawl[0])):
        val = (crawl[0][j], crawl[1][j], crawl[2][j], "new")
        cursor.execute(sql,val)
    
    if crawl == [[],[],[]]:
        break

db.commit()
