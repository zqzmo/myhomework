from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import  By
import time
import pymysql
br=webdriver.Chrome()
br.get('http://www.jd.com/')
wait=WebDriverWait(br,10)
def seach():#搜索
    input=wait.until(ec.presence_of_element_located((By.ID,'key')))
    button=wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,'#search > div > div.form > button')))
    input.send_keys("零食")
    button.click()
    l1,l2,l3,l4=getrouser()
    return  l1,l2,l3,l4
# def pageto(i):跳转页面
#     try:
#         input=wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,"#J_bottomPage > span.p-skip > input")))
#         time.sleep(3)
#         button=wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,"#J_bottomPage > span.p-skip > a")))
#         input.clear()
#         input.send_keys(i)
#         button.click()
#         l1, l2, l3, l4 = getrouser()
#         return l1, l2, l3, l4
#     except TimeoutError:
#         pageto(i)


def getrouser():#爬虫
    print('爬虫开始！')
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,"#J_main > div.m-list")))
    time.sleep(1)
    for i in range(0, 10):
        br.execute_script("window.scrollBy(0, 1000)")
        time.sleep(1)
    time.sleep(2)
    html=br.page_source
    l=BeautifulSoup(html,'lxml').find('div',id='J_goodsList')
    s=str(l)
    soup=BeautifulSoup(s,'lxml')
    a1=[]
    a2=[]
    a3=[]
    a4=[]
    l1=soup.find_all('div','p-img')
    l2=soup.find_all("div","p-price")
    l3=soup.find_all('div',class_='p-name p-name-type-2')
    l4=soup.find_all("span",class_="J_im_icon")
    for i in l1:
        a1.append(i.img['src'])
    for k in l2:
            a2.append(k.i.text)
    for i in l3:
        a3.append(i.em.text)
    for i in l4:
        a4.append(i.a['title'])
    print('爬虫结束！')
    return a1,a2,a3,a4

def main():
    #获得数据插入数据库
    print('开始插入数据库！')
    l1, l2, l3, l4 = seach()
    db = pymysql.connect("localhost", "root", "admin", "123", charset="utf8")
    cs = db.cursor()
    for i in range(len(l1)):
        sql = "insert into jd(shop,price,title,img) values('{0}','{1}','{2}','{3}')".format(l4[i], l2[i], l4[i], l1[i])

        cs.execute(sql)
        db.commit()
    db.close()
    print('插入数据库结束')
if __name__ == '__main__':
    main()








