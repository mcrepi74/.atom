import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36"}
url='https://www.goldmansachs.com/insights/topics/markets.html'
base='https://www.goldmansachs.com'

r=requests.get(url,headers=headers)
soup=BeautifulSoup(r.content,'html.parser')
cards=soup.find_all('div',class_='item story')

collection=[]

for card in cards:
    date= card.find('span', class_='date').text.strip()
    title=card.find('a',class_='title-link-hover').text.strip()
    url=base+card.find('a',class_='title-link-hover',href=True)['href']
    auth=card.find('span', class_='date').find_next().text
    c={
        'date':date,
        'title':title,
        'author':auth,
        'url':url
    }
    collection.append(c)
df=pd.DataFrame(collection)
d=dt.date.today()
df.to_csv(f'goldman_market_news_{d.day}{d.month}{d.year}.csv',sep='\t',index=False,encoding='utf-16')
