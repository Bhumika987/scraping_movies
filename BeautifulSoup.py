from bs4 import BeautifulSoup
import requests

# How To Get The HTML
url='https://subslikescript.com/movie/Bermuda_Island-14926914'
r=requests.get(url)
content=r.text
soup=BeautifulSoup(r.content,'lxml')
# print(soup.prettify())  # prints the HTML of the website

# Locate the data that contains title and transcript
data=soup.find('article', class_='main-article')

# Locate title and transcript
title=soup.find('h1').get_text()
d=soup.find('p', class_='plot').get_text(strip=True, separator=' ')
box=soup.find('div', class_='full-script').get_text()


# Exporting data in a text file with the "title" name
with open('tit.txt','w') as file:
    file.write(box)
