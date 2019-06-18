import requests
from bs4 import BeautifulSoup
import pymysql
def getdetiles():#爬虫函数
    ls = []
    lh = []
    lk = []
    lp = []
    for i in range(0,100,20):
        link='https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={0}&type=T'.format(i)
        links=link
        head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
        r=requests.get(links,headers=head)
        soup=BeautifulSoup(r.text,'lxml')
        l=soup.find_all('li',class_='subject-item')

        for i in l:
            ls.append((i.h2.text.replace('\n','').replace(' ','')))
            lh.append( i.find('div',class_='pub').text.strip().replace("'",""))

            lk.append(i.img['src'].replace("'",""))
            lp.append(i.p.text.replace("'",""))

    return ls,lh,lk,lp
l1,l2,l3,l4=getdetiles()
#获得数据插入数据
db = pymysql.connect("localhost", "root", "admin", "123", charset="utf8")
cs = db.cursor()
for i in range(len(l1)):


    sql = "insert into py(title,times,detile,imgs) values('{0}','{1}','{2}','{3}')".format(l1[i],l2[i],l4[i],l3[i])

    cs.execute(sql)
    db.commit()
print('数据插入完成')
db.close()

