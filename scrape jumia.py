#scraping the best reviewed laptops
from bs4 import BeautifulSoup
import requests
htmldoc=requests.get('https://www.jumia.co.ke/laptops/')
soup=BeautifulSoup(htmldoc.text,'lxml')
a=[]
b=[]
for category in soup.findAll("div",class_="crs row _no-g -fw-nw _6cl-4cm -pvxs"):
    for laptops in category.findAll('div',class_='name'):
        c=(laptops.text)
        a.append(c)
    for prices in category.findAll("div",class_="prc"):
        d=(prices.text)
        b.append(d)
    for a,b in zip(a,b):
        e=a+b
        print(e)  