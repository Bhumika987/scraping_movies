from bs4 import BeautifulSoup
import requests

url='https://subslikescript.com/movies'
r=requests.get(url)
content=r.text
soup=BeautifulSoup(content,'lxml')

main=soup.find('article', class_="main-article").get_text()

#links=[]
for a in soup.find_all('a',href=True,text='TEXT'):
    #links.append(a['href'])
    print (a['href'])

