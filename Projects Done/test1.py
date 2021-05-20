import requests
from bs4 import BeautifulSoup
import time

URL = ' https://en.wikipedia.org/wiki/Kgalagadi_Transfrontier_Park                                                '
response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')

page = soup.find(id='bodyContent')
page1 = soup.tbody
part = page1.find_all('tr')
i = 0
links = []
for art in part:
  j = i + 1
  k = art.text
  for kinks in art.find_all('a'):
    print(kinks.get('href'))
  #o = art.find('a')
  #print(o)
  #m = o.get('href')
  #print(m)
  #n = "{} - {}".format(m,l)
  #print(l)
  print("{}. \n {} \n \n .............\n".format(j, k))
  time.sleep(2)
  i += 1

  
print(len(page))
print(part[3])
print(links)