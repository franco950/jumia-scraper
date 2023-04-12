#scraping the best reviewed laptops
from bs4 import BeautifulSoup
import requests
htmldoc=requests.get('https://www.jumia.co.ke/laptops/')
soup=BeautifulSoup(htmldoc.text,'lxml')
a=[]
b=[]
with open('laptops.txt', 'w', encoding='utf-8') as f:
    
    for category in soup.find("div",class_="crs-w _main -phxs"):
        for all in category.findAll('a',class_='core'):
                
            for laptops in category.findAll('div',class_='name'):
                c =(laptops.text)
                a.append(c)
            for prices in category.findAll("div",class_="prc"):
                d=(prices.text)
                b.append(d)
        
            with open('laptops.txt', 'w', encoding='utf-8') as f:
                    for a,b in zip(a,b):                
                        f.write(a+b)
                        print(a+b) 