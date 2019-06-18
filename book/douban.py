import requests
from bs4 import BeautifulSoup
def getdetiles():
    ls = []
    lh = []
    lk = []
    lp = []
    for i in range(0,60,20):
        link='https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={0}&type=T'.format(i)
        links=link
        head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
        r=requests.get(links,headers=head)
        soup=BeautifulSoup(r.text,'lxml')
        l=soup.find_all('li',class_='subject-item')

        for i in l:
            ls.append((i.h2.text.replace('\n','').replace(' ','')))
            lh.append( i.find('div',class_='pub').text.strip())

            lk.append(i.img['src'])
            lp.append(i.p.text)

    return ls,lh,lk,lp
getdetiles()