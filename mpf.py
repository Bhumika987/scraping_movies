from bs4 import BeautifulSoup
import requests

url='https://subslikescript.com/movies'
r=requests.get(url)
content=r.text
soup=BeautifulSoup(r.content,'lxml')

main=soup.find('article', class_="main-article").get_text()
'''li_tag = soup.find("a", href=True)
li_tag.find_all(text=True, recursive=False)  # prints the html with tags and attr.
print(li_tag)'''

for a in soup.find_all('a', href=True):
      ex=str(print(a.get_text()))               #prints the text without tags and attr.
