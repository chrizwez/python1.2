import requests
from bs4 import BeautifulSoup
import time

URL = 'https://www.amazon.com/Best-Sellers-Womens-Boots/zgbs/fashion/679380011'
response = requests.get(URL)

soup = BeautifulSoup(response.content,'html.parser')

page01 = soup.find(id='zg-ordered-list')
page02 = page01.find_all('li')
for page in page02:
  j = page.find_all('div')
  i = j[3]
  i = i.text
  i = str(i)
  i = i.strip()
  x = page.select('.p13n-sc-price')
  #print(len(x))
  for t in x:
    y = x[0].text
    z = y
    if len(x) == 2:
      z = x[1].text
  print("{} is {} - {} \n".format(i, y, z))
  time.sleep(1)

#print(page02[2].prettify())
#print(soup.prettify())